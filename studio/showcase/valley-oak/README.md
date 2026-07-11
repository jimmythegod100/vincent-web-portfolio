# Valley Oak Collective — studio practice showcase

Fictional Central Valley café site used to prove the Docker + Python client template.

**Not a paid client.** Labeled clearly in the UI footer.

## Run (iMac)

```bash
cp .env.example .env
docker compose up --build
```

- Site: http://localhost:8090  
- API: http://localhost:8010/docs  

### With Postgres persistence

```bash
# in .env:
# DATABASE_URL=postgresql+psycopg://valley:valley_dev_change_me@db:5432/valley_oak
docker compose --profile db up --build
```

When `DATABASE_URL` is empty, contact messages stay in memory for the container lifetime.
