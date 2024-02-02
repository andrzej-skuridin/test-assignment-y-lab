from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    submenus = relationship('Submenu', back_populates='menu')


class Submenu(Base):
    __tablename__ = 'submenus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    dishes = relationship('Dish', back_populates='submenu')


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    submenu_id = Column(Integer, ForeignKey('submenus.id'))
    price = Column(Float, precision=2)
    description = Column(String)
