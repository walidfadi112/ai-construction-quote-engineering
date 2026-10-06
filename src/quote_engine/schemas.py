from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional

class QuoteItem(BaseModel):
    description: str
    quantity: float = Field(ge=0)
    unit: str = "u"
    unit_price_ht: float = Field(ge=0)
    total_ht: float = Field(ge=0)

class Quote(BaseModel):
    quote_number: str
    date: str
    company: str
    project: str
    currency: str = "EUR"
    items: List[QuoteItem]
    total_ht: float = Field(ge=0)
    vat_rate: float = Field(default=20.0, ge=0, le=100)
    total_ttc: float = Field(ge=0)
    confidence: float = Field(default=0.0, ge=0, le=1)

class ValidationResult(BaseModel):
    status: str
    confidence: float
    anomalies: List[str]
    checks: dict
