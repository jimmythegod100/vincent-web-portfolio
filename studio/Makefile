.PHONY: up up-db down logs health new-client bootstrap ps smoke showcase showcase-down

up:
	docker compose up --build -d

up-db:
	@grep -q 'DATABASE_URL=postgresql' .env 2>/dev/null || \
	  (echo 'Tip: set DATABASE_URL=postgresql+psycopg://studio:studio_dev_change_me@db:5432/studio in .env'; true)
	docker compose --profile db up --build -d

down:
	docker compose down

logs:
	docker compose logs -f studio-api

ps:
	docker compose ps

health:
	curl -s http://localhost:$${STUDIO_API_PORT:-8000}/health | python3 -m json.tool

bootstrap:
	./scripts/bootstrap-imac.sh

smoke:
	./scripts/smoke.sh

new-client:
	@test -n "$(NAME)" || (echo 'Usage: make new-client NAME=client-slug'; exit 1)
	./scripts/new-client.sh "$(NAME)"

showcase:
	@test -f showcase/valley-oak/.env || cp showcase/valley-oak/.env.example showcase/valley-oak/.env
	cd showcase/valley-oak && docker compose up --build -d

showcase-down:
	cd showcase/valley-oak && docker compose down
