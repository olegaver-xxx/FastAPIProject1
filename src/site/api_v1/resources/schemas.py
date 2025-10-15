from typing import List

from pydantic import BaseModel

# from src.site.api_v1.users.schemas import User


class ResourceBase(BaseModel):
    res_name: str


class ResourceCreate(ResourceBase):
    pass


class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True


# class ResourceSchema(Resource):
#     users: List[User]
