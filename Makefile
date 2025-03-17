# DEFAULT_GOAL := help

HOST ?= 127.0.0.1
PORT ?= 8080

.PHONY: run install uninstall help

run: ## Run the application using uvicorn with provided arguments on defaults
	#uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload for work with uvicorn
	#poetry run gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker -c gunicorn.conf.py --reload
	#uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload

install: ## Install a dependency using poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Uninstall a dependency using poetry
	@echo "Uninstalling dependency $(LIBRAßRY)"
	poetry remove $(LIBRARY)
migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply:
	alembic upgrade head
help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)