from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from backend.db import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    rating = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    is_active = Column(Boolean, default=True)
    supplier_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    category = relationship('Category', back_populates='products')
    