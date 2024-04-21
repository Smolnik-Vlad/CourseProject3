from fastapi import APIRouter, Depends

from src.routers.depends.use_case_depends import get_front_data_use_case
from src.use_case.data_front_use_case import DataFrontUseCase

front_data_router = APIRouter()


@front_data_router.get('/features')
async def get_features(
    dark_theme: bool = False,
    data_front_use_case: DataFrontUseCase = Depends(get_front_data_use_case),
):
    return await data_front_use_case.get_front_features(dark_theme)
