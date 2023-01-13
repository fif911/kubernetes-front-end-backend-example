from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    checked = Column(Boolean, )
