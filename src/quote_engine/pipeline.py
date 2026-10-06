from __future__ import annotations
from .schemas import Quote
from .validators import validate_quote

def run_pipeline(payload: dict) -> dict:
    # In production, this stage is fed by OCR/LLM adapters. The demo keeps the
    # business-critical validation deterministic and provider-independent.
    quote=Quote.model_validate(payload)
    result=validate_quote(quote)
    return {"quote":quote.model_dump(),"decision":result.model_dump()}
