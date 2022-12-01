from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from odmantic import AIOEngine

from young_tista.api.context import Context
from young_tista.api.models.mongo import Question
from young_tista.api.questions import Questions
from young_tista.api.shared import AIOEngineDependency

router = APIRouter()


@router.get(
    "/questions",
    description="Get all questions in the db",
    response_model=List[Question],
)
async def get_questions(
    skip: int = 0,
    limit: int = 10,
    engine: AIOEngine = Depends(AIOEngineDependency()),
    creds: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))
):
    async with Context.protected(engine=engine, access_token=creds):
        return await engine.find(Question, skip=skip, limit=limit, sort=Question.created_at.desc())


@router.post(
    "/questions",
    description="Ask a question to Young Tista",
    response_model=Question,
)
async def ask_question(
    q: str,
    temperature: float = 0.7,
    engine: AIOEngine = Depends(AIOEngineDependency()),
    creds: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))
):
    async with Context.protected(engine=engine, access_token=creds):
        return await Questions.ask_question(engine=engine, question=q, temperature=temperature)
