# Architecture technique

```text
                    ┌──────────────────────┐
                    │ Gmail / Drive /      │
                    │ Webhook / PDF        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ n8n orchestration    │
                    │ routing + retries   │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
          ┌──────────────┐          ┌──────────────┐
          │ OCR adapter  │          │ Metadata     │
          │ PDF → text  │          │ normalization│
          └──────┬───────┘          └──────┬───────┘
                 └────────────┬────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ LLM structured       │
                    │ extraction           │
                    │ JSON schema          │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Deterministic        │
                    │ business validation  │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Decision engine      │
                    │ confidence + rules   │
                    └───────┬───────┬──────┘
                            │       │
                    safe    │       │ risky
                            ▼       ▼
                    Auto approval  Human review
                            │       │
                            └───┬───┘
                                ▼
                    Audit / notification / DB
```

## Design principle

The LLM is deliberately **not** the final authority. It proposes structured facts; deterministic checks verify arithmetic and business constraints. Low confidence or contradictions route to human review. This separation improves auditability, testability and operational safety.
