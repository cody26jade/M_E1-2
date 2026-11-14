# Actual Application Execution Evidence

## NEITO Evaluation Criterion #1

This document contains actual console output
captured by executing the Python application.
It is direct runtime evidence, not sample output
or a description of expected behavior.

The application was executed in an independent
local Git clone of the submitted source commit.
Automated keyboard inputs were supplied through
standard input. Console output was captured
directly from the running Python process.

Only ANSI terminal color sequences were removed
for readability. Runtime output was not invented.

## 1. Execution Environment

- Execution date: 2026-11-15T00:38:48.172926+09:00
- Python version: 3.12.10
- Operating system: Windows
- Source commit: 94dbbe77662abbb1c70f1daaf50eaac157ded41e
- Application command: `python main.py`
- Execution method: actual subprocess execution

## 2. Actual Main Menu Startup and Exit

Executed command:

    python main.py

Actual keyboard input sequence:

    0

Actual console output (stdout):


    퀴즈 데이터 로드 완료: 20개


    데이터 저장 완료: state.json


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 기록 없음
     완료 게임 : 0회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    데이터 저장 완료: state.json


    프로그램을 종료합니다.


Process exit code: 0

## 3. Actual Quiz List

Executed command:

    python main.py

Actual keyboard input sequence:

    3
    0

Actual console output (stdout):


    퀴즈 데이터 로드 완료: 20개


    데이터 저장 완료: state.json


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 기록 없음
     완료 게임 : 0회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    ==================================================================
    QUESTION LIST
    ==================================================================

    [001] [초급] CNC의 의미는 무엇인가?

    [002] [초급] 머시닝센터 주축(Spindle)의 주요 역할은 무엇인가?

    [003] [초급] ATC의 주요 기능은 무엇인가?

    [004] [초급] 볼스크루(Ball Screw)의 주요 역할은 무엇인가?

    [005] [초급] 진동 가속도의 SI 단위는 무엇인가?

    [006] [초급] 주파수의 단위는 무엇인가?

    [007] [초급] RMS가 의미하는 것은 무엇인가?

    [008] [초급] FFT를 이용하는 주요 목적은 무엇인가?

    [009] [초급] 주축이 3000 rpm으로 회전할 때 회전주파수는 얼마인가?

    [010] [초급] 공진(Resonance)이 발생하기 쉬운 조건은 무엇인가?

    [011] [중급] 샘플링 주파수가 25.6 kHz일 때 1초 동안 취득하는 샘플 수는 얼마인가?

    [012] [중급] 샘플링 주파수가 25.6 kHz일 때 나이퀴스트 주파수는 얼마인가?

    [013] [중급] 10초 동안 측정한 신호 전체를 FFT할 때 기본 주파수 빈 간격은 얼마인가?

    [014] [중급] 회전체 불평형에서 대표적으로 관찰되는 진동 성분은 무엇인가?

    [015] [중급] BPFO는 어떤 베어링 결함과 관련된 주파수인가?

    [016] [중급] BPFI는 어떤 베어링 결함과 관련된 주파수인가?

    [017] [중급] 포락선 분석(Envelope Analysis)의 주요 활용 목적은 무엇인가?

    [018] [중급] 주파수 f에서 가속도 진폭 A를 속도 진폭 V로 변환하는 식은 무엇인가?

    [019] [중급] 3축 가속도 센서를 사용하는 주요 장점은 무엇인가?

    [020] [중급] 측정 피크와 베어링 이론 결함주파수가 일치할 때 가장 적절한 판단은 무엇인가?

    ------------------------------------------------------------------
     전체 등록 문제 : 20개


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 기록 없음
     완료 게임 : 0회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    데이터 저장 완료: state.json


    프로그램을 종료합니다.


Process exit code: 0

## 4. Actual Quiz Gameplay

Executed command:

    python main.py

Actual keyboard input sequence:

    1
    1
    1
    0

