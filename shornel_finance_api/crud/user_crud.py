from pymongo.database import Database

async def create_user(db:Database, user):
    result = await db.Users.insert_one(user.dict())
    if result.inserted_id:
        return {"result": "Success"}
    else:
        return {"result": "Error"}