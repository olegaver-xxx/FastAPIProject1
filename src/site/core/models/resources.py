from sqlalchemy.orm import Mapped, relationship

from .base import Base


class Resource(Base):
    res_name: Mapped[str]
    id: Mapped[int]


class CategoryResource(Base):
    category_name: Mapped[str]
    resources = relationship(
        "Resource",
        back_populates="category",
    )
