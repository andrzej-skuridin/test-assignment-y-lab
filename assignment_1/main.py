from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello!'}


# # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/menus/', response_model=list[schemas.Menu])
def get_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_menus(db, skip=skip, limit=limit)


@app.get('/menus/{menu_id}', response_model=schemas.Menu)
def get_menu(menu_id: int, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail='Menu not found')
    return db_menu


@app.get('/menus/{menu_id}/submenus/', response_model=list[schemas.Submenu])
def get_submenus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_submenus(db, skip=skip, limit=limit)


@app.get('/menus/{menu_id}/submenus/{submenu_id}', response_model=schemas.Submenu)
def get_submenu(submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = crud.get_submenu(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail='Submenu not found')
    return db_submenu


@app.post('/menus/{menu_id}/submenus/')
def create_submenu_for_menu(
    menu_id: int, 
    submenu: schemas.CreateSubmenu, 
    db: Session = Depends(get_db)
    ):
    return crud.create_submenu_for_menu(db=db, menu_id=menu_id, submenu=submenu)
