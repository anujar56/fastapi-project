from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Create an instance of the FastAPI application
app = FastAPI()

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


# Define a route for retrieving posts in HTML format
@app.get("/posts/html", response_class=HTMLResponse)
def get_posts_html():
    html_content = "<html><body><h1>Posts</h1><ul>"
    for p in post:
        html_content += f"<li><strong>{p['title']}</strong>: {p['content']}</li>"
    html_content += "</ul></body></html>"
    return HTMLResponse(content=html_content, status_code=200)

