from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.core.exceptions import CustomBaseException
from src.routers.routers.agents_route import agent_router
from src.routers.routers.front_data_route import front_data_router

app = FastAPI()

@app.exception_handler(CustomBaseException)
async def custom_exception_handler(request, exc):
    error_class_name = exc.__class__.__name__
    error_detail = f"Custom error: {error_class_name}"
    return JSONResponse(status_code=exc.status_code, content={"detail": error_detail})


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_router, prefix='/agents', tags=['agents'])
app.include_router(front_data_router, prefix='/front-data', tags=['front-data'])
