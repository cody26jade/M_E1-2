# Object-Oriented Design and Class Reusability

## 1. Purpose

This document explains why the Quiz and QuizGame
classes were selected for the Machine Tool and
Vibration Analysis Quiz application.

It addresses abstraction, encapsulation, reusability,
composition, maintainability, and testability.

## 2. Why Use Classes?

A class defines a reusable structure containing
related data and behavior.

Without classes, question data, answer validation,
game progress, and scoring could become scattered
across unrelated variables and functions.

Classes provide a consistent interface for managing
these responsibilities.

The application uses classes because multiple quiz
objects share the same structure and behavior,
while each object stores its own question data.

## 3. Quiz Class

Source: [quiz.py](../quiz.py)

The Quiz class represents an individual question.

Its data includes:

- Question identifier
- Question text
- Four answer choices
- Correct answer
- Difficulty
- Category
- Hint
- Explanation

Its behavior includes:

- Input and data validation
- Correct answer checking
- Hint retrieval
- Explanation retrieval
- Choice shuffling
- Dictionary serialization
- Object reconstruction from a dictionary

A single Quiz class can represent questions about
CNC machines, spindles, vibration, RMS, FFT,
bearing frequencies, and other engineering topics.

The question-specific data changes, but the shared
validation and answer-checking behavior is reused.

## 4. QuizGame Class

Source: [quiz_game.py](../quiz_game.py)

The QuizGame class manages the quiz collection
and the state of an individual game.

Its responsibilities include:

- Quiz collection management
- Duplicate question validation
- Question selection
- Randomized quiz sessions
- Game progress management
- Score calculation
- Best score management

QuizGame works with Quiz objects instead of
duplicating individual question validation logic.

The game logic is separated from the console
interface so that game behavior can be tested
without requiring manual keyboard input.

## 5. QuizStorage Class

Source: [storage.py](../storage.py)

The QuizStorage class is responsible for
persistent JSON data management.

Its responsibilities include:

- Loading saved state
- Saving quiz data and scores
- Validating stored data
- Recovering from supported invalid state cases
- Temporary-file-based state replacement

Separating persistence from game logic makes it
possible to test file handling independently.

## 6. Abstraction

Abstraction means providing a useful interface
while hiding unnecessary implementation details.

For example, Quiz.check_answer() allows callers
to check an answer without implementing the
answer comparison logic repeatedly.

QuizGame.start_game() provides an interface for
starting a quiz session without requiring the
console interface to reproduce the internal
question selection process.

QuizStorage.load() and QuizStorage.save() provide
interfaces for persistent state management.

The console interface can use these operations
without implementing JSON parsing itself.

## 7. Encapsulation

Encapsulation means organizing related data and
behavior within a class.

Quiz groups question data and answer validation.

QuizGame groups quiz collections and game state
with the operations that manage them.

QuizStorage groups persistence behavior with
the configuration of its storage path.

This organization improves consistency and
reduces the need for duplicated logic.

Python does not automatically make every class
attribute private. Encapsulation in this project
primarily concerns responsibility separation and
controlled operations rather than strict access
restrictions on every attribute.

## 8. Reusability

Reusability means using the same implementation
for multiple objects or application scenarios.

The default question bank contains twenty
different questions represented by the same
Quiz class.

Quiz.from_dict() reconstructs question objects
from structured data.

Quiz.to_dict() converts question objects back
into a serializable representation.

Quiz.check_answer() is reused for every question.

For example, CNC and FFT questions have different
text and answer choices, but both use the same
answer-checking method.

Adding a new engineering question does not require
creating a new class or rewriting the scoring
logic.

The same Quiz class can also be reused for
other subjects by supplying different data.

## 9. Composition and Separation of Responsibilities

Composition means constructing a larger system
using smaller objects with distinct responsibilities.

QuizGame manages a collection of Quiz objects.

The console interface coordinates user input,
game operations, and persistent storage.

QuizStorage handles JSON persistence separately
from question validation and game scoring.

This design avoids placing all application logic
inside a single large function or class.

## 10. Maintainability and Testability

The class structure supports independent tests
for question validation, game logic, and storage.

A change to console presentation does not
necessarily require a change to answer validation.

A change to storage implementation does not
necessarily require a change to scoring rules.

Tests can create independent Quiz and QuizGame
objects without changing the user's saved state.

Temporary storage paths can be used to test
persistence without modifying the real state.json.

This separation supports future maintenance
and controlled feature expansion.

## 11. Practical Reuse Example

The following example creates independent question
objects from the default question bank.

    import json
    from pathlib import Path
    from quiz import Quiz
    from quiz_game import QuizGame

    data = json.loads(
        Path("data/default_quizzes.json").read_text(
            encoding="utf-8"
        )
    )

    quizzes = [
        Quiz.from_dict(item)
        for item in data
    ]

    game = QuizGame(quizzes)

    for quiz in quizzes:
        assert quiz.check_answer(quiz.answer)

    assert len(game.list_quizzes()) == 20

The same Quiz class is reused for all twenty
questions.

This example uses the existing application
interfaces rather than a separate demonstration
implementation.

## 12. Why JSON Was Selected

JSON is a human-readable, structured data format.

It supports nested objects, arrays, strings,
numbers, booleans, and null values.

Python provides JSON support through its
standard-library json module.

UTF-8 encoding supports Korean question text
and other international characters.

JSON can be inspected with ordinary text editors
and processed by standard tools and programming
languages.

These characteristics make JSON appropriate
for a small, portable educational application.

For very large datasets or concurrent writers,
a database such as SQLite may provide more
efficient indexed access and transactional
updates.

## 13. Git Commit Message Convention

Meaningful commit messages describe the purpose
of each development change.

Recommended prefixes:

| Prefix | Purpose |
|---|---|
| Feat | Add a new feature |
| Fix | Correct a defect |
| Docs | Update documentation |
| Refactor | Improve internal code structure |
| Test | Add or improve automated tests |

Examples:

- Feat: Implement interactive quiz console
- Fix: Distinguish question and answer colors
- Docs: Add Git collaboration workflow guide
- Refactor: Simplify repeated validation logic
- Test: Verify exception handling

The Refactor example is illustrative and does
not claim that this exact commit exists.

Existing development history is preserved.

## 14. NEITO Evaluation Mapping

| Criterion | Evidence |
|---|---|
| 12 | Git commit message convention |
| 13 | Class abstraction and reusability |
| 14 | JSON readability and compatibility |

Criterion 13 is addressed explicitly by the
explanation of why Quiz and QuizGame are classes,
their abstraction benefits, and practical
examples of class reuse.

Actual execution records will be linked from
the consolidated evaluation evidence after
revision verification.
