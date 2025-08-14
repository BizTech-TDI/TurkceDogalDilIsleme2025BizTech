import random
import time
from agno.tools import tool
from app.data_stores import _otp_store, _user_store


@tool
def mock_verify_identity(user_id: str, name: str, birth_date: str) -> bool:
    """
    Kimlik doğrulama (mock): user_store ile eşleştirir.
    """
    u = _user_store.get(user_id)
    if not u:
        return False
    return (u.get("name") == name) and (u.get("birth_date") == birth_date)


@tool
def mock_send_otp(user_id: str, channel: str = "sms") -> bool:
    """
    OTP gönderir (mock) ve store'a kaydeder.
    """
    otp = f"{random.randint(100000, 999999)}"
    _otp_store.append({
        "user_id": user_id,
        "channel": channel,
        "otp": otp,
        "expires_at": time.time() + 300,
    })
    return True


@tool
def mock_validate_otp(user_id: str, otp: str) -> bool:
    """
    OTP doğrular.
    """
    now = time.time()
    for rec in reversed(_otp_store):
        if rec["user_id"] == user_id and rec["otp"] == otp and rec["expires_at"] >= now:
            rec["validated"] = True
            return True
    return False
