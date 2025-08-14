# TEKNOFEST 2025 Türkçe Doğal Dil İşleme Yarışması Projesi - Senaryo Kategorisi #BilisimVadisi2025 @turkiyeacikkaynakplatformu

Bu repo iki farklı çalışma biçimi sunar:

- Notebook ile tek dosyada deneyim: `teknofest.ipynb`
- Modüler Python uygulaması: `app/` klasörü üzerinden

İsteyen tüm kodu notebook içinde çalıştırabilir, isteyen de modüler hale getirilmiş sürümü doğrudan komut satırından başlatabilir.

---

## İçindekiler
- Proje Özeti
- Klasör Yapısı
- Kurulum (Windows odaklı)
- Notebook ile Çalıştırma
- Modüler Uygulama ile Çalıştırma
- Sesli Sohbet Akışı
- Ollama ve Modeller
- Yapılandırma (config)
- Mock Veri ve Araçlar (Tools)
- Gereksinimler
- Sorun Giderme

---

## Proje Özeti
Bu proje, Türkçe konuşabilen bir yapay zeka ajanı (Agent) ile müşteri destek senaryolarını simüle eder. Ajan, yerel LLM (Ollama) ve çeşitli yardımcı araçlarla (fatura, arıza, modem, kampanya vb.) entegre çalışır. Sistem mock (sahte/veri simülasyonu) modunda çalışır ve gerçek servisler yerine `app/data_stores.py` içindeki veri depolarını kullanır.

- Ajan kurulumları: `app/agent_setup.py`, `app/agent_setup_colab.py`, `app/agent_setup_kaggle.py`
- Giriş noktası (modüler): `app/main.py`
- Ses tanıma (STT): `app/stt.py` (Whisper)
- Metin okuma (TTS): `app/tts.py` (VITS)
- Ollama yardımcıları: `app/ollama_runtime.py`
- Konfigürasyon: `app/config.py`

---

## Klasör Yapısı
```
.
├─ app/
│  ├─ tools/                 # Mock araçlar (users, invoices, support_net, modem, vb.)
│  ├─ __init__.py
│  ├─ agent_setup.py         # Basit ajan kurulumu (Ollama + araçlar)
│  ├─ agent_setup_colab.py   # Colab için gelişmiş ajan
│  ├─ agent_setup_kaggle.py  # Kaggle için alternatif ajan
│  ├─ colab_audio.py         # Colab ses yardımcıları (yerelde placeholder)
│  ├─ config.py              # Konfigürasyon sabitleri
│  ├─ data_stores.py         # Mock veri depoları
│  ├─ evaluation.py          # Basit değerlendirme yardımcıları
│  ├─ main.py                # Modüler uygulama giriş noktası
│  ├─ ollama_runtime.py      # Ollama başlatma/çekme yardımcıları (Linux/Colab odaklı)
│  ├─ stt.py                 # Whisper tabanlı STT
│  └─ tts.py                 # VITS tabanlı TTS
├─ senaryolar/               # Bilgi tabanı (Markdown), Colab/Kaggle senaryoları için
├─ tmp/                      # Geçici DB ve LanceDB dosyaları
├─ teknofest.ipynb           # Tüm akışı notebook içinde deneyimlemek için
├─ requirements.txt
└─ README.md
```

---

## Kurulum (Windows)
1) Python kurulumu
- Python 3.10+ önerilir.
- Sanal ortam önerilir (örn. `python -m venv .venv` ve `./.venv/Scripts/activate`).

2) Bağımlılıkların yüklenmesi
```bash
pip install -r requirements.txt
```

3) (İsteğe bağlı) GPU hızlandırma
- Mevcut CUDA uyumlu PyTorch tekerini kullanmak için PyTorch resmi yönergelerini izleyin.

4) Ses dosyaları için
- `soundfile` paketi tekeri Windows için libsndfile içerir; ek adım gerekmemesi beklenir.

---

## Notebook ile Çalıştırma
- `teknofest.ipynb` dosyasını açın ve baştan sona çalıştırın.
- Colab/Kaggle ortamlarında gelişmiş ajan senaryoları için `app/agent_setup_colab.py` ve `app/agent_setup_kaggle.py` dosyalarındaki ayarlar kullanılır. Bilgi tabanı ve LanceDB yolları `app/config.py` içinde tanımlıdır.

---

## Modüler Uygulama ile Çalıştırma
Temel duman testi ve araç çağrıları:
```bash
python app/main.py
```
Sesli sohbet (tek sefer):
```bash
python app/main.py voice <girdi_wav_yolu> [cikti_wav_yolu] [model_id]
# Örnek:
python app/main.py voice input.wav agent_reply.wav llama3.1:8b
```
Bu akış `voice_chat_once()` fonksiyonunu çağırır: STT -> Agent -> TTS. Bkz. `app/main.py`.

---

## Sesli Sohbet Akışı
- STT: `app/stt.py` Whisper `openai/whisper-large-v3` modeliyle çalışır.
- Agent: `app/agent_setup.py` içindeki `build_agent()` fonksiyonu ile Ollama üzerinden model çağrılır.
- TTS: `app/tts.py` VITS tabanlı `facebook/mms-tts-tur` modeliyle WAV üretir.

