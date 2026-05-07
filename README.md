# Banking Ops Portal

Внутрішній портал банківських операцій (fullstack pet-проєкт), сфокусований на безпечних робочих процесах:
- життєвий цикл заявок
- погодження за ролями
- аудит дій
- JWT + OAuth2
- кеш і rate limiting через Redis
- Docker + pipeline у стилі GitLab CI

## Технологічний стек
- Backend: FastAPI
- Frontend: React + TypeScript
- БД: PostgreSQL
- Кеш/брокер: Redis
- Інфраструктура: Docker Compose, конфігурація GitLab CI

## Roadmap комітів (0 -> N)
0. Ініціалізація структури репозиторію
1. Каркас бекенду + залежності
2. Авторизація (JWT + RBAC)
3. Доменні моделі операцій
4. API workflow для заявок
5. Аудит-лог + security middleware
6. Redis-кеш + обмеження частоти запитів
7. Каркас фронтенду
8. Авторизація на фронтенді + дошки заявок
9. Повний Docker Compose стек
10. Тести + CI (GitHub Actions + gitlab-ci.yml)
11. Полірування документації + runbook

