"""
Kaggle için alternatif Agent kurulumu: 4096 boyutlu gömme ile.
"""
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.storage.sqlite import SqliteStorage
from agno.memory.sqlite import SqliteMemory as Memory

from app.config import OLLAMA_HOST, KAGGLE_KB_PATH, LANCEDB_URI, LANCEDB_TABLE

from app.tools.users import *  # noqa: F401,F403
from app.tools.invoices import *  # noqa: F401,F403
from app.tools.support_net import *  # noqa: F401,F403
from app.tools.addons import *  # noqa: F401,F403
from app.tools.superonline import *  # noqa: F401,F403
from app.tools.modem import *  # noqa: F401,F403
from app.tools.billing_payment import *  # noqa: F401,F403
from app.tools.usage_reco import *  # noqa: F401,F403
from app.tools.promo import *  # noqa: F401,F403
from app.tools.security import *  # noqa: F401,F403
from app.tools.outage import *  # noqa: F401,F403


def build_agent_kaggle(model_id: str = "llama3.1:8b", embedder_id: str = "nomic-embed-text", dimensions: int = 4096) -> Agent:
    llm = Ollama(id=model_id, host=OLLAMA_HOST)
    embeddings = OllamaEmbedder(id=embedder_id, dimensions=dimensions)
    kb = MarkdownKnowledgeBase(path=KAGGLE_KB_PATH)
    vectordb = LanceDb(uri=LANCEDB_URI, table_name=LANCEDB_TABLE, search_type=SearchType.hybrid, embedder=embeddings)
    storage = SqliteStorage()
    memory = Memory()

    tools = [obj for name, obj in globals().items() if getattr(obj, "__class__", None).__name__ == "Tool"]

    agent = Agent(
        model=llm,
        tools=tools,
        knowledge=kb,
        vectordb=vectordb,
        storage=storage,
        memory=memory,
        instructions=(
            "Türkçe konuş. Bilgi tabanını ve araçları gerektiğinde kullan."
        ),
    )
    return agent
