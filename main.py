"""Console interface for the machine tool vibration quiz."""

import sys

from quiz import Quiz
from quiz_game import QuizGame


LINE = "=" * 58
SUBLINE = "-" * 58

LEVEL_NAMES = {
    "beginner": "초급",
    "intermediate": "중급",
}


def read_text(prompt):
    """Read a non-empty string."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("빈칸은 입력할 수 없습니다.")


def read_int(prompt, minimum, maximum):
    """Read an integer within the allowed range."""

    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(
            f"{minimum}~{maximum} 사이의 "
            "숫자를 입력하세요."
        )


def show_menu(game):
    """Display the main engineering dashboard."""

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

    print()
    print(LINE)
    print("       MACHINE TOOL & VIBRATION QUIZ")
    print("       CODYSSEY AI ALL-IN-ONE | M_E1-2")
    print(LINE)

    print(f" 등록 문제 : {len(quizzes)}개")
    print(f" 초급 / 중급 : {beginner} / {intermediate}")
    print(f" 최고 점수 : {best}")

    print(SUBLINE)
    print(" [1] 퀴즈 풀기 (Play)")
    print(" [2] 문제 추가 (Add)")
    print(" [3] 문제 목록 (List)")
    print(" [4] 최고 점수 (Score)")
    print(" [0] 프로그램 종료 (Exit)")
    print(SUBLINE)


def show_question(game):
    """Display the current question and choices."""

    quiz = game.current_quiz

    print()
    print(LINE)

    print(
        f" QUESTION "
        f"{game.question_number:02d}"
        f" / {game.total_questions:02d}"
    )

    print(
        f" 난이도: {LEVEL_NAMES[quiz.difficulty]}"
        f" | 분야: {quiz.category}"
    )

    print(SUBLINE)
    print(quiz.question)
    print()

    for number, choice in enumerate(
        quiz.choices,
        start=1,
    ):
        print(f" [{number}] {choice}")

    print(SUBLINE)


def show_result(result):
    """Display the completed game result."""

    print()
    print(LINE)
    print("              GAME RESULT")
    print(LINE)

    print(
        f" 출제 문제 : "
        f"{result['total_questions']}개"
    )

    print(
        f" 정답 / 오답 : "
        f"{result['correct_count']} / "
        f"{result['wrong_count']}"
    )

    print(
        f" 힌트 사용 : "
        f"{result['hint_count']}회"
    )

    print(
        f" 획득 점수 : "
        f"{result['earned_points']} / "
        f"{result['max_points']}"
    )

    print(
        f" 최종 점수 : "
        f"{result['score']:.1f} / 100점"
    )

    print(
        f" 정답률 : "
        f"{result['accuracy']:.1f}%"
    )

    print(
        f" 최고 점수 : "
        f"{result['best_score']:.1f}점"
    )

    if result["new_best"]:
        print(" NEW BEST SCORE!")

    print(LINE)


def play_quiz(game):
    """Run an interactive quiz session."""

    available = len(game.list_quizzes())

    if available == 0:
        print("등록된 문제가 없습니다.")
        return

    print()
    print("===== QUIZ PLAY =====")

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

            value = input(
                "정답 번호 (1~4), H=힌트, Q=취소: "
            ).strip().upper()

            if value == "H":

                print(f"힌트: {game.use_hint()}")
                print("힌트 사용 후 정답은 5점입니다.")

                continue

            if value == "Q":

                game.cancel_game()
                print("게임을 취소했습니다.")

                return

            try:
                answer = int(value)

                result = game.submit_answer(
                    answer
                )

            except ValueError:
                print("1~4, H 또는 Q를 입력하세요.")
                continue

            if result["correct"]:
                print(
                    f"정답입니다! "
                    f"+{result['points']}점"
                )
            else:
                print("오답입니다. +0점")

            print(
                f"정답: "
                f"{result['correct_answer']}. "
                f"{result['correct_choice']}"
            )

            print(
                f"해설: {result['explanation']}"
            )

            break

    show_result(game.get_result())


def add_question(game):
    """Read and register a new question."""

    print()
    print("===== ADD QUESTION =====")

    question = read_text("문제 내용: ")

    if any(
        q.question.strip().casefold()
        == question.casefold()
        for q in game.list_quizzes()
    ):
        print("이미 등록된 문제입니다.")
        return

    choices = []

    for number in range(1, 5):

        while True:

            choice = read_text(
                f"보기 {number}: "
            )

            if choice in choices:
                print("중복된 보기입니다.")
                continue

            choices.append(choice)
            break

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

    print()
    print(f"문제 등록 완료! ID: {quiz_id}")
    print(
        f"전체 등록 문제: "
        f"{len(game.list_quizzes())}개"
    )


def list_questions(game):
    """Display all registered questions."""

    quizzes = game.list_quizzes()

    print()
    print(LINE)
    print("              QUESTION LIST")
    print(LINE)

    if not quizzes:
        print("등록된 문제가 없습니다.")
        return

    for quiz in quizzes:

        level = LEVEL_NAMES[quiz.difficulty]

        print(
            f"[{quiz.id:03d}] "
            f"[{level}] "
            f"{quiz.question}"
        )

    print(SUBLINE)
    print(f"전체 등록 문제: {len(quizzes)}개")


def show_score(game):
    """Display the best score."""

    print()
    print(LINE)
    print("              BEST SCORE")
    print(LINE)

    if game.best_score is None:
        print("아직 완료된 게임 기록이 없습니다.")

    else:
        print(
            f"최고 점수: "
            f"{game.best_score:.1f} / 100점"
        )

    print(LINE)


def run_menu(game):
    """Run the main menu until the user exits."""

    actions = {
        1: play_quiz,
        2: add_question,
        3: list_questions,
        4: show_score,
    }

    try:

        while True:

            show_menu(game)

            choice = read_int(
                "메뉴 선택 (0~4): ",
                0,
                4,
            )

            if choice == 0:
                print("프로그램을 종료합니다.")
                return

            try:
                actions[choice](game)

            except (ValueError, RuntimeError) as error:

                game.cancel_game()

                print(f"오류: {error}")

    except (KeyboardInterrupt, EOFError):

        game.cancel_game()

        print()
        print("입력이 중단되었습니다.")
        print("프로그램을 안전하게 종료합니다.")


def main():
    """Initialize the game and launch the menu."""

    game = QuizGame()

    try:
        game.load_default_quizzes()

    except (OSError, ValueError) as error:

        print(
            f"기본 퀴즈를 불러올 수 없습니다: "
            f"{error}"
        )

        return 1

    run_menu(game)

    return 0


if __name__ == "__main__":
    sys.exit(main())
