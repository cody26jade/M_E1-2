# M_E1-2 Evaluation Evidence

## 1. Evidence Policy

This document connects the application source code,
automated tests, and actual execution logs.

Execution results are taken from recorded
development sessions, not simulated results.

Windows user directory names may be masked
for privacy.

The screenshots are separate manual execution evidence.

## 2. Requirement Traceability

| Requirement | Implementation | Execution evidence |
|---|---|---|
| Python development environment | Python 3.10+ | [STEP01](../logs/01_development_environment.txt) |
| Git initialization | .gitignore and Git repository | [STEP02](../logs/02_project_structure_git.txt) |
| Original quiz questions | [Default dataset](../data/default_quizzes.json) | [STEP03](../logs/03_quiz_dataset_creation.txt) |
| Quiz class | [quiz.py](../quiz.py) | [STEP04](../logs/04_quiz_class_development.txt) |
| QuizGame class | [quiz_game.py](../quiz_game.py) | [STEP05](../logs/05_quizgame_development.txt) |
| Interactive menu | [main.py](../main.py) | [STEP06](../logs/06_console_development.txt) |
| Play quiz | [main.py](../main.py) | [Integration tests](../logs/11_integration_tests.txt) |
| Add question | [main.py](../main.py) | [Integration tests](../logs/11_integration_tests.txt) |
| List questions | [main.py](../main.py) | [Integration tests](../logs/11_integration_tests.txt) |
| Best score | [quiz_game.py](../quiz_game.py) | [Integration tests](../logs/11_integration_tests.txt) |
| JSON persistence | [storage.py](../storage.py) | [STEP07](../logs/07_json_persistence.txt) |
| Random questions | [quiz_game.py](../quiz_game.py) | [STEP08](../logs/08_bonus_features.txt) |
| Question count | [main.py](../main.py) | [STEP08](../logs/08_bonus_features.txt) |
| Hint and deduction | [quiz_game.py](../quiz_game.py) | [STEP08](../logs/08_bonus_features.txt) |
| Delete question | [main.py](../main.py) | [Integration tests](../logs/11_integration_tests.txt) |
| Play history | [history.py](../history.py) | [STEP08](../logs/08_bonus_features.txt) |
| Console UI | [console_ui.py](../console_ui.py) | [STEP08A](../logs/08A_console_ui.txt) |
| Question color | [console_ui.py](../console_ui.py) | [STEP08B](../logs/08B_question_color.txt) |
| Exception handling | [main.py](../main.py) | [STEP09](../logs/09_stability.txt) |
| Git push | Public GitHub repository | [STEP10B](../logs/10B_github_remote.txt) |
| Clone and merge | [Collaboration guide](COLLABORATION.md) | [STEP10C](../logs/10C_git_collaboration.txt) |
| Git pull | Original repository | [STEP10D](../logs/10D_git_pull.txt) |
| Ten or more commits | Git history | [STEP10D](../logs/10D_git_pull.txt) |
| Automated tests | [Test directory](../tests/) | [STEP11](../logs/11_integration_tests.txt) |
| README | [README.md](../README.md) | Final documentation |
| Screenshots | [Screenshot directory](../screenshots/) | [STEP12A](../logs/12A_screenshot_verification.txt) |

## 3. Actual Execution Records

The following sections reproduce the recorded
execution logs as indented Markdown code blocks.

### 01_development_environment.txt

[Original execution log](../logs/01_development_environment.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP01 - Development Environment
    Date: 2026-11-14 22:17:11

    01. Verify Project Directory

    > Get-Location

        if ((Get-Location).Path -ne "C:\2026Codyssey_AllInOne\M_E1-2") {
            throw "Incorrect project directory."
        }

        "PASS: Project directory verified"

    Path
    ----
    C:\2026Codyssey_AllInOne\M_E1-2
    PASS: Project directory verified
    Failed: False

    02. Verify Windows and PowerShell

    > "WINDOWS: $([System.Environment]::OSVersion.VersionString)"

        "POWERSHELL: $($PSVersionTable.PSVersion)"

        "PASS: Windows and PowerShell verified"
    WINDOWS: Microsoft Windows NT 10.0.26200.0
    POWERSHELL: 5.1.26100.9711
    PASS: Windows and PowerShell verified
    Failed: False

    03. Verify Python Version

    > python --version

        if ($LASTEXITCODE -ne 0) {
            throw "Python execution failed."
        }

        python -c "import sys; assert sys.version_info >= (3, 10); print('PASS: Python 3.10 or later')"

        if ($LASTEXITCODE -ne 0) {
            throw "Python version requirement failed."
        }
    Python 3.12.10
    PASS: Python 3.10 or later
    Failed: False

    04. Verify Python Standard Libraries

    > python -c "import json, random, pathlib, datetime, unittest; print('PASS: Required standard libraries available')"

        if ($LASTEXITCODE -ne 0) {
            throw "Python library verification failed."
        }
    PASS: Required standard libraries available
    Failed: False

    05. Verify Git

    > git --version

        if ($LASTEXITCODE -ne 0) {
            throw "Git verification failed."
        }

        "PASS: Git available"
    git version 2.56.0.windows.4
    PASS: Git available
    Failed: False

    06. Verify VS Code

    > code --version

        if ($LASTEXITCODE -ne 0) {
            throw "VS Code verification failed."
        }

        "PASS: VS Code available"
    1.146.0
    69047191fc427f2f92828279aae1d90d8eeda7ab
    x64
    PASS: VS Code available
    Failed: False

    07. Verify ZETA Report

    > Get-Command Start-MissionReport,
            Add-MissionStep,
            Show-MissionReport,
            zeta-copy -ErrorAction Stop |
            Select-Object Name, CommandType |
            Format-Table -AutoSize

        "PASS: ZETA Report functions available"

    Name                CommandType
    ----                -----------
    Start-MissionReport    Function
    Add-MissionStep        Function
    Show-MissionReport     Function
    zeta-copy              Function


    PASS: ZETA Report functions available
    Failed: False

    08. Create Evidence Directories

    > New-Item -ItemType Directory -Path ".\screenshots" -Force |
            Out-Null

        New-Item -ItemType Directory -Path ".\logs" -Force |
            Out-Null

        Get-ChildItem -Directory -Force |
            Select-Object Name

        "PASS: Evidence directories ready"

    Name
    ----
    logs
    screenshots
    PASS: Evidence directories ready
    Failed: False

    09. Verify Existing Project Files

    > Get-ChildItem -Force |
            Select-Object Mode, Name, Length |
            Format-Table -AutoSize

        "PASS: Project directory inspected"

    Mode   Name        Length
    ----   ----        ------
    d----- logs
    d----- screenshots


    PASS: Project directory inspected
    Failed: False



### 02_project_structure_git.txt

[Original execution log](../logs/02_project_structure_git.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP02 - Project Structure and Git Initialization
    Date: 2026-11-14 22:20:22

    01. Verify Project Directory

    > if ((Get-Location).Path -ne "C:\2026Codyssey_AllInOne\M_E1-2") {
            throw "Incorrect project directory."
        }

        Get-Location

        "PASS: Project directory verified"

    Path
    ----
    C:\2026Codyssey_AllInOne\M_E1-2
    PASS: Project directory verified
    Failed: False

    02. Create Project Directories

    > $folders = @(
            "data",
            "tests",
            "logs",
            "screenshots"
        )

        foreach ($folder in $folders) {

            New-Item -ItemType Directory -Path $folder -Force -ErrorAction Stop |
                Out-Null

            "READY: $folder"
        }

        "PASS: Project directories ready"
    READY: data
    READY: tests
    READY: logs
    READY: screenshots
    PASS: Project directories ready
    Failed: False

    03. Save STEP01 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP01*Development*Environment*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP01 execution log not found."
        }

        $content = Get-Content -LiteralPath $source.FullName -Raw -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP01 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 9) {
            throw "Expected nine successful STEP01 results."
        }

        $content = $content -replace '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', '${1}<USER>'

        $target = Join-Path (Get-Location).Path "logs\01_development_environment.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $target,
            $content,
            $utf8
        )

        Get-Item -LiteralPath $target |
            Select-Object Name, Length

        "PASS: Actual STEP01 execution evidence saved"

    Name                           Length
    ----                           ------
    01_development_environment.txt   3210
    PASS: Actual STEP01 execution evidence saved
    Failed: False

    04. Create Git Ignore Configuration

    > $path = Join-Path (Get-Location).Path ".gitignore"

        $content = @'
    # Python cache
    __pycache__/
    *.py[cod]

    # Virtual environments
    .venv/
    venv/

    # Local environment variables
    .env
    .env.*

    # Runtime user data
    state.json
    state.json.tmp
    state.json.corrupt-*

    # IDE and operating system
    .vscode/
    .DS_Store
    Thumbs.db

    # Test artifacts
    .coverage
    htmlcov/
    '@

        if (Test-Path -LiteralPath $path) {

            $existing = Get-Content -LiteralPath $path -Raw -Encoding UTF8

            if (($existing -replace "`r`n", "`n").TrimEnd() -ne
                ($content -replace "`r`n", "`n").TrimEnd()) {

                throw "Existing .gitignore differs. Review required."
            }

            "PASS: Existing .gitignore preserved"
        }
        else {

            $utf8 = New-Object System.Text.UTF8Encoding($false)

            [System.IO.File]::WriteAllText(
                $path,
                $content.TrimEnd() + "`n",
                $utf8
            )

            "PASS: Git ignore configuration created"
        }

        Get-Content -LiteralPath $path
    PASS: Git ignore configuration created
    # Python cache
    __pycache__/
    *.py[cod]

    # Virtual environments
    .venv/
    venv/

    # Local environment variables
    .env
    .env.*

    # Runtime user data
    state.json
    state.json.tmp
    state.json.corrupt-*

    # IDE and operating system
    .vscode/
    .DS_Store
    Thumbs.db

    # Test artifacts
    .coverage
    htmlcov/
    Failed: False

    05. Create Git Attributes

    > $path = Join-Path (Get-Location).Path ".gitattributes"

        $content = @'
    * text=auto

    *.py text eol=lf
    *.json text eol=lf
    *.md text eol=lf
    *.txt text eol=lf
    .gitattributes text eol=lf
    .gitignore text eol=lf

    *.png binary
    '@

        if (Test-Path -LiteralPath $path) {

            $existing = Get-Content -LiteralPath $path -Raw -Encoding UTF8

            if (($existing -replace "`r`n", "`n").TrimEnd() -ne
                ($content -replace "`r`n", "`n").TrimEnd()) {

                throw "Existing .gitattributes differs. Review required."
            }

            "PASS: Existing .gitattributes preserved"
        }
        else {

            $utf8 = New-Object System.Text.UTF8Encoding($false)

            [System.IO.File]::WriteAllText(
                $path,
                $content.TrimEnd() + "`n",
                $utf8
            )

            "PASS: Git attributes created"
        }

        Get-Content -LiteralPath $path
    PASS: Git attributes created
    * text=auto

    *.py text eol=lf
    *.json text eol=lf
    *.md text eol=lf
    *.txt text eol=lf
    .gitattributes text eol=lf
    .gitignore text eol=lf

    *.png binary
    Failed: False

    06. Create Initial README

    > $path = Join-Path (Get-Location).Path "README.md"

        $content = @'
    # M_E1-2

    ## Machine Tool and Vibration Analysis Quiz

    CODYSSEY AI ALL-IN-ONE Python Quiz Project

    ## Project Overview

    A Python console-based quiz application for learning
    machine tools and vibration analysis.

    ## Development Plan

    - Python 3.10 or later
    - Python standard library only
    - 20 default multiple-choice questions
    - Beginner and intermediate difficulty
    - Quiz and QuizGame classes
    - JSON-based data persistence
    - Best score and play history
    - Random questions and hints
    - Automated tests

    ## Development Status

    Project initialization in progress.

    ## Execution Evidence

    - [STEP01 - Development Environment](logs/01_development_environment.txt)

    Additional features and actual execution evidence
    will be documented during development.
    '@

        if (Test-Path -LiteralPath $path) {

            $existing = Get-Content -LiteralPath $path -Raw -Encoding UTF8

            if (($existing -replace "`r`n", "`n").TrimEnd() -ne
                ($content -replace "`r`n", "`n").TrimEnd()) {

                throw "Existing README differs. Review required."
            }

            "PASS: Existing README preserved"
        }
        else {

            $utf8 = New-Object System.Text.UTF8Encoding($false)

            [System.IO.File]::WriteAllText(
                $path,
                $content.TrimEnd() + "`n",
                $utf8
            )

            "PASS: Initial README created"
        }

        Get-Content -LiteralPath $path
    PASS: Initial README created
    # M_E1-2

    ## Machine Tool and Vibration Analysis Quiz

    CODYSSEY AI ALL-IN-ONE Python Quiz Project

    ## Project Overview

    A Python console-based quiz application for learning
    machine tools and vibration analysis.

    ## Development Plan

    - Python 3.10 or later
    - Python standard library only
    - 20 default multiple-choice questions
    - Beginner and intermediate difficulty
    - Quiz and QuizGame classes
    - JSON-based data persistence
    - Best score and play history
    - Random questions and hints
    - Automated tests

    ## Development Status

    Project initialization in progress.

    ## Execution Evidence

    - [STEP01 - Development Environment](logs/01_development_environment.txt)

    Additional features and actual execution evidence
    will be documented during development.
    Failed: False

    07. Initialize Git Repository

    > if (Test-Path ".\.git") {

            "PASS: Existing Git repository preserved"
        }
        else {

            git init -b main

            if ($LASTEXITCODE -ne 0) {
                throw "Git initialization failed."
            }
        }

        $root = git rev-parse --show-toplevel

        if ($LASTEXITCODE -ne 0 -or
            $root -ne "C:/2026Codyssey_AllInOne/M_E1-2") {

            throw "Unexpected Git repository root."
        }

        $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
            throw "Unexpected Git branch."
        }

        "BRANCH: $branch"

        "PASS: Git repository initialized"
    Initialized empty Git repository in C:/2026Codyssey_AllInOne/M_E1-2/.git/
    BRANCH: main
    PASS: Git repository initialized
    Failed: False

    08. Configure Local Git Identity

    > if (-not (Test-Path ".\.git")) {
            throw "Git repository not initialized."
        }

        $root = git rev-parse --show-toplevel

        if ($LASTEXITCODE -ne 0 -or
            $root -ne "C:/2026Codyssey_AllInOne/M_E1-2") {

            throw "Unexpected Git repository root."
        }

        $email = git -C "C:\2026Codyssey_AllInOne\M_E1-1" config --local user.email

        if ($LASTEXITCODE -ne 0 -or
            $email -notmatch '^\d+\+cody26jade@users\.noreply\.github\.com$') {

            throw "Verified GitHub noreply email not found."
        }

        git config --local user.name "cody26jade"

        if ($LASTEXITCODE -ne 0) {
            throw "Git username configuration failed."
        }

        git config --local user.email $email

        if ($LASTEXITCODE -ne 0) {
            throw "Git email configuration failed."
        }

        git config --local credential.username "cody26jade"

        if ($LASTEXITCODE -ne 0) {
            throw "Git credential username configuration failed."
        }

        git config --local credential.useHttpPath true

        if ($LASTEXITCODE -ne 0) {
            throw "Git credential configuration failed."
        }

        $name = git config --local user.name

        if ($LASTEXITCODE -ne 0 -or $name -ne "cody26jade") {
            throw "Git username verification failed."
        }

        $configuredEmail = git config --local user.email

        if ($LASTEXITCODE -ne 0 -or $configuredEmail -ne $email) {
            throw "Git email verification failed."
        }

        "GIT USER: $name"
        "EMAIL TYPE: GitHub noreply"

        "PASS: Repository-local Git identity configured"
        "PASS: GitHub noreply email verified"
        "PASS: Repository-specific credentials configured"
    GIT USER: cody26jade
    EMAIL TYPE: GitHub noreply
    PASS: Repository-local Git identity configured
    PASS: GitHub noreply email verified
    PASS: Repository-specific credentials configured
    Failed: False

    09. Verify Git Ignore Rules

    > git check-ignore --no-index state.json

        if ($LASTEXITCODE -ne 0) {
            throw "Runtime data ignore rule failed."
        }

        git check-ignore --no-index .env

        if ($LASTEXITCODE -ne 0) {
            throw "Environment file ignore rule failed."
        }

        git check-ignore --no-index __pycache__/quiz.pyc

        if ($LASTEXITCODE -ne 0) {
            throw "Python cache ignore rule failed."
        }

        "PASS: Git ignore rules verified"
    state.json
    .env
    __pycache__/quiz.pyc
    PASS: Git ignore rules verified
    Failed: False

    10. Verify Project Structure

    > Get-ChildItem -Force |
            Select-Object Mode, Name, Length |
            Format-Table -AutoSize

        git status --short --branch

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        "PASS: Initial project structure verified"

    Mode   Name           Length
    ----   ----           ------
    d--h-- .git
    d----- data
    d----- logs
    d----- screenshots
    d----- tests
    -a---- .gitattributes 148
    -a---- .gitignore     280
    -a---- README.md      748


    ## No commits yet on main
    ?? .gitattributes
    ?? .gitignore
    ?? README.md
    ?? logs/
    ?? screenshots/
    PASS: Initial project structure verified
    Failed: False



### 03_quiz_dataset_creation.txt

