from agno.tools import tool
from app.data_stores import _modem_status_store

@tool
def mock_power_cycle_modem(customer_no: str) -> bool:
    """
    Müşterinin modemini güç döngüsüne sokar (yeniden başlatma).
    """
    if customer_no in _modem_status_store:
        # Aç/kapa değişimi ile yeniden başlatmayı simüle et
        _modem_status_store[customer_no]["powered_on"] = False
        _modem_status_store[customer_no]["powered_on"] = True
        return True
    return False


@tool
def mock_check_modem_dsl_light(customer_no: str) -> bool:
    """
    Modemin DSL ışığının yanıp yanmadığını kontrol eder.
    DSL ışığı yanıyorsa True döndürür.
    """
    if customer_no in _modem_status_store:
        return bool(_modem_status_store[customer_no]["dsl_light"])
    return False
