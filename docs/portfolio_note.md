# Portfolio note

This repository is an original portfolio implementation by **Walid Fadi**. It is inspired by common AI document-processing architectures but is not a fork or rebranding of a third-party repository.

The project is intentionally designed around a realistic construction-quote automation use case: extracting structured information from supplier quotes, validating arithmetic and business constraints, and routing uncertain cases to a human.

External provider integrations (OCR, LLM, Gmail, PostgreSQL) are represented through explicit adapters/interfaces so credentials and vendor-specific assumptions are not committed to the repository.
