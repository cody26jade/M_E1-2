"""End-to-end integration tests for the quiz application."""

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
    list_questions,
    play_quiz,
    remove_question,
    run_menu,
    show_history,
    show_menu,
    show_question,
    show_score,
)

from storage import QuizStorage


class TestIntegration(unittest.TestCase):

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

    def play(self, answers):

        answers = iter(answers)

        def fake_input(prompt):

            if "출제 문제 수" in prompt:
                return str(self.question_count)

            action = next(answers)

            if action == "correct":
                return str(
                    self.game.current_quiz.answer
                )

            if action == "wrong":
                return str(
                    self.game.current_quiz.answer
                    % 4 + 1
                )

            return action

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

        return output.getvalue()

    def add_sample_question(self):

        inputs = [
            "Integration sample question",
            "Choice A",
            "Choice B",
            "Choice C",
            "Choice D",
            "1",
            "1",
            "Integration",
            "Sample hint",
            "Sample explanation",
        ]

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=inputs,
            ):

                add_question(
                    self.game,
                    self.storage,
                )

        return self.game.list_quizzes()[-1].id

    def test_01_default_bank_and_menu(self):

        quizzes = self.game.list_quizzes()

        self.assertEqual(len(quizzes), 20)

        self.assertEqual(
            len(self.game.list_quizzes("beginner")),
            10,
        )

        self.assertEqual(
            len(self.game.list_quizzes("intermediate")),
            10,
        )

        output = io.StringIO()

        with redirect_stdout(output):

            show_menu(self.game)

        text = output.getvalue()

        for label in (
            "Play",
            "Add",
            "List",
            "Score",
            "Delete",
            "History",
            "Exit",
        ):

            self.assertIn(label, text)

    def test_02_perfect_game_and_restart(self):

        self.question_count = 3

        self.play(
            ["correct", "correct", "correct"]
        )

        restored = self.storage.load()

        self.assertEqual(
            restored.best_score,
            100.0,
        )

        records = get_history(restored)

        self.assertEqual(len(records), 1)

        self.assertEqual(
            records[0]["correct_count"],
            3,
        )

        self.assertEqual(
            records[0]["score"],
            100.0,
        )

    def test_03_mixed_answers_and_hint_scoring(self):

        self.question_count = 4

        self.play([
            "correct",
            "H",
            "correct",
            "wrong",
            "correct",
        ])

        restored = self.storage.load()

        record = get_history(restored)[0]

        self.assertEqual(
            record["correct_count"],
            3,
        )

        self.assertEqual(
            record["wrong_count"],
            1,
        )

        self.assertEqual(
            record["hint_count"],
            1,
        )

        self.assertEqual(
            record["score"],
            62.5,
        )

        self.assertEqual(
            record["accuracy"],
            75.0,
        )

    def test_04_best_score_retained(self):

        self.question_count = 1

        self.play(["correct"])

        self.game = self.storage.load()

        self.play(["wrong"])

        restored = self.storage.load()

        self.assertEqual(
            restored.best_score,
            100.0,
        )

        self.assertEqual(
            len(get_history(restored)),
            2,
        )

    def test_05_add_list_and_restart(self):

        quiz_id = self.add_sample_question()

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            21,
        )

        added = next(
            quiz
            for quiz in restored.list_quizzes()
            if quiz.id == quiz_id
        )

        self.assertEqual(
            added.question,
            "Integration sample question",
        )

        output = io.StringIO()

        with redirect_stdout(output):

            list_questions(restored)

        self.assertIn(
            added.question,
            output.getvalue(),
        )

    def test_06_delete_and_restart(self):

        quiz_id = self.add_sample_question()

        self.game = self.storage.load()

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=[str(quiz_id), "Y"],
            ):

                self.game = remove_question(
                    self.game,
                    self.storage,
                )

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            20,
        )

        self.assertNotIn(
            quiz_id,
            [
                quiz.id
                for quiz in restored.list_quizzes()
            ],
        )

    def test_07_history_and_score_display(self):

        self.question_count = 2

        self.play(["correct", "wrong"])

        restored = self.storage.load()

        output = io.StringIO()

        with redirect_stdout(output):

            show_history(restored)
            show_score(restored)

        text = output.getvalue()

        self.assertIn("PLAY HISTORY", text)
        self.assertIn("BEST SCORE", text)
        self.assertIn("50.0", text)

    def test_08_cancel_preserves_completed_history(self):

        self.question_count = 1

        self.play(["correct"])

        original = self.path.read_bytes()

        self.question_count = 2

        self.play(["correct", "Q"])

        self.assertFalse(self.game.is_active)

        self.assertEqual(
            self.path.read_bytes(),
            original,
        )

        restored = self.storage.load()

        self.assertEqual(
            len(get_history(restored)),
            1,
        )

    def test_09_final_color_integration(self):

        self.game.start_game(count=1)

        question = self.game.current_quiz.question

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "console_ui.color_enabled",
                return_value=True,
            ):

                show_question(self.game)

        self.assertIn(
            "\033[95m\033[1m" + question,
            output.getvalue(),
        )

        self.game.cancel_game()

        self.question_count = 1

        with patch(
            "console_ui.color_enabled",
            return_value=True,
        ):

            correct = self.play(["correct"])

            wrong = self.play(["wrong"])

        self.assertIn(
            "\033[94m\033[1mCORRECT!",
            correct,
        )

        self.assertIn(
            "\033[91m\033[1mINCORRECT!",
            wrong,
        )

    def test_10_menu_exit_and_json_schema(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["3", "4", "6", "0"],
            ):

                result = run_menu(
                    self.game,
                    self.storage,
                )

        self.assertEqual(result, 0)

        self.assertTrue(self.path.exists())

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        self.assertIn("quizzes", data)
        self.assertIn("best_score", data)
        self.assertIn("history", data)

        self.assertEqual(
            len(data["quizzes"]),
            20,
        )

        self.assertEqual(
            data["history"],
            [],
        )


if __name__ == "__main__":
    unittest.main()
