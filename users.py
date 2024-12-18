
from typing import Optional
from sqlmodel import Field
from datetime import datetime
from fastsqlmodel.db import BaseTable

class User(BaseTable, table=True):
    name: Optional[str] = Field(nullable=True)
    email: str = Field(nullable=False)
    password: str = Field(nullable=False)
    joined_at: datetime = Field(nullable=False)
