"""
Basit Agno Agent kurulumu: Ollama LLM + mevcut tool'lar.
Not: Notebook'taki ileri düzey bellek/KB/LanceDB yapıları sadeleştirildi; 
önce temel sohbet + araç çağrıları çalışır hale getirildi.
"""
from agno.agent import Agent
from agno.models.ollama import Ollama

# Tool'lar: notebook'taki @tool fonksiyonları modüler dosyalarda
from app.tools.users import (
    mock_get_user_info,
    mock_get_available_packages,
    mock_initiate_package_change,
)
from app.tools.invoices import (
    mock_get_latest_invoice,
    mock_register_invoice_dispute,
)
from app.tools.support_net import (
    mock_check_service_status,
    mock_check_area_outage,
    mock_schedule_technician,
)
from app.tools.addons import (
    mock_get_available_addons,
    mock_purchase_addon,
)
from app.tools.superonline import (
    mock_ivr_identify_customer,
    mock_check_service_status_superonline,
    mock_check_regional_outage,
    mock_run_line_test,
    mock_reset_ip_session,
    mock_open_fault_ticket,
    mock_get_estimated_wait_time,
    mock_request_callback,
)
from app.tools.modem import (
    mock_power_cycle_modem,
    mock_check_modem_dsl_light,
)
from app.tools.billing_payment import (
    mock_get_billing_history,
    mock_pay_invoice,
    mock_get_payment_methods,
)
from app.tools.usage_reco import (
    mock_get_usage,
    mock_recommend_package,
    mock_calculate_proration,
    mock_cancel_subscription,
)
from app.tools.promo import (
    mock_list_promotions,
    mock_apply_promotion,
)
from app.tools.security import (
    mock_verify_identity,
    mock_send_otp,
    mock_validate_otp,
)
from app.tools.outage import (
    mock_get_outages,
    mock_refund_last_charge,
)
from app.config import OLLAMA_HOST


DEFAULT_INSTRUCTIONS = (
    "Türkçe konuş. Kullanıcının talebini kısa ve açık cevapla. Gerekirse araçları kullan."
)


def build_agent(model_id: str = "llama3.1:8b") -> Agent:
    """
    Basit bir Agent örneği döndürür. Ollama servisinin çalıştığından emin olun.
    """
    llm = Ollama(id=model_id, host=OLLAMA_HOST)

    tools = [
        # users
        mock_get_user_info,
        mock_get_available_packages,
        mock_initiate_package_change,
        # invoices
        mock_get_latest_invoice,
        mock_register_invoice_dispute,
        # support
        mock_check_service_status,
        mock_check_area_outage,
        mock_schedule_technician,
        # addons
        mock_get_available_addons,
        mock_purchase_addon,
        # superonline
        mock_ivr_identify_customer,
        mock_check_service_status_superonline,
        mock_check_regional_outage,
        mock_run_line_test,
        mock_reset_ip_session,
        mock_open_fault_ticket,
        mock_get_estimated_wait_time,
        mock_request_callback,
        # modem
        mock_power_cycle_modem,
        mock_check_modem_dsl_light,
        # billing/payment
        mock_get_billing_history,
        mock_pay_invoice,
        mock_get_payment_methods,
        # usage & recommendation
        mock_get_usage,
        mock_recommend_package,
        mock_calculate_proration,
        mock_cancel_subscription,
        # promo
        mock_list_promotions,
        mock_apply_promotion,
        # security/otp
        mock_verify_identity,
        mock_send_otp,
        mock_validate_otp,
        # outage
        mock_get_outages,
        mock_refund_last_charge,
    ]

    agent = Agent(
        model=llm,
        tools=tools,
        instructions=DEFAULT_INSTRUCTIONS,
        # verbose=True,  # isterseniz açabilirsiniz
    )
    return agent
