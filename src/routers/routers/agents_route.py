from typing import Optional

from fastapi import APIRouter, Depends

from src.routers.depends.use_case_depends import get_agents_use_case
from src.use_case.agents_use_case import AgentsUseCase

agent_router = APIRouter()


@agent_router.get("/agent")
async def get_agent(agent_use_case: AgentsUseCase = Depends(get_agents_use_case)):
    return await agent_use_case.get_agents()

@agent_router.post("/new_data")
async def new_data(agent_use_case: AgentsUseCase = Depends(get_agents_use_case)):
    return await agent_use_case.check_enter()

@agent_router.get("/new_data")
async def new_data(agent_use_case: AgentsUseCase = Depends(get_agents_use_case)):
    return await agent_use_case.get_data_from_neo4j()

@agent_router.post("/new_data_2")
async def new_data_2(agent_use_case: AgentsUseCase = Depends(get_agents_use_case)):
    return await agent_use_case.create_new_data()

@agent_router.get("/picture")
async def get_picture(
        name: Optional[str] = None,
        artist_name: Optional[str] = None,
        genre: Optional[str] = None,
        style: Optional[str] = None,
        agent_use_case: AgentsUseCase = Depends(get_agents_use_case)
):
    return await agent_use_case.get_picture(name, artist_name, genre, style)

