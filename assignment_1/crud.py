from sqlalchemy.orm import Session

from models import Menu, Submenu, Dish


def get_menus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Menu).offset(skip).limit(limit).all()


def get_menu(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()


def get_submenus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Submenu).offset(skip).limit(limit).all()


def get_submenu(db: Session, submenu_id: int):
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()
