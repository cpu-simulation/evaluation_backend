from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class QueueMessage(BaseModel):
    team_id : UUID
    host: Optional[str]