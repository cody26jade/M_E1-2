"""Additional stability and exception handling tests."""

import io
import json
import tempfile
import unittest

from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from history import get_history

from main import (
    add_question,
    play_quiz,
    read_int,
    read_text,
    remove_question,
    run_menu,
    save_state,
    show_score,
)

from quiz_game import QuizGame
from storage import QuizStorage


class TestStability(unittest.TestCase):

    def setUp(self):

        directory = tempfile.TemporaryDirectory()

        self.addCleanup(directory.cleanup)

        self.path = (
            Path(directory.name) / "state.json"
        )

        self.storage = QuizStorage(
            path=self.path
        )

        self.game = self.storage.load()

    def test_01_non_numeric_menu_input(self):

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=["ABC", "1"],
            ):

                result = read_int(
                    "Menu: ",
                    0,
                    6,
                )

        self.assertEqual(result, 1)

        self.assertIn(
            "숫자를 입력하세요",
            output.getvalue(),
        )

    def test_02_empty_menu_input(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["", "   ", "0"],
            ):

                result = read_int(
                    "Menu: ",
                    0,
                    6,
                )

        self.assertEqual(result, 0)

    def test_03_out_of_range_input(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["-1", "7", "99", "3"],
            ):

                result = read_int(
                    "Menu: ",
                    0,
                    6,
                )

        self.assertEqual(result, 3)

    def test_04_trim_whitespace(self):

        with patch(
            "builtins.input",
            return_value="  2  ",
        ):

            result = read_int(
                "Menu: ",
                0,
                6,
            )

        self.assertEqual(result, 2)

    def test_05_empty_text_input(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["", "   ", " FFT "],
            ):

                result = read_text("Text: ")

        self.assertEqual(result, "FFT")

    def test_06_invalid_answer_recovery(self):

        invalid = iter(
            ["ABC", "", "0", "5"]
        )

        def fake_input(prompt):

            if "출제 문제 수" in prompt:
                return "1"

            try:
                return next(invalid)

            except StopIteration:

                return str(
                    self.game.current_quiz.answer
                )

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=fake_input,
            ):

                play_quiz(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            self.game.best_score,
            100.0,
        )

        self.assertEqual(
            len(get_history(self.game)),
            1,
        )

        self.assertIn(
            "1~4, H 또는 Q",
            output.getvalue(),
        )

    def test_07_duplicate_question_rejected(self):

        question = (
            self.game.list_quizzes()[0].question
        )

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                return_value=question,
            ):

                add_question(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            len(self.game.list_quizzes()),
            20,
        )

    def test_08_duplicate_choice_recovery(self):

        inputs = [
            "Stability test question",
            "A",
            "A",
            "B",
            "C",
            "D",
            "1",
            "1",
            "Test",
            "Hint",
            "Explanation",
        ]

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=inputs,
            ):

                add_question(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            len(self.game.list_quizzes()),
            21,
        )

        self.assertEqual(
            self.game.list_quizzes()[-1].choices,
            ["A", "B", "C", "D"],
        )

        self.assertIn(
            "중복된 보기",
            output.getvalue(),
        )

    def test_09_empty_question_bank(self):

        game = QuizGame()

        output = io.StringIO()

        with redirect_stdout(output):

            play_quiz(
                game,
                self.storage,
            )

        self.assertFalse(game.is_active)

        self.assertIn(
            "등록된 문제가 없습니다",
            output.getvalue(),
        )

    def test_10_cancel_game(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["1", "Q"],
            ):

                play_quiz(
                    self.game,
                    self.storage,
                )

        self.assertFalse(self.game.is_active)
        self.assertIsNone(self.game.best_score)
        self.assertEqual(get_history(self.game), [])

    def test_11_keyboard_interrupt(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=KeyboardInterrupt,
            ):

                result = run_menu(
                    self.game,
                    self.storage,
                )

        self.assertEqual(result, 0)
        self.assertTrue(self.path.exists())

    def test_12_eof_safe_exit(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=EOFError,
            ):

                result = run_menu(
                    self.game,
                    self.storage,
                )

        self.assertEqual(result, 0)

        self.assertEqual(
            len(self.storage.load().list_quizzes()),
            20,
        )

    def test_13_interrupt_during_game(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=[
                    "1",
                    "2",
                    KeyboardInterrupt(),
                ],
            ):

                result = run_menu(
                    self.game,
                    self.storage,
                )

        self.assertEqual(result, 0)
        self.assertFalse(self.game.is_active)

        restored = self.storage.load()

        self.assertEqual(
            get_history(restored),
            [],
        )

        self.assertIsNone(restored.best_score)

    def test_14_missing_state_defaults(self):

        self.assertFalse(self.path.exists())

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            20,
        )

    def test_15_corrupt_json_backup(self):

        original = "{invalid JSON"

        self.path.write_text(
            original,
            encoding="utf-8",
        )

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            20,
        )

        self.assertIsNotNone(
            self.storage.last_warning
        )

        self.assertEqual(
            self.storage.last_backup.read_text(
                encoding="utf-8"
            ),
            original,
        )

    def test_16_invalid_history_recovery(self):

        self.storage.save(self.game)

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        data["history"] = [
            {"score": 999}
        ]

        self.path.write_text(
            json.dumps(data),
            encoding="utf-8",
        )

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            20,
        )

        self.assertEqual(
            get_history(restored),
            [],
        )

        self.assertIsNotNone(
            self.storage.last_backup
        )

    def test_17_atomic_save_preserves_original(self):

        self.storage.save(self.game)

        original = self.path.read_bytes()

        self.game.best_score = 80.0

        with patch(
            "storage.os.replace",
            side_effect=OSError("Simulated failure"),
        ):

            with self.assertRaises(OSError):

                self.storage.save(self.game)

        self.assertEqual(
            self.path.read_bytes(),
            original,
        )

        self.assertFalse(
            self.path.with_name(
                "state.json.tmp"
            ).exists()
        )

    def test_18_delete_save_failure(self):

        self.storage.save(self.game)

        original = self.path.read_bytes()

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["1", "Y"],
            ):

                with patch.object(
                    self.storage,
                    "save",
                    side_effect=OSError(
                        "Simulated failure"
                    ),
                ):

                    updated = remove_question(
                        self.game,
                        self.storage,
                    )

        self.assertIs(updated, self.game)

        self.assertEqual(
            len(updated.list_quizzes()),
            20,
        )

        self.assertEqual(
            self.path.read_bytes(),
            original,
        )

    def test_19_save_failure_message(self):

        output = io.StringIO()

        with redirect_stdout(output):

            with patch.object(
                self.storage,
                "save",
                side_effect=OSError(
                    "Simulated failure"
                ),
            ):

                result = save_state(
                    self.game,
                    self.storage,
                )

        self.assertFalse(result)

        self.assertIn(
            "저장 실패",
            output.getvalue(),
        )

    def test_20_no_score_display(self):

        output = io.StringIO()

        with redirect_stdout(output):

            show_score(self.game)

        self.assertIn(
            "아직 완료된 게임 기록이 없습니다",
            output.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()
