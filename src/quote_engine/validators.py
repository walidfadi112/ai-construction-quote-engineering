from __future__ import annotations
from .schemas import Quote, ValidationResult


def validate_quote(q: Quote) -> ValidationResult:
    anomalies=[]
    line_checks=[]
    for item in q.items:
        expected=round(item.quantity*item.unit_price_ht,2)
        ok=abs(expected-item.total_ht)<=0.02
        line_checks.append(ok)
        if not ok:
            anomalies.append(f"Line total mismatch: {item.description}")
    expected_ttc=round(q.total_ht*(1+q.vat_rate/100),2)
    ttc_ok=abs(expected_ttc-q.total_ttc)<=0.03
    if not ttc_ok: anomalies.append("TTC does not match HT + VAT")
    sum_ok=abs(round(sum(x.total_ht for x in q.items),2)-q.total_ht)<=0.03
    if not sum_ok: anomalies.append("HT total does not match line totals")
    confidence=q.confidence
    if anomalies: confidence=min(confidence,0.68)
    status="AUTO_APPROVED" if not anomalies and confidence>=0.90 else "HUMAN_REVIEW"
    return ValidationResult(status=status,confidence=round(confidence,3),anomalies=anomalies,checks={"line_totals":all(line_checks),"ht_sum":sum_ok,"ttc":ttc_ok})
