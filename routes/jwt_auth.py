from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# Resolve templates directory relative to project root
templates_dir = Path(__file__).resolve().parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

router = APIRouter(
    tags=["api"]
)

@router.get("/users/{user_id}")
def get_user(user_id: str):
    # accept numeric ids only to mirror main.user endpoints
    if not user_id.isdigit():
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": int(user_id)}

@router.get("/html")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )