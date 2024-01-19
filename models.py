from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class AnalysisRecord(BaseModel):
    """
    A basic Pydantic model representing an analysis record.
    """
    user_id: str  # related to a user in the users collection
    tool_id: str  # related to a tool in the tools collection
    timestamp: datetime = Field(default_factory=datetime.now)
    # according to the use case a lot of other fields can be added like agent, ip, etc.


class AnalysisRecordResponse(BaseModel):
    """
    Pydantic BaseModel representing the response format for analysis records.
    """
    records: List[AnalysisRecord]
