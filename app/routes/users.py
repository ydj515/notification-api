from fastapi import APIRouter
from starlette.requests import Request

from app.database.schema import Users
from app.errors.exceptions import NotFoundUserEx
from app.models import UserMe

router = APIRouter()


@router.get("/me", response_model=UserMe)
async def get_user(request: Request):
# async def get_user(request: Request, session: Session = Depends(db.session)):
    """
    get my info
    :param request:
    :return:
    """
    user = request.state.user
    # user_info = Users.get(id=user.id)
    
    user_info = Users.filter(id__gt=user.id).order_by("-email").all() # 내림차순
    # user_info = session.query(Users).filter(Users.id > user.id).order_by(Users.email.asc()).count() # session을 유지하려면. 근데 여기선 굳이 간단한 인증이라 session을 check 할 필요가 없어서 사용 x
    return user_info