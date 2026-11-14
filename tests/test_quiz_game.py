"""Unit tests for the QuizGame engine."""

import json
import random
import tempfile
import unittest
from pathlib import Path

from quiz import Quiz
from quiz_game import QuizGame


class TestQuizGame(unittest.TestCase):

    def setUp(self):
        self.game = QuizGame(
            rng=random.Random(42)
        )

        self.game.load_default_quizzes()

    def start(self, count=3):
        self.game.start_game(
            count=count,
            random_order=False,
            shuffle_choices=False,
        )

    def correct_answer(self):
        return self.game.submit_answer(
            self.game.current_quiz.answer
        )

    def wrong_answer(self):
        answer = self.game.current_quiz.answer
        wrong = answer % 4 + 1

        return self.game.submit_answer(wrong)

    def test_01_default_question_count(self):
        self.assertEqual(
            len(self.game.list_quizzes()),
            20,
        )

    def test_02_difficulty_filter(self):
        self.assertEqual(
            len(self.game.list_quizzes("beginner")),
            10,
        )

        self.assertEqual(
            len(self.game.list_quizzes("intermediate")),
            10,
        )

    def test_03_add_quiz(self):
        data = self.game.list_quizzes()[0].to_dict()

        data["id"] = 21
        data["question"] = "New test question"

        quiz = Quiz.from_dict(data)

        self.assertEqual(
            self.game.add_quiz(quiz),
            21,
        )

        self.assertEqual(
            len(self.game.list_quizzes()),
            21,
        )

    def test_04_duplicate_id(self):
        quiz = self.game.list_quizzes()[0]

        with self.assertRaises(ValueError):
            self.game.add_quiz(quiz)

    def test_05_duplicate_question(self):
        data = self.game.list_quizzes()[0].to_dict()
        data["id"] = 21

        with self.assertRaises(ValueError):
            self.game.add_quiz(
                Quiz.from_dict(data)
            )

    def test_06_next_id(self):
        self.assertEqual(
            self.game.next_quiz_id(),
            21,
        )

    def test_07_start_game(self):
        self.start(5)

        self.assertTrue(self.game.is_active)

        self.assertEqual(
            self.game.total_questions,
            5,
        )

        self.assertEqual(
            self.game.question_number,
            1,
        )

    def test_08_invalid_count(self):
        for count in (0, -1, 21, True, "5"):

            with self.subTest(count=count):

                with self.assertRaises(ValueError):
                    self.game.start_game(count=count)

    def test_09_empty_question_bank(self):
        game = QuizGame()

        with self.assertRaises(ValueError):
            game.start_game()

    def test_10_correct_answer_points(self):
        self.start(1)

        result = self.correct_answer()

        self.assertTrue(result["correct"])
        self.assertEqual(result["points"], 10)

    def test_11_wrong_answer_points(self):
        self.start(1)

        result = self.wrong_answer()

        self.assertFalse(result["correct"])
        self.assertEqual(result["points"], 0)

    def test_12_hint_points(self):
        self.start(1)

        self.game.use_hint()

        result = self.correct_answer()

        self.assertTrue(result["hint_used"])
        self.assertEqual(result["points"], 5)

    def test_13_repeated_hint(self):
        self.start(1)

        first = self.game.use_hint()
        second = self.game.use_hint()

        self.assertEqual(first, second)

        result = self.correct_answer()

        self.assertEqual(result["points"], 5)

    def test_14_hint_with_wrong_answer(self):
        self.start(1)

        self.game.use_hint()

        result = self.wrong_answer()

        self.assertEqual(result["points"], 0)

    def test_15_invalid_answer_does_not_advance(self):
        self.start(2)

        with self.assertRaises(ValueError):
            self.game.submit_answer(5)

        self.assertEqual(
            self.game.question_number,
            1,
        )

    def test_16_advance_question(self):
        self.start(2)

        self.correct_answer()

        self.assertEqual(
            self.game.question_number,
            2,
        )

    def test_17_normalized_score(self):
        self.start(3)

        self.correct_answer()

        self.game.use_hint()
        self.correct_answer()

        self.wrong_answer()

        result = self.game.get_result()

        self.assertEqual(result["earned_points"], 15)
        self.assertEqual(result["max_points"], 30)
        self.assertEqual(result["score"], 50.0)
        self.assertEqual(result["accuracy"], 66.7)
        self.assertEqual(result["correct_count"], 2)
        self.assertEqual(result["wrong_count"], 1)
        self.assertEqual(result["hint_count"], 1)

    def test_18_best_score(self):
        self.start(1)
        self.correct_answer()

        self.assertEqual(
            self.game.best_score,
            100.0,
        )

        self.start(1)
        self.wrong_answer()

        self.assertEqual(
            self.game.best_score,
            100.0,
        )

        self.assertFalse(
            self.game.get_result()["new_best"]
        )

    def test_19_cancel_game(self):
        self.start(2)

        self.correct_answer()

        self.assertTrue(self.game.cancel_game())

        self.assertFalse(self.game.is_active)
        self.assertIsNone(self.game.get_result())
        self.assertIsNone(self.game.best_score)

    def test_20_completed_game_state(self):
        self.start(1)

        self.correct_answer()

        self.assertFalse(self.game.is_active)
        self.assertIsNone(self.game.current_quiz)
        self.assertIsNotNone(self.game.get_result())

    def test_21_no_active_game(self):
        with self.assertRaises(RuntimeError):
            self.game.submit_answer(1)

        with self.assertRaises(RuntimeError):
            self.game.use_hint()

    def test_22_random_unique_questions(self):
        self.game.start_game(
            count=10,
            random_order=True,
            shuffle_choices=True,
        )

        ids = []

        while self.game.is_active:

            ids.append(
                self.game.current_quiz.id
            )

            self.correct_answer()

        self.assertEqual(len(ids), 10)
        self.assertEqual(len(set(ids)), 10)

        self.assertEqual(
            self.game.get_result()["score"],
            100.0,
        )

    def test_23_question_bank_unchanged(self):
        original = [
            q.to_dict()
            for q in self.game.list_quizzes()
        ]

        self.game.start_game(count=5)

        while self.game.is_active:
            self.correct_answer()

        after = [
            q.to_dict()
            for q in self.game.list_quizzes()
        ]

        self.assertEqual(original, after)

    def test_24_invalid_json_preserves_bank(self):
        with tempfile.TemporaryDirectory() as directory:

            path = Path(directory) / "invalid.json"

            path.write_text(
                "{invalid json",
                encoding="utf-8",
            )

            with self.assertRaises(json.JSONDecodeError):
                self.game.load_default_quizzes(path)

        self.assertEqual(
            len(self.game.list_quizzes()),
            20,
        )

    def test_25_prevent_changes_during_game(self):
        self.start(2)

        with self.assertRaises(RuntimeError):
            self.game.start_game()

        with self.assertRaises(RuntimeError):
            self.game.add_quiz(
                self.game.list_quizzes()[0]
            )

        with self.assertRaises(RuntimeError):
            self.game.load_default_quizzes()

    def test_26_result_is_independent(self):
        self.start(1)
        self.correct_answer()

        result = self.game.get_result()

        result["score"] = -100
        result["answers"][0]["points"] = -100

        original = self.game.get_result()

        self.assertEqual(original["score"], 100.0)

        self.assertEqual(
            original["answers"][0]["points"],
            10,
        )

    def test_27_zero_score_is_valid(self):
        self.start(1)
        self.wrong_answer()

        self.assertEqual(
            self.game.best_score,
            0.0,
        )

        self.assertTrue(
            self.game.get_result()["new_best"]
        )

    def test_28_hint_resets_next_question(self):
        self.start(2)

        self.game.use_hint()
        self.correct_answer()

        self.assertFalse(self.game.hint_used)

        result = self.correct_answer()

        self.assertEqual(result["points"], 10)


if __name__ == "__main__":
    unittest.main()
