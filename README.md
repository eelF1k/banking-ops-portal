# Banking Ops Portal

Internal banking operations portal (fullstack pet project) focused on secure workflows:
- request lifecycle
- approvals by role
- audit trail
- JWT + OAuth2
- Redis cache/rate limit
- Docker + GitLab CI style pipeline

## Tech stack
- Backend: FastAPI
- Frontend: React + TypeScript
- DB: PostgreSQL
- Cache/Broker: Redis
- Infra: Docker Compose, GitLab CI config

## Commit roadmap (0 -> N)
0. Init repo structure
1. Backend scaffold + dependencies
2. Auth (JWT + RBAC)
3. Operations domain models
4. Request workflow API
5. Audit log + security middleware
6. Redis cache + rate limiting
7. Frontend scaffold
8. Frontend auth + request boards
9. Docker compose full stack
10. Tests + CI (GitHub Actions + gitlab-ci.yml)
11. Docs polish + runbook

