"""
Colab için gelişmiş Agent kurulumu: Ollama LLM + OllamaEmbedder + Markdown KB + LanceDb + Memory + Storage.
Not: Çalıştırmadan önce ilgili dizinlerin mevcut olduğundan emin olun.
"""
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools import tool
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.storage.sqlite import SqliteStorage
from agno.memory.sqlite import SqliteMemory as Memory

from app.config import OLLAMA_HOST, COLAB_KB_PATH, LANCEDB_URI, LANCEDB_TABLE

# Tool'lar app.tools paketinden içe aktarılabilir
from app.tools.users import *  
from app.tools.invoices import *  
from app.tools.support_net import *  
from app.tools.addons import *  
from app.tools.superonline import *  
from app.tools.modem import *  
from app.tools.billing_payment import *  
from app.tools.usage_reco import *  
from app.tools.promo import *  
from app.tools.security import *  
from app.tools.outage import *  


def build_agent_colab(model_id: str = "llama3.1:8b", embedder_id: str = "bge-m3") -> Agent:
    llm = Ollama(id=model_id, host=OLLAMA_HOST)
    embeddings = OllamaEmbedder(id=embedder_id)
    kb = MarkdownKnowledgeBase(path=COLAB_KB_PATH)
    vectordb = LanceDb(uri=LANCEDB_URI, table_name=LANCEDB_TABLE, search_type=SearchType.hybrid, embedder=embeddings)
    storage = SqliteStorage()
    memory = Memory()

    # Tüm @tool fonksiyonları otomatik toplanabilir; burada açık tutuyoruz
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
