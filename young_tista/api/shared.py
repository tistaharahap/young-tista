import asyncio
from os import environ

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from fastapi import Request


class AIOEngineDependency:
    def __init__(self):
        mongo_url = environ.get("MONGO_URL")
        client = AsyncIOMotorClient(mongo_url)

        # Monkey patched, here's why: https://twitter.com/tista/status/1595658624449257472
        client.get_io_loop = asyncio.get_running_loop

        self.engine = AIOEngine(
            client=client,
            database="young-tista"
        )

    async def __call__(self, request: Request) -> AIOEngine:
        return self.engine
