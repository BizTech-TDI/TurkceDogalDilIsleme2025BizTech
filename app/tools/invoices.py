from agno.tools import tool
from app.data_stores import _invoice_store, _invoice_dispute_store

@tool
def mock_get_latest_invoice(user_id: str) -> dict:
    """
    Bir kullanıcının en güncel faturasını getirir.
    Bulunamazsa hata, bulunduğunda fatura detaylarını içeren bir sözlük döndürür.
    """
    invoices = _invoice_store.get(user_id)
    if not invoices:
        return {"error": "Fatura bulunamadı"}
    return dict(invoices[-1])  # Son fatura


@tool
def mock_register_invoice_dispute(user_id: str, invoice_id: str, reason: str) -> bool:
    """
    Belirli bir fatura için itiraz kaydı oluşturur.
    Kayıt başarılıysa True, fatura bulunamazsa False döndürür.
    """
    invoices = _invoice_store.get(user_id, [])
    if not any(inv["invoice_id"] == invoice_id for inv in invoices):
        return False

    _invoice_dispute_store.append({
        "user_id": user_id,
        "invoice_id": invoice_id,
        "reason": reason,
        "status": "Pending Review"
    })
    return True
