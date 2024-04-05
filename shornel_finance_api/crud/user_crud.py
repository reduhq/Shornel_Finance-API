from pymongo.database import Database

from shornel_finance_api.core.security import get_password_hash, verify_password

async def create_user(db:Database, user):
    new_user = user.dict()
    new_user['password'] = get_password_hash(user.password)
    result = await db.Users.insert_one(new_user)
    
    if result.inserted_id:
        return {"result": "Success"}
    else:
        return {"result": "Error"}
    
async def authenticate( db, username:str, password:str):
    user = await db.Users.find_one({"username": username})
    if not user:
        return None
    if not verify_password(password, user['password']):
        return None
    return user
    # user = [user async for user in db.Users.find_one({"username": username})]
    # print(user)
    # if not user:
    #     return None
    # if not verify_password(password, user.password):
    #     return None
    # return user