
.PHONY: install poetry-install pip-install run test lint format build-image run-container

install: poetry-install pip-install

poetry-install:
	poetry install

pip-install:
	pip install .

run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	flake8 .

format:
	black .

build-image:
	docker build -t my-shell .

run-container:
	docker run -d -p 8000:8000 --env-file .env my-shell
