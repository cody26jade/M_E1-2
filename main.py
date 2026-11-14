"""Colored console interface for the vibration quiz."""

import sys

import console_ui as ui

from history import (
    delete_question,
    get_history,
    history_summary,
    record_game,
)

from quiz import Quiz
from quiz_game import QuizGame
from storage import QuizStorage


LEVEL_NAMES = {
    "beginner": "초급",
    "intermediate": "중급",
}


def read_text(prompt):

    while True:

        value = ui.prompt(prompt).strip()

        if value:
            return value

        ui.message(
            "빈칸은 입력할 수 없습니다.",
            "red",
        )


def read_int(prompt, minimum, maximum):

    while True:

        value = ui.prompt(prompt).strip()

        try:
            number = int(value)

        except ValueError:

            ui.message(
                "숫자를 입력하세요.",
                "red",
            )

            continue

        if minimum <= number <= maximum:
            return number

        ui.message(
            f"{minimum}~{maximum} 사이의 "
            "숫자를 입력하세요.",
            "red",
        )


def save_state(game, storage):

    if storage is None:
        return True

    try:

        storage.save(game)

        ui.message(
            "데이터 저장 완료: state.json",
            "green",
        )

        return True

    except (OSError, ValueError, RuntimeError) as error:

        ui.message(
            f"저장 실패: {error}",
            "red",
        )

        print(
            "현재 실행 중인 데이터는 "
            "메모리에 유지됩니다."
        )

        return False


def show_menu(game):

    quizzes = game.list_quizzes()

    beginner = len(
        game.list_quizzes("beginner")
    )

    intermediate = len(
        game.list_quizzes("intermediate")
    )

    best = (
        "기록 없음"
        if game.best_score is None
        else f"{game.best_score:.1f}점"
    )

    ui.header(
        "MACHINE TOOL & VIBRATION QUIZ",
        "CODYSSEY AI ALL-IN-ONE | M_E1-2",
        color="cyan",
    )

    ui.field(
        "등록 문제",
        f"{len(quizzes)}개",
        "blue",
    )

    ui.field(
        "초급 / 중급",
        f"{beginner} / {intermediate}",
    )

    ui.field(
        "최고 점수",
        best,
        "purple",
    )

    ui.field(
        "완료 게임",
        f"{len(get_history(game))}회",
    )

    print()
    ui.line()

    print(
        ui.paint(
            " MAIN MENU",
            "yellow",
            True,
        )
    )

    print()

    ui.menu_item(1, "퀴즈 풀기 (Play)")
    ui.menu_item(2, "문제 추가 (Add)")
    ui.menu_item(3, "문제 목록 (List)")
    ui.menu_item(4, "최고 점수 (Score)")
    ui.menu_item(5, "문제 삭제 (Delete)")
    ui.menu_item(6, "플레이 이력 (History)")

    print()

    ui.menu_item(0, "프로그램 종료 (Exit)")

    print()
    ui.line()
    print()


def show_question(game):

    quiz = game.current_quiz

    ui.header(
        f"QUESTION "
        f"{game.question_number:02d}"
        f" / {game.total_questions:02d}",
        color="yellow",
    )

    ui.progress_bar(
        game.question_number,
        game.total_questions,
    )

    print()

    ui.field(
        "난이도",
        LEVEL_NAMES[quiz.difficulty],
        "cyan",
    )

    ui.field(
        "분야",
        quiz.category,
        "gray",
    )

    print()
    ui.line()
    print()

    print(
        ui.paint(
            quiz.question,
            "blue",
            True,
        )
    )

    print()

    for number, choice in enumerate(
        quiz.choices,
        start=1,
    ):

        ui.menu_item(number, choice)
        print()

    ui.line()

    print(
        ui.paint("[H] 힌트", "yellow")
        + "     "
        + ui.paint("[Q] 게임 취소", "gray")
    )

    print()


def show_result(result):

    ui.header("GAME RESULT")

    score = result["score"]

    print(
        ui.paint(
            f" 최종 점수 : {score:.1f} / 100점",
            "blue",
            True,
        )
    )

    print()

    ui.score_bar(score)

    print()
    ui.line()
    print()

    ui.field(
        "출제 문제",
        f"{result['total_questions']}개",
    )

    ui.field(
        "정답",
        f"{result['correct_count']}개",
        "blue",
    )

    ui.field(
        "오답",
        f"{result['wrong_count']}개",
        "red",
    )

    ui.field(
        "힌트 사용",
        f"{result['hint_count']}회",
        "yellow",
    )

    ui.field(
        "획득 점수",
        f"{result['earned_points']} / "
        f"{result['max_points']}",
    )

    ui.field(
        "정답률",
        f"{result['accuracy']:.1f}%",
        "cyan",
    )

    ui.field(
        "최고 점수",
        f"{result['best_score']:.1f}점",
        "purple",
    )

    if result["new_best"]:

        ui.message(
            "*** NEW BEST SCORE! ***",
            "purple",
        )

    print()
    ui.line("=")
    print()


