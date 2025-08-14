from typing import List, Dict, Any


def make_perf_target(max_latency_s: float = 5.0, min_accuracy: float = 0.7) -> dict:
    return {"max_latency_s": max_latency_s, "min_accuracy": min_accuracy}


def _actual_tools_from_resp(resp_text: str) -> List[str]:
    # Basit çıkarım: metin içinde belirli anahtarlar aranır
    keys = [
        "mock_get_user_info",
        "mock_get_latest_invoice",
        "mock_check_service_status",
    ]
    used = [k for k in keys if k in resp_text]
    return used


def run_reliability(agent_callable, prompts: List[str]) -> Dict[str, Any]:
    results = []
    for p in prompts:
        try:
            out = str(agent_callable(p))
            results.append({"ok": True, "out": out})
        except Exception as e:
            results.append({"ok": False, "error": str(e)})
    ok_ratio = sum(1 for r in results if r["ok"]) / max(len(results), 1)
    return {"ok_ratio": ok_ratio, "details": results}


def run_accuracy(references: List[str], outputs: List[str]) -> Dict[str, Any]:
    matches = 0
    for r, o in zip(references, outputs):
        if r.strip() == o.strip():
            matches += 1
    acc = matches / max(len(references), 1)
    return {"accuracy": acc}
