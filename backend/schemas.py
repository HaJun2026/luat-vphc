from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ViolationResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    category: str
    min_fine: int
    max_fine: int
    legal_basis: Optional[str] = None
    additional_penalty: Optional[str] = None
    remedial_measure: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class ViolationListResponse(BaseModel):
    items: list[ViolationResponse]
    total: int
    page: int
    limit: int
