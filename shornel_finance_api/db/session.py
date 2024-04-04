from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://root:example@mongo:27017/")
db = client["ShornelFinanceDB"]