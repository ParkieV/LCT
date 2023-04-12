from dotenv import load_dotenv
load_dotenv('backend/.env')
import grequests
from starlette.middleware.cors import CORSMiddleware
import logging
from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from .sql_app import models
from .sql_app.database import engine
from .routes.index import router

logging.basicConfig(format="%(asctime)s [%(name)s] - %(levelname)s: %(message)s", level=logging.INFO)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("/web", StaticFiles(directory=''), name="static")
app.mount("/static", StaticFiles(directory="c:/projects/lct2022_2/lct2022/frontend/static"), name="static")

logger = logging.getLogger(__name__)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "ok"}


# parser = Parser()
# parser.start()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

