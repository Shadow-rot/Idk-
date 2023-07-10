__all__ = ['get_collection']


import asyncio
from motor import motor_asyncio
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection
from RoroRobot import MONGO_DB_URI as DB_URL

print("Connecting to Database ...")

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(DB_URL)
_RUN = asyncio.get_event_loop().run_until_complete

if "KaguyaMongo" in _RUN(_MGCLIENT.list_database_names()):
    print("KaguyaMongo Database Found :) => Now Logging to it...")
else:
    print("KaguyaMongo Database Not Found :( => Creating New Database...")

_DATABASE: AgnosticDatabase = _MGCLIENT["Kaguya"]


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
