from typing import List

from pydantic import BaseModel, ConfigDict

# from site.api_v1.resources.schemas import Resource


class UserBase(BaseModel):
    username: str
    tg_id: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    # resources_ids: List[int]


# class UserSchema(User):
#     resources: List[Resource]
