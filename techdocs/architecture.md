app/
│
├── main.py
├── app_factory.py
│
├── core/                     # Cross-cutting concerns
│   ├── config.py
│   ├── logging.py
│   ├── security.py
│   ├── middleware.py
│   ├── events.py
│   └── exceptions.py
│
├── shared/                   # Shared kernel (DDD)
│   ├── schemas/
│   ├── utils/
│   ├── constants.py
│   └── enums.py
│
├── modules/                  # BOUNDED CONTEXTS (IMPORTANT)
│   ├── auth/
│   ├── users/
│   ├── accounts/
│   ├── transactions/
│   ├── risk/
│   └── reporting/
│
├── infrastructure/           # External systems
│   ├── db/
│   ├── cache/
│   ├── messaging/
│   └── external_services/
│
├── api/                      # API exposure layer
│   ├── deps.py
│   ├── routers.py
│   └── v1/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
└── alembic/
