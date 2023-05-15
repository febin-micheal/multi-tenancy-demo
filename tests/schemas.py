from typing import List, Union

from pydantic import Field

# from pydantic import BaseModel

from utils.schemas import AbstractBaseModel


# class DetailBase(BaseModel):
#     name: str
#
#
# class DetailCreate(DetailBase):
#     pass
#
#
# class Detail(DetailBase):
#     id: int
#     code: str
#     description: Union[str, None] = None
#     header_id: int
#
#     class Config:
#         orm_mode = True
#
#
# class HeaderBase(BaseModel):
#     email: str
#
#
# class HeaderCreate(HeaderBase):
#     password: str
#
#
# class Header(HeaderBase):
#     id: int
#     is_active: bool
#     details: List[Detail] = []
#
#     class Config:
#         orm_mode = True


class TenantInfo(AbstractBaseModel):
    name: str
    db_schema: str = Field(alias="schema")
    host: str