[Original execution log](../logs/03_quiz_dataset_creation.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP03 - Quiz Dataset Creation
    Date: 2026-11-14 22:26:53

    01. Verify Project Environment

    > if ((Get-Location).Path -ne "C:\2026Codyssey_AllInOne\M_E1-2") {
            throw "Incorrect project directory."
        }

        $required = @(
            ".git",
            ".gitignore",
            ".gitattributes",
            "README.md",
            "data",
            "tests",
            "logs",
            "screenshots",
            "logs/01_development_environment.txt"
        )

        foreach ($item in $required) {

            if (-not (Test-Path -LiteralPath $item)) {
                throw "Missing required item: $item"
            }

            "READY: $item"
        }

        "PASS: Project environment verified"
    READY: .git
    READY: .gitignore
    READY: .gitattributes
    READY: README.md
    READY: data
    READY: tests
    READY: logs
    READY: screenshots
    READY: logs/01_development_environment.txt
    PASS: Project environment verified
    Failed: False

    02. Save STEP02 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP02*Project*Structure*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP02 execution log not found."
        }

        $content = Get-Content -LiteralPath $source.FullName -Raw -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP02 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 10) {
            throw "Expected ten successful STEP02 results."
        }

        $content = $content -replace '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', '${1}<USER>'

        $target = Join-Path (Get-Location).Path "logs\02_project_structure_git.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $target,
            $content,
            $utf8
        )

        "PASS: Actual STEP02 execution evidence saved"
    PASS: Actual STEP02 execution evidence saved
    Failed: False

    03. Create Default Quiz Dataset

    > $path = Join-Path (Get-Location).Path "data\default_quizzes.json"

        if (Test-Path -LiteralPath $path) {
            throw "Quiz dataset already exists. Review required."
        }

        $content = @'
    [
        {
            "id": 1,
            "difficulty": "beginner",
            "category": "공작기계",
            "question": "CNC의 의미는 무엇인가?",
            "choices": [
                "Computer Numerical Control",
                "Central Network Computer",
                "Control Number Calculation",
                "Computer Noise Control"
            ],
            "answer": 1,
            "hint": "컴퓨터를 이용한 수치 제어를 의미합니다.",
            "explanation": "CNC는 Computer Numerical Control의 약자로 컴퓨터 수치 제어를 의미합니다."
        },
        {
            "id": 2,
            "difficulty": "beginner",
            "category": "공작기계",
            "question": "머시닝센터 주축(Spindle)의 주요 역할은 무엇인가?",
            "choices": [
                "절삭유 저장",
                "공구 회전 및 절삭 동력 전달",
                "공작물 세척",
                "기계 외부 조명 제어"
            ],
            "answer": 2,
            "hint": "절삭공구를 회전시키는 장치입니다.",
            "explanation": "머시닝센터 주축은 공구를 회전시키고 절삭에 필요한 동력을 전달합니다."
        },
        {
            "id": 3,
            "difficulty": "beginner",
            "category": "공작기계",
            "question": "ATC의 주요 기능은 무엇인가?",
            "choices": [
                "주축 온도 측정",
                "절삭유 냉각",
                "자동 공구 교환",
                "진동 데이터 저장"
            ],
            "answer": 3,
            "hint": "Automatic Tool Changer의 약자입니다.",
            "explanation": "ATC는 가공 프로그램에 따라 공구를 자동으로 교환하는 장치입니다."
        },
        {
            "id": 4,
            "difficulty": "beginner",
            "category": "공작기계",
            "question": "볼스크루(Ball Screw)의 주요 역할은 무엇인가?",
            "choices": [
                "전기에너지를 열에너지로 변환",
                "진동 신호 증폭",
                "공구 마모 측정",
                "회전운동을 직선운동으로 변환"
            ],
            "answer": 4,
            "hint": "이송축의 직선 이동에 사용됩니다.",
            "explanation": "볼스크루는 모터의 회전운동을 이송축의 직선운동으로 변환합니다."
        },
        {
            "id": 5,
            "difficulty": "beginner",
            "category": "진동 기초",
            "question": "진동 가속도의 SI 단위는 무엇인가?",
            "choices": [
                "m/s²",
                "mm",
                "Hz",
                "N"
            ],
            "answer": 1,
            "hint": "속도를 시간으로 미분한 물리량입니다.",
            "explanation": "가속도는 단위 시간당 속도 변화량으로 SI 단위는 m/s²입니다."
        },
        {
            "id": 6,
            "difficulty": "beginner",
            "category": "진동 기초",
            "question": "주파수의 단위는 무엇인가?",
            "choices": [
                "W",
                "Hz",
                "Pa",
                "kg"
            ],
            "answer": 2,
            "hint": "1초 동안 반복되는 횟수를 나타냅니다.",
            "explanation": "주파수의 단위는 헤르츠(Hz)이며 1 Hz는 초당 1회 반복을 의미합니다."
        },
        {
            "id": 7,
            "difficulty": "beginner",
            "category": "진동 기초",
            "question": "RMS가 의미하는 것은 무엇인가?",
            "choices": [
                "최댓값",
                "최솟값",
                "제곱평균제곱근",
                "주파수의 합계"
            ],
            "answer": 3,
            "hint": "Root Mean Square의 약자입니다.",
            "explanation": "RMS는 신호를 제곱하고 평균한 후 제곱근을 취한 값으로 진동 크기의 대표 지표입니다."
        },
        {
            "id": 8,
            "difficulty": "beginner",
            "category": "FFT 분석",
            "question": "FFT를 이용하는 주요 목적은 무엇인가?",
            "choices": [
                "센서의 무게 측정",
                "기계의 온도 감소",
                "데이터 파일 삭제",
                "시간영역 신호의 주파수 성분 분석"
            ],
            "answer": 4,
            "hint": "복합 진동 신호에 포함된 주파수를 분석합니다.",
            "explanation": "FFT는 이산 푸리에 변환을 효율적으로 계산하여 시간영역 신호의 주파수 성분을 분석합니다."
        },
        {
            "id": 9,
            "difficulty": "beginner",
            "category": "회전체 진동",
            "question": "주축이 3000 rpm으로 회전할 때 회전주파수는 얼마인가?",
            "choices": [
                "50 Hz",
                "30 Hz",
                "300 Hz",
                "3000 Hz"
            ],
            "answer": 1,
            "hint": "회전수를 60으로 나누어 계산합니다.",
            "explanation": "회전주파수는 rpm을 60으로 나눈 값입니다. 3000/60 = 50 Hz입니다."
        },
        {
            "id": 10,
            "difficulty": "beginner",
            "category": "진동 기초",
            "question": "공진(Resonance)이 발생하기 쉬운 조건은 무엇인가?",
            "choices": [
                "가진력이 완전히 없는 경우",
                "가진주파수가 고유진동수에 가까운 경우",
                "회전수가 항상 0인 경우",
                "센서의 측정 단위가 변경된 경우"
            ],
            "answer": 2,
            "hint": "외부에서 가해지는 주파수와 구조물의 고유 특성을 비교합니다.",
            "explanation": "가진주파수가 고유진동수에 가까워지면 감쇠 조건에 따라 진동 응답이 크게 증가할 수 있습니다."
        },
        {
            "id": 11,
            "difficulty": "intermediate",
            "category": "신호 처리",
            "question": "샘플링 주파수가 25.6 kHz일 때 1초 동안 취득하는 샘플 수는 얼마인가?",
            "choices": [
                "256개",
                "2560개",
                "25600개",
                "256000개"
            ],
            "answer": 3,
            "hint": "kHz를 Hz로 변환합니다.",
            "explanation": "25.6 kHz는 초당 25600개의 샘플을 취득한다는 의미입니다."
        },
        {
            "id": 12,
            "difficulty": "intermediate",
            "category": "신호 처리",
            "question": "샘플링 주파수가 25.6 kHz일 때 나이퀴스트 주파수는 얼마인가?",
            "choices": [
                "6.4 kHz",
                "25.6 kHz",
                "51.2 kHz",
                "12.8 kHz"
            ],
            "answer": 4,
            "hint": "샘플링 주파수의 절반입니다.",
            "explanation": "나이퀴스트 주파수는 Fs/2이므로 25.6/2 = 12.8 kHz입니다."
        },
        {
            "id": 13,
            "difficulty": "intermediate",
            "category": "FFT 분석",
            "question": "10초 동안 측정한 신호 전체를 FFT할 때 기본 주파수 빈 간격은 얼마인가?",
            "choices": [
                "0.1 Hz",
                "1 Hz",
                "10 Hz",
                "100 Hz"
            ],
            "answer": 1,
            "hint": "제로 패딩이 없다면 주파수 빈 간격은 측정시간의 역수입니다.",
            "explanation": "제로 패딩 없이 전체 신호를 FFT하면 주파수 빈 간격은 1/T = 0.1 Hz입니다. 실제 분리 성능은 윈도우 등의 영향도 받습니다."
        },
        {
            "id": 14,
            "difficulty": "intermediate",
            "category": "회전체 진동",
            "question": "회전체 불평형에서 대표적으로 관찰되는 진동 성분은 무엇인가?",
            "choices": [
                "항상 0 Hz",
                "회전주파수 1X",
                "항상 1000 Hz",
                "샘플링 주파수"
            ],
            "answer": 2,
            "hint": "회전체가 한 바퀴 회전할 때 반복되는 힘을 생각합니다.",
            "explanation": "불평형은 일반적으로 회전주파수 1X 성분을 발생시키지만 1X 성분만으로 불평형을 확정할 수는 없습니다."
        },
        {
            "id": 15,
            "difficulty": "intermediate",
            "category": "베어링 진단",
            "question": "BPFO는 어떤 베어링 결함과 관련된 주파수인가?",
            "choices": [
                "내륜 결함",
                "전동체 결함",
                "외륜 결함",
                "윤활유 온도"
            ],
            "answer": 3,
            "hint": "Outer Race에 해당합니다.",
            "explanation": "BPFO는 Ball Pass Frequency Outer Race로 외륜 결함 관련 특성주파수입니다."
        },
        {
            "id": 16,
            "difficulty": "intermediate",
            "category": "베어링 진단",
            "question": "BPFI는 어떤 베어링 결함과 관련된 주파수인가?",
            "choices": [
                "외륜 결함",
                "케이지 결함",
                "전동체 결함",
                "내륜 결함"
            ],
            "answer": 4,
            "hint": "Inner Race에 해당합니다.",
            "explanation": "BPFI는 Ball Pass Frequency Inner Race로 내륜 결함 관련 특성주파수입니다."
        },
        {
            "id": 17,
            "difficulty": "intermediate",
            "category": "베어링 진단",
            "question": "포락선 분석(Envelope Analysis)의 주요 활용 목적은 무엇인가?",
            "choices": [
                "충격에 의해 변조된 신호에서 반복 결함 성분 검출",
                "공작물 치수 측정",
                "주축 회전수 강제 감소",
                "절삭유 점도 측정"
            ],
            "answer": 1,
            "hint": "고주파 공진을 유발하는 반복 충격 신호에 활용됩니다.",
            "explanation": "포락선 분석은 고주파 충격 응답에 포함된 반복적인 변조 성분을 추출하여 베어링 결함 진단 등에 활용합니다."
        },
        {
            "id": 18,
            "difficulty": "intermediate",
            "category": "FFT 분석",
            "question": "주파수 f에서 가속도 진폭 A를 속도 진폭 V로 변환하는 식은 무엇인가?",
            "choices": [
                "V = A × 2πf",
                "V = A / (2πf)",
                "V = A + f",
                "V = A × f²"
            ],
            "answer": 2,
            "hint": "가속도를 적분하면 속도가 됩니다.",
            "explanation": "0 Hz를 제외한 주파수 성분에서 동일한 진폭 정의를 사용하면 V = A/(2πf)입니다."
        },
        {
            "id": 19,
            "difficulty": "intermediate",
            "category": "진동 계측",
            "question": "3축 가속도 센서를 사용하는 주요 장점은 무엇인가?",
            "choices": [
                "샘플링이 필요하지 않음",
                "항상 모든 진동을 제거함",
                "서로 직교하는 세 방향의 진동 측정",
                "온도 측정만 가능함"
            ],
            "answer": 3,
            "hint": "X축, Y축, Z축 방향을 생각합니다.",
            "explanation": "3축 가속도 센서는 세 방향의 진동을 측정하여 방향별 진동 특성을 비교할 수 있습니다."
        },
        {
            "id": 20,
            "difficulty": "intermediate",
            "category": "베어링 진단",
            "question": "측정 피크와 베어링 이론 결함주파수가 일치할 때 가장 적절한 판단은 무엇인가?",
            "choices": [
                "무조건 베어링 불량으로 확정한다.",
                "측정 결과를 삭제한다.",
                "주파수가 일치하면 정상으로 확정한다.",
                "결함 가능성을 검토하고 추가 증거를 확인한다."
            ],
            "answer": 4,
            "hint": "주파수 일치는 결함 가능성을 판단하는 근거 중 하나입니다.",
            "explanation": "결함주파수 일치만으로 불량을 확정할 수 없습니다. 진폭, 고조파, 사이드밴드, 운전조건 및 반복 측정 결과를 함께 검토해야 합니다."
        }
    ]
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        Get-Item -LiteralPath $path |
            Select-Object Name, Length

        "PASS: Default quiz dataset created"

    Name                 Length
    ----                 ------
    default_quizzes.json  11863
    PASS: Default quiz dataset created
    Failed: False

    04. Validate JSON Syntax

    > python -c "import json; from pathlib import Path; data=json.loads(Path('data/default_quizzes.json').read_text(encoding='utf-8')); print('JSON TYPE:', type(data).__name__); print('QUESTION COUNT:', len(data)); assert isinstance(data,list); assert len(data)==20; print('PASS: JSON syntax and question count verified')"

        if ($LASTEXITCODE -ne 0) {
            throw "JSON syntax validation failed."
        }
    JSON TYPE: list
    QUESTION COUNT: 20
    PASS: JSON syntax and question count verified
    Failed: False

    05. Validate Quiz Schema

    > $validation = @'
    import json
    from pathlib import Path
    from collections import Counter

    path = Path("data/default_quizzes.json")
    quizzes = json.loads(path.read_text(encoding="utf-8"))

    required = {
        "id",
        "difficulty",
        "category",
        "question",
        "choices",
        "answer",
        "hint",
        "explanation"
    }

    ids = set()
    questions = set()

    for quiz in quizzes:
        assert set(quiz) == required, "Invalid schema"
        assert type(quiz["id"]) is int
        assert quiz["id"] not in ids, "Duplicate ID"
        assert quiz["question"] not in questions, "Duplicate question"

        assert quiz["difficulty"] in (
            "beginner",
            "intermediate"
        )

        assert isinstance(quiz["choices"], list)
        assert len(quiz["choices"]) == 4
        assert len(set(quiz["choices"])) == 4

        assert type(quiz["answer"]) is int
        assert 1 <= quiz["answer"] <= 4

        for field in (
            "category",
            "question",
            "hint",
            "explanation"
        ):
            assert isinstance(quiz[field], str)
            assert quiz[field].strip()

        for choice in quiz["choices"]:
            assert isinstance(choice, str)
            assert choice.strip()

        ids.add(quiz["id"])
        questions.add(quiz["question"])

        print(
            f"PASS: Question {quiz['id']:02d} | "
            f"{quiz['difficulty']} | "
            f"Answer {quiz['answer']}"
        )

    assert ids == set(range(1, 21))

    levels = Counter(
        quiz["difficulty"] for quiz in quizzes
    )

    answers = Counter(
        quiz["answer"] for quiz in quizzes
    )

    assert levels["beginner"] == 10
    assert levels["intermediate"] == 10

    print()
    print("TOTAL QUESTIONS:", len(quizzes))
    print("BEGINNER:", levels["beginner"])
    print("INTERMEDIATE:", levels["intermediate"])
    print("ANSWER DISTRIBUTION:", dict(sorted(answers.items())))
    print("PASS: ALL QUIZ DATA VALIDATION TESTS COMPLETED")
    '@

        $validation | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Quiz schema validation failed."
        }
    PASS: Question 01 | beginner | Answer 1
    PASS: Question 02 | beginner | Answer 2
    PASS: Question 03 | beginner | Answer 3
    PASS: Question 04 | beginner | Answer 4
    PASS: Question 05 | beginner | Answer 1
    PASS: Question 06 | beginner | Answer 2
    PASS: Question 07 | beginner | Answer 3
    PASS: Question 08 | beginner | Answer 4
    PASS: Question 09 | beginner | Answer 1
    PASS: Question 10 | beginner | Answer 2
    PASS: Question 11 | intermediate | Answer 3
    PASS: Question 12 | intermediate | Answer 4
    PASS: Question 13 | intermediate | Answer 1
    PASS: Question 14 | intermediate | Answer 2
    PASS: Question 15 | intermediate | Answer 3
    PASS: Question 16 | intermediate | Answer 4
    PASS: Question 17 | intermediate | Answer 1
    PASS: Question 18 | intermediate | Answer 2
    PASS: Question 19 | intermediate | Answer 3
    PASS: Question 20 | intermediate | Answer 4

    TOTAL QUESTIONS: 20
    BEGINNER: 10
    INTERMEDIATE: 10
    ANSWER DISTRIBUTION: {1: 5, 2: 5, 3: 5, 4: 5}
    PASS: ALL QUIZ DATA VALIDATION TESTS COMPLETED
    Failed: False

    06. Verify UTF-8 Encoding

    > $path = (Resolve-Path ".\data\default_quizzes.json").Path

        $bytes = [System.IO.File]::ReadAllBytes($path)

        $strictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)

        $text = $strictUtf8.GetString($bytes)

        if ($bytes.Length -ge 3 -and
            $bytes[0] -eq 239 -and
            $bytes[1] -eq 187 -and
            $bytes[2] -eq 191) {

            throw "Unexpected UTF-8 BOM."
        }

        if ($text -notmatch '[가-힣]') {
            throw "Korean quiz text not detected."
        }

        "FILE SIZE: $($bytes.Length) bytes"
        "ENCODING: UTF-8 without BOM"

        "PASS: Korean text and UTF-8 encoding verified"
    FILE SIZE: 11863 bytes
    ENCODING: UTF-8 without BOM
    PASS: Korean text and UTF-8 encoding verified
    Failed: False

    07. Verify Git Identity and Repository

    > $root = git rev-parse --show-toplevel

        if ($LASTEXITCODE -ne 0 -or
            $root -ne "C:/2026Codyssey_AllInOne/M_E1-2") {

            throw "Unexpected Git repository."
        }

        $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
            throw "Unexpected Git branch."
        }

        $email = git var GIT_AUTHOR_IDENT

        if ($LASTEXITCODE -ne 0 -or
            $email -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

            throw "Git author email privacy verification failed."
        }

        $committer = git var GIT_COMMITTER_IDENT

        if ($LASTEXITCODE -ne 0 -or
            $committer -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

            throw "Git committer email privacy verification failed."
        }

        "BRANCH: $branch"
        "PASS: Git repository verified"
        "PASS: Author and committer email privacy verified"
    BRANCH: main
    PASS: Git repository verified
    PASS: Author and committer email privacy verified
    Failed: False

    08. Create Initial Git Commit

    > $required = @(
            ".gitignore",
            ".gitattributes",
            "README.md",
            "logs/01_development_environment.txt",
            "logs/02_project_structure_git.txt",
            "data/default_quizzes.json",
            "screenshots/01_Development_Environment.png",
            "screenshots/02_Git_Configuration.png"
        )

        foreach ($file in $required) {

            if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
                throw "Missing required file: $file"
            }
        }

        git rev-parse --verify HEAD 2>$null

        if ($LASTEXITCODE -eq 0) {
            throw "Initial commit already exists. Review required."
        }

        python -c "import json; from pathlib import Path; q=json.loads(Path('data/default_quizzes.json').read_text(encoding='utf-8')); assert len(q)==20; assert len({x['id'] for x in q})==20; assert all(len(x['choices'])==4 and 1<=x['answer']<=4 for x in q); print('PASS: Pre-commit dataset check')"

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit dataset check failed."
        }

        foreach ($file in $required) {

            if ($file -notlike "*.png") {

                $text = Get-Content -LiteralPath $file -Raw -Encoding UTF8

                if ($text -match 'github_pat_[A-Za-z0-9_]+|gh[pousr]_[A-Za-z0-9]+|sk-[A-Za-z0-9_-]{15,}|-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----') {

                    throw "Sensitive pattern detected in $file"
                }
            }
        }

        git add -- $required

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staged file verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $required `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged file list."
        }

        git diff --cached --stat

        if ($LASTEXITCODE -ne 0) {
            throw "Git staged summary failed."
        }

        git commit -m "Initialize quiz project and add 20 default questions"

        if ($LASTEXITCODE -ne 0) {
            throw "Initial Git commit failed."
        }

        "PASS: Initial Git commit created"
    PASS: Pre-commit dataset check
    git : warning: in the working copy of 'logs/01_development_environment.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:616 문자:5
    +     git add -- $required
    +     ~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    warning: in the working copy of 'logs/02_project_structure_git.txt', CRLF will be replaced by LF the next time Git touches it
     .gitattributes                             |  10 +
     .gitignore                                 |  25 ++
     README.md                                  |  33 ++
     data/default_quizzes.json                  | 302 +++++++++++++++++
     logs/01_development_environment.txt        | 146 +++++++++
     logs/02_project_structure_git.txt          | 510 +++++++++++++++++++++++++++++
     screenshots/01_Development_Environment.png | Bin 0 -> 89978 bytes
     screenshots/02_Git_Configuration.png       | Bin 0 -> 16977 bytes
     8 files changed, 1026 insertions(+)
    [main (root-commit) f161dea] Initialize quiz project and add 20 default questions
     8 files changed, 1026 insertions(+)
     create mode 100644 .gitattributes
     create mode 100644 .gitignore
     create mode 100644 README.md
     create mode 100644 data/default_quizzes.json
     create mode 100644 logs/01_development_environment.txt
     create mode 100644 logs/02_project_structure_git.txt
     create mode 100644 screenshots/01_Development_Environment.png
     create mode 100644 screenshots/02_Git_Configuration.png
    PASS: Initial Git commit created
    Failed: False

    09. Verify Git Commit and Status

    > git log -1 --oneline

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit verification failed."
        }

        git status --short --branch

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        "PASS: Working tree is clean"
        "PASS: STEP03 completed"
    f161dea Initialize quiz project and add 20 default questions
    ## main
    PASS: Working tree is clean
    PASS: STEP03 completed
    Failed: False



### 04_quiz_class_development.txt

[Original execution log](../logs/04_quiz_class_development.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP04 - Quiz Class Development
    Date: 2026-11-14 22:30:15

    01. Verify Previous Stage

    > $required = @(
            ".git",
            "data/default_quizzes.json",
            "logs/02_project_structure_git.txt",
            "tests"
        )

        foreach ($item in $required) {

            if (-not (Test-Path -LiteralPath $item)) {
                throw "Missing required item: $item"
            }

            "READY: $item"
        }

        git log -1 --oneline

        if ($LASTEXITCODE -ne 0) {
            throw "Previous commit not found."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        "PASS: Previous stage verified"
    READY: .git
    READY: data/default_quizzes.json
    READY: logs/02_project_structure_git.txt
    READY: tests
    f161dea Initialize quiz project and add 20 default questions
    PASS: Previous stage verified
    Failed: False

    02. Save STEP03 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP03*Quiz*Dataset*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP03 execution log not found."
        }

        $content = Get-Content `
            -LiteralPath $source.FullName `
            -Raw `
            -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP03 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 9) {
            throw "Expected nine successful STEP03 results."
        }

        $content = $content -replace `
            '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
            '${1}<USER>'

        $path = Join-Path `
            (Get-Location).Path `
            "logs\03_quiz_dataset_creation.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content,
            $utf8
        )

        "PASS: STEP03 actual execution evidence saved"
    PASS: STEP03 actual execution evidence saved
    Failed: False

    03. Create Quiz Class

    > $path = Join-Path (Get-Location).Path "quiz.py"

        if (Test-Path -LiteralPath $path) {
            throw "quiz.py already exists. Review required."
        }

        $content = @'
    """Individual quiz question model."""

    import random


    class Quiz:
        """Represent one multiple-choice quiz question."""

        def __init__(
            self,
            id,
            difficulty,
            category,
            question,
            choices,
            answer,
            hint,
            explanation,
        ):
            self.id = id
            self.difficulty = difficulty
            self.category = category
            self.question = question
            self.choices = (
                list(choices)
                if isinstance(choices, list)
                else choices
            )
            self.answer = answer
            self.hint = hint
            self.explanation = explanation

            self.validate()

        def validate(self):
            """Validate all quiz fields."""

            if type(self.id) is not int or self.id < 1:
                raise ValueError("문제 번호는 양의 정수여야 합니다.")

            if self.difficulty not in (
                "beginner",
                "intermediate",
            ):
                raise ValueError("지원하지 않는 난이도입니다.")

            text_fields = {
                "category": self.category,
                "question": self.question,
                "hint": self.hint,
                "explanation": self.explanation,
            }

            for name, value in text_fields.items():
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(
                        f"{name}: 비어 있지 않은 문자열이어야 합니다."
                    )

            if not isinstance(self.choices, list):
                raise ValueError("보기는 리스트여야 합니다.")

            if len(self.choices) != 4:
                raise ValueError("보기는 정확히 4개여야 합니다.")

            for choice in self.choices:
                if not isinstance(choice, str) or not choice.strip():
                    raise ValueError("보기는 비어 있을 수 없습니다.")

            if len({c.strip() for c in self.choices}) != 4:
                raise ValueError("중복된 보기는 허용되지 않습니다.")

            if type(self.answer) is not int:
                raise ValueError("정답 번호는 정수여야 합니다.")

            if not 1 <= self.answer <= 4:
                raise ValueError("정답 번호는 1~4여야 합니다.")

            return True

        def check_answer(self, user_answer):
            """Return True when the selected answer is correct."""

            if type(user_answer) is not int:
                raise ValueError("입력값은 정수여야 합니다.")

            if not 1 <= user_answer <= 4:
                raise ValueError("1~4 사이의 번호를 입력하세요.")

            return user_answer == self.answer

        def get_hint(self):
            """Return the question hint."""

            return self.hint

        def get_explanation(self):
            """Return the answer explanation."""

            return self.explanation

        def get_correct_choice(self):
            """Return the text of the correct choice."""

            return self.choices[self.answer - 1]

        def shuffled(self, rng=None):
            """Return a new quiz with randomized choice order."""

            generator = rng if rng is not None else random

            correct_choice = self.get_correct_choice()

            choices = self.choices.copy()

            generator.shuffle(choices)

            data = self.to_dict()

            data["choices"] = choices
            data["answer"] = choices.index(correct_choice) + 1

            return Quiz.from_dict(data)

        def to_dict(self):
            """Convert this quiz into a JSON-compatible dictionary."""

            return {
                "id": self.id,
                "difficulty": self.difficulty,
                "category": self.category,
                "question": self.question,
                "choices": self.choices.copy(),
                "answer": self.answer,
                "hint": self.hint,
                "explanation": self.explanation,
            }

        @classmethod
        def from_dict(cls, data):
            """Create a Quiz object from a dictionary."""

            if not isinstance(data, dict):
                raise ValueError("퀴즈 데이터는 딕셔너리여야 합니다.")

            required = {
                "id",
                "difficulty",
                "category",
                "question",
                "choices",
                "answer",
                "hint",
                "explanation",
            }

            if set(data) != required:
                raise ValueError("퀴즈 데이터 구조가 올바르지 않습니다.")

            return cls(**data)

        def __repr__(self):
            return (
                f"Quiz(id={self.id}, "
                f"difficulty={self.difficulty!r}, "
                f"question={self.question!r})"
            )
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        Get-Item -LiteralPath $path |
            Select-Object Name, Length

        "PASS: Quiz class created"

    Name    Length
    ----    ------
    quiz.py   4599
    PASS: Quiz class created
    Failed: False

    04. Create Quiz Unit Tests

    > $path = Join-Path `
            (Get-Location).Path `
            "tests\test_quiz.py"

        if (Test-Path -LiteralPath $path) {
            throw "test_quiz.py already exists. Review required."
        }

        $content = @'
    """Unit tests for the Quiz class."""

    import json
    import random
    import unittest
    from pathlib import Path

    from quiz import Quiz


    class TestQuiz(unittest.TestCase):

        def setUp(self):
            self.data = {
                "id": 1,
                "difficulty": "beginner",
                "category": "Machine Tools",
                "question": "What does CNC mean?",
                "choices": [
                    "Computer Numerical Control",
                    "Central Network Computer",
                    "Control Number Calculation",
                    "Computer Noise Control",
                ],
                "answer": 1,
                "hint": "Computer-based numerical control",
                "explanation": "CNC means Computer Numerical Control.",
            }

            self.quiz = Quiz.from_dict(self.data)

        def test_01_create_object(self):
            self.assertIsInstance(self.quiz, Quiz)
            self.assertEqual(self.quiz.id, 1)

        def test_02_correct_answer(self):
            self.assertTrue(self.quiz.check_answer(1))

        def test_03_wrong_answer(self):
            self.assertFalse(self.quiz.check_answer(2))

        def test_04_invalid_answer_range(self):
            for value in (0, 5, -1, 100):
                with self.subTest(value=value):
                    with self.assertRaises(ValueError):
                        self.quiz.check_answer(value)

        def test_05_invalid_answer_type(self):
            for value in ("1", None, True, 1.5):
                with self.subTest(value=value):
                    with self.assertRaises(ValueError):
                        self.quiz.check_answer(value)

        def test_06_get_hint(self):
            self.assertEqual(
                self.quiz.get_hint(),
                self.data["hint"],
            )

        def test_07_get_explanation(self):
            self.assertEqual(
                self.quiz.get_explanation(),
                self.data["explanation"],
            )

        def test_08_correct_choice(self):
            self.assertEqual(
                self.quiz.get_correct_choice(),
                self.data["choices"][0],
            )

        def test_09_to_dict(self):
            self.assertEqual(
                self.quiz.to_dict(),
                self.data,
            )

        def test_10_round_trip(self):
            restored = Quiz.from_dict(
                self.quiz.to_dict()
            )

            self.assertEqual(
                restored.to_dict(),
                self.quiz.to_dict(),
            )

        def test_11_missing_field(self):
            data = self.data.copy()
            del data["question"]

            with self.assertRaises(ValueError):
                Quiz.from_dict(data)

        def test_12_invalid_choice_count(self):
            data = self.data.copy()
            data["choices"] = ["A", "B", "C"]

            with self.assertRaises(ValueError):
                Quiz.from_dict(data)

        def test_13_duplicate_choices(self):
            data = self.data.copy()
            data["choices"] = ["A", "A", "B", "C"]

            with self.assertRaises(ValueError):
                Quiz.from_dict(data)

        def test_14_invalid_difficulty(self):
            data = self.data.copy()
            data["difficulty"] = "unknown"

            with self.assertRaises(ValueError):
                Quiz.from_dict(data)

        def test_15_empty_question(self):
            data = self.data.copy()
            data["question"] = " "

            with self.assertRaises(ValueError):
                Quiz.from_dict(data)

        def test_16_invalid_correct_answer(self):
            data = self.data.copy()
            data["answer"] = 5

            with self.assertRaises(ValueError):
                Quiz.from_dict(data)

        def test_17_shuffle_preserves_answer(self):
            shuffled = self.quiz.shuffled(
                random.Random(42)
            )

            self.assertEqual(
                shuffled.get_correct_choice(),
                self.quiz.get_correct_choice(),
            )

            self.assertCountEqual(
                shuffled.choices,
                self.quiz.choices,
            )

            self.assertTrue(
                shuffled.check_answer(shuffled.answer)
            )

        def test_18_shuffle_preserves_original(self):
            original = self.quiz.to_dict()

            shuffled = self.quiz.shuffled(
                random.Random(42)
            )

            self.assertIsNot(shuffled, self.quiz)

            self.assertEqual(
                self.quiz.to_dict(),
                original,
            )

        def test_19_load_all_default_questions(self):
            root = Path(__file__).resolve().parents[1]

            path = root / "data" / "default_quizzes.json"

            data = json.loads(
                path.read_text(encoding="utf-8")
            )

            quizzes = [
                Quiz.from_dict(item)
                for item in data
            ]

            self.assertEqual(len(quizzes), 20)

            self.assertEqual(
                len({q.id for q in quizzes}),
                20,
            )

            for quiz in quizzes:
                self.assertTrue(
                    quiz.check_answer(quiz.answer)
                )

        def test_20_independent_choice_lists(self):
            exported = self.quiz.to_dict()

            exported["choices"][0] = "Changed"

            self.assertNotEqual(
                exported["choices"][0],
                self.quiz.choices[0],
            )


    if __name__ == "__main__":
        unittest.main()
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        Get-Item -LiteralPath $path |
            Select-Object Name, Length

        "PASS: Twenty unit tests created"

    Name         Length
    ----         ------
    test_quiz.py   5096
    PASS: Twenty unit tests created
    Failed: False

    05. Verify Python Syntax

    > python -m py_compile quiz.py tests/test_quiz.py

        if ($LASTEXITCODE -ne 0) {
            throw "Python syntax verification failed."
        }

        "PASS: Python syntax verified"
    PASS: Python syntax verified
    Failed: False

    06. Run Twenty Unit Tests

    > python -m unittest discover -s tests -p "test_quiz.py" -v 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Quiz unit tests failed."
        }

        "PASS: All Quiz unit tests completed"
    python : test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    위치 줄:521 문자:5
    +     python -m unittest discover -s tests -p "test_quiz.py" -v 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_create_..._object) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok

    ----------------------------------------------------------------------
    Ran 20 tests in 0.003s

    OK
    PASS: All Quiz unit tests completed
    Failed: False

    07. Verify Actual Quiz Objects

    > $code = @'
    import json
    import random
    from pathlib import Path

    from quiz import Quiz

    data = json.loads(
        Path("data/default_quizzes.json").read_text(
            encoding="utf-8"
        )
    )

    quizzes = [
        Quiz.from_dict(item)
        for item in data
    ]

    print("TOTAL QUIZ OBJECTS:", len(quizzes))

    for quiz in quizzes:
        shuffled = quiz.shuffled(
            random.Random(quiz.id)
        )

        assert shuffled.get_correct_choice() == quiz.get_correct_choice()

        assert shuffled.check_answer(shuffled.answer)

        print(
            f"PASS: Quiz {quiz.id:02d} | "
            f"Original answer: {quiz.answer} | "
            f"Shuffled answer: {shuffled.answer}"
        )

    print("PASS: All twenty quiz objects verified")
    print("PASS: Correct answers preserved after shuffling")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Quiz object verification failed."
        }
    TOTAL QUIZ OBJECTS: 20
    PASS: Quiz 01 | Original answer: 1 | Shuffled answer: 2
    PASS: Quiz 02 | Original answer: 2 | Shuffled answer: 1
    PASS: Quiz 03 | Original answer: 3 | Shuffled answer: 3
    PASS: Quiz 04 | Original answer: 4 | Shuffled answer: 3
    PASS: Quiz 05 | Original answer: 1 | Shuffled answer: 1
    PASS: Quiz 06 | Original answer: 2 | Shuffled answer: 3
    PASS: Quiz 07 | Original answer: 3 | Shuffled answer: 4
    PASS: Quiz 08 | Original answer: 4 | Shuffled answer: 3
    PASS: Quiz 09 | Original answer: 1 | Shuffled answer: 1
    PASS: Quiz 10 | Original answer: 2 | Shuffled answer: 3
    PASS: Quiz 11 | Original answer: 3 | Shuffled answer: 3
    PASS: Quiz 12 | Original answer: 4 | Shuffled answer: 4
    PASS: Quiz 13 | Original answer: 1 | Shuffled answer: 2
    PASS: Quiz 14 | Original answer: 2 | Shuffled answer: 1
    PASS: Quiz 15 | Original answer: 3 | Shuffled answer: 2
    PASS: Quiz 16 | Original answer: 4 | Shuffled answer: 2
    PASS: Quiz 17 | Original answer: 1 | Shuffled answer: 1
    PASS: Quiz 18 | Original answer: 2 | Shuffled answer: 4
    PASS: Quiz 19 | Original answer: 3 | Shuffled answer: 3
    PASS: Quiz 20 | Original answer: 4 | Shuffled answer: 3
    PASS: All twenty quiz objects verified
    PASS: Correct answers preserved after shuffling
    Failed: False

    08. Create Second Git Commit

    > $files = @(
            "quiz.py",
            "tests/test_quiz.py",
            "logs/03_quiz_dataset_creation.txt"
        )

        foreach ($file in $files) {

            if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
                throw "Missing required file: $file"
            }
        }

        $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "1") {
            throw "Unexpected previous commit count."
        }

        python -m unittest discover -s tests -p "test_quiz.py" 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit unit tests failed."
        }

        $identities = @(
            git var GIT_AUTHOR_IDENT
            git var GIT_COMMITTER_IDENT
        )

        if ($LASTEXITCODE -ne 0 -or $identities.Count -ne 2) {
            throw "Git identity verification failed."
        }

        foreach ($identity in $identities) {

            if ($identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {
                throw "Git email privacy verification failed."
            }
        }

        "PASS: Git email privacy verified"

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staging verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git diff --cached --stat

        if ($LASTEXITCODE -ne 0) {
            throw "Git diff failed."
        }

        git commit -m "Implement Quiz class with validation and unit tests"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: Second Git commit created"
    python : ....................
    위치 줄:599 문자:5
    +     python -m unittest discover -s tests -p "test_quiz.py" 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (....................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 20 tests in 0.001s

    OK
    PASS: Git email privacy verified
    git : warning: in the working copy of 'logs/03_quiz_dataset_creation.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:623 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

     logs/03_quiz_dataset_creation.txt | 760 ++++++++++++++++++++++++++++++++++++++
     quiz.py                           | 167 +++++++++
     tests/test_quiz.py                | 201 ++++++++++
     3 files changed, 1128 insertions(+)
    [main ccc8cb6] Implement Quiz class with validation and unit tests
     3 files changed, 1128 insertions(+)
     create mode 100644 logs/03_quiz_dataset_creation.txt
     create mode 100644 quiz.py
     create mode 100644 tests/test_quiz.py
    PASS: Second Git commit created
    Failed: False

    09. Verify Final Stage Status

    > git log -2 --oneline

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "2") {
            throw "Expected two Git commits."
        }

        "TOTAL COMMITS: $count"

        git status --short --branch

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        "PASS: Working tree is clean"
        "PASS: STEP04 completed"
    ccc8cb6 Implement Quiz class with validation and unit tests
    f161dea Initialize quiz project and add 20 default questions
    TOTAL COMMITS: 2
    ## main
    PASS: Working tree is clean
    PASS: STEP04 completed
    Failed: False



### 05_quizgame_development.txt

[Original execution log](../logs/05_quizgame_development.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP05 - QuizGame Class Development
    Date: 2026-11-14 22:34:30

    01. Verify Previous Stage

    > $required = @(
            "quiz.py",
            "tests/test_quiz.py",
            "data/default_quizzes.json",
            "logs/03_quiz_dataset_creation.txt"
        )

        foreach ($file in $required) {

            if (-not (Test-Path -LiteralPath $file)) {
                throw "Missing required file: $file"
            }

            "READY: $file"
        }

        $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "2") {
            throw "Expected two previous Git commits."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        python -m unittest discover -s tests -p "test_quiz.py" 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Previous Quiz tests failed."
        }

        "PASS: Previous stage verified"
    READY: quiz.py
    READY: tests/test_quiz.py
    READY: data/default_quizzes.json
    READY: logs/03_quiz_dataset_creation.txt
    python : ....................
    위치 줄:35 문자:5
    +     python -m unittest discover -s tests -p "test_quiz.py" 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (....................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 20 tests in 0.001s

    OK
    PASS: Previous stage verified
    Failed: False

    02. Save STEP04 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP04*Quiz*Class*Development*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP04 execution log not found."
        }

        $content = Get-Content `
            -LiteralPath $source.FullName `
            -Raw `
            -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP04 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 9) {
            throw "Expected nine successful STEP04 results."
        }

        $content = $content -replace `
            '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
            '${1}<USER>'

        $path = Join-Path `
            (Get-Location).Path `
            "logs\04_quiz_class_development.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content,
            $utf8
        )

        "PASS: STEP04 actual execution evidence saved"
    PASS: STEP04 actual execution evidence saved
    Failed: False

    03. Create QuizGame Class

    > $path = Join-Path (Get-Location).Path "quiz_game.py"

        if (Test-Path -LiteralPath $path) {
            throw "quiz_game.py already exists. Review required."
        }

        $content = @'
    """Quiz game engine for machine tool and vibration quizzes."""

    import json
    import random
    from pathlib import Path

    from quiz import Quiz


    class QuizGame:
        """Manage quiz questions, game sessions and scores."""

        FULL_POINTS = 10
        HINT_POINTS = 5

        def __init__(self, quizzes=None, rng=None):
            self.quizzes = []
            self.best_score = None

            self._rng = (
                rng if rng is not None else random.Random()
            )

            self._session = []
            self._index = 0
            self._hint_used = False
            self._active = False
            self._answers = []
            self._last_result = None

            if quizzes is not None:
                for quiz in quizzes:
                    self.add_quiz(quiz)

        @property
        def is_active(self):
            """Return whether a game is in progress."""

            return self._active

        @property
        def current_quiz(self):
            """Return the current question or None."""

            if not self._active:
                return None

            return self._session[self._index]

        @property
        def question_number(self):
            """Return the current question number."""

            if not self._active:
                return 0

            return self._index + 1

        @property
        def total_questions(self):
            """Return the number of questions in the session."""

            return len(self._session)

        @property
        def hint_used(self):
            """Return whether the current hint has been used."""

            return self._hint_used

        def _require_inactive(self):
            """Prevent question changes during a game."""

            if self._active:
                raise RuntimeError(
                    "게임 진행 중에는 문제를 변경할 수 없습니다."
                )

        def _require_active(self):
            """Require an active game session."""

            if not self._active:
                raise RuntimeError(
                    "진행 중인 게임이 없습니다."
                )

        def load_default_quizzes(self, path=None):
            """Load and validate the default quiz dataset."""

            self._require_inactive()

            if path is None:
                path = (
                    Path(__file__).resolve().parent
                    / "data"
                    / "default_quizzes.json"
                )

            path = Path(path)

            data = json.loads(
                path.read_text(encoding="utf-8")
            )

            if not isinstance(data, list):
                raise ValueError(
                    "퀴즈 데이터는 리스트여야 합니다."
                )

            loaded = []
            ids = set()
            questions = set()

            for item in data:
                quiz = Quiz.from_dict(item)

                if quiz.id in ids:
                    raise ValueError(
                        "중복된 문제 번호가 있습니다."
                    )

                key = quiz.question.strip().casefold()

                if key in questions:
                    raise ValueError(
                        "중복된 문제가 있습니다."
                    )

                ids.add(quiz.id)
                questions.add(key)
                loaded.append(quiz)

            self.quizzes = loaded

            return len(self.quizzes)

        def add_quiz(self, quiz):
            """Add a validated and independent quiz object."""

            self._require_inactive()

            if not isinstance(quiz, Quiz):
                raise TypeError(
                    "Quiz 객체만 등록할 수 있습니다."
                )

            quiz.validate()

            if any(q.id == quiz.id for q in self.quizzes):
                raise ValueError(
                    "이미 존재하는 문제 번호입니다."
                )

            key = quiz.question.strip().casefold()

            if any(
                q.question.strip().casefold() == key
                for q in self.quizzes
            ):
                raise ValueError(
                    "이미 등록된 문제입니다."
                )

            self.quizzes.append(
                Quiz.from_dict(quiz.to_dict())
            )

            return quiz.id

        def next_quiz_id(self):
            """Return the next available quiz ID."""

            return max(
                (quiz.id for quiz in self.quizzes),
                default=0,
            ) + 1

        def list_quizzes(self, difficulty=None):
            """Return copies of the registered quiz questions."""

            if difficulty not in (
                None,
                "beginner",
                "intermediate",
            ):
                raise ValueError(
                    "지원하지 않는 난이도입니다."
                )

            selected = [
                quiz
                for quiz in self.quizzes
                if difficulty is None
                or quiz.difficulty == difficulty
            ]

            return [
                Quiz.from_dict(quiz.to_dict())
                for quiz in selected
            ]

        def start_game(
            self,
            count=None,
            difficulty=None,
            random_order=True,
            shuffle_choices=True,
        ):
            """Create a new game session."""

            self._require_inactive()

            available = self.list_quizzes(difficulty)

            if not available:
                raise ValueError(
                    "출제할 문제가 없습니다."
                )

            if count is None:
                count = len(available)

            if type(count) is not int:
                raise ValueError(
                    "문제 수는 정수여야 합니다."
                )

            if not 1 <= count <= len(available):
                raise ValueError(
                    f"문제 수는 1~{len(available)}개여야 합니다."
                )

            if random_order:
                selected = self._rng.sample(
                    available,
                    count,
                )
            else:
                selected = available[:count]

            if shuffle_choices:
                selected = [
                    quiz.shuffled(self._rng)
                    for quiz in selected
                ]

            self._session = selected
            self._index = 0
            self._hint_used = False
            self._answers = []
            self._last_result = None
            self._active = True

            return self.total_questions

        def use_hint(self):
            """Reveal the current hint and mark the deduction."""

            self._require_active()

            self._hint_used = True

            return self.current_quiz.get_hint()

        def submit_answer(self, user_answer):
            """Check an answer and advance the game."""

            self._require_active()

            quiz = self.current_quiz

            correct = quiz.check_answer(user_answer)

            if correct:
                points = (
                    self.HINT_POINTS
                    if self._hint_used
                    else self.FULL_POINTS
                )
            else:
                points = 0

            answer_result = {
                "quiz_id": quiz.id,
                "question": quiz.question,
                "selected_answer": user_answer,
                "correct_answer": quiz.answer,
                "correct_choice": quiz.get_correct_choice(),
                "correct": correct,
                "hint_used": self._hint_used,
                "points": points,
                "explanation": quiz.get_explanation(),
            }

            self._answers.append(answer_result)

            self._index += 1
            self._hint_used = False

            if self._index >= len(self._session):
                self._finish_game()

            return answer_result.copy()

        def _finish_game(self):
            """Calculate the completed session result."""

            total = len(self._session)

            correct = sum(
                answer["correct"]
                for answer in self._answers
            )

            hints = sum(
                answer["hint_used"]
                for answer in self._answers
            )

            points = sum(
                answer["points"]
                for answer in self._answers
            )

            max_points = total * self.FULL_POINTS

            score = round(
                points / max_points * 100,
                1,
            )

            accuracy = round(
                correct / total * 100,
                1,
            )

            new_best = (
                self.best_score is None
                or score > self.best_score
            )

            if new_best:
                self.best_score = score

            self._last_result = {
                "total_questions": total,
                "correct_count": correct,
                "wrong_count": total - correct,
                "hint_count": hints,
                "earned_points": points,
                "max_points": max_points,
                "score": score,
                "accuracy": accuracy,
                "best_score": self.best_score,
                "new_best": new_best,
                "answers": [
                    answer.copy()
                    for answer in self._answers
                ],
            }

            self._active = False

        def get_result(self):
            """Return a copy of the latest completed result."""

            if self._last_result is None:
                return None

            result = self._last_result.copy()

            result["answers"] = [
                answer.copy()
                for answer in self._last_result["answers"]
            ]

            return result

        def cancel_game(self):
            """Cancel an incomplete game without scoring it."""

            if not self._active:
                return False

            self._session = []
            self._index = 0
            self._hint_used = False
            self._answers = []
            self._last_result = None
            self._active = False

            return True
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        Get-Item -LiteralPath $path |
            Select-Object Name, Length

        "PASS: QuizGame class created"

    Name         Length
    ----         ------
    quiz_game.py   9320
    PASS: QuizGame class created
    Failed: False

    04. Create QuizGame Unit Tests

    > $path = Join-Path `
            (Get-Location).Path `
            "tests\test_quiz_game.py"

        if (Test-Path -LiteralPath $path) {
            throw "test_quiz_game.py already exists. Review required."
        }

        $content = @'
    """Unit tests for the QuizGame engine."""

    import json
    import random
    import tempfile
    import unittest
    from pathlib import Path

    from quiz import Quiz
    from quiz_game import QuizGame


    class TestQuizGame(unittest.TestCase):

        def setUp(self):
            self.game = QuizGame(
                rng=random.Random(42)
            )

            self.game.load_default_quizzes()

        def start(self, count=3):
            self.game.start_game(
                count=count,
                random_order=False,
                shuffle_choices=False,
            )

        def correct_answer(self):
            return self.game.submit_answer(
                self.game.current_quiz.answer
            )

        def wrong_answer(self):
            answer = self.game.current_quiz.answer
            wrong = answer % 4 + 1

            return self.game.submit_answer(wrong)

        def test_01_default_question_count(self):
            self.assertEqual(
                len(self.game.list_quizzes()),
                20,
            )

        def test_02_difficulty_filter(self):
            self.assertEqual(
                len(self.game.list_quizzes("beginner")),
                10,
            )

            self.assertEqual(
                len(self.game.list_quizzes("intermediate")),
                10,
            )

        def test_03_add_quiz(self):
            data = self.game.list_quizzes()[0].to_dict()

            data["id"] = 21
            data["question"] = "New test question"

            quiz = Quiz.from_dict(data)

            self.assertEqual(
                self.game.add_quiz(quiz),
                21,
            )

            self.assertEqual(
                len(self.game.list_quizzes()),
                21,
            )

        def test_04_duplicate_id(self):
            quiz = self.game.list_quizzes()[0]

            with self.assertRaises(ValueError):
                self.game.add_quiz(quiz)

        def test_05_duplicate_question(self):
            data = self.game.list_quizzes()[0].to_dict()
            data["id"] = 21

            with self.assertRaises(ValueError):
                self.game.add_quiz(
                    Quiz.from_dict(data)
                )

        def test_06_next_id(self):
            self.assertEqual(
                self.game.next_quiz_id(),
                21,
            )

        def test_07_start_game(self):
            self.start(5)

            self.assertTrue(self.game.is_active)

            self.assertEqual(
                self.game.total_questions,
                5,
            )

            self.assertEqual(
                self.game.question_number,
                1,
            )

        def test_08_invalid_count(self):
            for count in (0, -1, 21, True, "5"):

                with self.subTest(count=count):

                    with self.assertRaises(ValueError):
                        self.game.start_game(count=count)

        def test_09_empty_question_bank(self):
            game = QuizGame()

            with self.assertRaises(ValueError):
                game.start_game()

        def test_10_correct_answer_points(self):
            self.start(1)

            result = self.correct_answer()

            self.assertTrue(result["correct"])
            self.assertEqual(result["points"], 10)

        def test_11_wrong_answer_points(self):
            self.start(1)

            result = self.wrong_answer()

            self.assertFalse(result["correct"])
            self.assertEqual(result["points"], 0)

        def test_12_hint_points(self):
            self.start(1)

            self.game.use_hint()

            result = self.correct_answer()

            self.assertTrue(result["hint_used"])
            self.assertEqual(result["points"], 5)

        def test_13_repeated_hint(self):
            self.start(1)

            first = self.game.use_hint()
            second = self.game.use_hint()

            self.assertEqual(first, second)

            result = self.correct_answer()

            self.assertEqual(result["points"], 5)

        def test_14_hint_with_wrong_answer(self):
            self.start(1)

            self.game.use_hint()

            result = self.wrong_answer()

            self.assertEqual(result["points"], 0)

        def test_15_invalid_answer_does_not_advance(self):
            self.start(2)

            with self.assertRaises(ValueError):
                self.game.submit_answer(5)

            self.assertEqual(
                self.game.question_number,
                1,
            )

        def test_16_advance_question(self):
            self.start(2)

            self.correct_answer()

            self.assertEqual(
                self.game.question_number,
                2,
            )

        def test_17_normalized_score(self):
            self.start(3)

            self.correct_answer()

            self.game.use_hint()
            self.correct_answer()

            self.wrong_answer()

            result = self.game.get_result()

            self.assertEqual(result["earned_points"], 15)
            self.assertEqual(result["max_points"], 30)
            self.assertEqual(result["score"], 50.0)
            self.assertEqual(result["accuracy"], 66.7)
            self.assertEqual(result["correct_count"], 2)
            self.assertEqual(result["wrong_count"], 1)
            self.assertEqual(result["hint_count"], 1)

        def test_18_best_score(self):
            self.start(1)
            self.correct_answer()

            self.assertEqual(
                self.game.best_score,
                100.0,
            )

            self.start(1)
            self.wrong_answer()

            self.assertEqual(
                self.game.best_score,
                100.0,
            )

            self.assertFalse(
                self.game.get_result()["new_best"]
            )

        def test_19_cancel_game(self):
            self.start(2)

            self.correct_answer()

            self.assertTrue(self.game.cancel_game())

            self.assertFalse(self.game.is_active)
            self.assertIsNone(self.game.get_result())
            self.assertIsNone(self.game.best_score)

        def test_20_completed_game_state(self):
            self.start(1)

            self.correct_answer()

            self.assertFalse(self.game.is_active)
            self.assertIsNone(self.game.current_quiz)
            self.assertIsNotNone(self.game.get_result())

        def test_21_no_active_game(self):
            with self.assertRaises(RuntimeError):
                self.game.submit_answer(1)

            with self.assertRaises(RuntimeError):
                self.game.use_hint()

        def test_22_random_unique_questions(self):
            self.game.start_game(
                count=10,
                random_order=True,
                shuffle_choices=True,
            )

            ids = []

            while self.game.is_active:

                ids.append(
                    self.game.current_quiz.id
                )

                self.correct_answer()

            self.assertEqual(len(ids), 10)
            self.assertEqual(len(set(ids)), 10)

            self.assertEqual(
                self.game.get_result()["score"],
                100.0,
            )

        def test_23_question_bank_unchanged(self):
            original = [
                q.to_dict()
                for q in self.game.list_quizzes()
            ]

            self.game.start_game(count=5)

            while self.game.is_active:
                self.correct_answer()

            after = [
                q.to_dict()
                for q in self.game.list_quizzes()
            ]

            self.assertEqual(original, after)

        def test_24_invalid_json_preserves_bank(self):
            with tempfile.TemporaryDirectory() as directory:

                path = Path(directory) / "invalid.json"

                path.write_text(
                    "{invalid json",
                    encoding="utf-8",
                )

                with self.assertRaises(json.JSONDecodeError):
                    self.game.load_default_quizzes(path)

            self.assertEqual(
                len(self.game.list_quizzes()),
                20,
            )

        def test_25_prevent_changes_during_game(self):
            self.start(2)

            with self.assertRaises(RuntimeError):
                self.game.start_game()

            with self.assertRaises(RuntimeError):
                self.game.add_quiz(
                    self.game.list_quizzes()[0]
                )

            with self.assertRaises(RuntimeError):
                self.game.load_default_quizzes()

        def test_26_result_is_independent(self):
            self.start(1)
            self.correct_answer()

            result = self.game.get_result()

            result["score"] = -100
            result["answers"][0]["points"] = -100

            original = self.game.get_result()

            self.assertEqual(original["score"], 100.0)

            self.assertEqual(
                original["answers"][0]["points"],
                10,
            )

        def test_27_zero_score_is_valid(self):
            self.start(1)
            self.wrong_answer()

            self.assertEqual(
                self.game.best_score,
                0.0,
            )

            self.assertTrue(
                self.game.get_result()["new_best"]
            )

        def test_28_hint_resets_next_question(self):
            self.start(2)

            self.game.use_hint()
            self.correct_answer()

            self.assertFalse(self.game.hint_used)

            result = self.correct_answer()

            self.assertEqual(result["points"], 10)


    if __name__ == "__main__":
        unittest.main()
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        Get-Item -LiteralPath $path |
            Select-Object Name, Length

        "PASS: Twenty-eight QuizGame tests created"

    Name              Length
    ----              ------
    test_quiz_game.py   8786
    PASS: Twenty-eight QuizGame tests created
    Failed: False

    05. Verify Python Syntax

    > python -m py_compile `
            quiz.py `
            quiz_game.py `
            tests/test_quiz.py `
            tests/test_quiz_game.py

        if ($LASTEXITCODE -ne 0) {
            throw "Python syntax verification failed."
        }

        "PASS: Python syntax verified"
    PASS: Python syntax verified
    Failed: False

    06. Run All Forty-Eight Unit Tests

    > python -m unittest discover -s tests -v 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Unit tests failed."
        }

        "PASS: All Quiz and QuizGame unit tests completed"
    python : test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    위치 줄:936 문자:5
    +     python -m unittest discover -s tests -v 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_create_..._object) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok
    test_01_default_question_count (test_quiz_game.TestQuizGame.test_01_default_question_count) ... ok
    test_02_difficulty_filter (test_quiz_game.TestQuizGame.test_02_difficulty_filter) ... ok
    test_03_add_quiz (test_quiz_game.TestQuizGame.test_03_add_quiz) ... ok
    test_04_duplicate_id (test_quiz_game.TestQuizGame.test_04_duplicate_id) ... ok
    test_05_duplicate_question (test_quiz_game.TestQuizGame.test_05_duplicate_question) ... ok
    test_06_next_id (test_quiz_game.TestQuizGame.test_06_next_id) ... ok
    test_07_start_game (test_quiz_game.TestQuizGame.test_07_start_game) ... ok
    test_08_invalid_count (test_quiz_game.TestQuizGame.test_08_invalid_count) ... ok
    test_09_empty_question_bank (test_quiz_game.TestQuizGame.test_09_empty_question_bank) ... ok
    test_10_correct_answer_points (test_quiz_game.TestQuizGame.test_10_correct_answer_points) ... ok
    test_11_wrong_answer_points (test_quiz_game.TestQuizGame.test_11_wrong_answer_points) ... ok
    test_12_hint_points (test_quiz_game.TestQuizGame.test_12_hint_points) ... ok
    test_13_repeated_hint (test_quiz_game.TestQuizGame.test_13_repeated_hint) ... ok
    test_14_hint_with_wrong_answer (test_quiz_game.TestQuizGame.test_14_hint_with_wrong_answer) ... ok
    test_15_invalid_answer_does_not_advance (test_quiz_game.TestQuizGame.test_15_invalid_answer_does_not_advance) ... ok
    test_16_advance_question (test_quiz_game.TestQuizGame.test_16_advance_question) ... ok
    test_17_normalized_score (test_quiz_game.TestQuizGame.test_17_normalized_score) ... ok
    test_18_best_score (test_quiz_game.TestQuizGame.test_18_best_score) ... ok
    test_19_cancel_game (test_quiz_game.TestQuizGame.test_19_cancel_game) ... ok
    test_20_completed_game_state (test_quiz_game.TestQuizGame.test_20_completed_game_state) ... ok
    test_21_no_active_game (test_quiz_game.TestQuizGame.test_21_no_active_game) ... ok
    test_22_random_unique_questions (test_quiz_game.TestQuizGame.test_22_random_unique_questions) ... ok
    test_23_question_bank_unchanged (test_quiz_game.TestQuizGame.test_23_question_bank_unchanged) ... ok
    test_24_invalid_json_preserves_bank (test_quiz_game.TestQuizGame.test_24_invalid_json_preserves_bank) ... ok
    test_25_prevent_changes_during_game (test_quiz_game.TestQuizGame.test_25_prevent_changes_during_game) ... ok
    test_26_result_is_independent (test_quiz_game.TestQuizGame.test_26_result_is_independent) ... ok
    test_27_zero_score_is_valid (test_quiz_game.TestQuizGame.test_27_zero_score_is_valid) ... ok
    test_28_hint_resets_next_question (test_quiz_game.TestQuizGame.test_28_hint_resets_next_question) ... ok

    ----------------------------------------------------------------------
    Ran 48 tests in 0.026s

    OK
    PASS: All Quiz and QuizGame unit tests completed
    Failed: False

    07. Run Actual Game Simulation

    > $code = @'
    import random

    from quiz_game import QuizGame

    game = QuizGame(
        rng=random.Random(42)
    )

    loaded = game.load_default_quizzes()

    print("LOADED QUESTIONS:", loaded)

    game.start_game(
        count=5,
        random_order=False,
        shuffle_choices=False,
    )

    for index in range(5):

        quiz = game.current_quiz

        if index == 2:
            game.use_hint()

        if index == 3:
            answer = quiz.answer % 4 + 1
        else:
            answer = quiz.answer

        result = game.submit_answer(answer)

        print(
            f"QUESTION {index + 1}: "
            f"ID={result['quiz_id']} | "
            f"CORRECT={result['correct']} | "
            f"HINT={result['hint_used']} | "
            f"POINTS={result['points']}"
        )

    result = game.get_result()

    print()
    print("===== FINAL GAME RESULT =====")
    print("TOTAL QUESTIONS:", result["total_questions"])
    print("CORRECT:", result["correct_count"])
    print("WRONG:", result["wrong_count"])
    print("HINTS USED:", result["hint_count"])
    print("EARNED POINTS:", result["earned_points"])
    print("MAX POINTS:", result["max_points"])
    print("NORMALIZED SCORE:", result["score"])
    print("ACCURACY:", result["accuracy"])
    print("BEST SCORE:", result["best_score"])

    assert result["total_questions"] == 5
    assert result["correct_count"] == 4
    assert result["wrong_count"] == 1
    assert result["hint_count"] == 1
    assert result["earned_points"] == 35
    assert result["score"] == 70.0
    assert result["accuracy"] == 80.0
    assert result["best_score"] == 70.0

    print("PASS: Actual game simulation completed")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Game simulation failed."
        }
    LOADED QUESTIONS: 20
    QUESTION 1: ID=1 | CORRECT=True | HINT=False | POINTS=10
    QUESTION 2: ID=2 | CORRECT=True | HINT=False | POINTS=10
    QUESTION 3: ID=3 | CORRECT=True | HINT=True | POINTS=5
    QUESTION 4: ID=4 | CORRECT=False | HINT=False | POINTS=0
    QUESTION 5: ID=5 | CORRECT=True | HINT=False | POINTS=10

    ===== FINAL GAME RESULT =====
    TOTAL QUESTIONS: 5
    CORRECT: 4
    WRONG: 1
    HINTS USED: 1
    EARNED POINTS: 35
    MAX POINTS: 50
    NORMALIZED SCORE: 70.0
    ACCURACY: 80.0
    BEST SCORE: 70.0
    PASS: Actual game simulation completed
    Failed: False

    08. Create Third Git Commit

    > $files = @(
            "quiz_game.py",
            "tests/test_quiz_game.py",
            "logs/04_quiz_class_development.txt"
        )

        foreach ($file in $files) {

            if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
                throw "Missing required file: $file"
            }
        }

        $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "2") {
            throw "Unexpected previous commit count."
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 48:
        raise SystemExit("Expected 48 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        $author = git var GIT_AUTHOR_IDENT

        if ($LASTEXITCODE -ne 0 -or
            $author -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

            throw "Git author email privacy verification failed."
        }

        $committer = git var GIT_COMMITTER_IDENT

        if ($LASTEXITCODE -ne 0 -or
            $committer -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

            throw "Git committer email privacy verification failed."
        }

        foreach ($file in $files) {

            $text = Get-Content `
                -LiteralPath $file `
                -Raw `
                -Encoding UTF8

            if ($text -match 'github_pat_[A-Za-z0-9_]+|gh[pousr]_[A-Za-z0-9]+|sk-[A-Za-z0-9_-]{15,}|-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----') {

                throw "Sensitive pattern detected in $file"
            }
        }

        "PASS: Git identity and sensitive pattern checks"

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staging verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git diff --cached --stat

        if ($LASTEXITCODE -ne 0) {
            throw "Git diff failed."
        }

        git commit -m "Implement QuizGame engine and scoring tests"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: Third Git commit created"
    python : ................................................
    위치 줄:1063 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 48 tests in 0.025s

    OK
    DISCOVERED TESTS: 48
    PASS: Git identity and sensitive pattern checks
    git : warning: in the working copy of 'logs/04_quiz_class_development.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:1100 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

     logs/04_quiz_class_development.txt | 799 +++++++++++++++++++++++++++++++++++++
     quiz_game.py                       | 392 ++++++++++++++++++
     tests/test_quiz_game.py            | 381 ++++++++++++++++++
     3 files changed, 1572 insertions(+)
    [main a49c5db] Implement QuizGame engine and scoring tests
     3 files changed, 1572 insertions(+)
     create mode 100644 logs/04_quiz_class_development.txt
     create mode 100644 quiz_game.py
     create mode 100644 tests/test_quiz_game.py
    PASS: Third Git commit created
    Failed: False

    09. Verify Final Stage Status

    > git log -3 --oneline

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "3") {
            throw "Expected three Git commits."
        }

        "TOTAL COMMITS: $count"

        git status --short --branch

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        "PASS: Working tree is clean"
        "PASS: STEP05 completed"
    a49c5db Implement QuizGame engine and scoring tests
    ccc8cb6 Implement Quiz class with validation and unit tests
    f161dea Initialize quiz project and add 20 default questions
    TOTAL COMMITS: 3
    ## main
    PASS: Working tree is clean
    PASS: STEP05 completed
    Failed: False



