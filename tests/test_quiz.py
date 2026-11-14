"""Unit tests for the Quiz class."""

import json
import random
import unittest
from pathlib import Path

from quiz import Quiz


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.data = {
            "id": 1,
            "difficulty": "beginner",
            "category": "Machine Tools",
            "question": "What does CNC mean?",
            "choices": [
                "Computer Numerical Control",
                "Central Network Computer",
                "Control Number Calculation",
                "Computer Noise Control",
            ],
            "answer": 1,
            "hint": "Computer-based numerical control",
            "explanation": "CNC means Computer Numerical Control.",
        }

        self.quiz = Quiz.from_dict(self.data)

    def test_01_create_object(self):
        self.assertIsInstance(self.quiz, Quiz)
        self.assertEqual(self.quiz.id, 1)

    def test_02_correct_answer(self):
        self.assertTrue(self.quiz.check_answer(1))

    def test_03_wrong_answer(self):
        self.assertFalse(self.quiz.check_answer(2))

    def test_04_invalid_answer_range(self):
        for value in (0, 5, -1, 100):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    self.quiz.check_answer(value)

    def test_05_invalid_answer_type(self):
        for value in ("1", None, True, 1.5):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    self.quiz.check_answer(value)

    def test_06_get_hint(self):
        self.assertEqual(
            self.quiz.get_hint(),
            self.data["hint"],
        )

    def test_07_get_explanation(self):
        self.assertEqual(
            self.quiz.get_explanation(),
            self.data["explanation"],
        )

    def test_08_correct_choice(self):
        self.assertEqual(
            self.quiz.get_correct_choice(),
            self.data["choices"][0],
        )

    def test_09_to_dict(self):
        self.assertEqual(
            self.quiz.to_dict(),
            self.data,
        )

    def test_10_round_trip(self):
        restored = Quiz.from_dict(
            self.quiz.to_dict()
        )

        self.assertEqual(
            restored.to_dict(),
            self.quiz.to_dict(),
        )

    def test_11_missing_field(self):
        data = self.data.copy()
        del data["question"]

        with self.assertRaises(ValueError):
            Quiz.from_dict(data)

    def test_12_invalid_choice_count(self):
        data = self.data.copy()
        data["choices"] = ["A", "B", "C"]

        with self.assertRaises(ValueError):
            Quiz.from_dict(data)

    def test_13_duplicate_choices(self):
        data = self.data.copy()
        data["choices"] = ["A", "A", "B", "C"]

        with self.assertRaises(ValueError):
            Quiz.from_dict(data)

    def test_14_invalid_difficulty(self):
        data = self.data.copy()
        data["difficulty"] = "unknown"

        with self.assertRaises(ValueError):
            Quiz.from_dict(data)

    def test_15_empty_question(self):
        data = self.data.copy()
        data["question"] = " "

        with self.assertRaises(ValueError):
            Quiz.from_dict(data)

    def test_16_invalid_correct_answer(self):
        data = self.data.copy()
        data["answer"] = 5

        with self.assertRaises(ValueError):
            Quiz.from_dict(data)

    def test_17_shuffle_preserves_answer(self):
        shuffled = self.quiz.shuffled(
            random.Random(42)
        )

        self.assertEqual(
            shuffled.get_correct_choice(),
            self.quiz.get_correct_choice(),
        )

        self.assertCountEqual(
            shuffled.choices,
            self.quiz.choices,
        )

        self.assertTrue(
            shuffled.check_answer(shuffled.answer)
        )

    def test_18_shuffle_preserves_original(self):
        original = self.quiz.to_dict()

        shuffled = self.quiz.shuffled(
            random.Random(42)
        )

        self.assertIsNot(shuffled, self.quiz)

        self.assertEqual(
            self.quiz.to_dict(),
            original,
        )

    def test_19_load_all_default_questions(self):
        root = Path(__file__).resolve().parents[1]

        path = root / "data" / "default_quizzes.json"

        data = json.loads(
            path.read_text(encoding="utf-8")
        )

        quizzes = [
            Quiz.from_dict(item)
            for item in data
        ]

        self.assertEqual(len(quizzes), 20)

        self.assertEqual(
            len({q.id for q in quizzes}),
            20,
        )

        for quiz in quizzes:
            self.assertTrue(
                quiz.check_answer(quiz.answer)
            )

    def test_20_independent_choice_lists(self):
        exported = self.quiz.to_dict()

        exported["choices"][0] = "Changed"

        self.assertNotEqual(
            exported["choices"][0],
            self.quiz.choices[0],
        )


if __name__ == "__main__":
    unittest.main()
