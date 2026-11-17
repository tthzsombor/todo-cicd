# Teendőlista – CI/CD pipeline projekt

Mini webalkalmazás (Flask) teljes CI/CD folyamattal: **GitHub → GitHub Actions → GHCR (Docker image) → Render**.

## Üzleti funkciók
- Teendők listázása, felvétele, késznek jelölése, törlése (web UI + REST API)
- `GET /health` – állapotellenőrzés

## Lokális futtatás
```bash
pip install -r requirements-dev.txt
pytest -v
python -m flask --app wsgi run        # http://127.0.0.1:5000
# vagy Dockerrel:
docker build -t todo . && docker run -p 8000:8000 todo
```

## Pipeline (.github/workflows/ci-cd.yml)
| Job | Feladat |
|---|---|
| test | Függőségek telepítése, `pytest` (build + teszt) |
| docker | Docker image build, push a GHCR-be (`latest` + commit SHA tag) |
| deploy | Render deploy hook hívása, majd `/health` smoke test |

Szükséges GitHub Secrets: `RENDER_DEPLOY_HOOK_URL`, `APP_URL`.
