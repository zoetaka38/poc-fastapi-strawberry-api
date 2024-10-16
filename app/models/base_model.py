from datetime import datetime

from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    created_at: datetime | None
    updated_at: datetime | None
    deleted_at: datetime | None
