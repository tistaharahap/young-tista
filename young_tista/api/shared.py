from os import environ

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from fastapi import Request


class AIOEngineDependency:
    def __init__(self):
        mongo_url = environ.get("MONGO_URL")
        client = AsyncIOMotorClient(mongo_url)
        self.engine = AIOEngine(
            client=client,
            database="young-tista"
        )

    async def __call__(self, request: Request) -> AIOEngine:
        return self.engine
