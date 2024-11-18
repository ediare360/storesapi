from fastapi import FastAPI
from routers.post import router as post_router


app = FastAPI()

app.include_router(post_router)




# @app.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
# def create_post(post:schemas.PostCreate, db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
#     # new_post = post.model_dump()
#     # print(**post.model_dump())
#     # new_post =models.Post(title=post.title, content=post.content, published=post.published)
#     # print("pleasedddddddddddddddddddddddddddddd")
#     # print(user_id.id)
    
#     new_post = models.Post(own_id= user_id.id, **post.model_dump())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post
