"""
Konfigürasyon sabitleri. 
"""

# Ollama
OLLAMA_HOST = "http://127.0.0.1:11434"

# Vektör DB ve depolama yolları
TMP_DB_FILE = "tmp/agent.db"
LANCEDB_URI = "tmp/lancedb"
LANCEDB_TABLE = "agno_docs"

# Bilgi tabanı yolları (iki alternatif ortam)
COLAB_KB_PATH = "/content/senaryolar"
KAGGLE_KB_PATH = "/kaggle/input/senaryolar/senaryolar"
