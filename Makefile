.PHONY: \
	backend-test \
	backend-lint \
	backend-format-check \
	backend-fix \
	backend-validate \
	frontend-check \
	frontend-build \
	frontend-dev \
	frontend-start \
	frontend-validate \
	validate

backend-test:
	cd backend && python -mpytest

backend-lint:
	cd backend && \
	ruff check .

backend-format-check:
	cd backend && \
	ruff format --check .

backend-fix:
	cd backend && \
	ruff check . --fix && \
	ruff format .

backend-validate:
	cd backend && \
	ruff format --check . && \
	ruff check . && \
	python -m pytest

frontend-check:
	npm --prefix frontend run check

frontend-fix:
	npm --prefix frontend run fix

frontend-build:
	npm --prefix frontend run build

frontend-dev:
	npm --prefix frontend run dev

frontend-start:
	npm --prefix frontend run build && \
	npm --prefix frontend run start


frontend-validate:
	npm --prefix frontend run check && \
	npm --prefix frontend run build

validate:
	$(MAKE) backend-validate
	$(MAKE) frontend-validate