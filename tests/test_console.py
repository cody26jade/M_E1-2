"""Tests for the interactive console interface."""

import io
import random
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from main import (
    read_text,
    read_int,
    show_menu,
    play_quiz,
    add_question,
    list_questions,
    show_score,
    run_menu,
)

from quiz_game import QuizGame


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.game = QuizGame(
            rng=random.Random(42)
        )

        self.game.load_default_quizzes()

    def capture(self, function, *args, inputs=None):

        output = io.StringIO()

        with redirect_stdout(output):

            if inputs is None:
                result = function(*args)

            else:

                with patch(
                    "builtins.input",
                    side_effect=inputs,
                ):
                    result = function(*args)

        return result, output.getvalue()

    def test_01_read_text_validation(self):

        result, output = self.capture(
            read_text,
            "Question: ",
            inputs=["", " ", "  CNC  "],
        )

        self.assertEqual(result, "CNC")
        self.assertIn("빈칸", output)

    def test_02_read_int_validation(self):

        result, output = self.capture(
            read_int,
            "Number: ",
            1,
            4,
            inputs=["", "abc", "0", "5", " 2 "],
        )

        self.assertEqual(result, 2)
        self.assertIn("숫자를 입력하세요", output)

    def test_03_show_menu(self):

        _, output = self.capture(
            show_menu,
            self.game,
        )

        self.assertIn("20개", output)
        self.assertIn("[1]", output)
        self.assertIn("[0]", output)

    def test_04_list_questions(self):

        _, output = self.capture(
            list_questions,
            self.game,
        )

        self.assertIn("[001]", output)
        self.assertIn("[020]", output)
        self.assertIn("20개", output)

    def test_05_empty_question_list(self):

        _, output = self.capture(
            list_questions,
            QuizGame(),
        )

        self.assertIn(
            "등록된 문제가 없습니다",
            output,
        )

    def test_06_add_question(self):

        _, output = self.capture(
            add_question,
            self.game,
            inputs=[
                "New console question",
                "Choice A",
                "Choice B",
                "Choice C",
                "Choice D",
                "1",
                "2",
                "Test category",
                "Test hint",
                "Test explanation",
            ],
        )

        self.assertEqual(
            len(self.game.list_quizzes()),
            21,
        )

        self.assertIn("ID: 21", output)

    def test_07_duplicate_question(self):

        question = (
            self.game.list_quizzes()[0].question
        )

        _, output = self.capture(
            add_question,
            self.game,
            inputs=[question],
        )

        self.assertIn(
            "이미 등록된 문제",
            output,
        )

        self.assertEqual(
            len(self.game.list_quizzes()),
            20,
        )

    def test_08_score_without_record(self):

        _, output = self.capture(
            show_score,
            self.game,
        )

        self.assertIn(
            "아직 완료된 게임 기록",
            output,
        )

    def test_09_play_with_correct_answer(self):

        def fake_input(prompt):

            if "출제 문제 수" in prompt:
                return "1"

            return str(
                self.game.current_quiz.answer
            )

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=fake_input,
            ):
                play_quiz(self.game)

        self.assertEqual(
            self.game.best_score,
            100.0,
        )

        self.assertIn(
            "GAME RESULT",
            output.getvalue(),
        )

    def test_10_play_with_hint(self):

        hint_requested = False

        def fake_input(prompt):

            nonlocal hint_requested

            if "출제 문제 수" in prompt:
                return "1"

            if not hint_requested:

                hint_requested = True

                return "H"

            return str(
                self.game.current_quiz.answer
            )

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=fake_input,
            ):
                play_quiz(self.game)

        self.assertEqual(
            self.game.best_score,
            50.0,
        )

    def test_11_cancel_game(self):

        _, output = self.capture(
            play_quiz,
            self.game,
            inputs=["2", "Q"],
        )

        self.assertFalse(self.game.is_active)

        self.assertIsNone(
            self.game.best_score
        )

        self.assertIn("취소", output)

    def test_12_empty_game(self):

        _, output = self.capture(
            play_quiz,
            QuizGame(),
        )

        self.assertIn(
            "등록된 문제가 없습니다",
            output,
        )

    def test_13_menu_exit(self):

        _, output = self.capture(
            run_menu,
            self.game,
            inputs=["0"],
        )

        self.assertIn(
            "프로그램을 종료합니다",
            output,
        )

    def test_14_menu_invalid_input(self):

        _, output = self.capture(
            run_menu,
            self.game,
            inputs=["abc", "9", "", "0"],
        )

        self.assertIn(
            "숫자를 입력하세요",
            output,
        )

        self.assertIn(
            "프로그램을 종료합니다",
            output,
        )

    def test_15_keyboard_interrupt(self):

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=KeyboardInterrupt,
            ):
                run_menu(self.game)

        self.assertIn(
            "안전하게 종료",
            output.getvalue(),
        )

    def test_16_eof_error(self):

        output = io.StringIO()

        with redirect_stdout(output):

            with patch(
                "builtins.input",
                side_effect=EOFError,
            ):
                run_menu(self.game)

        self.assertIn(
            "안전하게 종료",
            output.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()
