from agno.tools import tool
from app.data_stores import _area_outage_store, _regional_outage_store, _invoice_store


@tool
def mock_get_outages(city: str) -> dict:
    """
    Şehir bazlı kesinti bilgisini döndürür (genel ve bölgesel kaynaklardan).
    """
    return {
        "city": city,
        "mobile_outage": bool(_area_outage_store.get(city, False)),
        "fixed_outage": bool(_regional_outage_store.get(city, False)),
    }


@tool
def mock_refund_last_charge(user_id: str) -> bool:
    """
    Son faturadaki bedelin iadesini (mock) işaretler.
    """
    invoices = _invoice_store.get(user_id)
    if not invoices:
        return False
    invoices[-1]["status"] = "Refunded"
    return True
