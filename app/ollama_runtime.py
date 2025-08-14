"""
Ollama kurulum/çalıştırma yardımcıları.
"""
import time
import subprocess
import requests

from app.config import OLLAMA_HOST


def install_ollama_once() -> None:
    """
    Colab/Linux ortamına özgü kurulum komutu. Windows'ta kullanmayın.
    """
    try:
        subprocess.run(["bash", "-lc", "curl -fsSL https://ollama.com/install.sh | sh"], check=False)
    except Exception:
        pass


def start_ollama_background() -> None:
    """
    Ollama arka planda başlatma (Linux/Colab için tipik).
    """
    try:
        subprocess.Popen(["bash", "-lc", "OLLAMA_HOST=0.0.0.0:11434 ollama serve &"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass


def wait_ollama_ready(timeout_sec: int = 120) -> bool:
    """
    OLLAMA_HOST /api/tags endpoint'i ile hazır olana kadar bekler.
    """
    t0 = time.time()
    while time.time() - t0 < timeout_sec:
        try:
            r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=3)
            if r.status_code == 200:
                return True
        except Exception:
            time.sleep(2)
    return False


def pull_models(models: list[str]) -> None:
    """
    Gerekli Ollama modellerini indirir (pull).
    """
    for m in models:
        try:
            requests.post(f"{OLLAMA_HOST}/api/pull", json={"name": m}, timeout=30)
        except Exception:
            pass
