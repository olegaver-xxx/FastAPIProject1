from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, relationship
from .base import Base


class SelectedResource(Base):
    resource_id = Column(Integer, ForeignKey("resources.id"))
    user_id = Column(Integer, ForeignKey("users.id"))


# selected_resources = Table(
#     "selected_resources",
#     Base.metadata,
#     Column("resource_id", Integer, ForeignKey("resources.id")),
#     Column("user_id", Integer, ForeignKey("users.id")),
# )


class Resource(Base):
    res_name: Mapped[str]
    id: Mapped[int]
    users = relationship("SelectedResource", back_populates="resources")


class CategoryResource(Base):
    category_name: Mapped[str]
    resources = relationship(
        "Resources",
        back_populates="category",
    )


class User(Base):
    username: Mapped[str]
    tg_id: Mapped[int]
    id: Mapped[UUID]

    resources = relationship(
        "SelectedResource",
        back_populates="users",
    )
