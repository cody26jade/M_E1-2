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
