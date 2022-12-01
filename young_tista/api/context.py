from contextlib import asynccontextmanager

from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from odmantic import AIOEngine

from young_tista.api.models.mongo import Token


class Context:
    @classmethod
    @asynccontextmanager
    async def protected(cls, engine: AIOEngine, access_token: HTTPAuthorizationCredentials):
        if not access_token:
            raise HTTPException(status_code=401, detail="Unauthorized")
        access_token = access_token.credentials

        query = {"token": access_token, "deleted_at": None}
        token = await engine.find_one(Token, query)
        if not token:
            raise HTTPException(status_code=401, detail="Unauthorized")

        yield
