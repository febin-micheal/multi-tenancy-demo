from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from utils.models import Base


# class Header(Base):
#     name = Column(String, index=True)
#
#     details = relationship("Detail", back_populates="header")
#
#
# class Detail(Base):
#
#     code = Column(String, index=True)
#     description = Column(String, index=True)
#     header_id = Column(Integer, ForeignKey("header.id"))
#
#     header = relationship("Header", back_populates="details")
#

class Tenant(Base):

    # __tablename__ = "tenants"

    name = Column(String, nullable=False, unique=True)
    schema = Column(String, nullable=False, unique=True)
    host = Column(String, nullable=False, unique=True)

    __table_args__ = ({"schema": "shared"},)


class Item(Base):

    name = Column(String, nullable=False, unique=True)

    # __table_args__ = ({"schema": "tenant"},)


class Product(Base):

    name = Column(String, nullable=False, unique=True)

    # __table_args__ = ({"schema": "tenant"},)


class Bottle(Base):

    name = Column(String, nullable=False, unique=True)

    # __tab
