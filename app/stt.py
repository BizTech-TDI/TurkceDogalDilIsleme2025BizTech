"""
Speech-to-Text (Whisper) ve yardımcı fonksiyon.
"""
from transformers import pipeline

# Whisper STT 
stt = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")

def speech_to_text(audio_file: str) -> str:
    """
    Verilen ses dosyasını (path) Whisper ile metne dönüştürür.
    Zaman damgaları notebook'taki gibi etkin, dönüş değeri yalnızca metindir.
    """
    result = stt(audio_file, return_timestamps=True)
    return result["text"]
