from __future__ import annotations

from datetime import datetime

from odmantic import Model, Field


class Question(Model):
    question: str
    answer: str
    gpt_response: dict

    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)

    class Config:
        collection = "questions"


class Token(Model):
    token: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None

    class Config:
        collection = "tokens"
