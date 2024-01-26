from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class MongoDB:

    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        """Initializes the Database class with the specified collection.

        Args:
            collection (str): The name of the collection to work with, passed as string.
        """
        self.collection = self.database[collection]

    def seed(self, amount):

        # make a new empty list (append)
        self.collection.insert_many(
            [Monster().to_dict() for i in range(amount)])

        return f"Successfully inserted {amount} documents"

    def reset(self):
        """
        Erase all records in the collection
        """
        return {"Collection reset successfully": f"{self.collection.delete_many(filter={}).acknowledged}"}

    def count(self) -> int:
        """
        Return the number of records in the collection.
        """
        return self.collection.count_documents(filter={})

    def dataframe(self) -> DataFrame:
        """
        Return a DataFrame containing all records in the collection
        """

        return DataFrame(self.collection.find(dict(), {"_id": False}))

    def html_table(self) -> str:
        """
        Return an HTML table containing all records in the collection
        """
        df = self.dataframe()
        return df.html
