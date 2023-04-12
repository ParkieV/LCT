from fastapi import APIRouter, Depends, Response, HTTPException, Request, Path
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .. import service
from ..sql_app import schemas
from ..sql_app.crud import create_register_request, authenticate_user,\
    get_user_by_email, get_register_request_by_email
from ..sql_app.database import get_db
from ..utils.workWithFile import get_flats_from_excel_file, save_file, update_file

userRouter = APIRouter(prefix="/user",
                       tags=["user"])


@userRouter.get("/register")
async def register(request: Request, detail: str = None):
    templates_reg = Jinja2Templates(directory='frontend/templates/registration')
    return templates_reg.TemplateResponse("registration.html", {"request": request})


@userRouter.post("/register", status_code=204, response_class=Response)
async def register(register_request: schemas.RegisterUserRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, register_request.email)
    if user:
        raise HTTPException(status_code=400, detail="Пользователь с такой почтой уже существует")
    request = get_register_request_by_email(db, register_request.email)
    if request:
        raise HTTPException(status_code=400, detail="Ваш запрос уже существует")
    create_register_request(db, register_request)
    return HTTPException(status_code=200, detail="success!")


@userRouter.get("/login")
async def login(request: Request, detail: str = None):
    templates_auth = Jinja2Templates(directory='frontend/templates/authification')
    return templates_auth.TemplateResponse("auth.html", {"request": request})


@userRouter.post("/login", response_model=schemas.User)
async def login(login_request: schemas.LoginUserRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_request)
    if not user:
        raise HTTPException(status_code=400, detail="Почта или пароль некорректны")
    return user


@userRouter.post("/uploadFile", response_model=list[schemas.Flat])
async def create_upload_file(create_file_request: schemas.UploadFileRequest):
    flats = await get_flats_from_excel_file(create_file_request.file)
    await save_file(create_file_request.file, f'flats/{create_file_request.user.name}/{create_file_request.file.filename}')
    return flats


@userRouter.post("/getAnalogs")
async def get_analogs(base_flats: dict[int, schemas.Flat]):
    print(base_flats)
    for flat in base_flats:
        base_flats[flat] = dict(base_flats[flat])
    analogs = service.find_analogs(base_flats)
    return analogs


@userRouter.get("/calculateCost")
async def calculate_cost(calculate_request: schemas.CalculateCostRequest):
    flats = service.calculate_cost(calculate_request.flats, calculate_request.base_flats)
    return flats


@userRouter.post("/downloadFile")
async def download_file(flat_request: schemas.FlatRequest):
    await update_file(flat_request)
    return FileResponse('files/' + flat_request.filename)


@userRouter.get("/{user_id}")
async def profile(request: Request, user_id: str = Path(min_length=3, max_length=20), detail: str = None):
    templates_profile = Jinja2Templates(directory="frontend/templates/users_prof")
    return templates_profile.TemplateResponse("users_personal_account.html", {"request": request})

