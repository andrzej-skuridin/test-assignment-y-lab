from sqlalchemy.orm import Session
import models, schemas

# from models import Menu, Submenu, Dish


def get_menus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Menu).offset(skip).limit(limit).all()


def get_menu(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def get_submenus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Submenu).offset(skip).limit(limit).all()


def get_submenu(db: Session, submenu_id: int):
    return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()


def create_submenu_for_menu(db: Session, submenu: schemas.CreateSubmenu, menu_id: int):
    db_submenu = models.Submenu(**submenu.model_dump(), menu_id=menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu