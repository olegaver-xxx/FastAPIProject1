from pydantic import BaseModel


class ResourceBase(BaseModel):
    name: str


class ResourceCreate(ResourceBase):
    pass


class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True