Girdi sesinizin yolu `voice_chat_once()` fonksiyonuna verilir; çıktı `agent_reply.wav` varsayılanıyla kaydedilir.

---

## Ollama ve Modeller
Yerel LLM için Ollama gereklidir.

- Ollama kurulumu (Windows için resmi yönergelere bakınız) ve servis başlatma.
- `app/config.py` içinde `OLLAMA_HOST` varsayılanı: `http://127.0.0.1:11434`
- Önerilen model: `llama3.1:8b`
- Gelişmiş kullanımda embedder: `bge-m3` (Colab) veya `nomic-embed-text` (Kaggle, 4096 boyut)

Model çekme (Ollama API veya CLI):
```bash
ollama pull llama3.1:8b
# (Gelişmiş) Embedding modelleri, ortamınıza göre:
ollama pull bge-m3
ollama pull nomic-embed-text
```
Not: `app/ollama_runtime.py` Linux/Colab için arka plan başlatma yardımcıları içerir; Windows’ta doğrudan kullanılmayabilir.

---

## Yapılandırma (config)
`app/config.py` içinde ana sabitler:
- `OLLAMA_HOST`: Ollama sunucu adresi
- `TMP_DB_FILE`, `LANCEDB_URI`, `LANCEDB_TABLE`: vektör veritabanı/LanceDB yolları
- `COLAB_KB_PATH`, `KAGGLE_KB_PATH`: bilgi tabanı (Markdown) yolu

Colab/Kaggle senaryolarında `agent_setup_colab.py` ve `agent_setup_kaggle.py` bu yolları kullanır.

---

## Mock Veri ve Araçlar (Tools)
Mock veriler: `app/data_stores.py`
- Kullanıcılar (`_user_store`), paketler (`_package_store`)
- Faturalar (`_invoice_store`), itirazlar (`_invoice_dispute_store`)
- Hizmet durumu, bölgesel kesintiler, teknisyen randevuları
- Superonline müşteri verileri, hat testleri, arıza kayıtları
- Modem durumu, ödeme yöntemleri, kullanım, promosyonlar, OTP

Araçlar (örn. `app/tools/*.py`):
- `users.py`: kullanıcı bilgisi ve paket işlemleri (`mock_get_user_info`, `mock_get_available_packages`, `mock_initiate_package_change`)
- `invoices.py`: fatura işlemleri (`mock_get_latest_invoice`, `mock_register_invoice_dispute`)
- `support_net.py`: internet destek/kesinti ve randevu
- `addons.py`: ek paket listeleme/satın alma
- `superonline.py`: IVR tanıma, servis durumu, bölgesel kesinti, hat testi, IP oturumu sıfırlama, arıza kaydı, bekleme süresi, geri arama
- `modem.py`: modem güç döngüsü, DSL ışığı kontrolü
- `billing_payment.py`: fatura ödeme geçmişi/yöntemleri/ödeme
- `usage_reco.py`: kullanım verisi, paket öneri, proration, iptal
- `promo.py`: promosyon listele/uygula
- `security.py`: kimlik doğrulama, OTP gönder/doğrula
- `outage.py`: kesinti bilgisi ve iade

Ajan kurulumu sırasında araçlar toplanır ve LLM tarafından çağrılabilir (bkz. `app/agent_setup.py` ve gelişmiş varyantlar).

---

## Gereksinimler
`requirements.txt` içeriği (özet):
- Ajan: `agno`
- Ollama istemcisi: `ollama`
- Vektör DB: `lancedb`, `tantivy`
- Doküman işleme: `unstructured`
- NLP: `transformers`, `torch`
- IO/yardımcılar: `numpy`, `pandas`, `requests`, `duckduckgo-search`, `soundfile`
- API (opsiyonel): `fastapi`, `uvicorn`

Kurulum:
```bash
pip install -r requirements.txt
```

---

## Sorun Giderme
- Ollama bağlantı hatası: `app/config.py` içindeki `OLLAMA_HOST` adresini kontrol edin ve Ollama servisinin çalıştığından emin olun. Gerekirse `ollama run llama3.1:8b` ile hızlı test yapın.
- STT model indirme yavaş: `transformers` ilk kullanımda modeli indirir; sabırlı olun veya önceden indirip cache paylaşın.
- TTS çıktı seviyesi/ses: `app/tts.py` içinde örnek hız (sample_rate) 22050 Hz. Gereksinime göre değiştirilebilir.
- Ses kütüphanesi: `soundfile` için tekerler Windows’ta libsndfile içerir; nadir durumlarda PATH veya antivirüs engeline dikkat edin.
- Colab/Kaggle yolları: `app/config.py` içindeki `COLAB_KB_PATH` ve `KAGGLE_KB_PATH` ortamınıza uygun olmalı.

---

## Lisans
Bu proje, Apache-2.0 lisansını kullanır:

- Kaynak lisans: https://github.com/BizTech-TDI/TurkceDogalDilIsleme2025BizTech?tab=Apache-2.0-1-ov-file