Actual console output (stdout):


    퀴즈 데이터 로드 완료: 20개


    데이터 저장 완료: state.json


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 기록 없음
     완료 게임 : 0회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    ==================================================================
    QUIZ PLAY
    ==================================================================

    출제 문제 수 (1~20):
    ==================================================================
    QUESTION 01 / 01
    ==================================================================

     [##############################] 100%

     난이도 : 중급
     분야 : 회전체 진동

    ------------------------------------------------------------------

    회전체 불평형에서 대표적으로 관찰되는 진동 성분은 무엇인가?

     [1]  항상 1000 Hz

     [2]  항상 0 Hz

     [3]  샘플링 주파수

     [4]  회전주파수 1X

    ------------------------------------------------------------------
    [H] 힌트     [Q] 게임 취소

    정답 번호 (1~4), H=힌트, Q=취소:
    ------------------------------------------------------------------

    INCORRECT! 오답입니다. +0점

     선택 : 1. 항상 1000 Hz
     정답 : 4. 회전주파수 1X

    해설
    불평형은 일반적으로 회전주파수 1X 성분을 발생시키지만 1X 성분만으로 불평형을 확정할 수는 없습니다.

    ------------------------------------------------------------------


    ==================================================================
    GAME RESULT
    ==================================================================

     최종 점수 : 0.0 / 100점

     [------------------------------] 0%

    ------------------------------------------------------------------

     출제 문제 : 1개
     정답 : 0개
     오답 : 1개
     힌트 사용 : 0회
     획득 점수 : 0 / 10
     정답률 : 0.0%
     최고 점수 : 0.0점

    *** NEW BEST SCORE! ***


    ==================================================================


    데이터 저장 완료: state.json


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 0.0점
     완료 게임 : 1회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    데이터 저장 완료: state.json


    프로그램을 종료합니다.


Process exit code: 0

## 5. Actual Restart, Best Score and Play History

Executed command:

    python main.py

Actual keyboard input sequence:

    4
    6
    0

Actual console output (stdout):


    퀴즈 데이터 로드 완료: 20개


    데이터 저장 완료: state.json


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 0.0점
     완료 게임 : 1회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    ==================================================================
    BEST SCORE
    ==================================================================

     최고 점수 : 0.0 / 100점

     [------------------------------] 0%

    ==================================================================


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 0.0점
     완료 게임 : 1회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    ==================================================================
    PLAY HISTORY
    ==================================================================

     완료 게임 : 1회
     평균 점수 : 0.0점
     최고 점수 : 0.0점

    ------------------------------------------------------------------
     No. Date / Time           N  OK  NG Hint  Score   Acc%
    ------------------------------------------------------------------
       1 2026-11-15 00:38:48   1   0   1    0    0.0    0.0
    ==================================================================


    ==================================================================
    MACHINE TOOL & VIBRATION QUIZ
    CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==================================================================

     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 0.0점
     완료 게임 : 1회

    ------------------------------------------------------------------
     MAIN MENU

     [1]  퀴즈 풀기 (Play)
     [2]  문제 추가 (Add)
     [3]  문제 목록 (List)
     [4]  최고 점수 (Score)
     [5]  문제 삭제 (Delete)
     [6]  플레이 이력 (History)

     [0]  프로그램 종료 (Exit)

    ------------------------------------------------------------------

    메뉴 선택 (0~6):
    데이터 저장 완료: state.json


    프로그램을 종료합니다.


Process exit code: 0

## 6. Actual Runtime Verification Results

| Verification | Actual result |
|---|---|
| Main menu execution | PASS |
| Questions listed | 20 |
| Quiz gameplay | PASS |
| Score display | PASS |
| History display | PASS |
| Application restart | PASS |
| Persisted questions | 20 |
| Persisted best score | 0.0 |
| Persisted history count | 1 |
| State preserved after restart | PASS |
| All process exit codes | 0 |

Actual saved gameplay record:

    {
      "played_at": "2026-11-15T00:38:48+09:00",
      "total_questions": 1,
      "correct_count": 0,
      "wrong_count": 1,
      "hint_count": 0,
      "score": 0.0,
      "accuracy": 0.0
    }

## 7. Original Data Protection

The runtime evidence was collected in an isolated
Git clone. The original project state.json was
not used for the gameplay execution.

## 8. Related Evidence

- [Application source](../main.py)
- [Raw execution log](../logs/R08_actual_execution.txt)
- [Evaluation evidence](EVALUATION_EVIDENCE.md)
- [Main menu screenshot](../screenshots/03_Quiz_Main_Menu.png)
