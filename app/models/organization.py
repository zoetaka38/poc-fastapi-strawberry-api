from __future__ import annotations

import logging
import uuid
from datetime import datetime, timedelta, timezone
from typing import AsyncIterator, List, Optional

from sqlalchemy import Column, String, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from uuid6 import uuid7

from .base import Base  # noqa: E402
from .base_model import BaseModel  # noqa: E402
from .m2m_mapping import OrganizationUser  # noqa: E402


class Organization(Base):
    __tablename__ = "organization"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)
    name: Mapped[str] = mapped_column("name", String(length=100), nullable=False, unique=False)

    users: Mapped[list[User]] = relationship(
        "User",
        back_populates="organizations",
        secondary=OrganizationUser.__tablename__,
    )


from .user import User  # noqa: E402
