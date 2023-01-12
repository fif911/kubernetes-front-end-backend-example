from app.db.base_class import Base
from sqlalchemy import Column, Integer, String


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
