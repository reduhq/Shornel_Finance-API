from fastapi import APIRouter
from fastapi import Depends, Body


from shornel_finance_api.api.deps import get_db
from shornel_finance_api.crud import user_crud

router = APIRouter()

from pydantic import BaseModel
class a(BaseModel):
    name:str

@router.post(
    path="/",
    response_model=None
)
async def create(
    db =  Depends(get_db),
    user: a = Body(...)
):
    return await user_crud.create_user(db, user)
