from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class CreateUser(BaseModel):
    id: int
    username: Annotated[str, MinLen(6), MaxLen(32)]
    password: Annotated[str, MinLen(8), MaxLen(16)]
