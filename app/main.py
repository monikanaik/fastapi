from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), "templates")
)

# Serve static files like CSS, images, etc.
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")),
    name="static",
)


@app.get("/")
async def read_root(request: Request):
    # You can pass variables to the template in the `context` dict
    context = {
        "request": request,
        "title": "Welcome to FastAPI",
        "content": "Hello, FastAPI with Jinja2!",
    }
    return templates.TemplateResponse("home.html", context)
