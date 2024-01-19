from typing import Optional

from fastapi import FastAPI

from db import MongoDB
from models import AnalysisRecord, AnalysisRecordResponse

# Create a FastAPI app instance
app = FastAPI()

mongo = MongoDB(database_url="mongodb://localhost:27017/",  # DB url should be placed in .env file
                database_name="mindlab", collection_name="analysis_records")


# A token-based authentication should be added to all endpoints
@app.post("/records/")
async def submit_record(record: AnalysisRecord):
    """
    Endpoint to submit an analysis record.
    Args:
        record (AnalysisRecord): Analysis record data.
    Returns:
        dict: Response message and record ID.
    """
    record_dict = record.model_dump()
    record_id = await mongo.insert_record(record_dict)
    return {"message": "Record submitted successfully", "record_id": record_id}


@app.get("/records/", response_model=AnalysisRecordResponse)
async def get_records(skip: Optional[int] = 0, limit: Optional[int] = 10):
    """
    Endpoint to retrieve paginated analysis records sorted by timestamp in descending order.
    Args:
        skip (int): Number of records to skip (pagination offset).
        limit (int): Number of records to retrieve per page.
    Returns:
        dict: Response containing a list of paginated records.
    """
    records = await mongo.get_all_records(skip=skip, limit=limit)
    return {"records": records}
