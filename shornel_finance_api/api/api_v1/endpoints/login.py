from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from shornel_finance_api.api.deps import get_db
from shornel_finance_api.crud.user_crud import(
    authenticate
)

router = APIRouter()

@router.post(
    path="/login/access-token"
)
async def login(
    db = Depends(get_db),
    form_data:OAuth2PasswordRequestForm = Depends()
):
    await authenticate(db, form_data.username, form_data.password)