def play_quiz(game, storage=None):

    available = len(game.list_quizzes())

    if available == 0:

        ui.message(
            "등록된 문제가 없습니다.",
            "yellow",
        )

        return

    ui.header("QUIZ PLAY")

    count = read_int(
        f"출제 문제 수 (1~{available}): ",
        1,
        available,
    )

    game.start_game(
        count=count,
        random_order=True,
        shuffle_choices=True,
    )

    while game.is_active:

        show_question(game)

        while True:

            value = ui.prompt(
                "정답 번호 (1~4), H=힌트, Q=취소: "
            ).strip().upper()

            if value == "H":

                ui.message(
                    f"힌트: {game.use_hint()}",
                    "yellow",
                )

                print(
                    ui.paint(
                        "힌트 사용 후 정답은 5점입니다.",
                        "yellow",
                    )
                )

                print()
                continue

            if value == "Q":

                game.cancel_game()

                ui.message(
                    "게임을 취소했습니다.",
                    "yellow",
                )

                return

            try:

                answer = int(value)

                selected = (
                    game.current_quiz.choices[answer - 1]
                    if 1 <= answer <= 4
                    else None
                )

                result = game.submit_answer(answer)

            except ValueError:

                ui.message(
                    "1~4, H 또는 Q를 입력하세요.",
                    "red",
                )

                continue

            print()
            ui.line()

            if result["correct"]:

                ui.message(
                    "CORRECT! 정답입니다! "
                    f"+{result['points']}점",
                    "blue",
                )

            else:

                ui.message(
                    "INCORRECT! 오답입니다. +0점",
                    "red",
                )

                ui.field(
                    "선택",
                    f"{answer}. {selected}",
                    "red",
                )

            ui.field(
                "정답",
                f"{result['correct_answer']}. "
                f"{result['correct_choice']}",
                "blue",
            )

            print()

            print(
                ui.paint(
                    "해설",
                    "gray",
                    True,
                )
            )

            print(result["explanation"])

            print()
            ui.line()
            print()

            break

    result = game.get_result()

    record_game(game, result)

    show_result(result)

    save_state(game, storage)


def add_question(game, storage=None):

    ui.header("ADD QUESTION")

    question = read_text("문제 내용: ")

    if any(
        q.question.strip().casefold()
        == question.casefold()
        for q in game.list_quizzes()
    ):

        ui.message(
            "이미 등록된 문제입니다.",
            "yellow",
        )

        return

    print()

    choices = []

    for number in range(1, 5):

        while True:

            choice = read_text(
                f"보기 {number}: "
            )

            if choice in choices:

                ui.message(
                    "중복된 보기입니다.",
                    "red",
                )

                continue

            choices.append(choice)
            break

    print()

    answer = read_int(
        "정답 번호 (1~4): ",
        1,
        4,
    )

    level = read_int(
        "난이도 (1=초급, 2=중급): ",
        1,
        2,
    )

    difficulty = (
        "beginner"
        if level == 1
        else "intermediate"
    )

    print()

    category = read_text("분야: ")
    hint = read_text("힌트: ")
    explanation = read_text("해설: ")

    quiz = Quiz(
        id=game.next_quiz_id(),
        difficulty=difficulty,
        category=category,
        question=question,
        choices=choices,
        answer=answer,
        hint=hint,
        explanation=explanation,
    )

    quiz_id = game.add_quiz(quiz)

    ui.message(
        f"문제 등록 완료! ID: {quiz_id}",
        "green",
    )

    ui.field(
        "전체 등록 문제",
        f"{len(game.list_quizzes())}개",
        "cyan",
    )

    save_state(game, storage)


def list_questions(game):

    quizzes = game.list_quizzes()

    ui.header("QUESTION LIST")

    if not quizzes:

        ui.message(
            "등록된 문제가 없습니다.",
            "yellow",
        )

        return

    for quiz in quizzes:

        level = LEVEL_NAMES[quiz.difficulty]

        color = (
            "green"
            if quiz.difficulty == "beginner"
            else "yellow"
        )

        print(
            ui.paint(
                f"[{quiz.id:03d}]",
                "cyan",
                True,
            )
            + " "
            + ui.paint(
                f"[{level}]",
                color,
            )
            + " "
            + quiz.question
        )

        print()

    ui.line()

    ui.field(
        "전체 등록 문제",
        f"{len(quizzes)}개",
        "cyan",
    )

    print()


def show_score(game):

    ui.header("BEST SCORE")

    if game.best_score is None:

        ui.message(
            "아직 완료된 게임 기록이 없습니다.",
            "yellow",
        )

    else:

        ui.field(
            "최고 점수",
            f"{game.best_score:.1f} / 100점",
            "purple",
        )

        print()

        ui.score_bar(game.best_score)

    print()
    ui.line("=")
    print()


