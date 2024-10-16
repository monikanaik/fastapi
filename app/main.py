"""
This is the main module for the FastAPI application.
It sets up routing, templates, and static files.
"""

import os
import logging
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Create a logging configuration
logging.basicConfig(
    filename="app.log",  # Log file name
    level=logging.ERROR,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Create a logger instance
logger = logging.getLogger(__name__)

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


@app.on_event("startup")
async def startup_event():
    """Log startup event for testing"""
    logger.info("Application has started")


@app.on_event("shutdown")
async def shutdown_event():
    """Log shutdown event for testing"""
    logger.info("Application is shutting down")


@app.get("/")
async def read_root(request: Request):
    """
    First app for web development rendering template.
    """
    context = {
        "request": request,
        "title": "Welcome to FastAPI",
        "content": "Hello, FastAPI with Jinja2!",
    }
    return templates.TemplateResponse("home.html", context)
