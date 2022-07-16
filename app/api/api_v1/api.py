from fastapi import APIRouter
from app.api.api_v1.endpoints import rules, copies

api_router = APIRouter()
api_router.include_router(copies.router, prefix="/copies", tags=["copies"])
api_router.include_router(rules.router, prefix="/rules", tags=["rules"])