def remove_question(game, storage=None):

    quizzes = game.list_quizzes()

    if not quizzes:

        ui.message(
            "삭제할 문제가 없습니다.",
            "yellow",
        )

        return game

    ui.header("DELETE QUESTION", color="red")

    list_questions(game)

    valid_ids = {
        quiz.id
        for quiz in quizzes
    }

    while True:

        quiz_id = read_int(
            "삭제할 문제 ID (0=취소): ",
            0,
            max(valid_ids),
        )

        if quiz_id == 0:

            ui.message(
                "삭제를 취소했습니다.",
                "yellow",
            )

            return game

        if quiz_id in valid_ids:
            break

        ui.message(
            "존재하지 않는 문제 ID입니다.",
            "red",
        )

    selected = next(
        quiz
        for quiz in quizzes
        if quiz.id == quiz_id
    )

    ui.message(
        f"삭제 대상: {selected.question}",
        "red",
    )

    while True:

        answer = ui.prompt(
            "정말 삭제하시겠습니까? (Y/N): "
        ).strip().upper()

        if answer == "N":

            ui.message(
                "삭제를 취소했습니다.",
                "yellow",
            )

            return game

        if answer == "Y":
            break

        ui.message(
            "Y 또는 N을 입력하세요.",
            "red",
        )

    replacement = delete_question(
        game,
        quiz_id,
    )

    if not save_state(replacement, storage):

        ui.message(
            "저장 실패로 삭제를 취소합니다.",
            "red",
        )

        return game

    ui.message(
        f"문제 삭제 완료! ID: {quiz_id}",
        "green",
    )

    ui.field(
        "전체 등록 문제",
        f"{len(replacement.list_quizzes())}개",
        "cyan",
    )

    return replacement


def show_history(game):

    records = get_history(game)

    summary = history_summary(game)

    ui.header("PLAY HISTORY")

    if not records:

        ui.message(
            "아직 완료된 플레이 이력이 없습니다.",
            "yellow",
        )

        return

    ui.field(
        "완료 게임",
        f"{summary['count']}회",
        "cyan",
    )

    ui.field(
        "평균 점수",
        f"{summary['average']:.1f}점",
        "blue",
    )

    if summary["best"] is not None:

        ui.field(
            "최고 점수",
            f"{summary['best']:.1f}점",
            "purple",
        )

    print()
    ui.line()

    print(
        ui.paint(
            f"{'No.':>4} "
            f"{'Date / Time':<19} "
            f"{'N':>3} "
            f"{'OK':>3} "
            f"{'NG':>3} "
            f"{'Hint':>4} "
            f"{'Score':>6} "
            f"{'Acc%':>6}",
            "yellow",
            True,
        )
    )

    ui.line()

    for number, record in enumerate(
        records,
        start=1,
    ):

        stamp = (
            record["played_at"][:19]
            .replace("T", " ")
        )

        print(
            f"{number:>4} "
            f"{stamp:<19} "
            f"{record['total_questions']:>3} "
            + ui.paint(
                f"{record['correct_count']:>3}",
                "blue",
            )
            + " "
            + ui.paint(
                f"{record['wrong_count']:>3}",
                "red",
            )
            + " "
            + ui.paint(
                f"{record['hint_count']:>4}",
                "yellow",
            )
            + " "
            + ui.paint(
                f"{record['score']:>6.1f}",
                "blue",
            )
            + f" {record['accuracy']:>6.1f}"
        )

    ui.line("=")
    print()


def run_menu(game, storage=None):

    try:

        while True:

            show_menu(game)

            choice = read_int(
                "메뉴 선택 (0~6): ",
                0,
                6,
            )

            if choice == 0:

                if not save_state(game, storage):

                    ui.message(
                        "저장하지 못했습니다. "
                        "다시 종료를 시도하세요.",
                        "red",
                    )

                    continue

                ui.message(
                    "프로그램을 종료합니다.",
                    "cyan",
                )

                return 0

            try:

                if choice == 1:
                    play_quiz(game, storage)

                elif choice == 2:
                    add_question(game, storage)

                elif choice == 3:
                    list_questions(game)

                elif choice == 4:
                    show_score(game)

                elif choice == 5:

                    game = remove_question(
                        game,
                        storage,
                    )

                elif choice == 6:
                    show_history(game)

            except (ValueError, RuntimeError) as error:

                game.cancel_game()

                ui.message(
                    f"오류: {error}",
                    "red",
                )

    except (KeyboardInterrupt, EOFError):

        game.cancel_game()

        ui.message(
            "입력이 중단되었습니다.",
            "yellow",
        )

        if save_state(game, storage):

            ui.message(
                "프로그램을 안전하게 종료합니다.",
                "cyan",
            )

            return 0

        ui.message(
            "저장 실패 상태로 프로그램을 종료합니다.",
            "red",
        )

        return 1


def main():

    storage = QuizStorage()

    try:

        game = storage.load()

    except (OSError, ValueError) as error:

        ui.message(
            f"퀴즈 데이터를 불러올 수 없습니다: {error}",
            "red",
        )

        return 1

    if storage.last_warning:

        ui.message(
            f"경고: {storage.last_warning}",
            "yellow",
        )

    ui.message(
        f"퀴즈 데이터 로드 완료: "
        f"{len(game.list_quizzes())}개",
        "green",
    )

    if not save_state(game, storage):
        return 1

    return run_menu(game, storage)


if __name__ == "__main__":
    sys.exit(main())
