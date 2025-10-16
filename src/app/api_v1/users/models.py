from app.core.db import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped


class User(Base):
    tg_id: Mapped[int]
    username: Mapped[str] = mapped_column(nullable=True)
