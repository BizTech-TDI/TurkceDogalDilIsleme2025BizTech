from agno.tools import tool
from app.data_stores import _addon_store, _user_addon_store

@tool
def mock_get_available_addons(user_id: str) -> list[dict]:
    """
    Kullanıcı için mevcut eklentilerin (add-on) listesini döndürür.
    """
    # Gerçek mantıkta uygunluk durumuna göre filtreleme yapılabilir
    return [dict(addon) for addon in _addon_store]


@tool
def mock_purchase_addon(user_id: str, addon_id: str) -> bool:
    """
    Kullanıcı için bir eklenti (add-on) satın alır.
    Başarılıysa True, bulunamazsa False döndürür.
    """
    addon = next((a for a in _addon_store if a["id"] == addon_id), None)
    if not addon:
        return False

    _user_addon_store.append({
        "user_id": user_id,
        "addon_id": addon_id,
        "purchase_date": "2025-08-14",
        "status": "Active"
    })
    return True
