"""
Text-to-Speech (VITS) kurulum ve kullanım yardımcıları.
"""
import torch
import soundfile as sf
from transformers import VitsModel, AutoTokenizer

# Model kimliği (notebook'ta kullanılan Türkçe TTS modeli)
TTS_MODEL_ID = "facebook/mms-tts-tur"

# Cihaz seçimi: CUDA varsa kullan
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model ve tokenizer tek seferlik yükleme
_tokenizer = AutoTokenizer.from_pretrained(TTS_MODEL_ID)
_model = VitsModel.from_pretrained(TTS_MODEL_ID).to(_device)


def text_to_speech(text: str, output_path: str = "output.wav", sample_rate: int = 22050) -> str:
    """
    Verilen metni .wav dosyası olarak kaydeder ve dosya yolunu döndürür.
    """
    inputs = _tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        audio = _model(**{k: v.to(_device) for k, v in inputs.items()}).waveform.cpu().numpy()[0]
    sf.write(output_path, audio, sample_rate)
    return output_path
