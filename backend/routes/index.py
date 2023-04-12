from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from starlette.background import BackgroundTasks

from .admin import adminRouter
from .user import userRouter

router = APIRouter(prefix="/api")

router.include_router(adminRouter)
router.include_router(userRouter)

@router.get("/map")
async def map(request: Request):
    template_map = Jinja2Templates(directory="frontend/templates/map")
    return template_map.TemplateResponse("map.html", {"request": request})