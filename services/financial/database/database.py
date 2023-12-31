from os import getenv
import motor.motor_asyncio
from os import getenv

client = motor.motor_asyncio.AsyncIOMotorClient(
    f'mongodb+srv://{getenv("MONGO_USERNAME")}:{getenv("MONGO_PASSWORD")}@{getenv("MONGO_HOSTNAME")}/?retryWrites=true&w=majority',
    getenv("MONGO_PORT", default=27017)
)


db = client[getenv("FINANCIAL_ADVISOR_SERVICE_MONGO_DATABASE_NAME")]
