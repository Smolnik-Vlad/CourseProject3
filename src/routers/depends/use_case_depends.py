from fastapi import Depends

from src.repositorise.repository import KnowledgeBaseRepository
from src.repositorise.sessions import get_session_knowledge_base
from src.use_case.agents_use_case import AgentsUseCase


def get_knowledgebase_rep():
    return KnowledgeBaseRepository(session=Depends(get_session_knowledge_base))


def get_agents_use_case(knowledgebase_rep: KnowledgeBaseRepository = Depends(get_knowledgebase_rep)) -> AgentsUseCase:
    return AgentsUseCase(knowledgebase_rep)