### 06_console_development.txt

[Original execution log](../logs/06_console_development.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP06 - Console Application Development
    Date: 2026-11-14 22:38:15

    01. Verify Previous Unit Tests

    > python -m unittest discover -s tests 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Previous unit tests failed."
        }

        "PASS: Previous development stage verified"
    python : ................................................
    위치 줄:51 문자:5
    +     python -m unittest discover -s tests 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 48 tests in 0.025s

    OK
    PASS: Previous development stage verified
    Failed: False

    02. Save STEP05 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP05*QuizGame*Class*Development*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP05 execution log not found."
        }

        $content = Get-Content `
            -LiteralPath $source.FullName `
            -Raw `
            -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP05 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 9) {
            throw "Expected nine successful STEP05 results."
        }

        $content = $content -replace `
            '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
            '${1}<USER>'

        $path = Join-Path `
            (Get-Location).Path `
            "logs\05_quizgame_development.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content,
            $utf8
        )

        "PASS: STEP05 execution evidence saved"
    PASS: STEP05 execution evidence saved
    Failed: False

    03. Create Feature Branch

    > if (-not (Test-Path "logs/05_quizgame_development.txt")) {
            throw "Previous evidence not found."
        }

        python -m unittest discover -s tests 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-branch tests failed."
        }

        git checkout -b feature/quiz-console

        if ($LASTEXITCODE -ne 0) {
            throw "Feature branch creation failed."
        }

        git branch --list

        if ($LASTEXITCODE -ne 0) {
            throw "Branch verification failed."
        }

        "PASS: Console development branch created"
    python : ................................................
    위치 줄:116 문자:5
    +     python -m unittest discover -s tests 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 48 tests in 0.023s

    OK
    git : Switched to a new branch 'feature/quiz-console'
    위치 줄:122 문자:5
    +     git checkout -b feature/quiz-console
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (Switched to a n...e/quiz-console':String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    * feature/quiz-console
      main
    PASS: Console development branch created
    Failed: False

    04. Create Main Console Application

    > $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or
            $branch -ne "feature/quiz-console") {

            throw "Incorrect development branch."
        }

        $path = Join-Path (Get-Location).Path "main.py"

        if (Test-Path -LiteralPath $path) {
            throw "main.py already exists. Review required."
        }

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        Get-Item -LiteralPath $path |
            Select-Object Name, Length

        "PASS: Main console application created"

    Name    Length
    ----    ------
    main.py   8746
    PASS: Main console application created
    Failed: False

    05. Create Console Unit Tests

    > $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or
            $branch -ne "feature/quiz-console") {

            throw "Incorrect development branch."
        }

        $path = Join-Path `
            (Get-Location).Path `
            "tests\test_console.py"

        if (Test-Path -LiteralPath $path) {
            throw "test_console.py already exists."
        }

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Sixteen console tests created"
    PASS: Sixteen console tests created
    Failed: False

    06. Verify Syntax and All Unit Tests

    > python -m py_compile `
            main.py `
            quiz.py `
            quiz_game.py `
            tests/test_console.py

        if ($LASTEXITCODE -ne 0) {
            throw "Python syntax verification failed."
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 64:
        raise SystemExit("Expected 64 tests.")

    result = unittest.TextTestRunner(
        verbosity=2
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Unit tests failed."
        }

        "PASS: All 64 unit tests completed"
    python : test_01_read_text_validation (test_console.TestConsole.test_01_read_text_validation) ... ok
    위치 줄:1012 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_read_te...idation) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_read_int_validation (test_console.TestConsole.test_02_read_int_validation) ... ok
    test_03_show_menu (test_console.TestConsole.test_03_show_menu) ... ok
    test_04_list_questions (test_console.TestConsole.test_04_list_questions) ... ok
    test_05_empty_question_list (test_console.TestConsole.test_05_empty_question_list) ... ok
    test_06_add_question (test_console.TestConsole.test_06_add_question) ... ok
    test_07_duplicate_question (test_console.TestConsole.test_07_duplicate_question) ... ok
    test_08_score_without_record (test_console.TestConsole.test_08_score_without_record) ... ok
    test_09_play_with_correct_answer (test_console.TestConsole.test_09_play_with_correct_answer) ... ok
    test_10_play_with_hint (test_console.TestConsole.test_10_play_with_hint) ... ok
    test_11_cancel_game (test_console.TestConsole.test_11_cancel_game) ... ok
    test_12_empty_game (test_console.TestConsole.test_12_empty_game) ... ok
    test_13_menu_exit (test_console.TestConsole.test_13_menu_exit) ... ok
    test_14_menu_invalid_input (test_console.TestConsole.test_14_menu_invalid_input) ... ok
    test_15_keyboard_interrupt (test_console.TestConsole.test_15_keyboard_interrupt) ... ok
    test_16_eof_error (test_console.TestConsole.test_16_eof_error) ... ok
    test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok
    test_01_default_question_count (test_quiz_game.TestQuizGame.test_01_default_question_count) ... ok
    test_02_difficulty_filter (test_quiz_game.TestQuizGame.test_02_difficulty_filter) ... ok
    test_03_add_quiz (test_quiz_game.TestQuizGame.test_03_add_quiz) ... ok
    test_04_duplicate_id (test_quiz_game.TestQuizGame.test_04_duplicate_id) ... ok
    test_05_duplicate_question (test_quiz_game.TestQuizGame.test_05_duplicate_question) ... ok
    test_06_next_id (test_quiz_game.TestQuizGame.test_06_next_id) ... ok
    test_07_start_game (test_quiz_game.TestQuizGame.test_07_start_game) ... ok
    test_08_invalid_count (test_quiz_game.TestQuizGame.test_08_invalid_count) ... ok
    test_09_empty_question_bank (test_quiz_game.TestQuizGame.test_09_empty_question_bank) ... ok
    test_10_correct_answer_points (test_quiz_game.TestQuizGame.test_10_correct_answer_points) ... ok
    test_11_wrong_answer_points (test_quiz_game.TestQuizGame.test_11_wrong_answer_points) ... ok
    test_12_hint_points (test_quiz_game.TestQuizGame.test_12_hint_points) ... ok
    test_13_repeated_hint (test_quiz_game.TestQuizGame.test_13_repeated_hint) ... ok
    test_14_hint_with_wrong_answer (test_quiz_game.TestQuizGame.test_14_hint_with_wrong_answer) ... ok
    test_15_invalid_answer_does_not_advance (test_quiz_game.TestQuizGame.test_15_invalid_answer_does_not_advance) ... ok
    test_16_advance_question (test_quiz_game.TestQuizGame.test_16_advance_question) ... ok
    test_17_normalized_score (test_quiz_game.TestQuizGame.test_17_normalized_score) ... ok
    test_18_best_score (test_quiz_game.TestQuizGame.test_18_best_score) ... ok
    test_19_cancel_game (test_quiz_game.TestQuizGame.test_19_cancel_game) ... ok
    test_20_completed_game_state (test_quiz_game.TestQuizGame.test_20_completed_game_state) ... ok
    test_21_no_active_game (test_quiz_game.TestQuizGame.test_21_no_active_game) ... ok
    test_22_random_unique_questions (test_quiz_game.TestQuizGame.test_22_random_unique_questions) ... ok
    test_23_question_bank_unchanged (test_quiz_game.TestQuizGame.test_23_question_bank_unchanged) ... ok
    test_24_invalid_json_preserves_bank (test_quiz_game.TestQuizGame.test_24_invalid_json_preserves_bank) ... ok
    test_25_prevent_changes_during_game (test_quiz_game.TestQuizGame.test_25_prevent_changes_during_game) ... ok
    test_26_result_is_independent (test_quiz_game.TestQuizGame.test_26_result_is_independent) ... ok
    test_27_zero_score_is_valid (test_quiz_game.TestQuizGame.test_27_zero_score_is_valid) ... ok
    test_28_hint_resets_next_question (test_quiz_game.TestQuizGame.test_28_hint_resets_next_question) ... ok

    ----------------------------------------------------------------------
    Ran 64 tests in 0.048s

    OK
    DISCOVERED TESTS: 64
    PASS: All 64 unit tests completed
    Failed: False

    07. Run Actual Console Smoke Test

    > $env:PYTHONIOENCODING = "utf-8"

        $previousEncoding = [Console]::OutputEncoding

        try {

            [Console]::OutputEncoding = `
                New-Object System.Text.UTF8Encoding($false)

            $output = @(
                @("3", "4", "0") |
                    python main.py 2>&1
            )

            $exitCode = $LASTEXITCODE

            $output | ForEach-Object {
                "$_"
            }

            if ($exitCode -ne 0) {
                throw "Console application failed."
            }

            $text = $output -join "`n"

            foreach ($marker in @(
                "MACHINE TOOL & VIBRATION QUIZ",
                "QUESTION LIST",
                "BEST SCORE"
            )) {

                if (-not $text.Contains($marker)) {
                    throw "Missing console output: $marker"
                }
            }

            "PASS: Actual console smoke test completed"
        }
        finally {

            [Console]::OutputEncoding = $previousEncoding

            Remove-Item Env:PYTHONIOENCODING `
                -ErrorAction SilentlyContinue
        }

    ==========================================================
           MACHINE TOOL & VIBRATION QUIZ
           CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==========================================================
     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 기록 없음
    ----------------------------------------------------------
     [1] 퀴즈 풀기 (Play)
     [2] 문제 추가 (Add)
     [3] 문제 목록 (List)
     [4] 최고 점수 (Score)
     [0] 프로그램 종료 (Exit)
    ----------------------------------------------------------
    메뉴 선택 (0~4):
    ==========================================================
                  QUESTION LIST
    ==========================================================
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
    ----------------------------------------------------------
    전체 등록 문제: 20개

    ==========================================================
           MACHINE TOOL & VIBRATION QUIZ
           CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==========================================================
     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 기록 없음
    ----------------------------------------------------------
     [1] 퀴즈 풀기 (Play)
     [2] 문제 추가 (Add)
     [3] 문제 목록 (List)
     [4] 최고 점수 (Score)
     [0] 프로그램 종료 (Exit)
    ----------------------------------------------------------
    메뉴 선택 (0~4):
    ==========================================================
                  BEST SCORE
    ==========================================================
    아직 완료된 게임 기록이 없습니다.
    ==========================================================

    ==========================================================
           MACHINE TOOL & VIBRATION QUIZ
           CODYSSEY AI ALL-IN-ONE | M_E1-2
    ==========================================================
     등록 문제 : 20개
     초급 / 중급 : 10 / 10
     최고 점수 : 기록 없음
    ----------------------------------------------------------
     [1] 퀴즈 풀기 (Play)
     [2] 문제 추가 (Add)
     [3] 문제 목록 (List)
     [4] 최고 점수 (Score)
     [0] 프로그램 종료 (Exit)
    ----------------------------------------------------------
    메뉴 선택 (0~4): 프로그램을 종료합니다.
    PASS: Actual console smoke test completed
    Failed: False

    08. Commit Console Feature

    > $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or
            $branch -ne "feature/quiz-console") {

            throw "Incorrect feature branch."
        }

        $files = @(
            "main.py",
            "tests/test_console.py",
            "logs/05_quizgame_development.txt"
        )

        foreach ($file in $files) {

            if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
                throw "Missing required file: $file"
            }
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    if suite.countTestCases() != 64:
        raise SystemExit("Expected 64 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staged file verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git commit -m "Feat: Implement interactive quiz console"

        if ($LASTEXITCODE -ne 0) {
            throw "Console feature commit failed."
        }

        "PASS: Console feature committed"
    python : ................................................................
    위치 줄:1111 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 64 tests in 0.039s

    OK
    git : warning: in the working copy of 'logs/05_quizgame_development.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:1117 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    [feature/quiz-console 2c19fe7] Feat: Implement interactive quiz console
     3 files changed, 2088 insertions(+)
     create mode 100644 logs/05_quizgame_development.txt
     create mode 100644 main.py
     create mode 100644 tests/test_console.py
    PASS: Console feature committed
    Failed: False

    09. Merge Feature Branch into Main

    > $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or
            $branch -ne "feature/quiz-console") {

            throw "Incorrect feature branch."
        }

        $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "4") {
            throw "Expected four commits before merge."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Feature branch is not clean."
        }

        python -m unittest discover -s tests 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-merge tests failed."
        }

        git checkout main

        if ($LASTEXITCODE -ne 0) {
            throw "Checkout main failed."
        }

        git merge --no-ff feature/quiz-console `
            -m "Merge feature/quiz-console into main"

        if ($LASTEXITCODE -ne 0) {
            throw "Feature branch merge failed."
        }

        "PASS: Feature branch merged into main"
    python : ................................................................
    위치 줄:1170 문자:5
    +     python -m unittest discover -s tests 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 64 tests in 0.041s

    OK
    git : Switched to branch 'main'
    위치 줄:1176 문자:5
    +     git checkout main
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (Switched to branch 'main':String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    Merge made by the 'ort' strategy.
     logs/05_quizgame_development.txt | 1311 ++++++++++++++++++++++++++++++++++++++
     main.py                          |  446 +++++++++++++
     tests/test_console.py            |  331 ++++++++++
     3 files changed, 2088 insertions(+)
     create mode 100644 logs/05_quizgame_development.txt
     create mode 100644 main.py
     create mode 100644 tests/test_console.py
    PASS: Feature branch merged into main
    Failed: False

    10. Verify Final Status

    > $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
            throw "Expected main branch."
        }

        $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "5") {
            throw "Expected five Git commits."
        }

        git log --oneline --graph --all

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        git status --short --branch

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        python -m unittest discover -s tests 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Post-merge tests failed."
        }

        "TOTAL COMMITS: $count"
        "TOTAL UNIT TESTS EXPECTED: 64"
        "PASS: STEP06 completed"
    *   a01099c Merge feature/quiz-console into main
    |\
    | * 2c19fe7 Feat: Implement interactive quiz console
    |/
    * a49c5db Implement QuizGame engine and scoring tests
    * ccc8cb6 Implement Quiz class with validation and unit tests
    * f161dea Initialize quiz project and add 20 default questions
    ## main
    python : ................................................................
    위치 줄:1224 문자:5
    +     python -m unittest discover -s tests 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 64 tests in 0.034s

    OK
    TOTAL COMMITS: 5
    TOTAL UNIT TESTS EXPECTED: 64
    PASS: STEP06 completed
    Failed: False



