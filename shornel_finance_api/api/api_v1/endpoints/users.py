from fastapi import APIRouter
from fastapi import Depends, Body

from shornel_finance_api import models, schemas
from shornel_finance_api.api.deps import get_db
from shornel_finance_api.crud import user_crud

router = APIRouter()


@router.post(
    path="/",
    response_model=None
)
async def create(
    db =  Depends(get_db),
    user: schemas.User = Body(...)
):
    return await user_crud.create_user(db, user)