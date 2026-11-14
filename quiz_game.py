"""Quiz game engine for machine tool and vibration quizzes."""

import json
import random
from pathlib import Path

from quiz import Quiz


class QuizGame:
    """Manage quiz questions, game sessions and scores."""

    FULL_POINTS = 10
    HINT_POINTS = 5

    def __init__(self, quizzes=None, rng=None):
        self.quizzes = []
        self.best_score = None

        self._rng = (
            rng if rng is not None else random.Random()
        )

        self._session = []
        self._index = 0
        self._hint_used = False
        self._active = False
        self._answers = []
        self._last_result = None

        if quizzes is not None:
            for quiz in quizzes:
                self.add_quiz(quiz)

    @property
    def is_active(self):
        """Return whether a game is in progress."""

        return self._active

    @property
    def current_quiz(self):
        """Return the current question or None."""

        if not self._active:
            return None

        return self._session[self._index]

    @property
    def question_number(self):
        """Return the current question number."""

        if not self._active:
            return 0

        return self._index + 1

    @property
    def total_questions(self):
        """Return the number of questions in the session."""

        return len(self._session)

    @property
    def hint_used(self):
        """Return whether the current hint has been used."""

        return self._hint_used

    def _require_inactive(self):
        """Prevent question changes during a game."""

        if self._active:
            raise RuntimeError(
                "게임 진행 중에는 문제를 변경할 수 없습니다."
            )

    def _require_active(self):
        """Require an active game session."""

        if not self._active:
            raise RuntimeError(
                "진행 중인 게임이 없습니다."
            )

    def load_default_quizzes(self, path=None):
        """Load and validate the default quiz dataset."""

        self._require_inactive()

        if path is None:
            path = (
                Path(__file__).resolve().parent
                / "data"
                / "default_quizzes.json"
            )

        path = Path(path)

        data = json.loads(
            path.read_text(encoding="utf-8")
        )

        if not isinstance(data, list):
            raise ValueError(
                "퀴즈 데이터는 리스트여야 합니다."
            )

        loaded = []
        ids = set()
        questions = set()

        for item in data:
            quiz = Quiz.from_dict(item)

            if quiz.id in ids:
                raise ValueError(
                    "중복된 문제 번호가 있습니다."
                )

            key = quiz.question.strip().casefold()

            if key in questions:
                raise ValueError(
                    "중복된 문제가 있습니다."
                )

            ids.add(quiz.id)
            questions.add(key)
            loaded.append(quiz)

        self.quizzes = loaded

        return len(self.quizzes)

    def add_quiz(self, quiz):
        """Add a validated and independent quiz object."""

        self._require_inactive()

        if not isinstance(quiz, Quiz):
            raise TypeError(
                "Quiz 객체만 등록할 수 있습니다."
            )

        quiz.validate()

        if any(q.id == quiz.id for q in self.quizzes):
            raise ValueError(
                "이미 존재하는 문제 번호입니다."
            )

        key = quiz.question.strip().casefold()

        if any(
            q.question.strip().casefold() == key
            for q in self.quizzes
        ):
            raise ValueError(
                "이미 등록된 문제입니다."
            )

        self.quizzes.append(
            Quiz.from_dict(quiz.to_dict())
        )

        return quiz.id

    def next_quiz_id(self):
        """Return the next available quiz ID."""

        return max(
            (quiz.id for quiz in self.quizzes),
            default=0,
        ) + 1

    def list_quizzes(self, difficulty=None):
        """Return copies of the registered quiz questions."""

        if difficulty not in (
            None,
            "beginner",
            "intermediate",
        ):
            raise ValueError(
                "지원하지 않는 난이도입니다."
            )

        selected = [
            quiz
            for quiz in self.quizzes
            if difficulty is None
            or quiz.difficulty == difficulty
        ]

        return [
            Quiz.from_dict(quiz.to_dict())
            for quiz in selected
        ]

    def start_game(
        self,
        count=None,
        difficulty=None,
        random_order=True,
        shuffle_choices=True,
    ):
        """Create a new game session."""

        self._require_inactive()

        available = self.list_quizzes(difficulty)

        if not available:
            raise ValueError(
                "출제할 문제가 없습니다."
            )

        if count is None:
            count = len(available)

        if type(count) is not int:
            raise ValueError(
                "문제 수는 정수여야 합니다."
            )

        if not 1 <= count <= len(available):
            raise ValueError(
                f"문제 수는 1~{len(available)}개여야 합니다."
            )

        if random_order:
            selected = self._rng.sample(
                available,
                count,
            )
        else:
            selected = available[:count]

        if shuffle_choices:
            selected = [
                quiz.shuffled(self._rng)
                for quiz in selected
            ]

        self._session = selected
        self._index = 0
        self._hint_used = False
        self._answers = []
        self._last_result = None
        self._active = True

        return self.total_questions

    def use_hint(self):
        """Reveal the current hint and mark the deduction."""

        self._require_active()

        self._hint_used = True

        return self.current_quiz.get_hint()

    def submit_answer(self, user_answer):
        """Check an answer and advance the game."""

        self._require_active()

        quiz = self.current_quiz

        correct = quiz.check_answer(user_answer)

        if correct:
            points = (
                self.HINT_POINTS
                if self._hint_used
                else self.FULL_POINTS
            )
        else:
            points = 0

        answer_result = {
            "quiz_id": quiz.id,
            "question": quiz.question,
            "selected_answer": user_answer,
            "correct_answer": quiz.answer,
            "correct_choice": quiz.get_correct_choice(),
            "correct": correct,
            "hint_used": self._hint_used,
            "points": points,
            "explanation": quiz.get_explanation(),
        }

        self._answers.append(answer_result)

        self._index += 1
        self._hint_used = False

        if self._index >= len(self._session):
            self._finish_game()

        return answer_result.copy()

    def _finish_game(self):
        """Calculate the completed session result."""

        total = len(self._session)

        correct = sum(
            answer["correct"]
            for answer in self._answers
        )

        hints = sum(
            answer["hint_used"]
            for answer in self._answers
        )

        points = sum(
            answer["points"]
            for answer in self._answers
        )

        max_points = total * self.FULL_POINTS

        score = round(
            points / max_points * 100,
            1,
        )

        accuracy = round(
            correct / total * 100,
            1,
        )

        new_best = (
            self.best_score is None
            or score > self.best_score
        )

        if new_best:
            self.best_score = score

        self._last_result = {
            "total_questions": total,
            "correct_count": correct,
            "wrong_count": total - correct,
            "hint_count": hints,
            "earned_points": points,
            "max_points": max_points,
            "score": score,
            "accuracy": accuracy,
            "best_score": self.best_score,
            "new_best": new_best,
            "answers": [
                answer.copy()
                for answer in self._answers
            ],
        }

        self._active = False

    def get_result(self):
        """Return a copy of the latest completed result."""

        if self._last_result is None:
            return None

        result = self._last_result.copy()

        result["answers"] = [
            answer.copy()
            for answer in self._last_result["answers"]
        ]

        return result

    def cancel_game(self):
        """Cancel an incomplete game without scoring it."""

        if not self._active:
            return False

        self._session = []
        self._index = 0
        self._hint_used = False
        self._answers = []
        self._last_result = None
        self._active = False

        return True
