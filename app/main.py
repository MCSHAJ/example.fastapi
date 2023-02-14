from fastapi import FastAPI, Response, status,HTTPException, Depends
#from fastapi.params import Body
#from typing import Optional, List
#from random import randrange
#from sqlalchemy.orm import Session
#from sqlalchemy.sql.functions import mode
from .import models, schemas, utils
from .database import engine, get_db
from pydantic import BaseSettings
from.config import Settings
from .routers import post, user, auth, vote



#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
#my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
 #{"title": "favorite foods", "content": "i like pizza", "id":2}]

#def find_post(id):
#    for p in my_posts:
#        if p["id"] == id:
 #           return p

#def find_index_post(id):
 #   for i, p in enumerate(my_posts):
 #       if p['id'] == id:
 #           return p


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello ruhama and rumaan, humza"}

#@app.get("/sqlalchemy")
#def test_posts(db: Session = Depends(get_db)):

   # posts = db.query(models.Post).all()
   # return {"status": posts}    

