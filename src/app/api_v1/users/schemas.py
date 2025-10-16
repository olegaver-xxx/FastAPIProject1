from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    tg_id: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
