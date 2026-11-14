"""Console interface for the machine tool vibration quiz."""

import sys

from history import (
    delete_question,
    get_history,
    history_summary,
    record_game,
)

from quiz import Quiz
from quiz_game import QuizGame
from storage import QuizStorage


LINE = "=" * 66
SUBLINE = "-" * 66

LEVEL_NAMES = {
    "beginner": "초급",
    "intermediate": "중급",
}


def read_text(prompt):

    while True:

        value = input(prompt).strip()

        if value:
            return value

        print("빈칸은 입력할 수 없습니다.")


def read_int(prompt, minimum, maximum):

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


def save_state(game, storage):

    if storage is None:
        return True

    try:

        storage.save(game)

        print("데이터 저장 완료: state.json")

        return True

    except (OSError, ValueError, RuntimeError) as error:

        print(f"저장 실패: {error}")
        print("현재 실행 중인 데이터는 메모리에 유지됩니다.")

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

    print()
    print(LINE)
    print("           MACHINE TOOL & VIBRATION QUIZ")
    print("           CODYSSEY AI ALL-IN-ONE | M_E1-2")
    print(LINE)

    print(f" 등록 문제 : {len(quizzes)}개")
    print(f" 초급 / 중급 : {beginner} / {intermediate}")
    print(f" 최고 점수 : {best}")
    print(f" 완료 게임 : {len(get_history(game))}회")

    print(SUBLINE)
    print(" [1] 퀴즈 풀기 (Play)")
    print(" [2] 문제 추가 (Add)")
    print(" [3] 문제 목록 (List)")
    print(" [4] 최고 점수 (Score)")
    print(" [5] 문제 삭제 (Delete)")
    print(" [6] 플레이 이력 (History)")
    print(" [0] 프로그램 종료 (Exit)")
    print(SUBLINE)


def show_question(game):

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

    print()
    print(LINE)
    print("                   GAME RESULT")
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


def play_quiz(game, storage=None):

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

    result = game.get_result()

    record_game(game, result)

    show_result(result)

    save_state(game, storage)


def add_question(game, storage=None):

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

    save_state(game, storage)


def list_questions(game):

    quizzes = game.list_quizzes()

    print()
    print(LINE)
    print("                   QUESTION LIST")
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

    print()
    print(LINE)
    print("                   BEST SCORE")
    print(LINE)

    if game.best_score is None:

        print("아직 완료된 게임 기록이 없습니다.")

    else:

        print(
            f"최고 점수: "
            f"{game.best_score:.1f} / 100점"
        )

    print(LINE)


def remove_question(game, storage=None):

    quizzes = game.list_quizzes()

    if not quizzes:

        print("삭제할 문제가 없습니다.")

        return game

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

            print("삭제를 취소했습니다.")

            return game

        if quiz_id in valid_ids:
            break

        print("존재하지 않는 문제 ID입니다.")

    selected = next(
        quiz
        for quiz in quizzes
        if quiz.id == quiz_id
    )

    print(f"삭제 대상: {selected.question}")

    while True:

        answer = input(
            "정말 삭제하시겠습니까? (Y/N): "
        ).strip().upper()

        if answer == "N":

            print("삭제를 취소했습니다.")

            return game

        if answer == "Y":
            break

        print("Y 또는 N을 입력하세요.")

    replacement = delete_question(
        game,
        quiz_id,
    )

    if not save_state(replacement, storage):

        print("저장 실패로 삭제를 취소합니다.")

        return game

    print(f"문제 삭제 완료! ID: {quiz_id}")

    print(
        f"전체 등록 문제: "
        f"{len(replacement.list_quizzes())}개"
    )

    return replacement


def show_history(game):

    records = get_history(game)

    summary = history_summary(game)

    print()
    print(LINE)
    print("                   PLAY HISTORY")
    print(LINE)

    if not records:

        print("아직 완료된 플레이 이력이 없습니다.")

        return

    print(f" 완료 게임 : {summary['count']}회")
    print(f" 평균 점수 : {summary['average']:.1f}점")

    if summary["best"] is not None:

        print(f" 최고 점수 : {summary['best']:.1f}점")

    print(SUBLINE)

    print(
        f"{'No.':>4} "
        f"{'Date / Time':<19} "
        f"{'N':>3} "
        f"{'OK':>3} "
        f"{'NG':>3} "
        f"{'Hint':>4} "
        f"{'Score':>6} "
        f"{'Acc%':>6}"
    )

    print(SUBLINE)

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
            f"{record['correct_count']:>3} "
            f"{record['wrong_count']:>3} "
            f"{record['hint_count']:>4} "
            f"{record['score']:>6.1f} "
            f"{record['accuracy']:>6.1f}"
        )

    print(LINE)


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

                    print(
                        "저장하지 못했습니다. "
                        "메뉴에서 다시 종료를 시도하세요."
                    )

                    continue

                print("프로그램을 종료합니다.")

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

                print(f"오류: {error}")

    except (KeyboardInterrupt, EOFError):

        game.cancel_game()

        print()
        print("입력이 중단되었습니다.")

        if save_state(game, storage):

            print("프로그램을 안전하게 종료합니다.")

            return 0

        print("저장 실패 상태로 프로그램을 종료합니다.")

        return 1


def main():

    storage = QuizStorage()

    try:

        game = storage.load()

    except (OSError, ValueError) as error:

        print(
            f"퀴즈 데이터를 불러올 수 없습니다: "
            f"{error}"
        )

        return 1

    if storage.last_warning:

        print(f"경고: {storage.last_warning}")

    print(
        f"퀴즈 데이터 로드 완료: "
        f"{len(game.list_quizzes())}개"
    )

    if not save_state(game, storage):
        return 1

    return run_menu(game, storage)


if __name__ == "__main__":
    sys.exit(main())
