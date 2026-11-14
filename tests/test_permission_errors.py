"""Permission error and recovery regression tests."""

import io
import tempfile
import unittest

from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from main import save_state
from storage import QuizStorage


class PermissionErrorTests(unittest.TestCase):

    def setUp(self):

        self.directory = tempfile.TemporaryDirectory()

        self.addCleanup(
            self.directory.cleanup
        )

        self.path = (
            Path(self.directory.name)
            / "state.json"
        )

        self.temporary = self.path.with_name(
            "state.json.tmp"
        )

        self.storage = QuizStorage(
            path=self.path
        )

        self.game = self.storage.load()

        self.storage.save(
            self.game
        )

        self.original = self.path.read_bytes()

    def assert_original_preserved(self):

        self.assertEqual(
            self.path.read_bytes(),
            self.original
        )

    def test_01_permission_error_inheritance(self):

        self.assertTrue(
            issubclass(
                PermissionError,
                OSError
            )
        )

    def test_02_read_permission_error(self):

        with patch.object(
            Path,
            "read_text",
            side_effect=PermissionError(
                "Read access denied"
            )
        ):

            with self.assertRaises(
                PermissionError
            ):
                self.storage.load()

        self.assert_original_preserved()

        self.assertIsNone(
            self.storage.last_backup
        )

        self.assertEqual(
            list(
                self.path.parent.glob(
                    "state.json.corrupt-*"
                )
            ),
            []
        )

    def test_03_temporary_write_permission_error(self):

        self.game.best_score = 75.0

        with patch.object(
            Path,
            "open",
            side_effect=PermissionError(
                "Write access denied"
            )
        ):

            with self.assertRaises(
                PermissionError
            ):
                self.storage.save(
                    self.game
                )

        self.assert_original_preserved()

        self.assertFalse(
            self.temporary.exists()
        )

    def test_04_replace_permission_error(self):

        self.game.best_score = 80.0

        with patch(
            "storage.os.replace",
            side_effect=PermissionError(
                "Replacement denied"
            )
        ):

            with self.assertRaises(
                PermissionError
            ):
                self.storage.save(
                    self.game
                )

        self.assert_original_preserved()

        self.assertFalse(
            self.temporary.exists()
        )

    def test_05_directory_permission_error(self):

        self.game.best_score = 85.0

        with patch.object(
            Path,
            "mkdir",
            side_effect=PermissionError(
                "Directory access denied"
            )
        ):

            with self.assertRaises(
                PermissionError
            ):
                self.storage.save(
                    self.game
                )

        self.assert_original_preserved()

        self.assertFalse(
            self.temporary.exists()
        )

    def test_06_console_error_message(self):

        self.game.best_score = 90.0

        output = io.StringIO()

        with patch(
            "storage.os.replace",
            side_effect=PermissionError(
                "Access denied"
            )
        ):

            with redirect_stdout(output):

                result = save_state(
                    self.game,
                    self.storage
                )

        self.assertFalse(result)

        self.assertIn(
            "Access denied",
            output.getvalue()
        )

        self.assertEqual(
            self.game.best_score,
            90.0
        )

        self.assert_original_preserved()

        self.assertFalse(
            self.temporary.exists()
        )

    def test_07_save_retry_after_permission_error(self):

        self.game.best_score = 95.0

        with patch(
            "storage.os.replace",
            side_effect=PermissionError(
                "File temporarily locked"
            )
        ):

            with redirect_stdout(
                io.StringIO()
            ):

                failed = save_state(
                    self.game,
                    self.storage
                )

        self.assertFalse(failed)

        self.assert_original_preserved()

        with redirect_stdout(
            io.StringIO()
        ):

            succeeded = save_state(
                self.game,
                self.storage
            )

        self.assertTrue(succeeded)

        self.assertNotEqual(
            self.path.read_bytes(),
            self.original
        )

        self.assertFalse(
            self.temporary.exists()
        )

    def test_08_reload_after_successful_retry(self):

        self.game.best_score = 100.0

        expected = [
            quiz.to_dict()
            for quiz in self.game.list_quizzes()
        ]

        with patch(
            "storage.os.replace",
            side_effect=PermissionError(
                "Permission denied"
            )
        ):

            with self.assertRaises(
                PermissionError
            ):

                self.storage.save(
                    self.game
                )

        self.assert_original_preserved()

        self.storage.save(
            self.game
        )

        restored = self.storage.load()

        self.assertEqual(
            restored.best_score,
            100.0
        )

        self.assertEqual(
            [
                quiz.to_dict()
                for quiz in restored.list_quizzes()
            ],
            expected
        )

        self.assertFalse(
            self.temporary.exists()
        )


if __name__ == "__main__":
    unittest.main()
