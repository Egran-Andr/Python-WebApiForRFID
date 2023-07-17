from fastapi import APIRouter
from apis.version1 import route_general_pages
from apis.version1 import route_users
from apis.version1 import route_userworkplace
from apis.version1 import route_workplace
from apis.version1 import route_genders
from apis.version1 import route_balance

api_router = APIRouter()
api_router.include_router(route_users.router,prefix="/users",tags=["users"])
api_router.include_router(route_workplace.router,prefix="/workplace",tags=["workplace"])
api_router.include_router(route_userworkplace.router,prefix="/userworkpace",tags=["userworkpace"])
api_router.include_router(route_genders.router,prefix="/gender",tags=["gender"])
api_router.include_router(route_balance.router,prefix="/balance",tags=["balance"])