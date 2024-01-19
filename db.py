from motor.motor_asyncio import AsyncIOMotorClient


class MongoDB:
    """
    MongoDB class for handling interactions with the database.
    """

    def __init__(self, database_url: str, database_name: str, collection_name: str):
        """
        Initializes the MongoDB client and sets the database and collection.
        Args:
            database_url (str): MongoDB server URL.
            database_name (str): Name of the database.
            collection_name (str): Name of the collection.
        """
        self.client = AsyncIOMotorClient(database_url)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    async def insert_record(self, record_data: dict):
        """
        Inserts a record into the MongoDB collection.
        Args:
            record_data (dict): Data to be inserted as a record.
        Returns:
            str: Inserted record's ID.
        """
        result = await self.collection.insert_one(record_data)
        return str(result.inserted_id)

    async def get_all_records(self, skip: int = 0, limit: int = 10):
        """
        Retrieves paginated records from the MongoDB collection, sorted by timestamp in descending order.
        Args:
            skip (int): Number of records to skip (pagination offset).
            limit (int): Number of records to retrieve per page.
        Returns:
            List[dict]: List of paginated records.
        """
        records = await self.collection.find().sort("timestamp", -1).skip(skip).limit(limit).to_list(length=None)
        return records
