from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, relationship
from .base import Base


selected_resources = Table(
    "selected_resources",
    Base.metadata,
    Column("resource_id", Integer, ForeignKey("resources.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)


class Resource(Base):
    res_name: Mapped[str]
    id: Mapped[int]
    users = relationship(
        argument="User", secondary=selected_resources, back_populates="resources"
    )


class CategoryResource(Base):
    category_name: Mapped[str]
    resources = Column(
        "resources",
        ForeignKey("resources.id"),
        primary_key=True,
    )


class User(Base):
    username: Mapped[str]
    tg_id: Mapped[int]
    id: Mapped[UUID]
    resources = relationship(
        argument="Resource", secondary=selected_resources, back_populates="users"
    )
