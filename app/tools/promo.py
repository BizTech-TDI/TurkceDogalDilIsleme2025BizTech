from agno.tools import tool
from app.data_stores import _promotion_store, _applied_promo_store, _user_store


@tool
def mock_list_promotions(user_id: str) -> list[dict]:
    """
    Kullanıcı mevcut paketine göre uygun promosyonları listeler.
    """
    user = _user_store.get(user_id)
    if not user:
        return []
    pkg = user.get("current_package")
    eligible = [p for p in _promotion_store if pkg in p.get("eligible_packages", [])]
    return [dict(p) for p in eligible]


@tool
def mock_apply_promotion(user_id: str, code: str) -> bool:
    """
    Promosyonu uygular; basitçe kayıt altına alır.
    """
    promo = next((p for p in _promotion_store if p.get("code") == code), None)
    if not promo:
        return False
    _applied_promo_store.append({
        "user_id": user_id,
        "code": code,
        "status": "applied"
    })
    return True
