from agno.tools import tool
from app.data_stores import _usage_store, _package_store, _user_store


@tool
def mock_get_usage(user_id: str) -> dict:
    """
    Aylık kullanım bilgisi (GB/dk). Bulunamazsa boş döner.
    """
    return dict(_usage_store.get(user_id, {}))


@tool
def mock_recommend_package(user_id: str) -> str:
    """
    Basit kural: data_gb>50 ise Premium, >20 ise Gold, aksi halde Basic öner.
    """
    usage = _usage_store.get(user_id)
    if not usage:
        return "Basic"
    data = usage.get("data_gb", 0)
    if data > 50:
        return "Premium"
    if data > 20:
        return "Gold"
    return "Basic"


@tool
def mock_calculate_proration(current_pkg_id: str, new_pkg_id: str) -> float:
    """
    Prorasyon: yeni - eski paket fiyat farkı (basit yaklaşım).
    """
    prices = {p["id"]: float(p["price"]) for p in _package_store}
    old_p = prices.get(current_pkg_id, 0.0)
    new_p = prices.get(new_pkg_id, 0.0)
    return max(new_p - old_p, 0.0)


@tool
def mock_cancel_subscription(user_id: str, effective_date: str) -> bool:
    """
    Aboneliği iptal (mock): kullanıcıya bir durum alanı ekler.
    """
    user = _user_store.get(user_id)
    if not user:
        return False
    user["cancel_scheduled_for"] = effective_date
    return True
