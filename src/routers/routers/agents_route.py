from fastapi import APIRouter, Depends

from src.routers.depends.use_case_depends import get_agents_use_case
from src.use_case.agents_use_case import AgentsUseCase

agent_router = APIRouter()


@agent_router.get("/agent")
async def get_agent(agent_use_case: AgentsUseCase = Depends(get_agents_use_case)):
    return await agent_use_case.get_agents()
