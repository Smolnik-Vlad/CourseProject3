from fastapi import Depends

from src.repositories.repository import KnowledgeBaseRepository
from src.repositories.sessions import async_session_maker
from src.use_case.agents_use_case import AgentsUseCase

# def get_session_knowledge_base():
#     return session_knowledge_base


def get_knowledgebase_rep(session=Depends(async_session_maker)):
    return KnowledgeBaseRepository(session)


def get_agents_use_case(knowledgebase_rep: KnowledgeBaseRepository = Depends(get_knowledgebase_rep)) -> AgentsUseCase:
    return AgentsUseCase(knowledgebase_rep)
