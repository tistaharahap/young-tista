from fastapi import FastAPI

from young_tista.api.views import router

app = FastAPI(title="Young Tista API", version="0.1.0")

app.include_router(router)
