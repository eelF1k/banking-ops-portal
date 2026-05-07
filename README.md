# Banking Ops Portal

## Назва проєкту
Banking Ops Portal

## Це мій пет проєкт про...
Це мій пет проєкт про внутрішній банківський портал для керування заявками, ролями погодження та аудитом дій.

## Технологічний стек
- Backend: FastAPI
- Frontend: React + TypeScript
- БД: PostgreSQL
- Кеш/черги: Redis
- Інфраструктура: Docker Compose, GitHub Actions, GitLab CI

## Що реалізовано
- Каркас бекенду з health/readiness ендпоінтами.
- Базова структура модулів auth/workflow/ops.
- Підготовка fullstack архітектури під рольову обробку заявок.
- CI-ready структура для подальшого розвитку.

## Структура
- `backend/` — API та бізнес-логіка
- `frontend/` — клієнтський інтерфейс
- `infra/` — docker/ci конфігурація
- `docs/` — документація проєкту

## Архітектура
- Backend надає API для auth та workflow заявок.
- Frontend працює з API для відображення станів процесів.
- PostgreSQL зберігає операційні дані.
- Redis використовується для кешу та службових задач.

## Що потрібно встановити для тесту
- Python 3.12+
- Node.js 20+
- Docker Desktop

## Як запустити
```bash
docker compose up --build
```
Або локально:
```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8000
```

