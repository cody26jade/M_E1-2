"""Tests for JSON persistence and recovery."""

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from main import add_question, play_quiz, run_menu
from quiz import Quiz
from quiz_game import QuizGame
from storage import QuizStorage


class TestStorage(unittest.TestCase):

    def setUp(self):

        self.directory = tempfile.TemporaryDirectory()

        self.addCleanup(
            self.directory.cleanup
        )

        self.path = (
            Path(self.directory.name)
            / "state.json"
        )

        self.storage = QuizStorage(
            path=self.path
        )

        self.game = self.storage.load()

    def complete_game(self):

        self.game.start_game(
            count=1,
            random_order=False,
            shuffle_choices=False,
        )

        self.game.submit_answer(
            self.game.current_quiz.answer
        )

    def add_sample(self):

        data = (
            self.game.list_quizzes()[0]
            .to_dict()
        )

        data["id"] = 21
        data["question"] = "진동 데이터 저장 테스트"

        self.game.add_quiz(
            Quiz.from_dict(data)
        )

    def test_01_missing_state(self):

        self.assertFalse(self.path.exists())

        self.assertEqual(
            len(self.game.list_quizzes()),
            20,
        )

        self.assertIsNone(self.game.best_score)

    def test_02_create_state(self):

        self.storage.save(self.game)

        self.assertTrue(self.path.is_file())

    def test_03_required_schema(self):

        self.storage.save(self.game)

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(
            data["schema_version"],
            1,
        )

        self.assertIn("quizzes", data)
        self.assertIn("best_score", data)

    def test_04_quiz_persistence(self):

        self.add_sample()

        self.storage.save(self.game)

        restored = QuizStorage(
            path=self.path
        ).load()

        self.assertEqual(
            len(restored.list_quizzes()),
            21,
        )

        self.assertEqual(
            restored.list_quizzes()[-1].question,
            "진동 데이터 저장 테스트",
        )

    def test_05_best_score_persistence(self):

        self.complete_game()

        self.storage.save(self.game)

        restored = self.storage.load()

        self.assertEqual(
            restored.best_score,
            100.0,
        )

    def test_06_none_score_persistence(self):

        self.storage.save(self.game)

        self.assertIsNone(
            self.storage.load().best_score
        )

    def test_07_zero_score_persistence(self):

        self.game.best_score = 0.0

        self.storage.save(self.game)

        self.assertEqual(
            self.storage.load().best_score,
            0.0,
        )

    def test_08_empty_bank_persistence(self):

        self.storage.save(
            QuizGame()
        )

        restored = self.storage.load()

        self.assertEqual(
            restored.list_quizzes(),
            [],
        )

    def test_09_utf8_encoding(self):

        self.add_sample()

        self.storage.save(self.game)

        raw = self.path.read_bytes()

        self.assertFalse(
            raw.startswith(b"\xef\xbb\xbf")
        )

        self.assertIn(
            "진동 데이터 저장 테스트",
            raw.decode("utf-8"),
        )

    def test_10_corrupt_json_recovery(self):

        original = "{invalid json"

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

    def test_11_invalid_encoding_recovery(self):

        self.path.write_bytes(b"\xff\xfe\xff")

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            20,
        )

        self.assertEqual(
            self.storage.last_backup.read_bytes(),
            b"\xff\xfe\xff",
        )

    def test_12_invalid_schema_recovery(self):

        self.path.write_text(
            '{"quizzes": []}',
            encoding="utf-8",
        )

        restored = self.storage.load()

        self.assertEqual(
            len(restored.list_quizzes()),
            20,
        )

        self.assertIsNotNone(
            self.storage.last_backup
        )

    def test_13_invalid_score_validation(self):

        for score in (
            -1,
            101,
            True,
            "80",
            float("nan"),
            float("inf"),
        ):

            with self.subTest(score=score):

                self.game.best_score = score

                with self.assertRaises(ValueError):

                    self.storage.save(self.game)

    def test_14_duplicate_id_recovery(self):

        data = self.game.list_quizzes()[0].to_dict()

        state = {
            "quizzes": [data, data],
            "best_score": None,
        }

        self.path.write_text(
            json.dumps(state),
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

    def test_15_atomic_save_failure(self):

        self.storage.save(self.game)

        original = self.path.read_bytes()

        self.add_sample()

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

    def test_16_active_game_save_blocked(self):

        self.game.start_game(count=1)

        with self.assertRaises(RuntimeError):

            self.storage.save(self.game)

    def test_17_add_console_autosave(self):

        inputs = [
            "Persistence test question",
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

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=inputs,
            ):

                add_question(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            len(self.storage.load().list_quizzes()),
            21,
        )

    def test_18_game_console_autosave(self):

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

        self.assertEqual(
            self.storage.load().best_score,
            100.0,
        )

    def test_19_exit_saves_state(self):

        self.add_sample()

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                return_value="0",
            ):

                run_menu(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            len(self.storage.load().list_quizzes()),
            21,
        )

    def test_20_interrupt_saves_state(self):

        self.add_sample()

        with redirect_stdout(io.StringIO()):

            with patch(
                "builtins.input",
                side_effect=KeyboardInterrupt,
            ):

                run_menu(
                    self.game,
                    self.storage,
                )

        self.assertEqual(
            len(self.storage.load().list_quizzes()),
            21,
        )


if __name__ == "__main__":
    unittest.main()
