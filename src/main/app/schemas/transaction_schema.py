from pydantic import BaseModel
from typing import Optional

class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    description: Optional[str] = None

class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None