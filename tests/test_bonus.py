"""Tests for the five bonus quiz features."""

import io
import json
import random
import tempfile
import unittest

from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from history import (
    delete_question,
    get_history,
    history_summary,
    record_game,
    validate_history,
)

from main import (
    play_quiz,
    remove_question,
    show_history,
    run_menu,
)

from quiz_game import QuizGame
from storage import QuizStorage


class TestBonus(unittest.TestCase):

    def setUp(self):

        directory = tempfile.TemporaryDirectory()

        self.addCleanup(directory.cleanup)

        self.path = (
            Path(directory.name) / "state.json"
        )

        self.storage = QuizStorage(
            path=self.path
        )

        self.game = QuizGame(
            rng=random.Random(42)
        )

        self.game.load_default_quizzes()

    def complete(self, game=None):

        if game is None:
            game = self.game

        game.start_game(
            count=1,
            random_order=False,
            shuffle_choices=False,
        )

        game.submit_answer(
            game.current_quiz.answer
        )

        result = game.get_result()

        return record_game(game, result)

    def test_01_random_questions(self):

        self.game.start_game(
            count=20,
            random_order=True,
        )

        ids = []

        while self.game.is_active:

            ids.append(
                self.game.current_quiz.id
            )

            self.game.submit_answer(
                self.game.current_quiz.answer
            )

        self.assertEqual(len(set(ids)), 20)

        self.assertNotEqual(
            ids,
            list(range(1, 21)),
        )

    def test_02_selected_question_count(self):

        self.game.start_game(count=5)

        self.assertEqual(
            self.game.total_questions,
            5,
        )

    def test_03_hint_penalty(self):

        self.game.start_game(count=1)

        self.game.use_hint()

        self.game.submit_answer(
            self.game.current_quiz.answer
        )

        result = self.game.get_result()

        self.assertEqual(result["score"], 50.0)
        self.assertEqual(result["accuracy"], 100.0)

    def test_04_repeated_hint(self):

        self.game.start_game(count=1)

        self.game.use_hint()
        self.game.use_hint()

        self.game.submit_answer(
            self.game.current_quiz.answer
        )

        result = self.game.get_result()

        self.assertEqual(result["hint_count"], 1)
        self.assertEqual(result["score"], 50.0)

    def test_05_delete_question(self):

        updated = delete_question(
            self.game,
            1,
        )

        self.assertEqual(
            len(updated.list_quizzes()),
            19,
        )

        self.assertNotIn(
            1,
            [q.id for q in updated.list_quizzes()],
        )

    def test_06_delete_unknown_id(self):

        with self.assertRaises(ValueError):

            delete_question(
                self.game,
                999,
            )

    def test_07_delete_during_game(self):

        self.game.start_game(count=1)

        with self.assertRaises(RuntimeError):

            delete_question(
                self.game,
                1,
            )

    def test_08_delete_preserves_records(self):

        self.complete()

        updated = delete_question(
            self.game,
            1,
        )

        self.assertEqual(
            updated.best_score,
            100.0,
        )

        self.assertEqual(
            len(get_history(updated)),
            1,
        )

    def test_09_delete_persistence(self):

        updated = delete_question(
            self.game,
            1,
        )

        self.storage.save(updated)

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            19,
        )

    def test_10_delete_last_question(self):

        game = QuizGame(
            quizzes=[
                self.game.list_quizzes()[0]
            ]
        )

        updated = delete_question(
            game,
            1,
        )

        self.storage.save(updated)

        self.assertEqual(
            self.storage.load().list_quizzes(),
            [],
        )

    def test_11_empty_history(self):

        summary = history_summary(self.game)

        self.assertEqual(summary["count"], 0)
        self.assertIsNone(summary["average"])

    def test_12_record_completed_game(self):

        record = self.complete()

        self.assertEqual(record["score"], 100.0)

        self.assertIn("played_at", record)

        self.assertEqual(
            len(get_history(self.game)),
            1,
        )

    def test_13_history_persistence(self):

        self.complete()

        self.storage.save(self.game)

        restored = self.storage.load()

        self.assertEqual(
            get_history(restored),
            get_history(self.game),
        )

    def test_14_multiple_history_records(self):

        self.complete()
        self.complete()

        summary = history_summary(self.game)

        self.assertEqual(summary["count"], 2)
        self.assertEqual(summary["average"], 100.0)

    def test_15_old_schema_compatibility(self):

        data = {
            "schema_version": 1,
            "quizzes": [
                quiz.to_dict()
                for quiz in self.game.list_quizzes()
            ],
            "best_score": 80.0,
        }

        self.path.write_text(
            json.dumps(data),
            encoding="utf-8",
        )

        restored = self.storage.load()

        self.assertEqual(restored.best_score, 80.0)
        self.assertEqual(get_history(restored), [])

    def test_16_invalid_history(self):

        with self.assertRaises(ValueError):

            validate_history(
                [{"score": 999}]
            )

    def test_17_console_delete_cancel(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["1", "N"],
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

    def test_18_console_delete_confirm(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["1", "Y"],
            ):

                updated = remove_question(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            len(updated.list_quizzes()),
            19,
        )

        self.assertEqual(
            len(self.storage.load().list_quizzes()),
            19,
        )

    def test_19_console_cancel_no_history(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["1", "Q"],
            ):

                play_quiz(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            get_history(self.game),
            [],
        )

    def test_20_console_history_output(self):

        self.complete()

        output = io.StringIO()

        with redirect_stdout(output):

            show_history(self.game)

        self.assertIn(
            "PLAY HISTORY",
            output.getvalue(),
        )

        self.assertIn(
            "100.0",
            output.getvalue(),
        )

    def test_21_console_completed_history(self):

        def fake_input(prompt):

            if "출제 문제 수" in prompt:
                return "1"

            return str(
                self.game.current_quiz.answer
            )

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=fake_input,
            ):

                play_quiz(
                    self.game,
                    self.storage,
                )

        restored = self.storage.load()

        self.assertEqual(
            len(get_history(restored)),
            1,
        )

    def test_22_menu_delete_and_history(self):

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=[
                    "5", "1", "Y",
                    "6", "0",
                ],
            ):

                run_menu(
                    self.game,
                    self.storage,
                )

        self.assertIn(
            "PLAY HISTORY",
            output.getvalue(),
        )

        self.assertEqual(
            len(self.storage.load().list_quizzes()),
            19,
        )

    def test_23_delete_save_failure(self):

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=["1", "Y"],
            ):

                with patch.object(
                    self.storage,
                    "save",
                    side_effect=OSError("Test failure"),
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

    def test_24_empty_history_output(self):

        output = io.StringIO()

        with redirect_stdout(output):

            show_history(self.game)

        self.assertIn(
            "아직 완료된 플레이 이력이 없습니다",
            output.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()
