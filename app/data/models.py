"""
Data Layer Models
Represents Operational DB models and Data Lake schemas.
"""
from pydantic import BaseModel

class InsurerDataModel(BaseModel):
    id: str
    name: str
    claim_ratio: float
    solvency_ratio: float
