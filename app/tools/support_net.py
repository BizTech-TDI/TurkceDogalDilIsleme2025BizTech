from agno.tools import tool
from app.data_stores import _service_status_store, _area_outage_store, _technician_schedule_store

@tool
def mock_check_service_status(user_id: str) -> dict:
    """
    Kullanıcının internet hizmetinin aktif mi arızalı mı olduğunu kontrol eder.
    """
    status = _service_status_store.get(user_id)
    if not status:
        return {"error": "Hizmet bilgisi bulunamadı"}
    return dict(status)


@tool
def mock_check_area_outage(city: str) -> bool:
    """
    Kullanıcının şehrinde bilinen bir kesinti olup olmadığını kontrol eder.
    Kesinti varsa True, yoksa False döndürür.
    """
    return _area_outage_store.get(city, False)


@tool
def mock_schedule_technician(user_id: str, date: str) -> bool:
    """
    Teknisyen randevusu planlar.
    """
    _technician_schedule_store.append({
        "user_id": user_id,
        "date": date,
        "status": "Scheduled"
    })
    return True
