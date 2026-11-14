"""JSON persistence and recovery for the quiz application."""

import json
import math
import os
from datetime import datetime
from pathlib import Path

from history import get_history, validate_history
from quiz import Quiz
from quiz_game import QuizGame


ROOT = Path(__file__).resolve().parent

DEFAULT_PATH = ROOT / "data" / "default_quizzes.json"
STATE_PATH = ROOT / "state.json"


class QuizStorage:
    """Load, validate and atomically save quiz state."""

    def __init__(self, path=None, default_path=None):

        self.path = (
            Path(path)
            if path is not None
            else STATE_PATH
        )

        self.default_path = (
            Path(default_path)
            if default_path is not None
            else DEFAULT_PATH
        )

        self.last_warning = None
        self.last_backup = None

    @staticmethod
    def validate_score(score):

        if score is None:
            return

        if type(score) not in (int, float):
            raise ValueError("최고 점수의 형식이 올바르지 않습니다.")

        if not math.isfinite(score):
            raise ValueError("유효하지 않은 최고 점수입니다.")

        if not 0 <= score <= 100:
            raise ValueError("최고 점수는 0~100이어야 합니다.")

    def decode_state(self, data):
        """Validate saved data before creating a game."""

        if not isinstance(data, dict):
            raise ValueError("저장 데이터는 딕셔너리여야 합니다.")

        if not {"quizzes", "best_score"}.issubset(data):
            raise ValueError("필수 저장 항목이 없습니다.")

        version = data.get("schema_version", 1)

        if type(version) is not int or version != 1:
            raise ValueError("지원하지 않는 저장 형식입니다.")

        if not isinstance(data["quizzes"], list):
            raise ValueError("문제 데이터는 리스트여야 합니다.")

        self.validate_score(data["best_score"])

        quizzes = [
            Quiz.from_dict(item)
            for item in data["quizzes"]
        ]

        game = QuizGame(quizzes=quizzes)

        game.best_score = (
            None
            if data["best_score"] is None
            else float(data["best_score"])
        )

        game.play_history = validate_history(
            data.get("history", [])
        )

        return game

    def load_defaults(self):

        game = QuizGame()

        game.load_default_quizzes(
            self.default_path
        )

        game.play_history = []

        return game

    def backup_corrupt_state(self):

        stamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        backup = self.path.with_name(
            f"{self.path.name}.corrupt-{stamp}"
        )

        self.path.rename(backup)

        self.last_backup = backup

        return backup

    def load(self):

        self.last_warning = None
        self.last_backup = None

        try:

            text = self.path.read_text(
                encoding="utf-8"
            )

        except FileNotFoundError:

            return self.load_defaults()

        except UnicodeError:

            game = self.load_defaults()
            backup = self.backup_corrupt_state()

            self.last_warning = (
                "저장 파일 인코딩이 손상되었습니다. "
                f"백업: {backup.name}. "
                "기본 문제로 복구합니다."
            )

            return game

        try:

            data = json.loads(text)

            return self.decode_state(data)

        except (ValueError, TypeError, KeyError) as error:

            game = self.load_defaults()
            backup = self.backup_corrupt_state()

            self.last_warning = (
                "저장 파일이 손상되었습니다. "
                f"원인: {error}. "
                f"백업: {backup.name}. "
                "기본 문제로 복구합니다."
            )

            return game

    def save(self, game):

        if not isinstance(game, QuizGame):
            raise TypeError("QuizGame 객체가 필요합니다.")

        if game.is_active:
            raise RuntimeError(
                "게임 진행 중에는 저장할 수 없습니다."
            )

        self.validate_score(game.best_score)

        data = {
            "schema_version": 1,
            "quizzes": [
                quiz.to_dict()
                for quiz in game.list_quizzes()
            ],
            "best_score": game.best_score,
            "history": validate_history(
                get_history(game)
            ),
        }

        self.decode_state(data)

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        temporary = self.path.with_name(
            self.path.name + ".tmp"
        )

        try:

            with temporary.open(
                "w",
                encoding="utf-8",
                newline="\n",
            ) as file:

                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4,
                    allow_nan=False,
                )

                file.write("\n")
                file.flush()

                os.fsync(file.fileno())

            os.replace(
                temporary,
                self.path,
            )

        finally:

            if temporary.exists():
                temporary.unlink()

        return self.path
