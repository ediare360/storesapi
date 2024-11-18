from fastapi import APIRouter
from models.post import UserPost , UserPostIn, comment, CommentIn


router = APIRouter()

@router.get("/")
async def root():
    return{"message":"Hello world"}


post_table = {}

def find_post_id(post_id:int):
    return post_table.get(post_id)

@router.post("/", response_model=UserPostIn)
async def create_post(post:UserPost):
    data = post.model_dump()
    new_post_id = len(post_table)
    new_post =  {** data, "id":new_post_id}

    post_table[new_post_id] = new_post
    print(post_table)
    return new_post

@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())



@router.post("/", response_model=UserPostIn)
async def create_post(post:UserPost):
    data = post.model_dump()
    new_post_id = len(post_table)
    new_post =  {** data, "id":new_post_id}

    post_table[new_post_id] = new_post
    print(post_table)
    return new_post






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
