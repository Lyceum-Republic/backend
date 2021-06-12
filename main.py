from fastapi import FastAPI, Request, HTTPException
from data.db_data.db_initialize import create_session, global_init
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    global_init('db/database.sqlite')


