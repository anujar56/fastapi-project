from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


# Create an instance of the FastAPI application
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Define a route for the root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# Define a list of posts as sample data
post : list[dict] = [
    {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the content of the third post."}
]

# Define a route for retrieving posts
@app.get("/posts")
def get_posts():
    return post 

@app.get("/",include_in_schema=False)
@app.get("/post",include_in_schema=False)
def get_post(request: Request):
    return templates.TemplateResponse(request,"home.html",{"posts": post})

