from agno.tools import tool
from app.data_stores import _user_store, _package_store

# Mock fonksiyonlar / Araçlar
@tool
def mock_get_user_info(user_id: str) -> dict:
    """
    user_id ile kullanıcı profilini getirir.
    Dönüş: user_id, name ve current_package alanlarını içeren bir sözlük.
    Kullanıcı bulunamazsa hata bilgisi içeren bir sözlük döndürür.
    """
    if user_id not in _user_store:
        return {"error": f"id={user_id} olan kullanıcı bulunamadı"}
    return dict(_user_store[user_id])


@tool
def mock_get_available_packages() -> list[dict]:
    """
    Tüm abonelik paketlerini listeler.
    Dönüş: id, price, description anahtarlarını içeren sözlüklerden oluşan bir liste.
    """
    return [dict(pkg) for pkg in _package_store]


@tool
def mock_initiate_package_change(user_id: str, new_pkg_id: str) -> bool:
    """
    Bir kullanıcının paketini değiştirir.
    user_id ve new_pkg_id geçerliyse günceller ve True döndürür,
    aksi halde False döndürür.
    """
    user = _user_store.get(user_id)
    if not user:
        return False

    pkg_ids = {pkg["id"] for pkg in _package_store}
    if new_pkg_id not in pkg_ids:
        return False

    user["current_package"] = new_pkg_id
    return True
