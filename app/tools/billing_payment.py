from agno.tools import tool
from app.data_stores import _invoice_store, _payment_method_store


@tool
def mock_get_billing_history(user_id: str) -> list[dict]:
    """
    Kullanıcının fatura geçmişini döndürür.
    """
    return [dict(inv) for inv in _invoice_store.get(user_id, [])]


@tool
def mock_pay_invoice(user_id: str, invoice_id: str, method: str = "default") -> bool:
    """
    Belirli bir faturayı ödenmiş olarak işaretler (mock).
    """
    invoices = _invoice_store.get(user_id, [])
    for inv in invoices:
        if inv.get("invoice_id") == invoice_id:
            inv["status"] = "Paid"
            inv["paid_with"] = method
            return True
    return False


@tool
def mock_get_payment_methods(user_id: str) -> list[dict]:
    """
    Kayıtlı ödeme yöntemlerini getirir.
    """
    return [dict(pm) for pm in _payment_method_store.get(user_id, [])]