### 07_json_persistence.txt

[Original execution log](../logs/07_json_persistence.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP07 - JSON Persistence
    Date: 2026-11-14 22:43:25

    01. Verify Previous Unit Tests

    > python -m unittest discover -s tests 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Previous tests failed."
        }

        "PASS: Previous development stage verified"
    python : ................................................................
    위치 줄:57 문자:5
    +     python -m unittest discover -s tests 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 64 tests in 0.035s

    OK
    PASS: Previous development stage verified
    Failed: False

    02. Save STEP06 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP06*Console*Application*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP06 execution log not found."
        }

        $content = Get-Content `
            -LiteralPath $source.FullName `
            -Raw `
            -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP06 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 10) {
            throw "Expected ten successful STEP06 results."
        }

        $content = $content -replace `
            '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
            '${1}<USER>'

        $path = Join-Path `
            (Get-Location).Path `
            "logs\06_console_development.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content,
            $utf8
        )

        "PASS: STEP06 execution evidence saved"
    PASS: STEP06 execution evidence saved
    Failed: False

    03. Create JSON Storage Module

    > $path = Join-Path (Get-Location).Path "storage.py"

        if (Test-Path -LiteralPath $path) {
            throw "storage.py already exists."
        }

        $content = @'
    """JSON persistence and recovery for the quiz application."""

    import json
    import math
    import os
    from datetime import datetime
    from pathlib import Path

    from quiz import Quiz
    from quiz_game import QuizGame


    ROOT = Path(__file__).resolve().parent

    DEFAULT_PATH = ROOT / "data" / "default_quizzes.json"
    STATE_PATH = ROOT / "state.json"


    class QuizStorage:
        """Load, validate and atomically save quiz state."""

        def __init__(self, path=None, default_path=None):

            self.path = (
                Path(path)
                if path is not None
                else STATE_PATH
            )

            self.default_path = (
                Path(default_path)
                if default_path is not None
                else DEFAULT_PATH
            )

            self.last_warning = None
            self.last_backup = None

        @staticmethod
        def validate_score(score):

            if score is None:
                return

            if type(score) not in (int, float):
                raise ValueError("최고 점수의 형식이 올바르지 않습니다.")

            if not math.isfinite(score):
                raise ValueError("유효하지 않은 최고 점수입니다.")

            if not 0 <= score <= 100:
                raise ValueError("최고 점수는 0~100이어야 합니다.")

        def decode_state(self, data):
            """Validate saved data before creating a game."""

            if not isinstance(data, dict):
                raise ValueError("저장 데이터는 딕셔너리여야 합니다.")

            if not {"quizzes", "best_score"}.issubset(data):
                raise ValueError("필수 저장 항목이 없습니다.")

            version = data.get("schema_version", 1)

            if type(version) is not int or version != 1:
                raise ValueError("지원하지 않는 저장 형식입니다.")

            if not isinstance(data["quizzes"], list):
                raise ValueError("문제 데이터는 리스트여야 합니다.")

            self.validate_score(data["best_score"])

            quizzes = [
                Quiz.from_dict(item)
                for item in data["quizzes"]
            ]

            game = QuizGame(quizzes=quizzes)

            game.best_score = (
                None
                if data["best_score"] is None
                else float(data["best_score"])
            )

            return game

        def load_defaults(self):
            """Create a game from the original question bank."""

            game = QuizGame()

            game.load_default_quizzes(
                self.default_path
            )

            return game

        def backup_corrupt_state(self):
            """Preserve a damaged state file before recovery."""

            stamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S_%f"
            )

            backup = self.path.with_name(
                f"{self.path.name}.corrupt-{stamp}"
            )

            self.path.rename(backup)

            self.last_backup = backup

            return backup

        def load(self):
            """Load saved state or initialize the default bank."""

            self.last_warning = None
            self.last_backup = None

            try:

                text = self.path.read_text(
                    encoding="utf-8"
                )

            except FileNotFoundError:

                return self.load_defaults()

            except UnicodeError:

                game = self.load_defaults()
                backup = self.backup_corrupt_state()

                self.last_warning = (
                    "저장 파일 인코딩이 손상되었습니다. "
                    f"백업: {backup.name}. "
                    "기본 문제로 복구합니다."
                )

                return game

            try:

                data = json.loads(text)

                return self.decode_state(data)

            except (ValueError, TypeError) as error:

                game = self.load_defaults()
                backup = self.backup_corrupt_state()

                self.last_warning = (
                    "저장 파일이 손상되었습니다. "
                    f"원인: {error}. "
                    f"백업: {backup.name}. "
                    "기본 문제로 복구합니다."
                )

                return game

        def save(self, game):
            """Save game state using an atomic file replacement."""

            if not isinstance(game, QuizGame):
                raise TypeError("QuizGame 객체가 필요합니다.")

            if game.is_active:
                raise RuntimeError(
                    "게임 진행 중에는 저장할 수 없습니다."
                )

            self.validate_score(game.best_score)

            data = {
                "schema_version": 1,
                "quizzes": [
                    quiz.to_dict()
                    for quiz in game.list_quizzes()
                ],
                "best_score": game.best_score,
            }

            self.decode_state(data)

            self.path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            temporary = self.path.with_name(
                self.path.name + ".tmp"
            )

            try:

                with temporary.open(
                    "w",
                    encoding="utf-8",
                    newline="\n",
                ) as file:

                    json.dump(
                        data,
                        file,
                        ensure_ascii=False,
                        indent=4,
                        allow_nan=False,
                    )

                    file.write("\n")
                    file.flush()

                    os.fsync(file.fileno())

                os.replace(
                    temporary,
                    self.path,
                )

            finally:

                if temporary.exists():
                    temporary.unlink()

            return self.path
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: JSON storage module created"
    PASS: JSON storage module created
    Failed: False

    04. Connect Storage to Console Application

    > if (-not (Test-Path "storage.py")) {
            throw "Storage module not found."
        }

        $path = Join-Path (Get-Location).Path "main.py"

        $content = @'
    """Console interface for the machine tool vibration quiz."""

    import sys

    from quiz import Quiz
    from quiz_game import QuizGame
    from storage import QuizStorage


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


    def save_state(game, storage):
        """Save the current state and report failures."""

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


    def play_quiz(game, storage=None):
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

        save_state(game, storage)


    def add_question(game, storage=None):
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

        save_state(game, storage)


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


    def run_menu(game, storage=None):
        """Run the main menu until the user exits."""

        actions = {
            1: lambda: play_quiz(game, storage),
            2: lambda: add_question(game, storage),
            3: lambda: list_questions(game),
            4: lambda: show_score(game),
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

                    if not save_state(game, storage):

                        print(
                            "저장하지 못했습니다. "
                            "메뉴에서 다시 종료를 시도하세요."
                        )

                        continue

                    print("프로그램을 종료합니다.")

                    return 0

                try:

                    actions[choice]()

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
        """Load persistent state and launch the menu."""

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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Persistent storage connected to main.py"
    PASS: Persistent storage connected to main.py
    Failed: False

    05. Create Storage Unit Tests

    > $path = Join-Path `
            (Get-Location).Path `
            "tests\test_storage.py"

        if (Test-Path -LiteralPath $path) {
            throw "test_storage.py already exists."
        }

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Twenty storage tests created"
    PASS: Twenty storage tests created
    Failed: False

    06. Run All Eighty-Four Unit Tests

    > python -m py_compile `
            main.py `
            quiz.py `
            quiz_game.py `
            storage.py `
            tests/test_storage.py

        if ($LASTEXITCODE -ne 0) {
            throw "Python syntax verification failed."
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 84:
        raise SystemExit("Expected 84 tests.")

    result = unittest.TextTestRunner(
        verbosity=2
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Unit tests failed."
        }

        "PASS: All 84 unit tests completed"
    python : test_01_read_text_validation (test_console.TestConsole.test_01_read_text_validation) ... ok
    위치 줄:1387 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_read_te...idation) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_read_int_validation (test_console.TestConsole.test_02_read_int_validation) ... ok
    test_03_show_menu (test_console.TestConsole.test_03_show_menu) ... ok
    test_04_list_questions (test_console.TestConsole.test_04_list_questions) ... ok
    test_05_empty_question_list (test_console.TestConsole.test_05_empty_question_list) ... ok
    test_06_add_question (test_console.TestConsole.test_06_add_question) ... ok
    test_07_duplicate_question (test_console.TestConsole.test_07_duplicate_question) ... ok
    test_08_score_without_record (test_console.TestConsole.test_08_score_without_record) ... ok
    test_09_play_with_correct_answer (test_console.TestConsole.test_09_play_with_correct_answer) ... ok
    test_10_play_with_hint (test_console.TestConsole.test_10_play_with_hint) ... ok
    test_11_cancel_game (test_console.TestConsole.test_11_cancel_game) ... ok
    test_12_empty_game (test_console.TestConsole.test_12_empty_game) ... ok
    test_13_menu_exit (test_console.TestConsole.test_13_menu_exit) ... ok
    test_14_menu_invalid_input (test_console.TestConsole.test_14_menu_invalid_input) ... ok
    test_15_keyboard_interrupt (test_console.TestConsole.test_15_keyboard_interrupt) ... ok
    test_16_eof_error (test_console.TestConsole.test_16_eof_error) ... ok
    test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok
    test_01_default_question_count (test_quiz_game.TestQuizGame.test_01_default_question_count) ... ok
    test_02_difficulty_filter (test_quiz_game.TestQuizGame.test_02_difficulty_filter) ... ok
    test_03_add_quiz (test_quiz_game.TestQuizGame.test_03_add_quiz) ... ok
    test_04_duplicate_id (test_quiz_game.TestQuizGame.test_04_duplicate_id) ... ok
    test_05_duplicate_question (test_quiz_game.TestQuizGame.test_05_duplicate_question) ... ok
    test_06_next_id (test_quiz_game.TestQuizGame.test_06_next_id) ... ok
    test_07_start_game (test_quiz_game.TestQuizGame.test_07_start_game) ... ok
    test_08_invalid_count (test_quiz_game.TestQuizGame.test_08_invalid_count) ... ok
    test_09_empty_question_bank (test_quiz_game.TestQuizGame.test_09_empty_question_bank) ... ok
    test_10_correct_answer_points (test_quiz_game.TestQuizGame.test_10_correct_answer_points) ... ok
    test_11_wrong_answer_points (test_quiz_game.TestQuizGame.test_11_wrong_answer_points) ... ok
    test_12_hint_points (test_quiz_game.TestQuizGame.test_12_hint_points) ... ok
    test_13_repeated_hint (test_quiz_game.TestQuizGame.test_13_repeated_hint) ... ok
    test_14_hint_with_wrong_answer (test_quiz_game.TestQuizGame.test_14_hint_with_wrong_answer) ... ok
    test_15_invalid_answer_does_not_advance (test_quiz_game.TestQuizGame.test_15_invalid_answer_does_not_advance) ... ok
    test_16_advance_question (test_quiz_game.TestQuizGame.test_16_advance_question) ... ok
    test_17_normalized_score (test_quiz_game.TestQuizGame.test_17_normalized_score) ... ok
    test_18_best_score (test_quiz_game.TestQuizGame.test_18_best_score) ... ok
    test_19_cancel_game (test_quiz_game.TestQuizGame.test_19_cancel_game) ... ok
    test_20_completed_game_state (test_quiz_game.TestQuizGame.test_20_completed_game_state) ... ok
    test_21_no_active_game (test_quiz_game.TestQuizGame.test_21_no_active_game) ... ok
    test_22_random_unique_questions (test_quiz_game.TestQuizGame.test_22_random_unique_questions) ... ok
    test_23_question_bank_unchanged (test_quiz_game.TestQuizGame.test_23_question_bank_unchanged) ... ok
    test_24_invalid_json_preserves_bank (test_quiz_game.TestQuizGame.test_24_invalid_json_preserves_bank) ... ok
    test_25_prevent_changes_during_game (test_quiz_game.TestQuizGame.test_25_prevent_changes_during_game) ... ok
    test_26_result_is_independent (test_quiz_game.TestQuizGame.test_26_result_is_independent) ... ok
    test_27_zero_score_is_valid (test_quiz_game.TestQuizGame.test_27_zero_score_is_valid) ... ok
    test_28_hint_resets_next_question (test_quiz_game.TestQuizGame.test_28_hint_resets_next_question) ... ok
    test_01_missing_state (test_storage.TestStorage.test_01_missing_state) ... ok
    test_02_create_state (test_storage.TestStorage.test_02_create_state) ... ok
    test_03_required_schema (test_storage.TestStorage.test_03_required_schema) ... ok
    test_04_quiz_persistence (test_storage.TestStorage.test_04_quiz_persistence) ... ok
    test_05_best_score_persistence (test_storage.TestStorage.test_05_best_score_persistence) ... ok
    test_06_none_score_persistence (test_storage.TestStorage.test_06_none_score_persistence) ... ok
    test_07_zero_score_persistence (test_storage.TestStorage.test_07_zero_score_persistence) ... ok
    test_08_empty_bank_persistence (test_storage.TestStorage.test_08_empty_bank_persistence) ... ok
    test_09_utf8_encoding (test_storage.TestStorage.test_09_utf8_encoding) ... ok
    test_10_corrupt_json_recovery (test_storage.TestStorage.test_10_corrupt_json_recovery) ... ok
    test_11_invalid_encoding_recovery (test_storage.TestStorage.test_11_invalid_encoding_recovery) ... ok
    test_12_invalid_schema_recovery (test_storage.TestStorage.test_12_invalid_schema_recovery) ... ok
    test_13_invalid_score_validation (test_storage.TestStorage.test_13_invalid_score_validation) ... ok
    test_14_duplicate_id_recovery (test_storage.TestStorage.test_14_duplicate_id_recovery) ... ok
    test_15_atomic_save_failure (test_storage.TestStorage.test_15_atomic_save_failure) ... ok
    test_16_active_game_save_blocked (test_storage.TestStorage.test_16_active_game_save_blocked) ... ok
    test_17_add_console_autosave (test_storage.TestStorage.test_17_add_console_autosave) ... ok
    test_18_game_console_autosave (test_storage.TestStorage.test_18_game_console_autosave) ... ok
    test_19_exit_saves_state (test_storage.TestStorage.test_19_exit_saves_state) ... ok
    test_20_interrupt_saves_state (test_storage.TestStorage.test_20_interrupt_saves_state) ... ok

    ----------------------------------------------------------------------
    Ran 84 tests in 0.122s

    OK
    DISCOVERED TESTS: 84
    PASS: All 84 unit tests completed
    Failed: False

    07. Verify Persistence Across Python Processes

    > $code = @'
    import os
    import subprocess
    import sys
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as directory:

        state = Path(directory) / "state.json"

        env = os.environ.copy()
        env["QUIZ_TEST_STATE"] = str(state)
        env["PYTHONIOENCODING"] = "utf-8"

        writer = """
    import os
    from quiz import Quiz
    from storage import QuizStorage

    storage = QuizStorage(
        path=os.environ["QUIZ_TEST_STATE"]
    )

    game = storage.load()

    data = game.list_quizzes()[0].to_dict()
    data["id"] = 21
    data["question"] = "Cross-process persistence test"

    game.add_quiz(Quiz.from_dict(data))

    game.start_game(count=1)
    game.submit_answer(game.current_quiz.answer)

    storage.save(game)

    print("PROCESS 1: SAVED")
    print("QUESTIONS:", len(game.list_quizzes()))
    print("BEST SCORE:", game.best_score)
    """

        reader = """
    import os
    from storage import QuizStorage

    storage = QuizStorage(
        path=os.environ["QUIZ_TEST_STATE"]
    )

    game = storage.load()

    assert len(game.list_quizzes()) == 21
    assert game.best_score == 100.0

    assert game.list_quizzes()[-1].question == (
        "Cross-process persistence test"
    )

    print("PROCESS 2: RESTORED")
    print("QUESTIONS:", len(game.list_quizzes()))
    print("BEST SCORE:", game.best_score)
    print("PASS: Independent process persistence verified")
    """

        for script in (writer, reader):

            result = subprocess.run(
                [sys.executable, "-c", script],
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=True,
            )

            print(result.stdout)

    print("PASS: Restart persistence test completed")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Cross-process persistence test failed."
        }
    PROCESS 1: SAVED
    QUESTIONS: 21
    BEST SCORE: 100.0

    PROCESS 2: RESTORED
    QUESTIONS: 21
    BEST SCORE: 100.0
    PASS: Independent process persistence verified

    PASS: Restart persistence test completed
    Failed: False

    08. Verify Corrupt State Recovery

    > $code = @'
    import tempfile
    from pathlib import Path

    from storage import QuizStorage

    with tempfile.TemporaryDirectory() as directory:

        path = Path(directory) / "state.json"

        original = "{broken json"

        path.write_text(
            original,
            encoding="utf-8"
        )

        storage = QuizStorage(path=path)

        game = storage.load()

        assert storage.last_warning
        assert storage.last_backup.is_file()

        assert storage.last_backup.read_text(
            encoding="utf-8"
        ) == original

        assert len(game.list_quizzes()) == 20

        print("CORRUPT STATE: DETECTED")
        print("BACKUP: CREATED")
        print("DEFAULT QUESTIONS:", len(game.list_quizzes()))

        storage.save(game)

        restored = storage.load()

        assert len(restored.list_quizzes()) == 20

        print("NEW STATE: VALID")
        print("PASS: Corrupt state recovery verified")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Corrupt state recovery test failed."
        }
    CORRUPT STATE: DETECTED
    BACKUP: CREATED
    DEFAULT QUESTIONS: 20
    NEW STATE: VALID
    PASS: Corrupt state recovery verified
    Failed: False

    09. Verify Runtime Data Ignore Rules

    > foreach ($file in @(
            "state.json",
            "state.json.tmp",
            "state.json.corrupt-test"
        )) {

            git check-ignore --no-index -- $file

            if ($LASTEXITCODE -ne 0) {
                throw "Ignore rule failed: $file"
            }
        }

        $tracked = @(
            git ls-files -- `
                "state.json" `
                "state.json.tmp" `
                "state.json.corrupt-*"
        )

        if ($LASTEXITCODE -ne 0 -or
            $tracked.Count -gt 0) {

            throw "Runtime data is tracked by Git."
        }

        "PASS: Runtime data excluded from Git"
    state.json
    state.json.tmp
    state.json.corrupt-test
    PASS: Runtime data excluded from Git
    Failed: False

    10. Commit JSON Persistence Feature

    > $files = @(
            "storage.py",
            "main.py",
            "tests/test_storage.py",
            "logs/06_console_development.txt",
            "screenshots/03_Quiz_Main_Menu.png"
        )

        foreach ($file in $files) {

            if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
                throw "Missing required file: $file"
            }
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    if suite.countTestCases() != 84:
        raise SystemExit("Expected 84 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        foreach ($kind in @(
            "GIT_AUTHOR_IDENT",
            "GIT_COMMITTER_IDENT"
        )) {

            $identity = git var $kind

            if ($LASTEXITCODE -ne 0 -or
                $identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

                throw "Git email privacy check failed."
            }
        }

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staging verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git diff --cached --stat

        if ($LASTEXITCODE -ne 0) {
            throw "Git diff failed."
        }

        git commit -m "Feat: Add JSON persistence and state recovery"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: JSON persistence feature committed"
    python : ....................................................................................
    위치 줄:1604 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 84 tests in 0.125s

    OK
    git : warning: in the working copy of 'logs/06_console_development.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:1624 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

     logs/06_console_development.txt   | 1459 +++++++++++++++++++++++++++++++++++++
     main.py                           |  100 ++-
     screenshots/03_Quiz_Main_Menu.png |  Bin 0 -> 12803 bytes
     storage.py                        |  229 ++++++
     tests/test_storage.py             |  426 +++++++++++
     5 files changed, 2198 insertions(+), 16 deletions(-)
    [main 03119eb] Feat: Add JSON persistence and state recovery
     5 files changed, 2198 insertions(+), 16 deletions(-)
     create mode 100644 logs/06_console_development.txt
     create mode 100644 screenshots/03_Quiz_Main_Menu.png
     create mode 100644 storage.py
     create mode 100644 tests/test_storage.py
    PASS: JSON persistence feature committed
    Failed: False

    11. Verify Final Stage Status

    > $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "6") {
            throw "Expected six Git commits."
        }

        git log -6 --oneline --graph

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or
            $status.Count -gt 0) {

            throw "Working tree is not clean."
        }

        "TOTAL COMMITS: $count"
        "TOTAL UNIT TESTS EXPECTED: 84"
        "PASS: Working tree is clean"
        "PASS: STEP07 completed"
    * 03119eb Feat: Add JSON persistence and state recovery
    *   a01099c Merge feature/quiz-console into main
    |\
    | * 2c19fe7 Feat: Implement interactive quiz console
    |/
    * a49c5db Implement QuizGame engine and scoring tests
    * ccc8cb6 Implement Quiz class with validation and unit tests
    * f161dea Initialize quiz project and add 20 default questions
    TOTAL COMMITS: 6
    TOTAL UNIT TESTS EXPECTED: 84
    PASS: Working tree is clean
    PASS: STEP07 completed
    Failed: False



### 08_bonus_features.txt

