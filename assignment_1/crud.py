from sqlalchemy.orm import Session
import models, schemas


def get_menus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Menu).offset(skip).limit(limit).all()


def get_menu(db: Session, menu_id: int):
    return db.get(entity=models.Menu, ident=menu_id) 


def get_submenus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Submenu).offset(skip).limit(limit).all()


def get_submenu(db: Session, submenu_id: int):
    return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()


def get_all_dishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dish).offset(skip).limit(limit).all()


def create_submenu_for_menu(db: Session, submenu: schemas.CreateSubmenu, menu_id: int):
    db_submenu = models.Submenu(**submenu.model_dump(), menu_id=menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def create_menu(db: Session, menu: schemas.CreateMenu):
    db_menu = models.Menu(**menu.model_dump())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def create_dish_for_submenu(db: Session, submenu_id: int, dish: schemas.CreateDish):
    db_dish = models.Dish(**dish.model_dump(), submenu_id=submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def delete_menu(db: Session, menu_id: int):
    db_menu = db.get(entity=models.Menu, ident=menu_id)
    db.delete(db_menu)
    db.commit()
    return {'menu_id': menu_id, 'status': 'deleted'}


def delete_submenu(db: Session, submenu_id: int):
    db_submenu = db.get(entity=models.Submenu, ident=submenu_id)
    db.delete(db_submenu)
    db.commit()
    return {'menu_id': submenu_id, 'status': 'deleted'}


def delete_dish(db: Session, dish_id: int):
    db_dish = db.get(entity=models.Dish, ident=dish_id)
    db.delete(db_dish)
    db.commit()
    return {'dish_id': dish_id, 'status': 'deleted'}