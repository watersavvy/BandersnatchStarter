from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """Class which holds a MongoDB and collection of MonsterLab Monster Library Objects"""
    # database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection='monsters'):
        """Initializes the Database class with the specified collection.

        Args:
            collection (str): The name of the collection to work with, passed as string.
        """
        load_dotenv()
        self.database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Bandersnatch"]
        self.collection = self.database.get_collection("Monsters")

    def seed(self, amount: int):
        """ number of records to create, make a new empty list (append)"""

        if amount == 1:
            record = Monster().to_dict()
            return self.collection.insert_one(record).acknowledged
        if amount > 1:
            records = [Monster().to_dict() for i in range(amount)]
            #print(f"Successfully inserted {records} documents")
            return self.collection.insert_many(records).acknowledged

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
        return df.to_html()