[Original execution log](../logs/08_bonus_features.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP08 - Bonus Features
    Date: 2026-11-14 22:49:25

    01. Save STEP07 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP07*JSON*Persistence*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP07 execution log not found."
        }

        $content = Get-Content `
            -LiteralPath $source.FullName `
            -Raw `
            -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP07 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 11) {
            throw "Expected eleven successful STEP07 results."
        }

        $content = $content -replace `
            '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
            '${1}<USER>'

        $path = Join-Path `
            (Get-Location).Path `
            "logs\07_json_persistence.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content,
            $utf8
        )

        "PASS: STEP07 execution evidence saved"
    PASS: STEP07 execution evidence saved
    Failed: False

    02. Create History and Delete Module

    > $path = Join-Path (Get-Location).Path "history.py"

        if (Test-Path -LiteralPath $path) {
            throw "history.py already exists."
        }

        $content = @'
    """Play history and question management."""

    import math
    from datetime import datetime

    from quiz_game import QuizGame


    def get_history(game):
        """Return the history associated with a game."""

        if not hasattr(game, "play_history"):
            game.play_history = []

        return game.play_history


    def validate_history(history):
        """Validate persistent history records."""

        if not isinstance(history, list):
            raise ValueError("History must be a list.")

        required = {
            "played_at",
            "total_questions",
            "correct_count",
            "wrong_count",
            "hint_count",
            "score",
            "accuracy",
        }

        for record in history:

            if not isinstance(record, dict):
                raise ValueError("Invalid history record.")

            if not required.issubset(record):
                raise ValueError("Missing history fields.")

            if not isinstance(record["played_at"], str):
                raise ValueError("Invalid history date.")

            datetime.fromisoformat(record["played_at"])

            for key in (
                "total_questions",
                "correct_count",
                "wrong_count",
                "hint_count",
            ):

                value = record[key]

                if type(value) is not int or value < 0:
                    raise ValueError("Invalid history count.")

            total = record["total_questions"]

            if total < 1:
                raise ValueError("Invalid question count.")

            if (
                record["correct_count"]
                + record["wrong_count"]
                != total
            ):
                raise ValueError("Invalid answer counts.")

            if record["hint_count"] > total:
                raise ValueError("Invalid hint count.")

            for key in ("score", "accuracy"):

                value = record[key]

                if type(value) not in (int, float):
                    raise ValueError("Invalid history score.")

                if not math.isfinite(value):
                    raise ValueError("Non-finite history score.")

                if not 0 <= value <= 100:
                    raise ValueError("History score out of range.")

        return [dict(record) for record in history]


    def record_game(game, result):
        """Record a completed quiz session."""

        if game.is_active:
            raise RuntimeError("Game is still active.")

        record = {
            "played_at": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            "total_questions": result["total_questions"],
            "correct_count": result["correct_count"],
            "wrong_count": result["wrong_count"],
            "hint_count": result["hint_count"],
            "score": result["score"],
            "accuracy": result["accuracy"],
        }

        validate_history([record])

        get_history(game).append(record)

        return dict(record)


    def history_summary(game):
        """Calculate summary statistics."""

        records = get_history(game)

        if not records:

            return {
                "count": 0,
                "average": None,
                "best": game.best_score,
            }

        average = sum(
            record["score"]
            for record in records
        ) / len(records)

        return {
            "count": len(records),
            "average": round(average, 1),
            "best": game.best_score,
        }


    def delete_question(game, quiz_id):
        """Delete a question while preserving completed records."""

        if game.is_active:
            raise RuntimeError(
                "Cannot delete questions during a game."
            )

        quizzes = game.list_quizzes()

        remaining = [
            quiz
            for quiz in quizzes
            if quiz.id != quiz_id
        ]

        if len(remaining) == len(quizzes):
            raise ValueError("Question ID not found.")

        replacement = QuizGame(quizzes=remaining)

        replacement.best_score = game.best_score

        replacement.play_history = validate_history(
            get_history(game)
        )

        return replacement
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: History and delete module created"
    PASS: History and delete module created
    Failed: False

    03. Upgrade JSON Storage

    > $path = Join-Path (Get-Location).Path "storage.py"

        $content = @'
    """JSON persistence and recovery for the quiz application."""

    import json
    import math
    import os
    from datetime import datetime
    from pathlib import Path

    from history import get_history, validate_history
    from quiz import Quiz
    from quiz_game import QuizGame


    ROOT = Path(__file__).resolve().parent

    DEFAULT_PATH = ROOT / "data" / "default_quizzes.json"
    STATE_PATH = ROOT / "state.json"


    class QuizStorage:
        """Load, validate and atomically save quiz state."""

        def __init__(self, path=None, default_path=None):

            self.path = (
                Path(path)
                if path is not None
                else STATE_PATH
            )

            self.default_path = (
                Path(default_path)
                if default_path is not None
                else DEFAULT_PATH
            )

            self.last_warning = None
            self.last_backup = None

        @staticmethod
        def validate_score(score):

            if score is None:
                return

            if type(score) not in (int, float):
                raise ValueError("최고 점수의 형식이 올바르지 않습니다.")

            if not math.isfinite(score):
                raise ValueError("유효하지 않은 최고 점수입니다.")

            if not 0 <= score <= 100:
                raise ValueError("최고 점수는 0~100이어야 합니다.")

        def decode_state(self, data):
            """Validate saved data before creating a game."""

            if not isinstance(data, dict):
                raise ValueError("저장 데이터는 딕셔너리여야 합니다.")

            if not {"quizzes", "best_score"}.issubset(data):
                raise ValueError("필수 저장 항목이 없습니다.")

            version = data.get("schema_version", 1)

            if type(version) is not int or version != 1:
                raise ValueError("지원하지 않는 저장 형식입니다.")

            if not isinstance(data["quizzes"], list):
                raise ValueError("문제 데이터는 리스트여야 합니다.")

            self.validate_score(data["best_score"])

            quizzes = [
                Quiz.from_dict(item)
                for item in data["quizzes"]
            ]

            game = QuizGame(quizzes=quizzes)

            game.best_score = (
                None
                if data["best_score"] is None
                else float(data["best_score"])
            )

            game.play_history = validate_history(
                data.get("history", [])
            )

            return game

        def load_defaults(self):

            game = QuizGame()

            game.load_default_quizzes(
                self.default_path
            )

            game.play_history = []

            return game

        def backup_corrupt_state(self):

            stamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S_%f"
            )

            backup = self.path.with_name(
                f"{self.path.name}.corrupt-{stamp}"
            )

            self.path.rename(backup)

            self.last_backup = backup

            return backup

        def load(self):

            self.last_warning = None
            self.last_backup = None

            try:

                text = self.path.read_text(
                    encoding="utf-8"
                )

            except FileNotFoundError:

                return self.load_defaults()

            except UnicodeError:

                game = self.load_defaults()
                backup = self.backup_corrupt_state()

                self.last_warning = (
                    "저장 파일 인코딩이 손상되었습니다. "
                    f"백업: {backup.name}. "
                    "기본 문제로 복구합니다."
                )

                return game

            try:

                data = json.loads(text)

                return self.decode_state(data)

            except (ValueError, TypeError, KeyError) as error:

                game = self.load_defaults()
                backup = self.backup_corrupt_state()

                self.last_warning = (
                    "저장 파일이 손상되었습니다. "
                    f"원인: {error}. "
                    f"백업: {backup.name}. "
                    "기본 문제로 복구합니다."
                )

                return game

        def save(self, game):

            if not isinstance(game, QuizGame):
                raise TypeError("QuizGame 객체가 필요합니다.")

            if game.is_active:
                raise RuntimeError(
                    "게임 진행 중에는 저장할 수 없습니다."
                )

            self.validate_score(game.best_score)

            data = {
                "schema_version": 1,
                "quizzes": [
                    quiz.to_dict()
                    for quiz in game.list_quizzes()
                ],
                "best_score": game.best_score,
                "history": validate_history(
                    get_history(game)
                ),
            }

            self.decode_state(data)

            self.path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            temporary = self.path.with_name(
                self.path.name + ".tmp"
            )

            try:

                with temporary.open(
                    "w",
                    encoding="utf-8",
                    newline="\n",
                ) as file:

                    json.dump(
                        data,
                        file,
                        ensure_ascii=False,
                        indent=4,
                        allow_nan=False,
                    )

                    file.write("\n")
                    file.flush()

                    os.fsync(file.fileno())

                os.replace(
                    temporary,
                    self.path,
                )

            finally:

                if temporary.exists():
                    temporary.unlink()

            return self.path
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: History persistence connected"
    PASS: History persistence connected
    Failed: False

    04. Create Final Console Application

    > $path = Join-Path (Get-Location).Path "main.py"

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Final console menu created"
    PASS: Final console menu created
    Failed: False

    05. Create Bonus Feature Tests

    > $path = Join-Path `
            (Get-Location).Path `
            "tests\test_bonus.py"

        if (Test-Path -LiteralPath $path) {
            throw "test_bonus.py already exists."
        }

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Twenty-four bonus feature tests created"
    PASS: Twenty-four bonus feature tests created
    Failed: False

    06. Run All 108 Unit Tests

    > python -m py_compile `
            main.py `
            quiz.py `
            quiz_game.py `
            storage.py `
            history.py `
            tests/test_bonus.py

        if ($LASTEXITCODE -ne 0) {
            throw "Python syntax verification failed."
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 108:
        raise SystemExit("Expected 108 tests.")

    result = unittest.TextTestRunner(
        verbosity=2
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Unit tests failed."
        }

        "PASS: All 108 unit tests completed"
    python : test_01_random_questions (test_bonus.TestBonus.test_01_random_questions) ... ok
    위치 줄:1765 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_random_...estions) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_selected_question_count (test_bonus.TestBonus.test_02_selected_question_count) ... ok
    test_03_hint_penalty (test_bonus.TestBonus.test_03_hint_penalty) ... ok
    test_04_repeated_hint (test_bonus.TestBonus.test_04_repeated_hint) ... ok
    test_05_delete_question (test_bonus.TestBonus.test_05_delete_question) ... ok
    test_06_delete_unknown_id (test_bonus.TestBonus.test_06_delete_unknown_id) ... ok
    test_07_delete_during_game (test_bonus.TestBonus.test_07_delete_during_game) ... ok
    test_08_delete_preserves_records (test_bonus.TestBonus.test_08_delete_preserves_records) ... ok
    test_09_delete_persistence (test_bonus.TestBonus.test_09_delete_persistence) ... ok
    test_10_delete_last_question (test_bonus.TestBonus.test_10_delete_last_question) ... ok
    test_11_empty_history (test_bonus.TestBonus.test_11_empty_history) ... ok
    test_12_record_completed_game (test_bonus.TestBonus.test_12_record_completed_game) ... ok
    test_13_history_persistence (test_bonus.TestBonus.test_13_history_persistence) ... ok
    test_14_multiple_history_records (test_bonus.TestBonus.test_14_multiple_history_records) ... ok
    test_15_old_schema_compatibility (test_bonus.TestBonus.test_15_old_schema_compatibility) ... ok
    test_16_invalid_history (test_bonus.TestBonus.test_16_invalid_history) ... ok
    test_17_console_delete_cancel (test_bonus.TestBonus.test_17_console_delete_cancel) ... ok
    test_18_console_delete_confirm (test_bonus.TestBonus.test_18_console_delete_confirm) ... ok
    test_19_console_cancel_no_history (test_bonus.TestBonus.test_19_console_cancel_no_history) ... ok
    test_20_console_history_output (test_bonus.TestBonus.test_20_console_history_output) ... ok
    test_21_console_completed_history (test_bonus.TestBonus.test_21_console_completed_history) ... ok
    test_22_menu_delete_and_history (test_bonus.TestBonus.test_22_menu_delete_and_history) ... ok
    test_23_delete_save_failure (test_bonus.TestBonus.test_23_delete_save_failure) ... ok
    test_24_empty_history_output (test_bonus.TestBonus.test_24_empty_history_output) ... ok
    test_01_read_text_validation (test_console.TestConsole.test_01_read_text_validation) ... ok
    test_02_read_int_validation (test_console.TestConsole.test_02_read_int_validation) ... ok
    test_03_show_menu (test_console.TestConsole.test_03_show_menu) ... ok
    test_04_list_questions (test_console.TestConsole.test_04_list_questions) ... ok
    test_05_empty_question_list (test_console.TestConsole.test_05_empty_question_list) ... ok
    test_06_add_question (test_console.TestConsole.test_06_add_question) ... ok
    test_07_duplicate_question (test_console.TestConsole.test_07_duplicate_question) ... ok
    test_08_score_without_record (test_console.TestConsole.test_08_score_without_record) ... ok
    test_09_play_with_correct_answer (test_console.TestConsole.test_09_play_with_correct_answer) ... ok
    test_10_play_with_hint (test_console.TestConsole.test_10_play_with_hint) ... ok
    test_11_cancel_game (test_console.TestConsole.test_11_cancel_game) ... ok
    test_12_empty_game (test_console.TestConsole.test_12_empty_game) ... ok
    test_13_menu_exit (test_console.TestConsole.test_13_menu_exit) ... ok
    test_14_menu_invalid_input (test_console.TestConsole.test_14_menu_invalid_input) ... ok
    test_15_keyboard_interrupt (test_console.TestConsole.test_15_keyboard_interrupt) ... ok
    test_16_eof_error (test_console.TestConsole.test_16_eof_error) ... ok
    test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok
    test_01_default_question_count (test_quiz_game.TestQuizGame.test_01_default_question_count) ... ok
    test_02_difficulty_filter (test_quiz_game.TestQuizGame.test_02_difficulty_filter) ... ok
    test_03_add_quiz (test_quiz_game.TestQuizGame.test_03_add_quiz) ... ok
    test_04_duplicate_id (test_quiz_game.TestQuizGame.test_04_duplicate_id) ... ok
    test_05_duplicate_question (test_quiz_game.TestQuizGame.test_05_duplicate_question) ... ok
    test_06_next_id (test_quiz_game.TestQuizGame.test_06_next_id) ... ok
    test_07_start_game (test_quiz_game.TestQuizGame.test_07_start_game) ... ok
    test_08_invalid_count (test_quiz_game.TestQuizGame.test_08_invalid_count) ... ok
    test_09_empty_question_bank (test_quiz_game.TestQuizGame.test_09_empty_question_bank) ... ok
    test_10_correct_answer_points (test_quiz_game.TestQuizGame.test_10_correct_answer_points) ... ok
    test_11_wrong_answer_points (test_quiz_game.TestQuizGame.test_11_wrong_answer_points) ... ok
    test_12_hint_points (test_quiz_game.TestQuizGame.test_12_hint_points) ... ok
    test_13_repeated_hint (test_quiz_game.TestQuizGame.test_13_repeated_hint) ... ok
    test_14_hint_with_wrong_answer (test_quiz_game.TestQuizGame.test_14_hint_with_wrong_answer) ... ok
    test_15_invalid_answer_does_not_advance (test_quiz_game.TestQuizGame.test_15_invalid_answer_does_not_advance) ... ok
    test_16_advance_question (test_quiz_game.TestQuizGame.test_16_advance_question) ... ok
    test_17_normalized_score (test_quiz_game.TestQuizGame.test_17_normalized_score) ... ok
    test_18_best_score (test_quiz_game.TestQuizGame.test_18_best_score) ... ok
    test_19_cancel_game (test_quiz_game.TestQuizGame.test_19_cancel_game) ... ok
    test_20_completed_game_state (test_quiz_game.TestQuizGame.test_20_completed_game_state) ... ok
    test_21_no_active_game (test_quiz_game.TestQuizGame.test_21_no_active_game) ... ok
    test_22_random_unique_questions (test_quiz_game.TestQuizGame.test_22_random_unique_questions) ... ok
    test_23_question_bank_unchanged (test_quiz_game.TestQuizGame.test_23_question_bank_unchanged) ... ok
    test_24_invalid_json_preserves_bank (test_quiz_game.TestQuizGame.test_24_invalid_json_preserves_bank) ... ok
    test_25_prevent_changes_during_game (test_quiz_game.TestQuizGame.test_25_prevent_changes_during_game) ... ok
    test_26_result_is_independent (test_quiz_game.TestQuizGame.test_26_result_is_independent) ... ok
    test_27_zero_score_is_valid (test_quiz_game.TestQuizGame.test_27_zero_score_is_valid) ... ok
    test_28_hint_resets_next_question (test_quiz_game.TestQuizGame.test_28_hint_resets_next_question) ... ok
    test_01_missing_state (test_storage.TestStorage.test_01_missing_state) ... ok
    test_02_create_state (test_storage.TestStorage.test_02_create_state) ... ok
    test_03_required_schema (test_storage.TestStorage.test_03_required_schema) ... ok
    test_04_quiz_persistence (test_storage.TestStorage.test_04_quiz_persistence) ... ok
    test_05_best_score_persistence (test_storage.TestStorage.test_05_best_score_persistence) ... ok
    test_06_none_score_persistence (test_storage.TestStorage.test_06_none_score_persistence) ... ok
    test_07_zero_score_persistence (test_storage.TestStorage.test_07_zero_score_persistence) ... ok
    test_08_empty_bank_persistence (test_storage.TestStorage.test_08_empty_bank_persistence) ... ok
    test_09_utf8_encoding (test_storage.TestStorage.test_09_utf8_encoding) ... ok
    test_10_corrupt_json_recovery (test_storage.TestStorage.test_10_corrupt_json_recovery) ... ok
    test_11_invalid_encoding_recovery (test_storage.TestStorage.test_11_invalid_encoding_recovery) ... ok
    test_12_invalid_schema_recovery (test_storage.TestStorage.test_12_invalid_schema_recovery) ... ok
    test_13_invalid_score_validation (test_storage.TestStorage.test_13_invalid_score_validation) ... ok
    test_14_duplicate_id_recovery (test_storage.TestStorage.test_14_duplicate_id_recovery) ... ok
    test_15_atomic_save_failure (test_storage.TestStorage.test_15_atomic_save_failure) ... ok
    test_16_active_game_save_blocked (test_storage.TestStorage.test_16_active_game_save_blocked) ... ok
    test_17_add_console_autosave (test_storage.TestStorage.test_17_add_console_autosave) ... ok
    test_18_game_console_autosave (test_storage.TestStorage.test_18_game_console_autosave) ... ok
    test_19_exit_saves_state (test_storage.TestStorage.test_19_exit_saves_state) ... ok
    test_20_interrupt_saves_state (test_storage.TestStorage.test_20_interrupt_saves_state) ... ok

    ----------------------------------------------------------------------
    Ran 108 tests in 0.197s

    OK
    DISCOVERED TESTS: 108
    PASS: All 108 unit tests completed
    Failed: False

    07. Verify All Five Bonus Features

    > $code = @'
    import random
    import tempfile
    from pathlib import Path

    from history import (
        delete_question,
        get_history,
        record_game,
    )

    from quiz_game import QuizGame
    from storage import QuizStorage

    with tempfile.TemporaryDirectory() as directory:

        storage = QuizStorage(
            path=Path(directory) / "state.json"
        )

        game = QuizGame(
            rng=random.Random(42)
        )

        game.load_default_quizzes()

        game.start_game(
            count=5,
            random_order=True,
            shuffle_choices=True,
        )

        ids = []

        game.use_hint()

        while game.is_active:

            ids.append(game.current_quiz.id)

            game.submit_answer(
                game.current_quiz.answer
            )

        result = game.get_result()

        assert len(ids) == 5
        assert len(set(ids)) == 5
        assert ids != [1, 2, 3, 4, 5]

        print("BONUS 1: RANDOM QUESTION ORDER")
        print("QUESTION IDS:", ids)

        print("BONUS 2: SELECTABLE QUESTION COUNT")
        print("SELECTED:", len(ids))

        assert result["score"] == 90.0
        assert result["accuracy"] == 100.0
        assert result["hint_count"] == 1

        print("BONUS 3: HINT PENALTY")
        print("SCORE:", result["score"])
        print("ACCURACY:", result["accuracy"])
        print("HINTS:", result["hint_count"])

        record_game(game, result)

        updated = delete_question(game, 1)

        storage.save(updated)

        restored = storage.load()

        assert len(restored.list_quizzes()) == 19
        assert 1 not in [
            quiz.id
            for quiz in restored.list_quizzes()
        ]

        print("BONUS 4: PERSISTENT DELETE")
        print("REMAINING QUESTIONS:", len(restored.list_quizzes()))

        records = get_history(restored)

        assert len(records) == 1
        assert records[0]["score"] == 90.0
        assert restored.best_score == 90.0

        print("BONUS 5: PERSISTENT PLAY HISTORY")
        print("HISTORY RECORDS:", len(records))
        print("BEST SCORE:", restored.best_score)

        print("PASS: All five bonus features verified")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Bonus integration test failed."
        }
    BONUS 1: RANDOM QUESTION ORDER
    QUESTION IDS: [4, 1, 9, 8, 17]
    BONUS 2: SELECTABLE QUESTION COUNT
    SELECTED: 5
    BONUS 3: HINT PENALTY
    SCORE: 90.0
    ACCURACY: 100.0
    HINTS: 1
    BONUS 4: PERSISTENT DELETE
    REMAINING QUESTIONS: 19
    BONUS 5: PERSISTENT PLAY HISTORY
    HISTORY RECORDS: 1
    BEST SCORE: 90.0
    PASS: All five bonus features verified
    Failed: False

    08. Verify Old JSON Compatibility

    > $code = @'
    import json
    import tempfile
    from pathlib import Path

    from history import get_history
    from storage import QuizStorage

    with tempfile.TemporaryDirectory() as directory:

        path = Path(directory) / "state.json"

        storage = QuizStorage(path=path)

        game = storage.load()

        old_state = {
            "schema_version": 1,
            "quizzes": [
                quiz.to_dict()
                for quiz in game.list_quizzes()
            ],
            "best_score": 80.0,
        }

        path.write_text(
            json.dumps(old_state),
            encoding="utf-8",
        )

        restored = storage.load()

        assert len(restored.list_quizzes()) == 20
        assert restored.best_score == 80.0
        assert get_history(restored) == []

        storage.save(restored)

        updated = json.loads(
            path.read_text(encoding="utf-8")
        )

        assert updated["history"] == []
        assert updated["best_score"] == 80.0

        print("OLD STATE: LOADED")
        print("QUESTIONS:", len(restored.list_quizzes()))
        print("BEST SCORE:", restored.best_score)
        print("NEW HISTORY FIELD:", updated["history"])
        print("PASS: Backward compatibility verified")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Backward compatibility test failed."
        }
    OLD STATE: LOADED
    QUESTIONS: 20
    BEST SCORE: 80.0
    NEW HISTORY FIELD: []
    PASS: Backward compatibility verified
    Failed: False

    09. Commit Bonus Features

    > $files = @(
            "history.py",
            "storage.py",
            "main.py",
            "tests/test_bonus.py",
            "logs/07_json_persistence.txt"
        )

        foreach ($file in $files) {

            if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
                throw "Missing required file: $file"
            }
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    if suite.countTestCases() != 108:
        raise SystemExit("Expected 108 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        foreach ($kind in @(
            "GIT_AUTHOR_IDENT",
            "GIT_COMMITTER_IDENT"
        )) {

            $identity = git var $kind

            if ($LASTEXITCODE -ne 0 -or
                $identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

                throw "Git email privacy check failed."
            }
        }

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staging verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git commit -m "Feat: Complete bonus features and persistent play history"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: Bonus features committed"
    python : ............................................................................................................
    위치 줄:1973 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 108 tests in 0.182s

    OK
    git : warning: in the working copy of 'logs/07_json_persistence.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:1993 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    [main da5ff1c] Feat: Complete bonus features and persistent play history
     5 files changed, 2673 insertions(+), 34 deletions(-)
     create mode 100644 history.py
     create mode 100644 logs/07_json_persistence.txt
     create mode 100644 tests/test_bonus.py
    PASS: Bonus features committed
    Failed: False

    10. Verify Final Stage Status

    > $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "7") {
            throw "Expected seven Git commits."
        }

        git log --oneline --graph --all

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or
            $status.Count -gt 0) {

            throw "Working tree is not clean."
        }

        "TOTAL COMMITS: $count"
        "TOTAL UNIT TESTS EXPECTED: 108"
        "BONUS FEATURES: 5 / 5"
        "PASS: STEP08 completed"
    * da5ff1c Feat: Complete bonus features and persistent play history
    * 03119eb Feat: Add JSON persistence and state recovery
    *   a01099c Merge feature/quiz-console into main
    |\
    | * 2c19fe7 Feat: Implement interactive quiz console
    |/
    * a49c5db Implement QuizGame engine and scoring tests
    * ccc8cb6 Implement Quiz class with validation and unit tests
    * f161dea Initialize quiz project and add 20 default questions
    TOTAL COMMITS: 7
    TOTAL UNIT TESTS EXPECTED: 108
    BONUS FEATURES: 5 / 5
    PASS: STEP08 completed
    Failed: False



### 08A_console_ui.txt

