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
