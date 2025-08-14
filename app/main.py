import sys
from app.stt import speech_to_text  
from app.tts import text_to_speech 
from app.tools.users import (
    mock_get_user_info,
    mock_get_available_packages,
    mock_initiate_package_change,
)
from app.tools.invoices import (
    mock_get_latest_invoice,
    mock_register_invoice_dispute,
)
from app.tools.support_net import (
    mock_check_service_status,
    mock_check_area_outage,
    mock_schedule_technician,
)
from app.tools.addons import (
    mock_get_available_addons,
    mock_purchase_addon,
)
from app.tools.superonline import (
    mock_ivr_identify_customer,
    mock_check_service_status_superonline,
    mock_check_regional_outage,
    mock_run_line_test,
    mock_reset_ip_session,
    mock_open_fault_ticket,
    mock_get_estimated_wait_time,
    mock_request_callback,
)
from app.tools.modem import (
    mock_power_cycle_modem,
    mock_check_modem_dsl_light,
)
from app.agent_setup import build_agent


def smoke_test() -> None:
    print("== Smoke Test Başladı ==")
    # Kullanıcı ve paketler
    print("Kullanıcı (12345):", mock_get_user_info("12345"))
    print("Paketler:", mock_get_available_packages())
    print("Paket Değiştir (12345 -> Premium):", mock_initiate_package_change("12345", "Premium"))

    # Fatura
    print("Son Fatura (12345):", mock_get_latest_invoice("12345"))
    print(
        "Fatura İtiraz Kaydı:",
        mock_register_invoice_dispute("12345", "INV202508", "Hatalı aşım ücreti")
    )

    # Destek
    print("Hizmet Durumu (12345):", mock_check_service_status("12345"))
    print("Bölge Kesintisi (Istanbul):", mock_check_area_outage("Istanbul"))
    print("Teknisyen Randevu:", mock_schedule_technician("12345", "2025-08-20"))

    # Add-on
    print("Add-on'lar:", mock_get_available_addons("12345"))
    print("Add-on Satın Al:", mock_purchase_addon("12345", "StreamingPack"))

    # Superonline
    print("IVR Tanıma (tel):", mock_ivr_identify_customer(phone="05321234567"))
    print("Servis Durumu (10000001):", mock_check_service_status_superonline("10000001"))
    print("Bölgesel Kesinti (Istanbul):", mock_check_regional_outage("Istanbul"))
    print("Hat Testi (10000001):", mock_run_line_test("10000001"))
    print("IP Reset:", mock_reset_ip_session("10000001"))
    print("Arıza Kaydı Aç:", mock_open_fault_ticket("10000001", "Bağlantı sık kopuyor"))
    print("Tahmini Bekleme (18):", mock_get_estimated_wait_time(18))
    print("Geri Arama Kaydı:", mock_request_callback("10000001"))

    # Modem
    print("Modem Güç Döngüsü:", mock_power_cycle_modem("10000001"))
    print("DSL Işığı:", mock_check_modem_dsl_light("10000001"))
    print("== Smoke Test Bitti ==")


def voice_chat_once(audio_path: str, reply_audio_path: str = "agent_reply.wav", model_id: str = "llama3.1:8b") -> str:
    """
    Sesli sohbet akışı: Kullanıcı sesi -> STT (metin) -> Agent yanıtı (metin) -> TTS (wav)
    Dönüş: oluşturulan yanıt ses dosyasının yolu.
    Not: Ollama servisinin hazır olduğundan emin olun (agent_setup'ı bkz.).
    """
    # 1) STT
    user_text = speech_to_text(audio_path)
    print(f"[STT] Kullanıcı: {user_text}")

    # 2) Agent
    agent = build_agent(model_id=model_id)
    try:
        agent_text = agent.run(user_text)  # Agno Agent tipik kullanım
    except Exception as e:
        print(f"[Agent] Hata: {e}")
        agent_text = "Üzgünüm, şu an yanıt üretemedim. Lütfen tekrar dener misiniz?"
    agent_text = str(agent_text)
    print(f"[Agent] Yanıt: {agent_text}")

    # 3) TTS
    out_path = text_to_speech(agent_text, output_path=reply_audio_path)
    print(f"[TTS] Ses dosyası: {out_path}")
    return out_path


if __name__ == "__main__":
    # Komut satırı kullanımı:
    # python app/main.py            -> smoke test
    # python app/main.py voice in.wav [out.wav] [model_id]
    if len(sys.argv) >= 2 and sys.argv[1].lower() == "voice":
        in_path = sys.argv[2] if len(sys.argv) >= 3 else "input.wav"
        out_path = sys.argv[3] if len(sys.argv) >= 4 else "agent_reply.wav"
        model = sys.argv[4] if len(sys.argv) >= 5 else "llama3.1:8b"
        voice_chat_once(in_path, out_path, model)
    else:
        smoke_test()
