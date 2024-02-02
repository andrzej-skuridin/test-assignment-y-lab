# Serializers

from pydantic import BaseModel


class Dish(BaseModel):
    id: int
    title: str
    submenu_id: int
    # price: float
    description: str

    class Config:
        orm_mode = True


class Submenu(BaseModel):
    id: int
    title: str
    menu_id: int
    dishes: list[Dish] = []

    class Config:
        orm_mode = True


class CreateSubmenu(BaseModel):
    id: int
    title: str


    class Config:
        orm_mode = True


class Menu(BaseModel):
    id: int
    title: str
    submenus: list[Submenu] = []

    class Config:
        orm_mode = True

