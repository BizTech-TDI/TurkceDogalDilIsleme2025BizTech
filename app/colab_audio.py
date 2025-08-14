"""
Colab'a özgü ses kayıt yardımcıları. Lokal Windows'ta kullanılmaz.
"""

def record_audio(output_path: str = "input.wav", duration_s: int = 5) -> str:
    """
    Colab ipywidgets tabanlı kayıt akışının yerine tutucu bir fonksiyon.
    Gerçek Colab akışında ipywidgets, javascript ve google.colab.output kullanılır.
    Burada yalnızca hedef dosya yolunu döndürürüz.
    """
    return output_path
