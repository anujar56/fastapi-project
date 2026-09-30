from fastapi import FastAPI, Request,HTTPException,status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tell FastAPI where Jinja2 templates live
templates = Jinja2Templates(directory="templates")

# Your post data
posts: list[dict] = [
    {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the content of the third post."},
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Pass the request and posts to the template
    return templates.TemplateResponse(
        request,    
        "home.html",
        {"title": home, "posts": posts}
    )
@app.get("/posts/{post_id}")
def get_post(request: Request,post_id: int):

    for post in posts:
        if post.get("id") == post_id:
            return templates.TemplateResponse(request,"posts.html",{"post": post} )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

