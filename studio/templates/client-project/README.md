# __CLIENT_NAME__

Custom site scaffold generated from `studio/templates/client-project`.

## Run on iMac

```bash
cp .env.example .env
docker compose up --build
```

- Site: http://localhost:8088 (or the `FRONTEND_PORT` in `.env`)
- API docs: http://localhost:8001/docs
- Health: http://localhost:8088/health

### Optional Postgres

```bash
# DATABASE_URL=postgresql+psycopg://client:client_dev_change_me@db:5432/__CLIENT_SLUG__
docker compose --profile db up --build
```

## Customize

1. Replace copy in `frontend/index.html`
2. Adjust colors/fonts in `frontend/css/style.css` (`:root` variables)
3. Drop brand photos in `assets/`
4. Extend API routes in `backend/app/routers/`
5. Fill `HANDOFF.md` before delivery
