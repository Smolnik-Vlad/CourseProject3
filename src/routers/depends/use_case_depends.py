from fastapi import Depends

from src.repositories.repository import KnowledgeBaseRepository
from src.repositories.sessions import session_knowledge_base
from src.use_case.agents_use_case import AgentsUseCase
from src.use_case.data_front_use_case import DataFrontUseCase

# def get_session_knowledge_base():
#     return session_knowledge_base


def get_knowledgebase_rep(session=Depends(session_knowledge_base)):
    return KnowledgeBaseRepository(session)


def get_agents_use_case(
    knowledgebase_rep: KnowledgeBaseRepository = Depends(
        get_knowledgebase_rep
    ),
) -> AgentsUseCase:
    return AgentsUseCase(knowledgebase_rep)


def get_front_data_use_case(
    knowledgebase_rep: KnowledgeBaseRepository = Depends(
        get_knowledgebase_rep
    ),
) -> DataFrontUseCase:
    return DataFrontUseCase(knowledgebase_rep)
