from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
@app.get('/blog') # write like /blog?limit=50 as a query
def index(limit=10, published:bool=True, sort: Optional[str] = None):
    #Only get given amt published blogs (Default=10)
    if published:
        return {'data': f"{limit} blogs"}
    else:
        return {'data': f"{limit} from the DB"}

@app.get('/blog/{id}') #Dynamic Route
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}
#Schema for REQ(BELOW):
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
##REQ__BODY
@app.post('/blog')
def Create_blog(blog:Blog):
    return {'data':f"Blog is Created with title as {blog.title}"}