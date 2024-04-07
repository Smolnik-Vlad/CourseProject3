from fastapi import APIRouter

from src.use_case.agents_use_case import AgentsUseCase


agent_router = APIRouter()


@agent_router.get("/agent")
async def get_agent():
    return await AgentsUseCase.get_agents()

# @agent_router.post("/new_data")
# async def new_data(agent_use_case: AgentsUseCase = Depends(get_agents_use_case)):
#     return await agent_use_case.check_enter()
#
@agent_router.get("/new_data")
async def new_data():
    return await AgentsUseCase.get_data_from_neo4j()
#
# @agent_router.post("/new_data_2")
# async def new_data_2(agent_use_case: AgentsUseCase = Depends(get_agents_use_case)):
#     return await agent_use_case.create_new_data()
