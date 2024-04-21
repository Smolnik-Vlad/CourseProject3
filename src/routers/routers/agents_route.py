from typing import Optional

from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import Response

from src.repositories.repositories.s3 import S3Client
from src.routers.depends.use_case_depends import get_agents_use_case
from src.use_case.agents_use_case import AgentsUseCase

agent_router = APIRouter()


@agent_router.get("/picture")
async def get_picture(
    name: Optional[str] = None,
    artist_name: Optional[str] = None,
    genre: Optional[str] = None,
    style: Optional[str] = None,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.get_picture(name, artist_name, genre, style)


@agent_router.get("/artist")
async def get_art_style(
    name: Optional[str] = None,
    picture_name: Optional[str] = None,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.get_artist(name, picture_name)


@agent_router.get("/art_style")
async def get_artist(
    name: Optional[str] = None,
    picture_name: Optional[str] = None,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.get_art_style(name, picture_name)


@agent_router.post(
    "/image",
)
async def post_image(file: UploadFile):
    s3 = S3Client()
    key = await s3.put_object('test', file.file.read())
    presigned = await s3.presign_obj(key)
    print(presigned)
    return {'key': key, 'presigned': presigned}


@agent_router.get("/picture/{picture_id}")
async def get_picture_by_id(
    picture_id: int,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.get_picture_by_id(picture_id)


@agent_router.get("/artist/{artist_id}")
async def get_artist_by_id(
    artist_id: int,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.get_artist_by_id(artist_id)


@agent_router.get("/art_style/{art_style_id}")
async def get_art_style_by_id(
    art_style_id: int,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.get_art_style_by_id(art_style_id)


@agent_router.post("/pictures/generate")
async def generate_picture_by_description(
    # data: dict[str, str],
    description: str,
    picture_name: str,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.generate_picture_by_description(
        description, picture_name
    )


@agent_router.post("/pictures/description/generate")
async def generate_description_by_picture(
    # data: dict[str, str],
    file: UploadFile,
    picture_name: str,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.generate_description_by_image(
        file.file.read(), picture_name
    )


@agent_router.get("/pictures/tags")
async def search_pictures_by_tags(
    description: str,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.search_pictures_by_tags(description)


@agent_router.get(
    "/generated_image_test",
    responses={200: {"content": {"image/jpg": {}}}},
    response_class=Response,
)
async def generate_picture_test(
    prompt: str, agent_use_case: AgentsUseCase = Depends(get_agents_use_case)
):
    image_bytes = await agent_use_case.generate_picture_test(prompt)
    return Response(content=image_bytes, media_type="image/jpg")


@agent_router.get("/tags/test")
async def get_tags_test(
    description: str,
    agent_use_case: AgentsUseCase = Depends(get_agents_use_case),
):
    return await agent_use_case.get_tags(description)
