# Python Practice Lab

A personal workspace where I practice and experiment with Python — clean code, object-oriented design, and small real-world projects.

## Contents

### `invoice_system/`

A small invoice management exercise built with plain Python.

```
invoice_system/
├── main.py                      # Entry point (work in progress)
├── models/
│   └── invoice.py               # Invoice model: tax, total, status, details
├── services/
│   └── invoice_service.py       # Invoice service layer
└── utils/
    └── calculations.py          # Shared calculation helpers
```

**Example:**

```python
from models.invoice import Invoice

invoice = Invoice("INV-001", "Acme Corp", 1000, 0.05)
print(invoice.get_invoice_details())
```

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
python invoice_system/main.py
```

## Purpose

This repo is a living practice ground. Structure and code will evolve as I learn and try new things.
