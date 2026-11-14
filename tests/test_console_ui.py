"""Tests for console colors and presentation."""

import io
import os
import unittest

from contextlib import redirect_stdout
from unittest.mock import patch

import console_ui as ui

from main import play_quiz, show_menu
from quiz_game import QuizGame


class TestConsoleUI(unittest.TestCase):

    def test_01_blue_color(self):

        with patch(
            "console_ui.color_enabled",
            return_value=True,
        ):

            self.assertEqual(
                ui.paint("Correct", "blue"),
                "\033[94mCorrect\033[0m",
            )

    def test_02_red_color(self):

        with patch(
            "console_ui.color_enabled",
            return_value=True,
        ):

            self.assertEqual(
                ui.paint("Incorrect", "red"),
                "\033[91mIncorrect\033[0m",
            )

    def test_03_plain_text(self):

        with patch(
            "console_ui.color_enabled",
            return_value=False,
        ):

            self.assertEqual(
                ui.paint("Plain text", "blue"),
                "Plain text",
            )

    def test_04_bold_text(self):

        with patch(
            "console_ui.color_enabled",
            return_value=True,
        ):

            self.assertIn(
                "\033[1m",
                ui.paint("Title", "cyan", True),
            )

    def test_05_no_color_environment(self):

        with patch.dict(
            os.environ,
            {"NO_COLOR": "1"},
        ):

            self.assertFalse(ui.color_enabled())

    def test_06_redirected_output(self):

        output = io.StringIO()

        with redirect_stdout(output):

            ui.header("TEST")

        self.assertNotIn(
            "\033[",
            output.getvalue(),
        )

    def test_07_header_spacing(self):

        output = io.StringIO()

        with redirect_stdout(output):

            ui.header("TEST")

        self.assertTrue(
            output.getvalue().startswith("\n")
        )

        self.assertTrue(
            output.getvalue().endswith("\n\n")
        )

    def test_08_progress_bar(self):

        output = io.StringIO()

        with redirect_stdout(output):

            ui.progress_bar(3, 10, width=10)

        self.assertIn(
            "[###-------] 30%",
            output.getvalue(),
        )

    def test_09_menu_colors(self):

        game = QuizGame()
        game.load_default_quizzes()

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "console_ui.color_enabled",
                return_value=True,
            ):

                show_menu(game)

        text = output.getvalue()

        self.assertIn("\033[96m", text)
        self.assertIn("\033[93m", text)
        self.assertIn("MAIN MENU", text)

    def test_10_answer_colors(self):

        for correct in (True, False):

            with self.subTest(correct=correct):

                game = QuizGame()
                game.load_default_quizzes()

                output = io.StringIO()

                def fake_input(prompt):

                    if "출제 문제 수" in prompt:
                        return "1"

                    answer = game.current_quiz.answer

                    if correct:
                        return str(answer)

                    return str(answer % 4 + 1)

                with redirect_stdout(output):

                    with patch(
                        "console_ui.color_enabled",
                        return_value=True,
                    ):

                        with patch(
                            "builtins.input",
                            side_effect=fake_input,
                        ):

                            play_quiz(game)

                text = output.getvalue()

                if correct:

                    self.assertIn(
                        "\033[94m\033[1mCORRECT!",
                        text,
                    )

                else:

                    self.assertIn(
                        "\033[91m\033[1mINCORRECT!",
                        text,
                    )


if __name__ == "__main__":
    unittest.main()
