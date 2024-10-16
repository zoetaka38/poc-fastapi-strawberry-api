from __future__ import annotations

import logging
import uuid

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid6 import uuid7

from .base import Base

logger = logging.getLogger(__name__)


class OrganizationUser(Base):
    __tablename__ = "organizations_users"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)
    organization_id: Mapped[uuid.UUID] = mapped_column(
        "organization_id", UUID(as_uuid=True), ForeignKey("organization.id"), primary_key=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column("user_id", UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    active: Mapped[bool] = mapped_column("active", default=True, server_default="true")
    policies: Mapped[dict[str, str]] = mapped_column("policies", JSONB, nullable=True)


class AssigneeTaskUser(Base):
    __tablename__ = "assignee_tasks_users"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)
    task_id: Mapped[uuid.UUID] = mapped_column("task_id", UUID(as_uuid=True), ForeignKey("task.id"), primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column("user_id", UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
