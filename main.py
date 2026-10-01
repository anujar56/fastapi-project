from fastapi import FastAPI, Request,HTTPException,status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

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

#app is the FastAPI application object. 
#.get means the HTTP method is GET. GET is the normal method used when you type a URL into your browser.
@app.get("/")
#request: Request means the function receives a Request object.
#This object contains information about the incoming request: headers, cookies, method, etc. FastAPI automatically provides it.
async def home(request: Request):
    # Pass the request and posts to the template
    #Request object: contains details about the incoming HTTP request.
    return templates.TemplateResponse(
        request,    
        "home.html",
        {"title": home, "posts": posts}
        #A dictionary {"post": post, "title": title} — this is the context.It passes variables into the template so the HTML can use them.
    )
@app.get("/posts/{post_id}")
def get_post(request: Request,post_id: int):

    for post in posts:
        if post.get("id") == post_id:
            #TemplateResponse tells FastAPI to render an HTML template file.
            return templates.TemplateResponse(request,"posts.html",{"post": post} )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.get("/api/posts")
def api_post():
    return posts

@app.get("/api/posts/{post_id}")
def api_get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post 
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")

@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message},
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code,
    )


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )



