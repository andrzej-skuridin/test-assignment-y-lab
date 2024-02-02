from pydantic import BaseModel


class Menu(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class Submenu(BaseModel):
    id: int
    title: str
    menu_id: int

    class Config:
        orm_mode = True


class Dish(BaseModel):
    id: int
    title: str
    submenu_id: int
    price: float
    description: str

    class Config:
        orm_mode = True
