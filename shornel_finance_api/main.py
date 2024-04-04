from fastapi import FastAPI
from shornel_finance_api.api.api_v1.api import api_router
from shornel_finance_api.core.config import settings

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)