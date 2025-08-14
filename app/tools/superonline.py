from agno.tools import tool
from app.data_stores import (
    _user_store_superonline,
    _regional_outage_store,
    _line_test_results,
    _fault_ticket_store,
)

@tool
def mock_ivr_identify_customer(phone: str = None, customer_no: str = None) -> dict:
    """
    Telefon numarası veya müşteri numarasına göre müşteriyi tanımlar.
    Bulunamazsa hata, bulunduğunda kullanıcı profilini döndürür.
    """
    if customer_no and customer_no in _user_store_superonline:
        return dict(_user_store_superonline[customer_no])
    if phone:
        for user in _user_store_superonline.values():
            if user["phone"] == phone:
                return dict(user)
    return {"error": "Müşteri bulunamadı"}


@tool
def mock_check_service_status_superonline(customer_no: str) -> str:
    """
    Hizmet durumunu döndürür: Active veya Suspended.
    """
    user = _user_store_superonline.get(customer_no)
    if not user:
        return "Not Found"
    return user["service_status"]


@tool
def mock_check_regional_outage(city: str) -> bool:
    """
    Müşterinin şehrinde kesinti olup olmadığını kontrol eder.
    """
    return _regional_outage_store.get(city, False)


@tool
def mock_run_line_test(customer_no: str) -> dict:
    """
    Müşterinin bağlantısı için otomatik hat testi çalıştırır.
    """
    return _line_test_results.get(customer_no, {"error": "Test yapılamadı"})


@tool
def mock_reset_ip_session(customer_no: str) -> bool:
    """
    Müşteri için IP oturumunu sıfırlar.
    """
    if customer_no in _line_test_results:
        _line_test_results[customer_no]["ip_session"] = "Active"
        return True
    return False


@tool
def mock_open_fault_ticket(customer_no: str, description: str) -> str:
    """
    Bir arıza kaydı açar ve kayıt numarasını döndürür.
    """
    ticket_id = f"TCK{len(_fault_ticket_store)+1:05d}"
    _fault_ticket_store.append({
        "ticket_id": ticket_id,
        "customer_no": customer_no,
        "description": description,
        "status": "Open"
    })
    return ticket_id


@tool
def mock_get_estimated_wait_time(hour: int) -> int:
    """
    Günün saatine göre bekleme süresini tahmin eder.
    Dakika cinsinden döndürür.
    """
    # 9-12 ve 17-20 saatlerini yoğun saat varsay
    if 9 <= hour <= 12 or 17 <= hour <= 20:
        return 45  # dakika
    return 5


@tool
def mock_request_callback(customer_no: str) -> bool:
    """
    Müşteri için geri arama talebi kaydeder.
    """
    # Gerçek durumda bu istek bir kuyruğa gönderilir
    return True