[Original execution log](../logs/08A_console_ui.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP08A - Console UI Improvement
    Date: 2026-11-14 23:02:39

    01. Save STEP08 Execution Evidence

    > $source = Get-ChildItem "C:\2026Codyssey_AllInOne\_Common\logs" -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP08*Bonus*Features*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP08 log not found."
        }

        $content = Get-Content `
            -LiteralPath $source.FullName `
            -Raw `
            -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP08 contains failed steps."
        }

        if ([regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        ).Count -ne 10) {
            throw "Expected ten successful results."
        }

        $content = $content -replace `
            '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
            '${1}<USER>'

        $path = Join-Path `
            (Get-Location).Path `
            "logs\08_bonus_features.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content,
            $utf8
        )

        "PASS: STEP08 evidence saved"
    PASS: STEP08 evidence saved
    Failed: False

    02. Create Reusable Console UI Module

    > $path = Join-Path `
            (Get-Location).Path `
            "console_ui.py"

        if (Test-Path -LiteralPath $path) {
            throw "console_ui.py already exists."
        }

        $content = @'
    """Reusable ANSI console styling utilities."""

    import os
    import sys


    COLORS = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "gray": "\033[90m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }

    WIDTH = 66


    def color_enabled():
        """Disable ANSI colors for redirected output."""

        if "NO_COLOR" in os.environ:
            return False

        if os.environ.get("TERM") == "dumb":
            return False

        return bool(sys.stdout.isatty())


    def paint(value, color="white", bold=False):
        """Apply a color and restore the default style."""

        text = str(value)

        if not color_enabled():
            return text

        prefix = COLORS[color]

        if bold:
            prefix += COLORS["bold"]

        return prefix + text + COLORS["reset"]


    def line(character="-"):
        """Print a neutral separator."""

        print(paint(character * WIDTH, "gray"))


    def header(title, subtitle=None, color="yellow"):
        """Display a section title with vertical spacing."""

        print()
        line("=")

        print(paint(title, color, bold=True))

        if subtitle:
            print(paint(subtitle, "gray"))

        line("=")
        print()


    def field(label, value, color="white"):
        """Display a labeled value."""

        print(
            f" {label} : "
            f"{paint(value, color, bold=True)}"
        )


    def menu_item(number, label):
        """Display a numbered menu item."""

        print(
            f" {paint(f'[{number}]', 'cyan', True)} "
            f" {label}"
        )


    def prompt(message):
        """Read user input using a colored prompt."""

        return input(paint(message, "green", True))


    def message(text, color="white"):
        """Display a separated status message."""

        print()
        print(paint(text, color, True))
        print()


    def progress_bar(current, total, width=30):
        """Display a text-based progress bar."""

        ratio = current / total if total else 0
        ratio = max(0.0, min(1.0, ratio))

        filled = int(ratio * width)

        bar = (
            paint("#" * filled, "cyan")
            + paint("-" * (width - filled), "gray")
        )

        print(f" [{bar}] {ratio * 100:.0f}%")


    def score_bar(score):
        """Display a normalized score bar."""

        progress_bar(score, 100)
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Reusable console UI module created"
    PASS: Reusable console UI module created
    Failed: False

    03. Replace Main Console Application

    > $path = Join-Path `
            (Get-Location).Path `
            "main.py"

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Colored console application created"
    PASS: Colored console application created
    Failed: False

    04. Create Console UI Unit Tests

    > $path = Join-Path `
            (Get-Location).Path `
            "tests\test_console_ui.py"

        if (Test-Path -LiteralPath $path) {
            throw "UI test file already exists."
        }

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Ten UI tests created"
    PASS: Ten UI tests created
    Failed: False

    05. Run All 118 Unit Tests

    > python -m py_compile `
            main.py `
            console_ui.py `
            tests/test_console_ui.py

        if ($LASTEXITCODE -ne 0) {
            throw "Syntax verification failed."
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 118:
        raise SystemExit("Expected 118 tests.")

    result = unittest.TextTestRunner(
        verbosity=2
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Unit tests failed."
        }

        "PASS: All 118 tests completed"
    python : test_01_random_questions (test_bonus.TestBonus.test_01_random_questions) ... ok
    위치 줄:1456 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_random_...estions) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_selected_question_count (test_bonus.TestBonus.test_02_selected_question_count) ... ok
    test_03_hint_penalty (test_bonus.TestBonus.test_03_hint_penalty) ... ok
    test_04_repeated_hint (test_bonus.TestBonus.test_04_repeated_hint) ... ok
    test_05_delete_question (test_bonus.TestBonus.test_05_delete_question) ... ok
    test_06_delete_unknown_id (test_bonus.TestBonus.test_06_delete_unknown_id) ... ok
    test_07_delete_during_game (test_bonus.TestBonus.test_07_delete_during_game) ... ok
    test_08_delete_preserves_records (test_bonus.TestBonus.test_08_delete_preserves_records) ... ok
    test_09_delete_persistence (test_bonus.TestBonus.test_09_delete_persistence) ... ok
    test_10_delete_last_question (test_bonus.TestBonus.test_10_delete_last_question) ... ok
    test_11_empty_history (test_bonus.TestBonus.test_11_empty_history) ... ok
    test_12_record_completed_game (test_bonus.TestBonus.test_12_record_completed_game) ... ok
    test_13_history_persistence (test_bonus.TestBonus.test_13_history_persistence) ... ok
    test_14_multiple_history_records (test_bonus.TestBonus.test_14_multiple_history_records) ... ok
    test_15_old_schema_compatibility (test_bonus.TestBonus.test_15_old_schema_compatibility) ... ok
    test_16_invalid_history (test_bonus.TestBonus.test_16_invalid_history) ... ok
    test_17_console_delete_cancel (test_bonus.TestBonus.test_17_console_delete_cancel) ... ok
    test_18_console_delete_confirm (test_bonus.TestBonus.test_18_console_delete_confirm) ... ok
    test_19_console_cancel_no_history (test_bonus.TestBonus.test_19_console_cancel_no_history) ... ok
    test_20_console_history_output (test_bonus.TestBonus.test_20_console_history_output) ... ok
    test_21_console_completed_history (test_bonus.TestBonus.test_21_console_completed_history) ... ok
    test_22_menu_delete_and_history (test_bonus.TestBonus.test_22_menu_delete_and_history) ... ok
    test_23_delete_save_failure (test_bonus.TestBonus.test_23_delete_save_failure) ... ok
    test_24_empty_history_output (test_bonus.TestBonus.test_24_empty_history_output) ... ok
    test_01_read_text_validation (test_console.TestConsole.test_01_read_text_validation) ... ok
    test_02_read_int_validation (test_console.TestConsole.test_02_read_int_validation) ... ok
    test_03_show_menu (test_console.TestConsole.test_03_show_menu) ... ok
    test_04_list_questions (test_console.TestConsole.test_04_list_questions) ... ok
    test_05_empty_question_list (test_console.TestConsole.test_05_empty_question_list) ... ok
    test_06_add_question (test_console.TestConsole.test_06_add_question) ... ok
    test_07_duplicate_question (test_console.TestConsole.test_07_duplicate_question) ... ok
    test_08_score_without_record (test_console.TestConsole.test_08_score_without_record) ... ok
    test_09_play_with_correct_answer (test_console.TestConsole.test_09_play_with_correct_answer) ... ok
    test_10_play_with_hint (test_console.TestConsole.test_10_play_with_hint) ... ok
    test_11_cancel_game (test_console.TestConsole.test_11_cancel_game) ... ok
    test_12_empty_game (test_console.TestConsole.test_12_empty_game) ... ok
    test_13_menu_exit (test_console.TestConsole.test_13_menu_exit) ... ok
    test_14_menu_invalid_input (test_console.TestConsole.test_14_menu_invalid_input) ... ok
    test_15_keyboard_interrupt (test_console.TestConsole.test_15_keyboard_interrupt) ... ok
    test_16_eof_error (test_console.TestConsole.test_16_eof_error) ... ok
    test_01_blue_color (test_console_ui.TestConsoleUI.test_01_blue_color) ... ok
    test_02_red_color (test_console_ui.TestConsoleUI.test_02_red_color) ... ok
    test_03_plain_text (test_console_ui.TestConsoleUI.test_03_plain_text) ... ok
    test_04_bold_text (test_console_ui.TestConsoleUI.test_04_bold_text) ... ok
    test_05_no_color_environment (test_console_ui.TestConsoleUI.test_05_no_color_environment) ... ok
    test_06_redirected_output (test_console_ui.TestConsoleUI.test_06_redirected_output) ... ok
    test_07_header_spacing (test_console_ui.TestConsoleUI.test_07_header_spacing) ... ok
    test_08_progress_bar (test_console_ui.TestConsoleUI.test_08_progress_bar) ... ok
    test_09_menu_colors (test_console_ui.TestConsoleUI.test_09_menu_colors) ... ok
    test_10_answer_colors (test_console_ui.TestConsoleUI.test_10_answer_colors) ... ok
    test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok
    test_01_default_question_count (test_quiz_game.TestQuizGame.test_01_default_question_count) ... ok
    test_02_difficulty_filter (test_quiz_game.TestQuizGame.test_02_difficulty_filter) ... ok
    test_03_add_quiz (test_quiz_game.TestQuizGame.test_03_add_quiz) ... ok
    test_04_duplicate_id (test_quiz_game.TestQuizGame.test_04_duplicate_id) ... ok
    test_05_duplicate_question (test_quiz_game.TestQuizGame.test_05_duplicate_question) ... ok
    test_06_next_id (test_quiz_game.TestQuizGame.test_06_next_id) ... ok
    test_07_start_game (test_quiz_game.TestQuizGame.test_07_start_game) ... ok
    test_08_invalid_count (test_quiz_game.TestQuizGame.test_08_invalid_count) ... ok
    test_09_empty_question_bank (test_quiz_game.TestQuizGame.test_09_empty_question_bank) ... ok
    test_10_correct_answer_points (test_quiz_game.TestQuizGame.test_10_correct_answer_points) ... ok
    test_11_wrong_answer_points (test_quiz_game.TestQuizGame.test_11_wrong_answer_points) ... ok
    test_12_hint_points (test_quiz_game.TestQuizGame.test_12_hint_points) ... ok
    test_13_repeated_hint (test_quiz_game.TestQuizGame.test_13_repeated_hint) ... ok
    test_14_hint_with_wrong_answer (test_quiz_game.TestQuizGame.test_14_hint_with_wrong_answer) ... ok
    test_15_invalid_answer_does_not_advance (test_quiz_game.TestQuizGame.test_15_invalid_answer_does_not_advance) ... ok
    test_16_advance_question (test_quiz_game.TestQuizGame.test_16_advance_question) ... ok
    test_17_normalized_score (test_quiz_game.TestQuizGame.test_17_normalized_score) ... ok
    test_18_best_score (test_quiz_game.TestQuizGame.test_18_best_score) ... ok
    test_19_cancel_game (test_quiz_game.TestQuizGame.test_19_cancel_game) ... ok
    test_20_completed_game_state (test_quiz_game.TestQuizGame.test_20_completed_game_state) ... ok
    test_21_no_active_game (test_quiz_game.TestQuizGame.test_21_no_active_game) ... ok
    test_22_random_unique_questions (test_quiz_game.TestQuizGame.test_22_random_unique_questions) ... ok
    test_23_question_bank_unchanged (test_quiz_game.TestQuizGame.test_23_question_bank_unchanged) ... ok
    test_24_invalid_json_preserves_bank (test_quiz_game.TestQuizGame.test_24_invalid_json_preserves_bank) ... ok
    test_25_prevent_changes_during_game (test_quiz_game.TestQuizGame.test_25_prevent_changes_during_game) ... ok
    test_26_result_is_independent (test_quiz_game.TestQuizGame.test_26_result_is_independent) ... ok
    test_27_zero_score_is_valid (test_quiz_game.TestQuizGame.test_27_zero_score_is_valid) ... ok
    test_28_hint_resets_next_question (test_quiz_game.TestQuizGame.test_28_hint_resets_next_question) ... ok
    test_01_missing_state (test_storage.TestStorage.test_01_missing_state) ... ok
    test_02_create_state (test_storage.TestStorage.test_02_create_state) ... ok
    test_03_required_schema (test_storage.TestStorage.test_03_required_schema) ... ok
    test_04_quiz_persistence (test_storage.TestStorage.test_04_quiz_persistence) ... ok
    test_05_best_score_persistence (test_storage.TestStorage.test_05_best_score_persistence) ... ok
    test_06_none_score_persistence (test_storage.TestStorage.test_06_none_score_persistence) ... ok
    test_07_zero_score_persistence (test_storage.TestStorage.test_07_zero_score_persistence) ... ok
    test_08_empty_bank_persistence (test_storage.TestStorage.test_08_empty_bank_persistence) ... ok
    test_09_utf8_encoding (test_storage.TestStorage.test_09_utf8_encoding) ... ok
    test_10_corrupt_json_recovery (test_storage.TestStorage.test_10_corrupt_json_recovery) ... ok
    test_11_invalid_encoding_recovery (test_storage.TestStorage.test_11_invalid_encoding_recovery) ... ok
    test_12_invalid_schema_recovery (test_storage.TestStorage.test_12_invalid_schema_recovery) ... ok
    test_13_invalid_score_validation (test_storage.TestStorage.test_13_invalid_score_validation) ... ok
    test_14_duplicate_id_recovery (test_storage.TestStorage.test_14_duplicate_id_recovery) ... ok
    test_15_atomic_save_failure (test_storage.TestStorage.test_15_atomic_save_failure) ... ok
    test_16_active_game_save_blocked (test_storage.TestStorage.test_16_active_game_save_blocked) ... ok
    test_17_add_console_autosave (test_storage.TestStorage.test_17_add_console_autosave) ... ok
    test_18_game_console_autosave (test_storage.TestStorage.test_18_game_console_autosave) ... ok
    test_19_exit_saves_state (test_storage.TestStorage.test_19_exit_saves_state) ... ok
    test_20_interrupt_saves_state (test_storage.TestStorage.test_20_interrupt_saves_state) ... ok

    ----------------------------------------------------------------------
    Ran 118 tests in 0.186s

    OK
    DISCOVERED TESTS: 118
    PASS: All 118 tests completed
    Failed: False

    06. Verify ANSI Color Palette

    > $code = @'
    from unittest.mock import patch

    import console_ui as ui

    with patch(
        "console_ui.color_enabled",
        return_value=True,
    ):

        for color in (
            "cyan",
            "yellow",
            "blue",
            "red",
            "green",
            "purple",
            "gray",
            "white",
        ):

            value = ui.paint(
                color.upper(),
                color,
                True,
            )

            assert value.startswith(
                ui.COLORS[color]
            )

            assert value.endswith(
                ui.COLORS["reset"]
            )

            print(
                color.upper(),
                repr(value),
            )

    print("PASS: Eight ANSI colors verified")
    print("PASS: Color reset verified")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "ANSI color verification failed."
        }
    CYAN '\x1b[96m\x1b[1mCYAN\x1b[0m'
    YELLOW '\x1b[93m\x1b[1mYELLOW\x1b[0m'
    BLUE '\x1b[94m\x1b[1mBLUE\x1b[0m'
    RED '\x1b[91m\x1b[1mRED\x1b[0m'
    GREEN '\x1b[92m\x1b[1mGREEN\x1b[0m'
    PURPLE '\x1b[95m\x1b[1mPURPLE\x1b[0m'
    GRAY '\x1b[90m\x1b[1mGRAY\x1b[0m'
    WHITE '\x1b[97m\x1b[1mWHITE\x1b[0m'
    PASS: Eight ANSI colors verified
    PASS: Color reset verified
    Failed: False

    07. Commit Console UI Improvement

    > $files = @(
            "console_ui.py",
            "main.py",
            "tests/test_console_ui.py",
            "logs/08_bonus_features.txt"
        )

        foreach ($file in $files) {

            if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
                throw "Missing file: $file"
            }
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    if suite.countTestCases() != 118:
        raise SystemExit("Expected 118 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        foreach ($kind in @(
            "GIT_AUTHOR_IDENT",
            "GIT_COMMITTER_IDENT"
        )) {

            $identity = git var $kind

            if ($LASTEXITCODE -ne 0 -or
                $identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

                throw "Git identity check failed."
            }
        }

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staging verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git commit -m "Feat: Improve console colors and visual readability"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: Console UI improvement committed"
    python : ......................................................................................................................
    위치 줄:1551 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 118 tests in 0.174s

    OK
    git : warning: in the working copy of 'logs/08_bonus_features.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:1571 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    [main 1533f93] Feat: Improve console colors and visual readability
     4 files changed, 2987 insertions(+), 172 deletions(-)
     create mode 100644 console_ui.py
     create mode 100644 logs/08_bonus_features.txt
     create mode 100644 tests/test_console_ui.py
    PASS: Console UI improvement committed
    Failed: False

    08. Verify Final Status

    > $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "8") {
            throw "Expected eight Git commits."
        }

        git log -3 --oneline

        if ($LASTEXITCODE -ne 0) {
            throw "Git log failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or
            $status.Count -gt 0) {

            throw "Working tree is not clean."
        }

        "TOTAL COMMITS: $count"
        "TOTAL TESTS EXPECTED: 118"
        "ANSI COLORS: 8"
        "PASS: STEP08A completed"
    1533f93 Feat: Improve console colors and visual readability
    da5ff1c Feat: Complete bonus features and persistent play history
    03119eb Feat: Add JSON persistence and state recovery
    TOTAL COMMITS: 8
    TOTAL TESTS EXPECTED: 118
    ANSI COLORS: 8
    PASS: STEP08A completed
    Failed: False



### 08B_question_color.txt

[Original execution log](../logs/08B_question_color.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP08B - Question Color Improvement
    Date: 2026-11-14 23:06:06

    01. Change Question Color to Purple

    > $path = Join-Path (Get-Location).Path "main.py"

        $content = [System.IO.File]::ReadAllText($path)

        $pattern = '(quiz\.question,\s*)"blue"'

        $matches = [regex]::Matches(
            $content,
            $pattern
        )

        if ($matches.Count -ne 1) {
            throw "Expected exactly one question color definition."
        }

        $updated = [regex]::Replace(
            $content,
            $pattern,
            '${1}"purple"'
        )

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $updated,
            $utf8
        )

        "BEFORE: Question = Blue"
        "AFTER : Question = Purple"
        "PASS: Question color updated"
    BEFORE: Question = Blue
    AFTER : Question = Purple
    PASS: Question color updated
    Failed: False

    02. Verify Source Code Changes

    > git diff -- main.py

        if ($LASTEXITCODE -ne 0) {
            throw "Git diff failed."
        }

        python -m py_compile main.py

        if ($LASTEXITCODE -ne 0) {
            throw "Python syntax verification failed."
        }

        "PASS: Source code verified"
    diff --git a/main.py b/main.py
    index c0bd18a..c78c0ea 100644
    --- a/main.py
    +++ b/main.py
    @@ -208,7 +208,7 @@ def show_question(game):
         print(
             ui.paint(
                 quiz.question,
    -            "blue",
    +            "purple",
                 True,
             )
         )
    PASS: Source code verified
    Failed: False

    03. Verify Question Color

    > $code = @'
    import io
    from contextlib import redirect_stdout
    from unittest.mock import patch

    from main import show_question
    from quiz_game import QuizGame

    game = QuizGame()
    game.load_default_quizzes()
    game.start_game(count=1)

    question = game.current_quiz.question

    output = io.StringIO()

    with redirect_stdout(output):
        with patch(
            "console_ui.color_enabled",
            return_value=True,
        ):
            show_question(game)

    expected = "\033[95m\033[1m" + question

    assert expected in output.getvalue()

    print("QUESTION COLOR: PURPLE")
    print("ANSI CODE: 95")
    print("PASS: Question color verified")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Question color verification failed."
        }
    QUESTION COLOR: PURPLE
    ANSI CODE: 95
    PASS: Question color verified
    Failed: False

    04. Run All Unit Tests

    > python -m unittest discover -s tests 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Unit tests failed."
        }

        "PASS: Existing functions preserved"
    python : ......................................................................................................................
    위치 줄:101 문자:5
    +     python -m unittest discover -s tests 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 118 tests in 0.170s

    OK
    PASS: Existing functions preserved
    Failed: False

    05. Commit Question Color Improvement

    > python -m unittest discover -s tests 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        $content = Get-Content main.py -Raw -Encoding UTF8

        if ($content -notmatch 'quiz\.question,\s*"purple"') {
            throw "Purple question color not found."
        }

        git add -- main.py

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        git commit -m "Fix: Distinguish question and answer colors"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        git log -3 --oneline

        "PASS: Question color improvement committed"
    python : ......................................................................................................................
    위치 줄:112 문자:5
    +     python -m unittest discover -s tests 2>&1
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 118 tests in 0.173s

    OK
    [main e1fcbcc] Fix: Distinguish question and answer colors
     1 file changed, 1 insertion(+), 1 deletion(-)
    e1fcbcc Fix: Distinguish question and answer colors
    1533f93 Feat: Improve console colors and visual readability
    da5ff1c Feat: Complete bonus features and persistent play history
    PASS: Question color improvement committed
    Failed: False



### 09_stability.txt

[Original execution log](../logs/09_stability.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP09 - Stability and Exception Handling
    Date: 2026-11-14 23:07:51

    01. Verify Existing 118 Unit Tests

    > $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("EXISTING TESTS:", count)

    if count != 118:
        raise SystemExit("Expected 118 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful() else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Existing tests failed."
        }

        "PASS: Existing functions verified"
    python : ......................................................................................................................
    위치 줄:50 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 118 tests in 0.186s

    OK
    EXISTING TESTS: 118
    PASS: Existing functions verified
    Failed: False

    02. Save UI Improvement Evidence

    > $items = @(
            @{
                Pattern = "*M_E1-2*STEP08A*Console*UI*"
                Target = "logs\08A_console_ui.txt"
                Count = 8
            },
            @{
                Pattern = "*M_E1-2*STEP08B*Question*Color*"
                Target = "logs\08B_question_color.txt"
                Count = 5
            }
        )

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        foreach ($item in $items) {

            $source = Get-ChildItem `
                "C:\2026Codyssey_AllInOne\_Common\logs" `
                -File |
                Where-Object {
                    $_.Name -like $item.Pattern
                } |
                Sort-Object LastWriteTime -Descending |
                Select-Object -First 1

            if (-not $source) {
                throw "Required execution log not found."
            }

            $content = Get-Content `
                -LiteralPath $source.FullName `
                -Raw `
                -Encoding UTF8

            if ($content -match '(?m)^Failed:\s*True\s*$') {
                throw "Previous execution contains errors."
            }

            $results = [regex]::Matches(
                $content,
                '(?m)^Failed:\s*False\s*$'
            )

            if ($results.Count -ne $item.Count) {
                throw "Unexpected result count."
            }

            $content = $content -replace `
                '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
                '${1}<USER>'

            $path = Join-Path `
                (Get-Location).Path `
                $item.Target

            [System.IO.File]::WriteAllText(
                $path,
                $content,
                $utf8
            )

            "PASS: $($item.Target)"
        }
    PASS: logs\08A_console_ui.txt
    PASS: logs\08B_question_color.txt
    Failed: False

    03. Create Stability Test Suite

    > $path = Join-Path `
            (Get-Location).Path `
            "tests\test_stability.py"

        $content = @'
    """Additional stability and exception handling tests."""

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
        play_quiz,
        read_int,
        read_text,
        remove_question,
        run_menu,
        save_state,
        show_score,
    )

    from quiz_game import QuizGame
    from storage import QuizStorage


    class TestStability(unittest.TestCase):

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

        def test_01_non_numeric_menu_input(self):

            output = io.StringIO()

            with redirect_stdout(output):

                with patch(
                    "builtins.input",
                    side_effect=["ABC", "1"],
                ):

                    result = read_int(
                        "Menu: ",
                        0,
                        6,
                    )

            self.assertEqual(result, 1)

            self.assertIn(
                "숫자를 입력하세요",
                output.getvalue(),
            )

        def test_02_empty_menu_input(self):

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=["", "   ", "0"],
                ):

                    result = read_int(
                        "Menu: ",
                        0,
                        6,
                    )

            self.assertEqual(result, 0)

        def test_03_out_of_range_input(self):

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=["-1", "7", "99", "3"],
                ):

                    result = read_int(
                        "Menu: ",
                        0,
                        6,
                    )

            self.assertEqual(result, 3)

        def test_04_trim_whitespace(self):

            with patch(
                "builtins.input",
                return_value="  2  ",
            ):

                result = read_int(
                    "Menu: ",
                    0,
                    6,
                )

            self.assertEqual(result, 2)

        def test_05_empty_text_input(self):

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=["", "   ", " FFT "],
                ):

                    result = read_text("Text: ")

            self.assertEqual(result, "FFT")

        def test_06_invalid_answer_recovery(self):

            invalid = iter(
                ["ABC", "", "0", "5"]
            )

            def fake_input(prompt):

                if "출제 문제 수" in prompt:
                    return "1"

                try:
                    return next(invalid)

                except StopIteration:

                    return str(
                        self.game.current_quiz.answer
                    )

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

            self.assertEqual(
                self.game.best_score,
                100.0,
            )

            self.assertEqual(
                len(get_history(self.game)),
                1,
            )

            self.assertIn(
                "1~4, H 또는 Q",
                output.getvalue(),
            )

        def test_07_duplicate_question_rejected(self):

            question = (
                self.game.list_quizzes()[0].question
            )

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    return_value=question,
                ):

                    add_question(
                        self.game,
                        self.storage,
                    )

            self.assertEqual(
                len(self.game.list_quizzes()),
                20,
            )

        def test_08_duplicate_choice_recovery(self):

            inputs = [
                "Stability test question",
                "A",
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

            output = io.StringIO()

            with redirect_stdout(output):

                with patch(
                    "builtins.input",
                    side_effect=inputs,
                ):

                    add_question(
                        self.game,
                        self.storage,
                    )

            self.assertEqual(
                len(self.game.list_quizzes()),
                21,
            )

            self.assertEqual(
                self.game.list_quizzes()[-1].choices,
                ["A", "B", "C", "D"],
            )

            self.assertIn(
                "중복된 보기",
                output.getvalue(),
            )

        def test_09_empty_question_bank(self):

            game = QuizGame()

            output = io.StringIO()

            with redirect_stdout(output):

                play_quiz(
                    game,
                    self.storage,
                )

            self.assertFalse(game.is_active)

            self.assertIn(
                "등록된 문제가 없습니다",
                output.getvalue(),
            )

        def test_10_cancel_game(self):

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=["1", "Q"],
                ):

                    play_quiz(
                        self.game,
                        self.storage,
                    )

            self.assertFalse(self.game.is_active)
            self.assertIsNone(self.game.best_score)
            self.assertEqual(get_history(self.game), [])

        def test_11_keyboard_interrupt(self):

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=KeyboardInterrupt,
                ):

                    result = run_menu(
                        self.game,
                        self.storage,
                    )

            self.assertEqual(result, 0)
            self.assertTrue(self.path.exists())

        def test_12_eof_safe_exit(self):

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=EOFError,
                ):

                    result = run_menu(
                        self.game,
                        self.storage,
                    )

            self.assertEqual(result, 0)

            self.assertEqual(
                len(self.storage.load().list_quizzes()),
                20,
            )

        def test_13_interrupt_during_game(self):

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=[
                        "1",
                        "2",
                        KeyboardInterrupt(),
                    ],
                ):

                    result = run_menu(
                        self.game,
                        self.storage,
                    )

            self.assertEqual(result, 0)
            self.assertFalse(self.game.is_active)

            restored = self.storage.load()

            self.assertEqual(
                get_history(restored),
                [],
            )

            self.assertIsNone(restored.best_score)

        def test_14_missing_state_defaults(self):

            self.assertFalse(self.path.exists())

            restored = self.storage.load()

            self.assertEqual(
                len(restored.list_quizzes()),
                20,
            )

        def test_15_corrupt_json_backup(self):

            original = "{invalid JSON"

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

        def test_16_invalid_history_recovery(self):

            self.storage.save(self.game)

            data = json.loads(
                self.path.read_text(
                    encoding="utf-8"
                )
            )

            data["history"] = [
                {"score": 999}
            ]

            self.path.write_text(
                json.dumps(data),
                encoding="utf-8",
            )

            restored = self.storage.load()

            self.assertEqual(
                len(restored.list_quizzes()),
                20,
            )

            self.assertEqual(
                get_history(restored),
                [],
            )

            self.assertIsNotNone(
                self.storage.last_backup
            )

        def test_17_atomic_save_preserves_original(self):

            self.storage.save(self.game)

            original = self.path.read_bytes()

            self.game.best_score = 80.0

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

        def test_18_delete_save_failure(self):

            self.storage.save(self.game)

            original = self.path.read_bytes()

            with redirect_stdout(io.StringIO()):

                with patch(
                    "builtins.input",
                    side_effect=["1", "Y"],
                ):

                    with patch.object(
                        self.storage,
                        "save",
                        side_effect=OSError(
                            "Simulated failure"
                        ),
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

            self.assertEqual(
                self.path.read_bytes(),
                original,
            )

        def test_19_save_failure_message(self):

            output = io.StringIO()

            with redirect_stdout(output):

                with patch.object(
                    self.storage,
                    "save",
                    side_effect=OSError(
                        "Simulated failure"
                    ),
                ):

                    result = save_state(
                        self.game,
                        self.storage,
                    )

            self.assertFalse(result)

            self.assertIn(
                "저장 실패",
                output.getvalue(),
            )

        def test_20_no_score_display(self):

            output = io.StringIO()

            with redirect_stdout(output):

                show_score(self.game)

            self.assertIn(
                "아직 완료된 게임 기록이 없습니다",
                output.getvalue(),
            )


    if __name__ == "__main__":
        unittest.main()
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Twenty stability tests created"
    PASS: Twenty stability tests created
    Failed: False

    04. Run Stability Tests

    > python -m py_compile tests/test_stability.py

        if ($LASTEXITCODE -ne 0) {
            throw "Syntax verification failed."
        }

        python -m unittest discover `
            -s tests `
            -p "test_stability.py" `
            -v 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Stability tests failed."
        }

        "PASS: Stability test suite completed"
    python : test_01_non_numeric_menu_input (test_stability.TestStability.test_01_non_numeric_menu_input) ... ok
    위치 줄:691 문자:5
    +     python -m unittest discover `
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_non_num...u_input) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_empty_menu_input (test_stability.TestStability.test_02_empty_menu_input) ... ok
    test_03_out_of_range_input (test_stability.TestStability.test_03_out_of_range_input) ... ok
    test_04_trim_whitespace (test_stability.TestStability.test_04_trim_whitespace) ... ok
    test_05_empty_text_input (test_stability.TestStability.test_05_empty_text_input) ... ok
    test_06_invalid_answer_recovery (test_stability.TestStability.test_06_invalid_answer_recovery) ... ok
    test_07_duplicate_question_rejected (test_stability.TestStability.test_07_duplicate_question_rejected) ... ok
    test_08_duplicate_choice_recovery (test_stability.TestStability.test_08_duplicate_choice_recovery) ... ok
    test_09_empty_question_bank (test_stability.TestStability.test_09_empty_question_bank) ... ok
    test_10_cancel_game (test_stability.TestStability.test_10_cancel_game) ... ok
    test_11_keyboard_interrupt (test_stability.TestStability.test_11_keyboard_interrupt) ... ok
    test_12_eof_safe_exit (test_stability.TestStability.test_12_eof_safe_exit) ... ok
    test_13_interrupt_during_game (test_stability.TestStability.test_13_interrupt_during_game) ... ok
    test_14_missing_state_defaults (test_stability.TestStability.test_14_missing_state_defaults) ... ok
    test_15_corrupt_json_backup (test_stability.TestStability.test_15_corrupt_json_backup) ... ok
    test_16_invalid_history_recovery (test_stability.TestStability.test_16_invalid_history_recovery) ... ok
    test_17_atomic_save_preserves_original (test_stability.TestStability.test_17_atomic_save_preserves_original) ... ok
    test_18_delete_save_failure (test_stability.TestStability.test_18_delete_save_failure) ... ok
    test_19_save_failure_message (test_stability.TestStability.test_19_save_failure_message) ... ok
    test_20_no_score_display (test_stability.TestStability.test_20_no_score_display) ... ok

    ----------------------------------------------------------------------
    Ran 20 tests in 0.075s

    OK
    PASS: Stability test suite completed
    Failed: False

    05. Run All 138 Unit Tests

    > $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 138:
        raise SystemExit("Expected 138 tests.")

    result = unittest.TextTestRunner(
        verbosity=2
    ).run(suite)

    print("TESTS RUN:", result.testsRun)
    print("FAILURES:", len(result.failures))
    print("ERRORS:", len(result.errors))
    print("SKIPPED:", len(result.skipped))

    raise SystemExit(
        0 if result.wasSuccessful()
        and not result.skipped
        else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Full test suite failed."
        }

        "PASS: All 138 unit tests completed"
    python : test_01_random_questions (test_bonus.TestBonus.test_01_random_questions) ... ok
    위치 줄:733 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_random_...estions) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_selected_question_count (test_bonus.TestBonus.test_02_selected_question_count) ... ok
    test_03_hint_penalty (test_bonus.TestBonus.test_03_hint_penalty) ... ok
    test_04_repeated_hint (test_bonus.TestBonus.test_04_repeated_hint) ... ok
    test_05_delete_question (test_bonus.TestBonus.test_05_delete_question) ... ok
    test_06_delete_unknown_id (test_bonus.TestBonus.test_06_delete_unknown_id) ... ok
    test_07_delete_during_game (test_bonus.TestBonus.test_07_delete_during_game) ... ok
    test_08_delete_preserves_records (test_bonus.TestBonus.test_08_delete_preserves_records) ... ok
    test_09_delete_persistence (test_bonus.TestBonus.test_09_delete_persistence) ... ok
    test_10_delete_last_question (test_bonus.TestBonus.test_10_delete_last_question) ... ok
    test_11_empty_history (test_bonus.TestBonus.test_11_empty_history) ... ok
    test_12_record_completed_game (test_bonus.TestBonus.test_12_record_completed_game) ... ok
    test_13_history_persistence (test_bonus.TestBonus.test_13_history_persistence) ... ok
    test_14_multiple_history_records (test_bonus.TestBonus.test_14_multiple_history_records) ... ok
    test_15_old_schema_compatibility (test_bonus.TestBonus.test_15_old_schema_compatibility) ... ok
    test_16_invalid_history (test_bonus.TestBonus.test_16_invalid_history) ... ok
    test_17_console_delete_cancel (test_bonus.TestBonus.test_17_console_delete_cancel) ... ok
    test_18_console_delete_confirm (test_bonus.TestBonus.test_18_console_delete_confirm) ... ok
    test_19_console_cancel_no_history (test_bonus.TestBonus.test_19_console_cancel_no_history) ... ok
    test_20_console_history_output (test_bonus.TestBonus.test_20_console_history_output) ... ok
    test_21_console_completed_history (test_bonus.TestBonus.test_21_console_completed_history) ... ok
    test_22_menu_delete_and_history (test_bonus.TestBonus.test_22_menu_delete_and_history) ... ok
    test_23_delete_save_failure (test_bonus.TestBonus.test_23_delete_save_failure) ... ok
    test_24_empty_history_output (test_bonus.TestBonus.test_24_empty_history_output) ... ok
    test_01_read_text_validation (test_console.TestConsole.test_01_read_text_validation) ... ok
    test_02_read_int_validation (test_console.TestConsole.test_02_read_int_validation) ... ok
    test_03_show_menu (test_console.TestConsole.test_03_show_menu) ... ok
    test_04_list_questions (test_console.TestConsole.test_04_list_questions) ... ok
    test_05_empty_question_list (test_console.TestConsole.test_05_empty_question_list) ... ok
    test_06_add_question (test_console.TestConsole.test_06_add_question) ... ok
    test_07_duplicate_question (test_console.TestConsole.test_07_duplicate_question) ... ok
    test_08_score_without_record (test_console.TestConsole.test_08_score_without_record) ... ok
    test_09_play_with_correct_answer (test_console.TestConsole.test_09_play_with_correct_answer) ... ok
    test_10_play_with_hint (test_console.TestConsole.test_10_play_with_hint) ... ok
    test_11_cancel_game (test_console.TestConsole.test_11_cancel_game) ... ok
    test_12_empty_game (test_console.TestConsole.test_12_empty_game) ... ok
    test_13_menu_exit (test_console.TestConsole.test_13_menu_exit) ... ok
    test_14_menu_invalid_input (test_console.TestConsole.test_14_menu_invalid_input) ... ok
    test_15_keyboard_interrupt (test_console.TestConsole.test_15_keyboard_interrupt) ... ok
    test_16_eof_error (test_console.TestConsole.test_16_eof_error) ... ok
    test_01_blue_color (test_console_ui.TestConsoleUI.test_01_blue_color) ... ok
    test_02_red_color (test_console_ui.TestConsoleUI.test_02_red_color) ... ok
    test_03_plain_text (test_console_ui.TestConsoleUI.test_03_plain_text) ... ok
    test_04_bold_text (test_console_ui.TestConsoleUI.test_04_bold_text) ... ok
    test_05_no_color_environment (test_console_ui.TestConsoleUI.test_05_no_color_environment) ... ok
    test_06_redirected_output (test_console_ui.TestConsoleUI.test_06_redirected_output) ... ok
    test_07_header_spacing (test_console_ui.TestConsoleUI.test_07_header_spacing) ... ok
    test_08_progress_bar (test_console_ui.TestConsoleUI.test_08_progress_bar) ... ok
    test_09_menu_colors (test_console_ui.TestConsoleUI.test_09_menu_colors) ... ok
    test_10_answer_colors (test_console_ui.TestConsoleUI.test_10_answer_colors) ... ok
    test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok
    test_01_default_question_count (test_quiz_game.TestQuizGame.test_01_default_question_count) ... ok
    test_02_difficulty_filter (test_quiz_game.TestQuizGame.test_02_difficulty_filter) ... ok
    test_03_add_quiz (test_quiz_game.TestQuizGame.test_03_add_quiz) ... ok
    test_04_duplicate_id (test_quiz_game.TestQuizGame.test_04_duplicate_id) ... ok
    test_05_duplicate_question (test_quiz_game.TestQuizGame.test_05_duplicate_question) ... ok
    test_06_next_id (test_quiz_game.TestQuizGame.test_06_next_id) ... ok
    test_07_start_game (test_quiz_game.TestQuizGame.test_07_start_game) ... ok
    test_08_invalid_count (test_quiz_game.TestQuizGame.test_08_invalid_count) ... ok
    test_09_empty_question_bank (test_quiz_game.TestQuizGame.test_09_empty_question_bank) ... ok
    test_10_correct_answer_points (test_quiz_game.TestQuizGame.test_10_correct_answer_points) ... ok
    test_11_wrong_answer_points (test_quiz_game.TestQuizGame.test_11_wrong_answer_points) ... ok
    test_12_hint_points (test_quiz_game.TestQuizGame.test_12_hint_points) ... ok
    test_13_repeated_hint (test_quiz_game.TestQuizGame.test_13_repeated_hint) ... ok
    test_14_hint_with_wrong_answer (test_quiz_game.TestQuizGame.test_14_hint_with_wrong_answer) ... ok
    test_15_invalid_answer_does_not_advance (test_quiz_game.TestQuizGame.test_15_invalid_answer_does_not_advance) ... ok
    test_16_advance_question (test_quiz_game.TestQuizGame.test_16_advance_question) ... ok
    test_17_normalized_score (test_quiz_game.TestQuizGame.test_17_normalized_score) ... ok
    test_18_best_score (test_quiz_game.TestQuizGame.test_18_best_score) ... ok
    test_19_cancel_game (test_quiz_game.TestQuizGame.test_19_cancel_game) ... ok
    test_20_completed_game_state (test_quiz_game.TestQuizGame.test_20_completed_game_state) ... ok
    test_21_no_active_game (test_quiz_game.TestQuizGame.test_21_no_active_game) ... ok
    test_22_random_unique_questions (test_quiz_game.TestQuizGame.test_22_random_unique_questions) ... ok
    test_23_question_bank_unchanged (test_quiz_game.TestQuizGame.test_23_question_bank_unchanged) ... ok
    test_24_invalid_json_preserves_bank (test_quiz_game.TestQuizGame.test_24_invalid_json_preserves_bank) ... ok
    test_25_prevent_changes_during_game (test_quiz_game.TestQuizGame.test_25_prevent_changes_during_game) ... ok
    test_26_result_is_independent (test_quiz_game.TestQuizGame.test_26_result_is_independent) ... ok
    test_27_zero_score_is_valid (test_quiz_game.TestQuizGame.test_27_zero_score_is_valid) ... ok
    test_28_hint_resets_next_question (test_quiz_game.TestQuizGame.test_28_hint_resets_next_question) ... ok
    test_01_non_numeric_menu_input (test_stability.TestStability.test_01_non_numeric_menu_input) ... ok
    test_02_empty_menu_input (test_stability.TestStability.test_02_empty_menu_input) ... ok
    test_03_out_of_range_input (test_stability.TestStability.test_03_out_of_range_input) ... ok
    test_04_trim_whitespace (test_stability.TestStability.test_04_trim_whitespace) ... ok
    test_05_empty_text_input (test_stability.TestStability.test_05_empty_text_input) ... ok
    test_06_invalid_answer_recovery (test_stability.TestStability.test_06_invalid_answer_recovery) ... ok
    test_07_duplicate_question_rejected (test_stability.TestStability.test_07_duplicate_question_rejected) ... ok
    test_08_duplicate_choice_recovery (test_stability.TestStability.test_08_duplicate_choice_recovery) ... ok
    test_09_empty_question_bank (test_stability.TestStability.test_09_empty_question_bank) ... ok
    test_10_cancel_game (test_stability.TestStability.test_10_cancel_game) ... ok
    test_11_keyboard_interrupt (test_stability.TestStability.test_11_keyboard_interrupt) ... ok
    test_12_eof_safe_exit (test_stability.TestStability.test_12_eof_safe_exit) ... ok
    test_13_interrupt_during_game (test_stability.TestStability.test_13_interrupt_during_game) ... ok
    test_14_missing_state_defaults (test_stability.TestStability.test_14_missing_state_defaults) ... ok
    test_15_corrupt_json_backup (test_stability.TestStability.test_15_corrupt_json_backup) ... ok
    test_16_invalid_history_recovery (test_stability.TestStability.test_16_invalid_history_recovery) ... ok
    test_17_atomic_save_preserves_original (test_stability.TestStability.test_17_atomic_save_preserves_original) ... ok
    test_18_delete_save_failure (test_stability.TestStability.test_18_delete_save_failure) ... ok
    test_19_save_failure_message (test_stability.TestStability.test_19_save_failure_message) ... ok
    test_20_no_score_display (test_stability.TestStability.test_20_no_score_display) ... ok
    test_01_missing_state (test_storage.TestStorage.test_01_missing_state) ... ok
    test_02_create_state (test_storage.TestStorage.test_02_create_state) ... ok
    test_03_required_schema (test_storage.TestStorage.test_03_required_schema) ... ok
    test_04_quiz_persistence (test_storage.TestStorage.test_04_quiz_persistence) ... ok
    test_05_best_score_persistence (test_storage.TestStorage.test_05_best_score_persistence) ... ok
    test_06_none_score_persistence (test_storage.TestStorage.test_06_none_score_persistence) ... ok
    test_07_zero_score_persistence (test_storage.TestStorage.test_07_zero_score_persistence) ... ok
    test_08_empty_bank_persistence (test_storage.TestStorage.test_08_empty_bank_persistence) ... ok
    test_09_utf8_encoding (test_storage.TestStorage.test_09_utf8_encoding) ... ok
    test_10_corrupt_json_recovery (test_storage.TestStorage.test_10_corrupt_json_recovery) ... ok
    test_11_invalid_encoding_recovery (test_storage.TestStorage.test_11_invalid_encoding_recovery) ... ok
    test_12_invalid_schema_recovery (test_storage.TestStorage.test_12_invalid_schema_recovery) ... ok
    test_13_invalid_score_validation (test_storage.TestStorage.test_13_invalid_score_validation) ... ok
    test_14_duplicate_id_recovery (test_storage.TestStorage.test_14_duplicate_id_recovery) ... ok
    test_15_atomic_save_failure (test_storage.TestStorage.test_15_atomic_save_failure) ... ok
    test_16_active_game_save_blocked (test_storage.TestStorage.test_16_active_game_save_blocked) ... ok
    test_17_add_console_autosave (test_storage.TestStorage.test_17_add_console_autosave) ... ok
    test_18_game_console_autosave (test_storage.TestStorage.test_18_game_console_autosave) ... ok
    test_19_exit_saves_state (test_storage.TestStorage.test_19_exit_saves_state) ... ok
    test_20_interrupt_saves_state (test_storage.TestStorage.test_20_interrupt_saves_state) ... ok

    ----------------------------------------------------------------------
    Ran 138 tests in 0.265s

    OK
    DISCOVERED TESTS: 138
    TESTS RUN: 138
    FAILURES: 0
    ERRORS: 0
    SKIPPED: 0
    PASS: All 138 unit tests completed
    Failed: False

    06. Verify Runtime State Protection

    > $before = $null

        if (Test-Path "state.json") {

            $before = (
                Get-FileHash `
                    "state.json" `
                    -Algorithm SHA256
            ).Hash

            "BEFORE SHA256: $before"
        }

        python -m unittest discover `
            -s tests `
            -p "test_stability.py" 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Stability tests failed."
        }

        if ($null -ne $before) {

            $after = (
                Get-FileHash `
                    "state.json" `
                    -Algorithm SHA256
            ).Hash

            "AFTER SHA256 : $after"

            if ($before -ne $after) {
                throw "Runtime state was modified."
            }

            "PASS: Runtime state unchanged"

        } else {

            if (Test-Path "state.json") {
                throw "Unexpected runtime state creation."
            }

            "PASS: Runtime state not created"
        }

        git check-ignore --no-index -- state.json

        if ($LASTEXITCODE -ne 0) {
            throw "Runtime state ignore rule failed."
        }

        "PASS: User data protected"
    BEFORE SHA256: 3075A2CAE341E84A758F632B6B9249C984734B9BF4A5D83C1BFDCEFB7EB9BAD7
    python : ....................
    위치 줄:757 문자:5
    +     python -m unittest discover `
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (....................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 20 tests in 0.070s

    OK
    AFTER SHA256 : 3075A2CAE341E84A758F632B6B9249C984734B9BF4A5D83C1BFDCEFB7EB9BAD7
    PASS: Runtime state unchanged
    state.json
    PASS: User data protected
    Failed: False

    07. Verify Application Source Integrity

    > git diff --exit-code HEAD -- `
            main.py `
            quiz.py `
            quiz_game.py `
            storage.py `
            history.py `
            console_ui.py `
            data/default_quizzes.json

        if ($LASTEXITCODE -ne 0) {
            throw "Application source changed unexpectedly."
        }

        $code = @'
    import io

    from contextlib import redirect_stdout
    from unittest.mock import patch

    from main import show_question
    from quiz_game import QuizGame

    game = QuizGame()
    game.load_default_quizzes()
    game.start_game(count=1)

    question = game.current_quiz.question

    output = io.StringIO()

    with redirect_stdout(output):

        with patch(
            "console_ui.color_enabled",
            return_value=True,
        ):

            show_question(game)

    assert (
        "\033[95m\033[1m" + question
        in output.getvalue()
    )

    print("QUESTION COLOR: PURPLE")
    print("PASS: Final UI preserved")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "UI verification failed."
        }

        "PASS: Existing application unchanged"
    QUESTION COLOR: PURPLE
    PASS: Final UI preserved
    PASS: Existing application unchanged
    Failed: False

    08. Commit Stability Verification

    > $files = @(
            "tests/test_stability.py",
            "logs/08A_console_ui.txt",
            "logs/08B_question_color.txt"
        )

        foreach ($file in $files) {

            if (-not (
                Test-Path `
                    -LiteralPath $file `
                    -PathType Leaf
            )) {
                throw "Missing required file: $file"
            }
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    if suite.countTestCases() != 138:
        raise SystemExit("Expected 138 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful()
        and not result.skipped
        else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        foreach ($kind in @(
            "GIT_AUTHOR_IDENT",
            "GIT_COMMITTER_IDENT"
        )) {

            $identity = git var $kind

            if ($LASTEXITCODE -ne 0 -or
                $identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

                throw "Git email privacy check failed."
            }
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        $expected = @(
            $files | ForEach-Object {
                "?? $_"
            }
        )

        $difference = @(
            Compare-Object `
                -ReferenceObject $expected `
                -DifferenceObject $status
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected working tree changes."
        }

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staging verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git commit -m "Test: Verify exception handling and runtime data protection"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: Stability verification committed"
    python : ..........................................................................................................................................
    위치 줄:896 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 138 tests in 0.281s

    OK
    git : warning: in the working copy of 'logs/08A_console_ui.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:938 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    warning: in the working copy of 'logs/08B_question_color.txt', CRLF will be replaced by LF the next time Git touches it
    [main 2fe8df1] Test: Verify exception handling and runtime data protection
     3 files changed, 2512 insertions(+)
     create mode 100644 logs/08A_console_ui.txt
     create mode 100644 logs/08B_question_color.txt
     create mode 100644 tests/test_stability.py
    PASS: Stability verification committed
    Failed: False

    09. Verify Final Stage Status

    > $count = git rev-list --count HEAD

        if ($LASTEXITCODE -ne 0 -or $count -ne "10") {
            throw "Expected ten Git commits."
        }

        git log --oneline --graph --all

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or
            $status.Count -gt 0) {

            throw "Working tree is not clean."
        }

        "TOTAL COMMITS: $count"
        "TOTAL TESTS EXPECTED: 138"
        "APPLICATION SOURCE: UNCHANGED"
        "PASS: Working tree is clean"
        "PASS: STEP09 completed"
    * 2fe8df1 Test: Verify exception handling and runtime data protection
    * e1fcbcc Fix: Distinguish question and answer colors
    * 1533f93 Feat: Improve console colors and visual readability
    * da5ff1c Feat: Complete bonus features and persistent play history
    * 03119eb Feat: Add JSON persistence and state recovery
    *   a01099c Merge feature/quiz-console into main
    |\
    | * 2c19fe7 Feat: Implement interactive quiz console
    |/
    * a49c5db Implement QuizGame engine and scoring tests
    * ccc8cb6 Implement Quiz class with validation and unit tests
    * f161dea Initialize quiz project and add 20 default questions
    TOTAL COMMITS: 10
    TOTAL TESTS EXPECTED: 138
    APPLICATION SOURCE: UNCHANGED
    PASS: Working tree is clean
    PASS: STEP09 completed
    Failed: False



### 10B_github_remote.txt

[Original execution log](../logs/10B_github_remote.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP10B - GitHub Remote and Push
    Date: 2026-11-14 23:18:31

    01. Verify Local Repository

    > $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
            throw "Expected main branch."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        $count = [int](git rev-list --count HEAD)

        if ($LASTEXITCODE -ne 0 -or $count -lt 10) {
            throw "Expected at least ten commits."
        }

        "CURRENT BRANCH: $branch"
        "TOTAL COMMITS: $count"
        "PASS: Local repository verified"
    CURRENT BRANCH: main
    TOTAL COMMITS: 10
    PASS: Local repository verified
    Failed: False

    02. Save STEP09 Execution Evidence

    > $source = Get-ChildItem `
            "C:\2026Codyssey_AllInOne\_Common\logs" `
            -File |
            Where-Object {
                $_.Name -like "*M_E1-2*STEP09*Stability*"
            } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if (-not $source) {
            throw "STEP09 log not found."
        }

        $content = Get-Content `
            -LiteralPath $source.FullName `
            -Raw `
            -Encoding UTF8

        if ($content -match '(?m)^Failed:\s*True\s*$') {
            throw "STEP09 contains failed steps."
        }

        $results = [regex]::Matches(
            $content,
            '(?m)^Failed:\s*False\s*$'
        )

        if ($results.Count -ne 9) {
            throw "Expected nine successful results."
        }

        $content = $content -replace `
            '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
            '${1}<USER>'

        $path = Join-Path `
            (Get-Location).Path `
            "logs\09_stability.txt"

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content,
            $utf8
        )

        "PASS: STEP09 evidence saved"
    PASS: STEP09 evidence saved
    Failed: False

    03. Configure GitHub Remote

    > $expected = "https://github.com/cody26jade/M_E1-2.git"

        $remotes = @(git remote)

        if ($LASTEXITCODE -ne 0) {
            throw "Git remote verification failed."
        }

        if ($remotes -contains "origin") {

            $actual = git remote get-url origin

            if ($LASTEXITCODE -ne 0 -or $actual -ne $expected) {
                throw "Unexpected existing remote URL."
            }

            "EXISTING REMOTE: $actual"

        } else {

            git remote add origin $expected

            if ($LASTEXITCODE -ne 0) {
                throw "Remote configuration failed."
            }

            "NEW REMOTE: $expected"
        }

        git config --local credential.username cody26jade

        if ($LASTEXITCODE -ne 0) {
            throw "Credential username setup failed."
        }

        git config --local credential.useHttpPath true

        if ($LASTEXITCODE -ne 0) {
            throw "Credential path setup failed."
        }

        git remote -v

        if ($LASTEXITCODE -ne 0) {
            throw "Remote verification failed."
        }

        "PASS: GitHub remote configured"
    NEW REMOTE: https://github.com/cody26jade/M_E1-2.git
    origin	https://github.com/cody26jade/M_E1-2.git (fetch)
    origin	https://github.com/cody26jade/M_E1-2.git (push)
    PASS: GitHub remote configured
    Failed: False

    04. Verify Git Identity and Privacy

    > foreach ($kind in @(
            "GIT_AUTHOR_IDENT",
            "GIT_COMMITTER_IDENT"
        )) {

            $identity = git var $kind

            if ($LASTEXITCODE -ne 0 -or
                $identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

                throw "Git identity privacy check failed."
            }

            "PASS: $kind uses GitHub noreply email"
        }

        $emails = @(git log --format="%ae%n%ce")

        if ($LASTEXITCODE -ne 0) {
            throw "Commit email verification failed."
        }

        $invalid = @(
            $emails | Where-Object {
                $_ -notmatch '^\d+\+cody26jade@users\.noreply\.github\.com$'
            }
        )

        if ($invalid.Count -gt 0) {
            throw "Unexpected email found in commit history."
        }

        "PASS: Commit history email privacy verified"
    PASS: GIT_AUTHOR_IDENT uses GitHub noreply email
    PASS: GIT_COMMITTER_IDENT uses GitHub noreply email
    PASS: Commit history email privacy verified
    Failed: False

    05. Verify Runtime Data Is Not Tracked

    > $tracked = @(git ls-files)

        if ($LASTEXITCODE -ne 0) {
            throw "Tracked file verification failed."
        }

        $private = @(
            $tracked | Where-Object {
                $_ -match '(^|/)(state\.json($|\.)|\.env($|\.))'
            }
        )

        if ($private.Count -gt 0) {
            throw "Private runtime files are tracked."
        }

        git check-ignore --no-index -- state.json

        if ($LASTEXITCODE -ne 0) {
            throw "Runtime state ignore rule failed."
        }

        "PASS: Runtime data excluded from Git"
    state.json
    PASS: Runtime data excluded from Git
    Failed: False

    06. Commit Stability Evidence

    > if (-not (Test-Path "logs/09_stability.txt")) {
            throw "Required stability evidence missing."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or
            $status.Count -ne 1 -or
            $status[0] -ne "?? logs/09_stability.txt") {

            throw "Unexpected working tree changes."
        }

        git add -- logs/09_stability.txt

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        git commit -m "Docs: Record stability verification evidence"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: Stability evidence committed"
    git : warning: in the working copy of 'logs/09_stability.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:213 문자:5
    +     git add -- logs/09_stability.txt
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    [main fb68f5c] Docs: Record stability verification evidence
     1 file changed, 1239 insertions(+)
     create mode 100644 logs/09_stability.txt
    PASS: Stability evidence committed
    Failed: False

    07. Verify Public GitHub Repository

    > $url = "https://api.github.com/repos/cody26jade/M_E1-2"

        $repo = Invoke-RestMethod `
            -Uri $url `
            -Headers @{
                "User-Agent" = "CODYSSEY-Mission"
            } `
            -ErrorAction Stop

        if ($repo.private -ne $false) {
            throw "Repository must be public."
        }

        if ($repo.full_name -ne "cody26jade/M_E1-2") {
            throw "Unexpected repository."
        }

        "REPOSITORY: $($repo.full_name)"
        "VISIBILITY: $($repo.visibility)"
        "URL: $($repo.html_url)"
        "PASS: Public repository verified"
    REPOSITORY: cody26jade/M_E1-2
    VISIBILITY: public
    URL: https://github.com/cody26jade/M_E1-2
    PASS: Public repository verified
    Failed: False



### 10C_git_collaboration.txt

[Original execution log](../logs/10C_git_collaboration.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP10C - Git Collaboration Practice
    Date: 2026-11-14 23:34:42

    01. Verify Initial GitHub Push

    > git status --short --branch

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        "LOCAL COMMIT : $local"
        "REMOTE COMMIT: $remoteHash"
        "PASS: Local and GitHub main match"
    ## main...origin/main
    LOCAL COMMIT : fb68f5ceb4b45270eee3cc450f49d25cb2f34804
    REMOTE COMMIT: fb68f5ceb4b45270eee3cc450f49d25cb2f34804
    PASS: Local and GitHub main match
    Failed: False

    02. Clone Repository into Separate Directory

    > git clone $url $clone

        if ($LASTEXITCODE -ne 0) {
            throw "Git clone failed."
        }

        $head = git -C $clone rev-parse HEAD

        if ($LASTEXITCODE -ne 0 -or $head -ne $local) {
            throw "Clone commit verification failed."
        }

        "CLONE DIRECTORY: $clone"
        "CLONE COMMIT: $head"
        "PASS: Independent clone created"
    git : Cloning into 'C:\2026Codyssey_AllInOne\M_E1-2_Clone'...
    위치 줄:52 문자:5
    +     git clone $url $clone
    +     ~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (Cloning into 'C..._E1-2_Clone'...:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    CLONE DIRECTORY: C:\2026Codyssey_AllInOne\M_E1-2_Clone
    CLONE COMMIT: fb68f5ceb4b45270eee3cc450f49d25cb2f34804
    PASS: Independent clone created
    Failed: False

    03. Configure Clone Git Identity

    > $email = git -C $root config --local user.email

        if ($LASTEXITCODE -ne 0 -or
            $email -notmatch '^\d+\+cody26jade@users\.noreply\.github\.com$') {

            throw "Invalid source Git email."
        }

        git -C $clone config --local user.name cody26jade

        if ($LASTEXITCODE -ne 0) {
            throw "Clone username setup failed."
        }

        git -C $clone config --local user.email $email

        if ($LASTEXITCODE -ne 0) {
            throw "Clone email setup failed."
        }

        git -C $clone config --local credential.username cody26jade

        if ($LASTEXITCODE -ne 0) {
            throw "Clone credential setup failed."
        }

        git -C $clone config --local credential.useHttpPath true

        if ($LASTEXITCODE -ne 0) {
            throw "Clone credential path setup failed."
        }

        "PASS: Clone Git identity configured"
    PASS: Clone Git identity configured
    Failed: False

    04. Create Collaboration Branch

    > git -C $clone checkout -b docs/collaboration-guide

        if ($LASTEXITCODE -ne 0) {
            throw "Branch creation failed."
        }

        git -C $clone branch

        if ($LASTEXITCODE -ne 0) {
            throw "Branch verification failed."
        }

        "PASS: Collaboration branch created"
    git : Switched to a new branch 'docs/collaboration-guide'
    위치 줄:108 문자:5
    +     git -C $clone checkout -b docs/collaboration-guide
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (Switched to a n...boration-guide':String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    * docs/collaboration-guide
      main
    PASS: Collaboration branch created
    Failed: False

    05. Create Collaboration Documentation

    > $branch = git -C $clone symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or
            $branch -ne "docs/collaboration-guide") {

            throw "Unexpected clone branch."
        }

        $directory = Join-Path $clone "docs"

        New-Item `
            -ItemType Directory `
            -Path $directory `
            -Force | Out-Null

        $path = Join-Path $directory "COLLABORATION.md"

        if (Test-Path -LiteralPath $path) {
            throw "Collaboration document already exists."
        }

        $content = @'
    # Git Collaboration Guide

    ## Project

    M_E1-2: Machine Tool and Vibration Analysis Quiz

    ## Purpose

    This document explains how to contribute to the project
    using a separate Git clone and a feature branch.

    ## Workflow

    1. Clone the public repository.
    2. Create a dedicated branch.
    3. Modify project documentation or source code.
    4. Run the automated tests.
    5. Commit the changes.
    6. Merge the branch into main.
    7. Push main to GitHub.
    8. Pull the changes into the original repository.

    ## Commands

        git clone https://github.com/cody26jade/M_E1-2.git
        git checkout -b feature/example
        python -m unittest discover -s tests
        git add .
        git commit -m "Describe the change"
        git checkout main
        git merge --no-ff feature/example
        git push origin main
        git pull --ff-only origin main

    ## Runtime Data Protection

    The local state.json file contains user-created questions,
    best scores and play history.

    It must not be committed or shared through GitHub.

    ## Testing

    Run the complete unit test suite before merging changes.

    Python 3.10 or later is required.
    No third-party Python packages are required.
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "CREATED: docs/COLLABORATION.md"
        "PASS: Collaboration documentation created"
    CREATED: docs/COLLABORATION.md
    PASS: Collaboration documentation created
    Failed: False

    06. Run Tests in Cloned Repository

    > Push-Location $clone

        try {

            $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 138:
        raise SystemExit("Expected 138 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    print("TESTS RUN:", result.testsRun)
    print("FAILURES:", len(result.failures))
    print("ERRORS:", len(result.errors))
    print("SKIPPED:", len(result.skipped))

    raise SystemExit(
        0 if result.wasSuccessful()
        and not result.skipped
        else 1
    )
    '@

            $code | python - 2>&1

            if ($LASTEXITCODE -ne 0) {
                throw "Clone tests failed."
            }

        } finally {

            Pop-Location
        }

        "PASS: All 138 cloned application tests passed"
    python : ..........................................................................................................................................
    위치 줄:242 문자:17
    +         $code | python - 2>&1
    +                 ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 138 tests in 0.221s

    OK
    DISCOVERED TESTS: 138
    TESTS RUN: 138
    FAILURES: 0
    ERRORS: 0
    SKIPPED: 0
    PASS: All 138 cloned application tests passed
    Failed: False

    07. Commit Collaboration Branch

    > $branch = git -C $clone symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or
            $branch -ne "docs/collaboration-guide") {

            throw "Unexpected clone branch."
        }

        foreach ($kind in @(
            "GIT_AUTHOR_IDENT",
            "GIT_COMMITTER_IDENT"
        )) {

            $identity = git -C $clone var $kind

            if ($LASTEXITCODE -ne 0 -or
                $identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

                throw "Clone Git identity verification failed."
            }
        }

        Push-Location $clone

        try {

            python -m unittest discover -s tests 2>&1

            if ($LASTEXITCODE -ne 0) {
                throw "Pre-commit tests failed."
            }

        } finally {

            Pop-Location
        }

        git -C $clone add -- docs/COLLABORATION.md

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git -C $clone diff --cached --name-only)

        if ($LASTEXITCODE -ne 0 -or
            $staged.Count -ne 1 -or
            $staged[0] -ne "docs/COLLABORATION.md") {

            throw "Unexpected staged files."
        }

        git -C $clone commit -m "Docs: Add Git collaboration workflow guide"

        if ($LASTEXITCODE -ne 0) {
            throw "Branch commit failed."
        }

        "PASS: Collaboration branch committed"
    python : ..........................................................................................................................................
    위치 줄:284 문자:9
    +         python -m unittest discover -s tests 2>&1
    +         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 138 tests in 0.198s

    OK
    [docs/collaboration-guide dc9964e] Docs: Add Git collaboration workflow guide
     1 file changed, 47 insertions(+)
     create mode 100644 docs/COLLABORATION.md
    PASS: Collaboration branch committed
    Failed: False

    08. Checkout Main and Merge Branch

    > $branch = git -C $clone symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or
            $branch -ne "docs/collaboration-guide") {

            throw "Unexpected branch before merge."
        }

        $status = @(git -C $clone status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Clone working tree is not clean."
        }

        $changed = @(
            git -C $clone diff --name-only "$local..HEAD"
        )

        if ($LASTEXITCODE -ne 0 -or
            $changed.Count -ne 1 -or
            $changed[0] -ne "docs/COLLABORATION.md") {

            throw "Expected committed collaboration document."
        }

        git -C $clone checkout main

        if ($LASTEXITCODE -ne 0) {
            throw "Checkout main failed."
        }

        git -C $clone merge --no-ff `
            docs/collaboration-guide `
            -m "Merge collaboration documentation branch"

        if ($LASTEXITCODE -ne 0) {
            throw "Branch merge failed."
        }

        $parents = git -C $clone log -1 --format="%P"

        if ($LASTEXITCODE -ne 0 -or
            ($parents -split '\s+').Count -ne 2) {

            throw "Expected a merge commit with two parents."
        }

        git -C $clone log -5 --oneline --graph --all

        if ($LASTEXITCODE -ne 0) {
            throw "Git graph verification failed."
        }

        "PASS: Branch merged into main"
    git : Switched to branch 'main'
    위치 줄:346 문자:5
    +     git -C $clone checkout main
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (Switched to branch 'main':String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    Your branch is up to date with 'origin/main'.
    Merge made by the 'ort' strategy.
     docs/COLLABORATION.md | 47 +++++++++++++++++++++++++++++++++++++++++++++++
     1 file changed, 47 insertions(+)
     create mode 100644 docs/COLLABORATION.md
    *   7079323 Merge collaboration documentation branch
    |\
    | * dc9964e Docs: Add Git collaboration workflow guide
    |/
    * fb68f5c Docs: Record stability verification evidence
    * 2fe8df1 Test: Verify exception handling and runtime data protection
    * e1fcbcc Fix: Distinguish question and answer colors
    PASS: Branch merged into main
    Failed: False

    09. Verify Clone Changes Before Push

    > $branch = git -C $clone symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
            throw "Expected clone main branch."
        }

        $status = @(git -C $clone status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Clone working tree is not clean."
        }

        $changed = @(
            git -C $clone diff --name-only "$local..HEAD"
        )

        if ($LASTEXITCODE -ne 0 -or
            $changed.Count -ne 1 -or
            $changed[0] -ne "docs/COLLABORATION.md") {

            throw "Unexpected collaboration changes."
        }

        $parents = git -C $clone log -1 --format="%P"

        if ($LASTEXITCODE -ne 0 -or
            ($parents -split '\s+').Count -ne 2) {

            throw "Merge commit verification failed."
        }

        $count = [int](git -C $clone rev-list --count HEAD)

        if ($LASTEXITCODE -ne 0 -or $count -lt 13) {
            throw "Expected at least thirteen commits."
        }

        "TOTAL COMMITS: $count"
        "PASS: Only collaboration documentation changed"
        "PASS: STEP10C completed"
    TOTAL COMMITS: 13
    PASS: Only collaboration documentation changed
    PASS: STEP10C completed
    Failed: False



### 10D_git_pull.txt

[Original execution log](../logs/10D_git_pull.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP10D - Pull and Collaboration Verification
    Date: 2026-11-14 23:38:46

    01. Verify Clone Push

    > $cloneHead = git -C $clone rev-parse HEAD

        if ($LASTEXITCODE -ne 0) {
            throw "Clone commit verification failed."
        }

        $remote = @(git ls-remote origin refs/heads/main)

        if ($LASTEXITCODE -ne 0 -or $remote.Count -ne 1) {
            throw "Remote verification failed."
        }

        $remoteHead = ($remote[0] -split '\s+')[0]

        if ($cloneHead -ne $remoteHead) {
            throw "Clone changes have not been pushed."
        }

        "CLONE : $cloneHead"
        "REMOTE: $remoteHead"
        "PASS: Clone push verified"
    CLONE : 7079323f74f8d67a7c88f52776cb6db7c217c165
    REMOTE: 7079323f74f8d67a7c88f52776cb6db7c217c165
    PASS: Clone push verified
    Failed: False

    02. Pull Changes into Original Repository

    > $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Original working tree is not clean."
        }

        $branch = git symbolic-ref --short HEAD

        if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
            throw "Expected main branch."
        }

        $before = git rev-parse HEAD

        if ($LASTEXITCODE -ne 0) {
            throw "Git HEAD verification failed."
        }

        git pull --ff-only origin main

        if ($LASTEXITCODE -ne 0) {
            throw "Git pull failed."
        }

        $after = git rev-parse HEAD

        if ($LASTEXITCODE -ne 0) {
            throw "Git HEAD verification failed."
        }

        if ($before -eq $after) {
            throw "Expected a new commit after pull."
        }

        "BEFORE: $before"
        "AFTER : $after"
        "PASS: Original repository updated"
    git : From https://github.com/cody26jade/M_E1-2
    위치 줄:52 문자:5
    +     git pull --ff-only origin main
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (From https://gi...dy26jade/M_E1-2:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

     * branch            main       -> FETCH_HEAD
    Updating fb68f5c..7079323
    Fast-forward
     docs/COLLABORATION.md | 47 +++++++++++++++++++++++++++++++++++++++++++++++
     1 file changed, 47 insertions(+)
     create mode 100644 docs/COLLABORATION.md
    BEFORE: fb68f5ceb4b45270eee3cc450f49d25cb2f34804
    AFTER : 7079323f74f8d67a7c88f52776cb6db7c217c165
    PASS: Original repository updated
    Failed: False

    03. Verify Collaboration Document

    > $original = "docs/COLLABORATION.md"
        $copied = Join-Path $clone $original

        if (-not (Test-Path $original)) {
            throw "Pulled document not found."
        }

        $hash1 = (Get-FileHash $original -Algorithm SHA256).Hash
        $hash2 = (Get-FileHash $copied -Algorithm SHA256).Hash

        if ($hash1 -ne $hash2) {
            throw "Document hash mismatch."
        }

        "ORIGINAL: $hash1"
        "CLONE   : $hash2"
        "PASS: Documents are identical"
    ORIGINAL: 6F7506D3C89972B908D2113CFF870565F138D31BBB904688F95E3FFFFBF07BC6
    CLONE   : 6F7506D3C89972B908D2113CFF870565F138D31BBB904688F95E3FFFFBF07BC6
    PASS: Documents are identical
    Failed: False

    04. Verify All Repository Commits

    > $originalHead = git rev-parse HEAD

        if ($LASTEXITCODE -ne 0) {
            throw "Original HEAD verification failed."
        }

        $cloneHead = git -C $clone rev-parse HEAD

        if ($LASTEXITCODE -ne 0) {
            throw "Clone HEAD verification failed."
        }

        $remote = @(git ls-remote origin refs/heads/main)

        if ($LASTEXITCODE -ne 0 -or $remote.Count -ne 1) {
            throw "Remote verification failed."
        }

        $remoteHead = ($remote[0] -split '\s+')[0]

        if ($originalHead -ne $cloneHead -or
            $originalHead -ne $remoteHead) {

            throw "Repository commits do not match."
        }

        "ORIGINAL: $originalHead"
        "CLONE   : $cloneHead"
        "GITHUB  : $remoteHead"
        "PASS: All three repositories synchronized"
    ORIGINAL: 7079323f74f8d67a7c88f52776cb6db7c217c165
    CLONE   : 7079323f74f8d67a7c88f52776cb6db7c217c165
    GITHUB  : 7079323f74f8d67a7c88f52776cb6db7c217c165
    PASS: All three repositories synchronized
    Failed: False

    05. Verify Application Tests

    > $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 138:
        raise SystemExit("Expected 138 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    print("TESTS RUN:", result.testsRun)
    print("FAILURES:", len(result.failures))
    print("ERRORS:", len(result.errors))
    print("SKIPPED:", len(result.skipped))

    raise SystemExit(
        0 if result.wasSuccessful()
        and not result.skipped
        else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Application tests failed."
        }

        "PASS: All 138 application tests passed"
    python : ..........................................................................................................................................
    위치 줄:158 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 138 tests in 0.190s

    OK
    DISCOVERED TESTS: 138
    TESTS RUN: 138
    FAILURES: 0
    ERRORS: 0
    SKIPPED: 0
    PASS: All 138 application tests passed
    Failed: False

    06. Verify Git History and Final Status

    > git log --oneline --graph --all

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        $count = [int](git rev-list --count HEAD)

        if ($LASTEXITCODE -ne 0 -or $count -lt 13) {
            throw "Expected at least thirteen commits."
        }

        $merges = @(git log --merges --oneline)

        if ($LASTEXITCODE -ne 0 -or $merges.Count -lt 1) {
            throw "Merge commit not found."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0 -or $status.Count -gt 0) {
            throw "Working tree is not clean."
        }

        "TOTAL COMMITS: $count"
        "MERGE COMMITS: $($merges.Count)"
        "PASS: Working tree is clean"
        "PASS: Git collaboration completed"
    *   7079323 Merge collaboration documentation branch
    |\
    | * dc9964e Docs: Add Git collaboration workflow guide
    |/
    * fb68f5c Docs: Record stability verification evidence
    * 2fe8df1 Test: Verify exception handling and runtime data protection
    * e1fcbcc Fix: Distinguish question and answer colors
    * 1533f93 Feat: Improve console colors and visual readability
    * da5ff1c Feat: Complete bonus features and persistent play history
    * 03119eb Feat: Add JSON persistence and state recovery
    *   a01099c Merge feature/quiz-console into main
    |\
    | * 2c19fe7 Feat: Implement interactive quiz console
    |/
    * a49c5db Implement QuizGame engine and scoring tests
    * ccc8cb6 Implement Quiz class with validation and unit tests
    * f161dea Initialize quiz project and add 20 default questions
    TOTAL COMMITS: 13
    MERGE COMMITS: 2
    PASS: Working tree is clean
    PASS: Git collaboration completed
    Failed: False



### 11_integration_tests.txt

[Original execution log](../logs/11_integration_tests.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP11 - Integration and Final Quality Tests
    Date: 2026-11-14 23:43:01

    01. Verify GitHub Synchronization

    > $local = git rev-parse HEAD

        if ($LASTEXITCODE -ne 0) {
            throw "Local HEAD verification failed."
        }

        $remote = @(git ls-remote origin refs/heads/main)

        if ($LASTEXITCODE -ne 0 -or $remote.Count -ne 1) {
            throw "Remote verification failed."
        }

        $remoteHead = ($remote[0] -split '\s+')[0]

        if ($local -ne $remoteHead) {
            throw "Local and remote commits do not match."
        }

        $count = [int](git rev-list --count HEAD)

        if ($LASTEXITCODE -ne 0 -or $count -lt 13) {
            throw "Expected at least thirteen commits."
        }

        "LOCAL : $local"
        "REMOTE: $remoteHead"
        "COMMITS: $count"
        "PASS: GitHub synchronization verified"
    LOCAL : 7079323f74f8d67a7c88f52776cb6db7c217c165
    REMOTE: 7079323f74f8d67a7c88f52776cb6db7c217c165
    COMMITS: 13
    PASS: GitHub synchronization verified
    Failed: False

    02. Save Git Collaboration Evidence

    > $items = @(
            @{
                Pattern = "*M_E1-2*STEP10B*GitHub*Remote*"
                Target = "logs\10B_github_remote.txt"
                Count = 7
            },
            @{
                Pattern = "*M_E1-2*STEP10C*Git*Collaboration*"
                Target = "logs\10C_git_collaboration.txt"
                Count = 9
            },
            @{
                Pattern = "*M_E1-2*STEP10D*Pull*Collaboration*"
                Target = "logs\10D_git_pull.txt"
                Count = 6
            }
        )

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        foreach ($item in $items) {

            $source = Get-ChildItem `
                "C:\2026Codyssey_AllInOne\_Common\logs" `
                -File |
                Where-Object {
                    $_.Name -like $item.Pattern
                } |
                Sort-Object LastWriteTime -Descending |
                Select-Object -First 1

            if (-not $source) {
                throw "Required collaboration log missing."
            }

            $content = Get-Content `
                -LiteralPath $source.FullName `
                -Raw `
                -Encoding UTF8

            if ($content -match '(?m)^Failed:\s*True\s*$') {
                throw "Previous execution contains errors."
            }

            $results = [regex]::Matches(
                $content,
                '(?m)^Failed:\s*False\s*$'
            )

            if ($results.Count -ne $item.Count) {
                throw "Unexpected result count."
            }

            $content = $content -replace `
                '(?i)([A-Z]:\\Users\\)[^\\\r\n]+(?=\\)', `
                '${1}<USER>'

            $path = Join-Path `
                (Get-Location).Path `
                $item.Target

            [System.IO.File]::WriteAllText(
                $path,
                $content,
                $utf8
            )

            "PASS: $($item.Target)"
        }
    PASS: logs\10B_github_remote.txt
    PASS: logs\10C_git_collaboration.txt
    PASS: logs\10D_git_pull.txt
    Failed: False

    03. Verify Existing 138 Unit Tests

    > $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("EXISTING TESTS:", count)

    if count != 138:
        raise SystemExit("Expected 138 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful()
        and not result.skipped
        else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Existing tests failed."
        }

        "PASS: All existing tests verified"
    python : ..........................................................................................................................................
    위치 줄:170 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 138 tests in 0.262s

    OK
    EXISTING TESTS: 138
    PASS: All existing tests verified
    Failed: False

    04. Create Integration Test Suite

    > $path = Join-Path `
            (Get-Location).Path `
            "tests\test_integration.py"

        $content = @'
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
    '@

        $utf8 = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $path,
            $content.TrimEnd() + "`n",
            $utf8
        )

        "PASS: Ten integration tests created"
    PASS: Ten integration tests created
    Failed: False

    05. Run Integration Tests

    > python -m py_compile tests/test_integration.py

        if ($LASTEXITCODE -ne 0) {
            throw "Integration test syntax check failed."
        }

        python -m unittest discover `
            -s tests `
            -p "test_integration.py" `
            -v 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Integration tests failed."
        }

        "PASS: All ten integration tests completed"
    python : test_01_default_bank_and_menu (test_integration.TestIntegration.test_01_default_bank_and_menu) ... ok
    위치 줄:649 문자:5
    +     python -m unittest discover `
    +     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_default...nd_menu) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_perfect_game_and_restart (test_integration.TestIntegration.test_02_perfect_game_and_restart) ... ok
    test_03_mixed_answers_and_hint_scoring (test_integration.TestIntegration.test_03_mixed_answers_and_hint_scoring) ... ok
    test_04_best_score_retained (test_integration.TestIntegration.test_04_best_score_retained) ... ok
    test_05_add_list_and_restart (test_integration.TestIntegration.test_05_add_list_and_restart) ... ok
    test_06_delete_and_restart (test_integration.TestIntegration.test_06_delete_and_restart) ... ok
    test_07_history_and_score_display (test_integration.TestIntegration.test_07_history_and_score_display) ... ok
    test_08_cancel_preserves_completed_history (test_integration.TestIntegration.test_08_cancel_preserves_completed_history) ... ok
    test_09_final_color_integration (test_integration.TestIntegration.test_09_final_color_integration) ... ok
    test_10_menu_exit_and_json_schema (test_integration.TestIntegration.test_10_menu_exit_and_json_schema) ... ok

    ----------------------------------------------------------------------
    Ran 10 tests in 0.055s

    OK
    PASS: All ten integration tests completed
    Failed: False

    06. Run Complete 148-Test Quality Suite

    > $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    count = suite.countTestCases()

    print("DISCOVERED TESTS:", count)

    if count != 148:
        raise SystemExit("Expected 148 tests.")

    result = unittest.TextTestRunner(
        verbosity=2
    ).run(suite)

    print()
    print("FINAL QUALITY TEST SUMMARY")
    print("TESTS RUN:", result.testsRun)
    print("FAILURES:", len(result.failures))
    print("ERRORS:", len(result.errors))
    print("SKIPPED:", len(result.skipped))

    passed = (
        result.testsRun
        - len(result.failures)
        - len(result.errors)
        - len(result.skipped)
        - len(result.expectedFailures)
        - len(result.unexpectedSuccesses)
    )

    print("PASSED:", passed)

    raise SystemExit(
        0 if result.wasSuccessful()
        and passed == 148
        else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Complete quality suite failed."
        }

        "PASS: All 148 tests completed"
    python : test_01_random_questions (test_bonus.TestBonus.test_01_random_questions) ... ok
    위치 줄:704 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (test_01_random_...estions) ... ok:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    test_02_selected_question_count (test_bonus.TestBonus.test_02_selected_question_count) ... ok
    test_03_hint_penalty (test_bonus.TestBonus.test_03_hint_penalty) ... ok
    test_04_repeated_hint (test_bonus.TestBonus.test_04_repeated_hint) ... ok
    test_05_delete_question (test_bonus.TestBonus.test_05_delete_question) ... ok
    test_06_delete_unknown_id (test_bonus.TestBonus.test_06_delete_unknown_id) ... ok
    test_07_delete_during_game (test_bonus.TestBonus.test_07_delete_during_game) ... ok
    test_08_delete_preserves_records (test_bonus.TestBonus.test_08_delete_preserves_records) ... ok
    test_09_delete_persistence (test_bonus.TestBonus.test_09_delete_persistence) ... ok
    test_10_delete_last_question (test_bonus.TestBonus.test_10_delete_last_question) ... ok
    test_11_empty_history (test_bonus.TestBonus.test_11_empty_history) ... ok
    test_12_record_completed_game (test_bonus.TestBonus.test_12_record_completed_game) ... ok
    test_13_history_persistence (test_bonus.TestBonus.test_13_history_persistence) ... ok
    test_14_multiple_history_records (test_bonus.TestBonus.test_14_multiple_history_records) ... ok
    test_15_old_schema_compatibility (test_bonus.TestBonus.test_15_old_schema_compatibility) ... ok
    test_16_invalid_history (test_bonus.TestBonus.test_16_invalid_history) ... ok
    test_17_console_delete_cancel (test_bonus.TestBonus.test_17_console_delete_cancel) ... ok
    test_18_console_delete_confirm (test_bonus.TestBonus.test_18_console_delete_confirm) ... ok
    test_19_console_cancel_no_history (test_bonus.TestBonus.test_19_console_cancel_no_history) ... ok
    test_20_console_history_output (test_bonus.TestBonus.test_20_console_history_output) ... ok
    test_21_console_completed_history (test_bonus.TestBonus.test_21_console_completed_history) ... ok
    test_22_menu_delete_and_history (test_bonus.TestBonus.test_22_menu_delete_and_history) ... ok
    test_23_delete_save_failure (test_bonus.TestBonus.test_23_delete_save_failure) ... ok
    test_24_empty_history_output (test_bonus.TestBonus.test_24_empty_history_output) ... ok
    test_01_read_text_validation (test_console.TestConsole.test_01_read_text_validation) ... ok
    test_02_read_int_validation (test_console.TestConsole.test_02_read_int_validation) ... ok
    test_03_show_menu (test_console.TestConsole.test_03_show_menu) ... ok
    test_04_list_questions (test_console.TestConsole.test_04_list_questions) ... ok
    test_05_empty_question_list (test_console.TestConsole.test_05_empty_question_list) ... ok
    test_06_add_question (test_console.TestConsole.test_06_add_question) ... ok
    test_07_duplicate_question (test_console.TestConsole.test_07_duplicate_question) ... ok
    test_08_score_without_record (test_console.TestConsole.test_08_score_without_record) ... ok
    test_09_play_with_correct_answer (test_console.TestConsole.test_09_play_with_correct_answer) ... ok
    test_10_play_with_hint (test_console.TestConsole.test_10_play_with_hint) ... ok
    test_11_cancel_game (test_console.TestConsole.test_11_cancel_game) ... ok
    test_12_empty_game (test_console.TestConsole.test_12_empty_game) ... ok
    test_13_menu_exit (test_console.TestConsole.test_13_menu_exit) ... ok
    test_14_menu_invalid_input (test_console.TestConsole.test_14_menu_invalid_input) ... ok
    test_15_keyboard_interrupt (test_console.TestConsole.test_15_keyboard_interrupt) ... ok
    test_16_eof_error (test_console.TestConsole.test_16_eof_error) ... ok
    test_01_blue_color (test_console_ui.TestConsoleUI.test_01_blue_color) ... ok
    test_02_red_color (test_console_ui.TestConsoleUI.test_02_red_color) ... ok
    test_03_plain_text (test_console_ui.TestConsoleUI.test_03_plain_text) ... ok
    test_04_bold_text (test_console_ui.TestConsoleUI.test_04_bold_text) ... ok
    test_05_no_color_environment (test_console_ui.TestConsoleUI.test_05_no_color_environment) ... ok
    test_06_redirected_output (test_console_ui.TestConsoleUI.test_06_redirected_output) ... ok
    test_07_header_spacing (test_console_ui.TestConsoleUI.test_07_header_spacing) ... ok
    test_08_progress_bar (test_console_ui.TestConsoleUI.test_08_progress_bar) ... ok
    test_09_menu_colors (test_console_ui.TestConsoleUI.test_09_menu_colors) ... ok
    test_10_answer_colors (test_console_ui.TestConsoleUI.test_10_answer_colors) ... ok
    test_01_default_bank_and_menu (test_integration.TestIntegration.test_01_default_bank_and_menu) ... ok
    test_02_perfect_game_and_restart (test_integration.TestIntegration.test_02_perfect_game_and_restart) ... ok
    test_03_mixed_answers_and_hint_scoring (test_integration.TestIntegration.test_03_mixed_answers_and_hint_scoring) ... ok
    test_04_best_score_retained (test_integration.TestIntegration.test_04_best_score_retained) ... ok
    test_05_add_list_and_restart (test_integration.TestIntegration.test_05_add_list_and_restart) ... ok
    test_06_delete_and_restart (test_integration.TestIntegration.test_06_delete_and_restart) ... ok
    test_07_history_and_score_display (test_integration.TestIntegration.test_07_history_and_score_display) ... ok
    test_08_cancel_preserves_completed_history (test_integration.TestIntegration.test_08_cancel_preserves_completed_history) ... ok
    test_09_final_color_integration (test_integration.TestIntegration.test_09_final_color_integration) ... ok
    test_10_menu_exit_and_json_schema (test_integration.TestIntegration.test_10_menu_exit_and_json_schema) ... ok
    test_01_create_object (test_quiz.TestQuiz.test_01_create_object) ... ok
    test_02_correct_answer (test_quiz.TestQuiz.test_02_correct_answer) ... ok
    test_03_wrong_answer (test_quiz.TestQuiz.test_03_wrong_answer) ... ok
    test_04_invalid_answer_range (test_quiz.TestQuiz.test_04_invalid_answer_range) ... ok
    test_05_invalid_answer_type (test_quiz.TestQuiz.test_05_invalid_answer_type) ... ok
    test_06_get_hint (test_quiz.TestQuiz.test_06_get_hint) ... ok
    test_07_get_explanation (test_quiz.TestQuiz.test_07_get_explanation) ... ok
    test_08_correct_choice (test_quiz.TestQuiz.test_08_correct_choice) ... ok
    test_09_to_dict (test_quiz.TestQuiz.test_09_to_dict) ... ok
    test_10_round_trip (test_quiz.TestQuiz.test_10_round_trip) ... ok
    test_11_missing_field (test_quiz.TestQuiz.test_11_missing_field) ... ok
    test_12_invalid_choice_count (test_quiz.TestQuiz.test_12_invalid_choice_count) ... ok
    test_13_duplicate_choices (test_quiz.TestQuiz.test_13_duplicate_choices) ... ok
    test_14_invalid_difficulty (test_quiz.TestQuiz.test_14_invalid_difficulty) ... ok
    test_15_empty_question (test_quiz.TestQuiz.test_15_empty_question) ... ok
    test_16_invalid_correct_answer (test_quiz.TestQuiz.test_16_invalid_correct_answer) ... ok
    test_17_shuffle_preserves_answer (test_quiz.TestQuiz.test_17_shuffle_preserves_answer) ... ok
    test_18_shuffle_preserves_original (test_quiz.TestQuiz.test_18_shuffle_preserves_original) ... ok
    test_19_load_all_default_questions (test_quiz.TestQuiz.test_19_load_all_default_questions) ... ok
    test_20_independent_choice_lists (test_quiz.TestQuiz.test_20_independent_choice_lists) ... ok
    test_01_default_question_count (test_quiz_game.TestQuizGame.test_01_default_question_count) ... ok
    test_02_difficulty_filter (test_quiz_game.TestQuizGame.test_02_difficulty_filter) ... ok
    test_03_add_quiz (test_quiz_game.TestQuizGame.test_03_add_quiz) ... ok
    test_04_duplicate_id (test_quiz_game.TestQuizGame.test_04_duplicate_id) ... ok
    test_05_duplicate_question (test_quiz_game.TestQuizGame.test_05_duplicate_question) ... ok
    test_06_next_id (test_quiz_game.TestQuizGame.test_06_next_id) ... ok
    test_07_start_game (test_quiz_game.TestQuizGame.test_07_start_game) ... ok
    test_08_invalid_count (test_quiz_game.TestQuizGame.test_08_invalid_count) ... ok
    test_09_empty_question_bank (test_quiz_game.TestQuizGame.test_09_empty_question_bank) ... ok
    test_10_correct_answer_points (test_quiz_game.TestQuizGame.test_10_correct_answer_points) ... ok
    test_11_wrong_answer_points (test_quiz_game.TestQuizGame.test_11_wrong_answer_points) ... ok
    test_12_hint_points (test_quiz_game.TestQuizGame.test_12_hint_points) ... ok
    test_13_repeated_hint (test_quiz_game.TestQuizGame.test_13_repeated_hint) ... ok
    test_14_hint_with_wrong_answer (test_quiz_game.TestQuizGame.test_14_hint_with_wrong_answer) ... ok
    test_15_invalid_answer_does_not_advance (test_quiz_game.TestQuizGame.test_15_invalid_answer_does_not_advance) ... ok
    test_16_advance_question (test_quiz_game.TestQuizGame.test_16_advance_question) ... ok
    test_17_normalized_score (test_quiz_game.TestQuizGame.test_17_normalized_score) ... ok
    test_18_best_score (test_quiz_game.TestQuizGame.test_18_best_score) ... ok
    test_19_cancel_game (test_quiz_game.TestQuizGame.test_19_cancel_game) ... ok
    test_20_completed_game_state (test_quiz_game.TestQuizGame.test_20_completed_game_state) ... ok
    test_21_no_active_game (test_quiz_game.TestQuizGame.test_21_no_active_game) ... ok
    test_22_random_unique_questions (test_quiz_game.TestQuizGame.test_22_random_unique_questions) ... ok
    test_23_question_bank_unchanged (test_quiz_game.TestQuizGame.test_23_question_bank_unchanged) ... ok
    test_24_invalid_json_preserves_bank (test_quiz_game.TestQuizGame.test_24_invalid_json_preserves_bank) ... ok
    test_25_prevent_changes_during_game (test_quiz_game.TestQuizGame.test_25_prevent_changes_during_game) ... ok
    test_26_result_is_independent (test_quiz_game.TestQuizGame.test_26_result_is_independent) ... ok
    test_27_zero_score_is_valid (test_quiz_game.TestQuizGame.test_27_zero_score_is_valid) ... ok
    test_28_hint_resets_next_question (test_quiz_game.TestQuizGame.test_28_hint_resets_next_question) ... ok
    test_01_non_numeric_menu_input (test_stability.TestStability.test_01_non_numeric_menu_input) ... ok
    test_02_empty_menu_input (test_stability.TestStability.test_02_empty_menu_input) ... ok
    test_03_out_of_range_input (test_stability.TestStability.test_03_out_of_range_input) ... ok
    test_04_trim_whitespace (test_stability.TestStability.test_04_trim_whitespace) ... ok
    test_05_empty_text_input (test_stability.TestStability.test_05_empty_text_input) ... ok
    test_06_invalid_answer_recovery (test_stability.TestStability.test_06_invalid_answer_recovery) ... ok
    test_07_duplicate_question_rejected (test_stability.TestStability.test_07_duplicate_question_rejected) ... ok
    test_08_duplicate_choice_recovery (test_stability.TestStability.test_08_duplicate_choice_recovery) ... ok
    test_09_empty_question_bank (test_stability.TestStability.test_09_empty_question_bank) ... ok
    test_10_cancel_game (test_stability.TestStability.test_10_cancel_game) ... ok
    test_11_keyboard_interrupt (test_stability.TestStability.test_11_keyboard_interrupt) ... ok
    test_12_eof_safe_exit (test_stability.TestStability.test_12_eof_safe_exit) ... ok
    test_13_interrupt_during_game (test_stability.TestStability.test_13_interrupt_during_game) ... ok
    test_14_missing_state_defaults (test_stability.TestStability.test_14_missing_state_defaults) ... ok
    test_15_corrupt_json_backup (test_stability.TestStability.test_15_corrupt_json_backup) ... ok
    test_16_invalid_history_recovery (test_stability.TestStability.test_16_invalid_history_recovery) ... ok
    test_17_atomic_save_preserves_original (test_stability.TestStability.test_17_atomic_save_preserves_original) ... ok
    test_18_delete_save_failure (test_stability.TestStability.test_18_delete_save_failure) ... ok
    test_19_save_failure_message (test_stability.TestStability.test_19_save_failure_message) ... ok
    test_20_no_score_display (test_stability.TestStability.test_20_no_score_display) ... ok
    test_01_missing_state (test_storage.TestStorage.test_01_missing_state) ... ok
    test_02_create_state (test_storage.TestStorage.test_02_create_state) ... ok
    test_03_required_schema (test_storage.TestStorage.test_03_required_schema) ... ok
    test_04_quiz_persistence (test_storage.TestStorage.test_04_quiz_persistence) ... ok
    test_05_best_score_persistence (test_storage.TestStorage.test_05_best_score_persistence) ... ok
    test_06_none_score_persistence (test_storage.TestStorage.test_06_none_score_persistence) ... ok
    test_07_zero_score_persistence (test_storage.TestStorage.test_07_zero_score_persistence) ... ok
    test_08_empty_bank_persistence (test_storage.TestStorage.test_08_empty_bank_persistence) ... ok
    test_09_utf8_encoding (test_storage.TestStorage.test_09_utf8_encoding) ... ok
    test_10_corrupt_json_recovery (test_storage.TestStorage.test_10_corrupt_json_recovery) ... ok
    test_11_invalid_encoding_recovery (test_storage.TestStorage.test_11_invalid_encoding_recovery) ... ok
    test_12_invalid_schema_recovery (test_storage.TestStorage.test_12_invalid_schema_recovery) ... ok
    test_13_invalid_score_validation (test_storage.TestStorage.test_13_invalid_score_validation) ... ok
    test_14_duplicate_id_recovery (test_storage.TestStorage.test_14_duplicate_id_recovery) ... ok
    test_15_atomic_save_failure (test_storage.TestStorage.test_15_atomic_save_failure) ... ok
    test_16_active_game_save_blocked (test_storage.TestStorage.test_16_active_game_save_blocked) ... ok
    test_17_add_console_autosave (test_storage.TestStorage.test_17_add_console_autosave) ... ok
    test_18_game_console_autosave (test_storage.TestStorage.test_18_game_console_autosave) ... ok
    test_19_exit_saves_state (test_storage.TestStorage.test_19_exit_saves_state) ... ok
    test_20_interrupt_saves_state (test_storage.TestStorage.test_20_interrupt_saves_state) ... ok

    ----------------------------------------------------------------------
    Ran 148 tests in 0.310s

    OK
    DISCOVERED TESTS: 148

    FINAL QUALITY TEST SUMMARY
    TESTS RUN: 148
    FAILURES: 0
    ERRORS: 0
    SKIPPED: 0
    PASSED: 148
    PASS: All 148 tests completed
    Failed: False

    07. Verify Default Dataset and Python Files

    > $code = @'
    import json
    import py_compile

    from pathlib import Path
    from collections import Counter

    from quiz import Quiz

    path = Path("data/default_quizzes.json")

    data = json.loads(
        path.read_text(encoding="utf-8")
    )

    quizzes = [
        Quiz.from_dict(item)
        for item in data
    ]

    assert len(quizzes) == 20

    assert len({
        quiz.id
        for quiz in quizzes
    }) == 20

    levels = Counter(
        quiz.difficulty
        for quiz in quizzes
    )

    assert levels["beginner"] == 10
    assert levels["intermediate"] == 10

    for quiz in quizzes:

        assert len(quiz.choices) == 4

        assert 1 <= quiz.answer <= 4

        assert quiz.check_answer(quiz.answer)

    print("DEFAULT QUESTIONS:", len(quizzes))
    print("BEGINNER:", levels["beginner"])
    print("INTERMEDIATE:", levels["intermediate"])

    files = sorted(Path(".").glob("*.py"))

    files += sorted(Path("tests").glob("*.py"))

    for file in files:

        py_compile.compile(
            str(file),
            doraise=True,
        )

        print("SYNTAX PASS:", file)

    print("PASS: Dataset and Python files verified")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "Dataset or source validation failed."
        }
    DEFAULT QUESTIONS: 20
    BEGINNER: 10
    INTERMEDIATE: 10
    SYNTAX PASS: console_ui.py
    SYNTAX PASS: history.py
    SYNTAX PASS: main.py
    SYNTAX PASS: quiz.py
    SYNTAX PASS: quiz_game.py
    SYNTAX PASS: storage.py
    SYNTAX PASS: tests\test_bonus.py
    SYNTAX PASS: tests\test_console.py
    SYNTAX PASS: tests\test_console_ui.py
    SYNTAX PASS: tests\test_integration.py
    SYNTAX PASS: tests\test_quiz.py
    SYNTAX PASS: tests\test_quiz_game.py
    SYNTAX PASS: tests\test_stability.py
    SYNTAX PASS: tests\test_storage.py
    PASS: Dataset and Python files verified
    Failed: False

    08. Verify Runtime Data Protection

    > if ($null -ne $stateBefore) {

            if (-not (Test-Path "state.json")) {
                throw "Runtime state file is missing."
            }

            $stateAfter = (
                Get-FileHash state.json -Algorithm SHA256
            ).Hash

            "BEFORE: $stateBefore"
            "AFTER : $stateAfter"

            if ($stateBefore -ne $stateAfter) {
                throw "Runtime state was modified."
            }

            "PASS: Runtime state unchanged"

        } else {

            if (Test-Path "state.json") {
                throw "Unexpected runtime state creation."
            }

            "PASS: Runtime state not created"
        }

        git check-ignore --no-index -- state.json

        if ($LASTEXITCODE -ne 0) {
            throw "Runtime state ignore verification failed."
        }

        $tracked = @(git ls-files)

        if ($LASTEXITCODE -ne 0) {
            throw "Tracked file verification failed."
        }

        $private = @(
            $tracked | Where-Object {
                $_ -match '(^|/)(state\.json($|\.)|\.env($|\.))'
            }
        )

        if ($private.Count -gt 0) {
            throw "Private runtime files are tracked."
        }

        "PASS: Runtime data excluded from Git"
    BEFORE: 3075A2CAE341E84A758F632B6B9249C984734B9BF4A5D83C1BFDCEFB7EB9BAD7
    AFTER : 3075A2CAE341E84A758F632B6B9249C984734B9BF4A5D83C1BFDCEFB7EB9BAD7
    PASS: Runtime state unchanged
    state.json
    PASS: Runtime data excluded from Git
    Failed: False

    09. Verify Application Source Integrity

    > git diff --exit-code HEAD -- `
            main.py `
            quiz.py `
            quiz_game.py `
            storage.py `
            history.py `
            console_ui.py `
            data/default_quizzes.json

        if ($LASTEXITCODE -ne 0) {
            throw "Application source changed unexpectedly."
        }

        "PASS: Application source unchanged"
        "PASS: Existing UI and game logic preserved"
    PASS: Application source unchanged
    PASS: Existing UI and game logic preserved
    Failed: False

    10. Commit Integration Tests and Evidence

    > $files = @(
            "tests/test_integration.py",
            "logs/10B_github_remote.txt",
            "logs/10C_git_collaboration.txt",
            "logs/10D_git_pull.txt"
        )

        foreach ($file in $files) {

            if (-not (
                Test-Path `
                    -LiteralPath $file `
                    -PathType Leaf
            )) {
                throw "Required file missing: $file"
            }
        }

        $code = @'
    import unittest

    suite = unittest.defaultTestLoader.discover("tests")

    if suite.countTestCases() != 148:
        raise SystemExit("Expected 148 tests.")

    result = unittest.TextTestRunner(
        verbosity=1
    ).run(suite)

    raise SystemExit(
        0 if result.wasSuccessful()
        and not result.skipped
        and not result.expectedFailures
        else 1
    )
    '@

        $code | python - 2>&1

        if ($LASTEXITCODE -ne 0) {
            throw "Pre-commit tests failed."
        }

        foreach ($kind in @(
            "GIT_AUTHOR_IDENT",
            "GIT_COMMITTER_IDENT"
        )) {

            $identity = git var $kind

            if ($LASTEXITCODE -ne 0 -or
                $identity -notmatch '<\d+\+cody26jade@users\.noreply\.github\.com>') {

                throw "Git identity privacy check failed."
            }
        }

        if ($null -ne $stateBefore) {

            if (-not (Test-Path "state.json")) {
                throw "Runtime state missing."
            }

            $currentHash = (
                Get-FileHash state.json -Algorithm SHA256
            ).Hash

            if ($currentHash -ne $stateBefore) {
                throw "Runtime state changed."
            }

        } elseif (Test-Path "state.json") {

            throw "Unexpected runtime state creation."
        }

        git diff --exit-code HEAD -- `
            main.py `
            quiz.py `
            quiz_game.py `
            storage.py `
            history.py `
            console_ui.py `
            data/default_quizzes.json

        if ($LASTEXITCODE -ne 0) {
            throw "Application source changed."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        $allowed = @(
            $files | ForEach-Object {
                "?? $_"
            }
        )

        $allowed += "?? screenshots/07_Git_History.png"

        $unexpected = @(
            $status | Where-Object {
                $_ -notin $allowed
            }
        )

        if ($unexpected.Count -gt 0) {
            throw "Unexpected working tree changes."
        }

        git add -- $files

        if ($LASTEXITCODE -ne 0) {
            throw "Git add failed."
        }

        $staged = @(git diff --cached --name-only)

        if ($LASTEXITCODE -ne 0) {
            throw "Staging verification failed."
        }

        $difference = @(
            Compare-Object `
                -ReferenceObject $files `
                -DifferenceObject $staged
        )

        if ($difference.Count -gt 0) {
            throw "Unexpected staged files."
        }

        git commit -m "Test: Validate complete quiz application integration"

        if ($LASTEXITCODE -ne 0) {
            throw "Git commit failed."
        }

        "PASS: Integration tests and evidence committed"
    python : ....................................................................................................................................................
    위치 줄:899 문자:13
    +     $code | python - 2>&1
    +             ~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (.................................:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    ----------------------------------------------------------------------
    Ran 148 tests in 0.284s

    OK
    git : warning: in the working copy of 'logs/10B_github_remote.txt', CRLF will be replaced by LF the next time Git touches it
    위치 줄:975 문자:5
    +     git add -- $files
    +     ~~~~~~~~~~~~~~~~~
        + CategoryInfo          : NotSpecified: (warning: in the... Git touches it:String) [], RemoteException
        + FullyQualifiedErrorId : NativeCommandError

    warning: in the working copy of 'logs/10C_git_collaboration.txt', CRLF will be replaced by LF the next time Git touches it
    warning: in the working copy of 'logs/10D_git_pull.txt', CRLF will be replaced by LF the next time Git touches it
    [main 394c5eb] Test: Validate complete quiz application integration
     4 files changed, 1452 insertions(+)
     create mode 100644 logs/10B_github_remote.txt
     create mode 100644 logs/10C_git_collaboration.txt
     create mode 100644 logs/10D_git_pull.txt
     create mode 100644 tests/test_integration.py
    PASS: Integration tests and evidence committed
    Failed: False

    11. Verify Final Quality Status

    > $count = [int](git rev-list --count HEAD)

        if ($LASTEXITCODE -ne 0 -or $count -lt 14) {
            throw "Expected at least fourteen commits."
        }

        $status = @(git status --porcelain)

        if ($LASTEXITCODE -ne 0) {
            throw "Git status failed."
        }

        $unexpected = @(
            $status | Where-Object {
                $_ -ne "?? screenshots/07_Git_History.png"
            }
        )

        if ($unexpected.Count -gt 0) {
            throw "Unexpected working tree changes."
        }

        git log -5 --oneline --graph

        if ($LASTEXITCODE -ne 0) {
            throw "Git history verification failed."
        }

        "TOTAL COMMITS: $count"
        "TOTAL TESTS EXPECTED: 148"
        "DEFAULT QUESTIONS: 20"
        "APPLICATION SOURCE: UNCHANGED"
        "PASS: STEP11 completed"
    * 394c5eb Test: Validate complete quiz application integration
    *   7079323 Merge collaboration documentation branch
    |\
    | * dc9964e Docs: Add Git collaboration workflow guide
    |/
    * fb68f5c Docs: Record stability verification evidence
    * 2fe8df1 Test: Verify exception handling and runtime data protection
    TOTAL COMMITS: 14
    TOTAL TESTS EXPECTED: 148
    DEFAULT QUESTIONS: 20
    APPLICATION SOURCE: UNCHANGED
    PASS: STEP11 completed
    Failed: False



### 12A_screenshot_verification.txt

[Original execution log](../logs/12A_screenshot_verification.txt)

    CODYSSEY MISSION REPORT SYSTEM
    M_E1-2 STEP12A - Screenshot Evidence Verification
    Date: 2026-11-14 23:52:11

    01. Verify Screenshot Files

    > $files = @(
            "01_Development_Environment.png",
            "02_Git_Configuration.png",
            "03_Quiz_Main_Menu.png",
            "04_Quiz_Add.png",
            "05_Quiz_List.png",
            "06_Quiz_Play.png",
            "07_Git_History.png",
            "08_Quiz_Result.png",
            "09_Quiz_Best_Score.png",
            "10_Quiz_History.png"
        )

        $missing = @()

        foreach ($file in $files) {

            $path = Join-Path "screenshots" $file

            if (Test-Path -LiteralPath $path -PathType Leaf) {

                $size = (Get-Item -LiteralPath $path).Length

                if ($size -gt 0) {

                    "PASS: $file ($size bytes)"

                } else {

                    $missing += $file

                    "EMPTY: $file"
                }

            } else {

                $missing += $file

                "MISSING: $file"
            }
        }

        "TOTAL EXPECTED: $($files.Count)"
        "TOTAL PRESENT : $($files.Count - $missing.Count)"

        if ($missing.Count -gt 0) {
            throw "Required screenshot files missing or empty."
        }

        "PASS: All ten screenshot files present"
    PASS: 01_Development_Environment.png (89978 bytes)
    PASS: 02_Git_Configuration.png (16977 bytes)
    PASS: 03_Quiz_Main_Menu.png (12330 bytes)
    PASS: 04_Quiz_Add.png (26922 bytes)
    PASS: 05_Quiz_List.png (40096 bytes)
    PASS: 06_Quiz_Play.png (27748 bytes)
    PASS: 07_Git_History.png (24692 bytes)
    PASS: 08_Quiz_Result.png (21097 bytes)
    PASS: 09_Quiz_Best_Score.png (9733 bytes)
    PASS: 10_Quiz_History.png (13128 bytes)
    TOTAL EXPECTED: 10
    TOTAL PRESENT : 10
    PASS: All ten screenshot files present
    Failed: False

    02. Verify PNG Image Format

    > $code = @'
    from pathlib import Path
    import struct

    files = sorted(Path("screenshots").glob("*.png"))

    assert files, "No PNG files found"

    for path in files:

        with path.open("rb") as stream:
            header = stream.read(24)

        assert len(header) == 24, path.name

        assert header[:8] == b"\x89PNG\r\n\x1a\n", path.name

        assert header[12:16] == b"IHDR", path.name

        width, height = struct.unpack(
            ">II",
            header[16:24],
        )

        assert width > 0 and height > 0, path.name

        print(
            f"PASS: {path.name} "
            f"({width} x {height})"
        )

    print("PASS: PNG image headers verified")
    '@

        $code | python -

        if ($LASTEXITCODE -ne 0) {
            throw "PNG verification failed."
        }
    PASS: 01_Development_Environment.png (845 x 905)
    PASS: 02_Git_Configuration.png (434 x 282)
    PASS: 03_Quiz_Main_Menu.png (441 x 393)
    PASS: 04_Quiz_Add.png (449 x 913)
    PASS: 05_Quiz_List.png (549 x 922)
    PASS: 06_Quiz_Play.png (401 x 825)
    PASS: 07_Git_History.png (592 x 293)
    PASS: 08_Quiz_Result.png (508 x 823)
    PASS: 09_Quiz_Best_Score.png (414 x 368)
    PASS: 10_Quiz_History.png (417 x 435)
    PASS: PNG image headers verified
    Failed: False

    03. Verify Original Runtime Data

    > if (-not $global:M_E1_2_DemoPath) {
            throw "Demo session information not found."
        }

        if ($null -ne $global:M_E1_2_StateHash) {

            if (-not (Test-Path "state.json")) {
                throw "Original state file missing."
            }

            $after = (
                Get-FileHash state.json -Algorithm SHA256
            ).Hash

            "BEFORE: $global:M_E1_2_StateHash"
            "AFTER : $after"

            if ($after -ne $global:M_E1_2_StateHash) {
                throw "Original runtime data changed."
            }

            "PASS: Original runtime data unchanged"

        } else {

            if (Test-Path "state.json") {
                throw "Unexpected original state creation."
            }

            "PASS: Original runtime state not created"
        }
    BEFORE: 3075A2CAE341E84A758F632B6B9249C984734B9BF4A5D83C1BFDCEFB7EB9BAD7
    AFTER : 3075A2CAE341E84A758F632B6B9249C984734B9BF4A5D83C1BFDCEFB7EB9BAD7
    PASS: Original runtime data unchanged
    Failed: False

    04. Verify Demo Runtime Data

    > $path = Join-Path `
            $global:M_E1_2_DemoPath `
            "state.json"

        if (-not (Test-Path -LiteralPath $path)) {
            throw "Demo runtime state not found."
        }

        $data = Get-Content `
            -LiteralPath $path `
            -Raw `
            -Encoding UTF8 |
            ConvertFrom-Json

        "DEMO QUESTIONS: $($data.quizzes.Count)"
        "DEMO BEST SCORE: $($data.best_score)"
        "DEMO HISTORY COUNT: $($data.history.Count)"

        if ($data.quizzes.Count -ne 21) {
            throw "Expected 21 demo questions."
        }

        if ($data.history.Count -lt 1) {
            throw "Expected completed demo game."
        }

        if ($null -eq $data.best_score) {
            throw "Expected a recorded best score."
        }

        "PASS: Demo question and play history verified"
    DEMO QUESTIONS: 21
    DEMO BEST SCORE: 70.0
    DEMO HISTORY COUNT: 1
    PASS: Demo question and play history verified
    Failed: False

    05. Verify Application Source Integrity

    > git diff --exit-code HEAD -- `
            main.py `
            quiz.py `
            quiz_game.py `
            storage.py `
            history.py `
            console_ui.py `
            data/default_quizzes.json

        if ($LASTEXITCODE -ne 0) {
            throw "Original application source changed."
        }

        git status --short

        if ($LASTEXITCODE -ne 0) {
            throw "Git status verification failed."
        }

        "PASS: Original application unchanged"
        "PASS: STEP12A screenshot verification completed"
     M screenshots/03_Quiz_Main_Menu.png
    ?? screenshots/04_Quiz_Add.png
    ?? screenshots/05_Quiz_List.png
    ?? screenshots/06_Quiz_Play.png
    ?? screenshots/07_Git_History.png
    ?? screenshots/08_Quiz_Result.png
    ?? screenshots/09_Quiz_Best_Score.png
    ?? screenshots/10_Quiz_History.png
    PASS: Original application unchanged
    PASS: STEP12A screenshot verification completed
    Failed: False



## 4. Manual Execution Screenshots

- [01_Development_Environment.png](../screenshots/01_Development_Environment.png)
- [02_Git_Configuration.png](../screenshots/02_Git_Configuration.png)
- [03_Quiz_Main_Menu.png](../screenshots/03_Quiz_Main_Menu.png)
- [04_Quiz_Add.png](../screenshots/04_Quiz_Add.png)
- [05_Quiz_List.png](../screenshots/05_Quiz_List.png)
- [06_Quiz_Play.png](../screenshots/06_Quiz_Play.png)
- [07_Git_History.png](../screenshots/07_Git_History.png)
- [08_Quiz_Result.png](../screenshots/08_Quiz_Result.png)
- [09_Quiz_Best_Score.png](../screenshots/09_Quiz_Best_Score.png)
- [10_Quiz_History.png](../screenshots/10_Quiz_History.png)

## 5. Evidence Limitations

Automated tests verify the implemented test cases.
They do not establish the absence of every possible defect.
Screenshot file verification checks file presence and PNG headers.
Visual content requires manual inspection.
