from fastapi import APIRouter

from .user_api import *
from .pareto_api import *
from .testing_api import *

api_router = APIRouter()

api_router.include_router(user_api.router, prefix='/user', tags=['Data Transaksi'])
api_router.include_router(pareto_api.router, prefix='/pareto', tags=['Pareto Per Item'])
api_router.include_router(testing_api.router, prefix='/testing', tags=['Transaksi Item'])