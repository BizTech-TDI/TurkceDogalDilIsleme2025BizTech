# Kullanıcı ve paket verisi
_user_store = {
    "12345": {
        "user_id": "12345",
        "name": "Ayşe",
        "birth_date": "1985-07-12",
        "current_package": "Gold"
    },
    "67890": {
        "user_id": "67890",
        "name": "Mehmet",
        "birth_date": "1990-05-25",
        "current_package": "Basic"
    },
    "54321": {
        "user_id": "54321",
        "name": "Zeynep",
        "birth_date": "1978-11-03",
        "current_package": "Premium"
    },
}

_package_store = [
    {"id": "Basic",   "price": 10.0, "description": "Basic subscription"},
    {"id": "Gold",    "price": 20.0, "description": "Gold tier with extra features"},
    {"id": "Premium", "price": 30.0, "description": "All-inclusive Premium package"},
]

# Fatura verileri
_invoice_store = {
    "12345": [
        {
            "invoice_id": "INV202508",
            "period": "2025-08",
            "amount": 150.75,
            "due_date": "2025-08-25",
            "breakdown": [
                {"item": "Abonelik Ücreti", "amount": 120.0},
                {"item": "Aşım Ücreti", "amount": 25.5},
                {"item": "Vergi", "amount": 5.25}
            ],
            "status": "Unpaid"
        }
    ],
    "67890": [
        {
            "invoice_id": "INV202508",
            "period": "2025-08",
            "amount": 50.0,
            "due_date": "2025-08-20",
            "breakdown": [
                {"item": "Abonelik Ücreti", "amount": 50.0}
            ],
            "status": "Paid"
        }
    ]
}

_invoice_dispute_store = []

# Teknik destek – internet arızası
_service_status_store = {
    "12345": {"status": "Active", "last_check": "2025-08-14 10:30"},
    "67890": {"status": "Fault Detected", "last_check": "2025-08-14 10:31"},
}

_area_outage_store = {
    "Ankara": False,
    "Istanbul": True
}

_technician_schedule_store = []

# Ek paketler
_addon_store = [
    {"id": "ExtraData1GB", "price": 5.0, "description": "Ek 1GB mobil internet", "duration_days": 30},
    {"id": "IntlCalls100", "price": 15.0, "description": "100 dakika uluslararası arama", "duration_days": 30},
    {"id": "StreamingPack", "price": 12.0, "description": "Sınırsız video platform erişimi", "duration_days": 30}
]

_user_addon_store = []

# Superonline müşteri ve hat verisi
_user_store_superonline = {
    "10000001": {
        "customer_no": "10000001",
        "phone": "05321234567",
        "name": "Ali Yılmaz",
        "city": "Ankara",
        "service_status": "Active",   # Aktif / Askıya Alındı
        "connection_type": "Fiber",
        "plan": "100 Mbps Limitsiz"
    },
    "10000002": {
        "customer_no": "10000002",
        "phone": "05419876543",
        "name": "Fatma Demir",
        "city": "Istanbul",
        "service_status": "Suspended",
        "connection_type": "ADSL",
        "plan": "24 Mbps Limitsiz"
    }
}

_regional_outage_store = {
    "Ankara": False,
    "Istanbul": True,
    "Izmir": False
}

_line_test_results = {
    "10000001": {
        "dsl_port_status": "UP",
        "ping_ms": 15,
        "sync_status": "OK",
        "ip_session": "Active"
    },
    "10000002": {
        "dsl_port_status": "DOWN",
        "ping_ms": None,
        "sync_status": "No Sync",
        "ip_session": "Inactive"
    }
}

_fault_ticket_store = []

# Modem durumu
_modem_status_store = {
    "10000001": {"powered_on": True, "dsl_light": True},
    "10000002": {"powered_on": True, "dsl_light": False}
}

# Ek: Ödeme yöntemleri, kullanım, promosyon ve OTP depoları
_payment_method_store = {
    "12345": [
        {"type": "credit_card", "masked": "**** **** **** 4242", "default": True},
    ],
    "67890": [],
}

_usage_store = {
    "12345": {"month": "2025-08", "data_gb": 85.2, "voice_min": 320},
    "67890": {"month": "2025-08", "data_gb": 12.7, "voice_min": 45},
}

_promotion_store = [
    {"code": "YAZ10", "description": "%10 indirim", "eligible_packages": ["Gold", "Premium"]},
    {"code": "DENEME1", "description": "İlk ay ücretsiz eklenti", "eligible_packages": ["Basic"]},
]

_applied_promo_store = []

_otp_store = []  # { user_id, channel, otp, expires_at }
