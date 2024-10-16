MARK:="not optional"

-include .env

clean:
	docker-compose stop
	docker-compose rm -f
	rm -rf test_modules

run:
	docker-compose up poc-api

test_modules: requirements_test.txt
	rm -rf test_modules
	docker run -it --rm -v "$$(pwd)":/app -w /app python:3.12 bash -c 'pip install -t test_modules -r requirements_test.txt'

test: test_modules
	@make test-pytest

test-pytest:
	STAGE=local docker-compose exec -e PYTHONPATH=test_modules poc-api python3 -m pytest -m ${MARK}

test-gh-actions: requirements_test.txt
	chmod o+rw .
	docker run --rm -v $$(pwd):/app -w /app python:3.11 bash -c 'pip install -t test_modules -r requirements_test.txt'
	docker-compose run --rm -e PYTHONPATH=test_modules poc-api python3 -m pytest

makemigrations:
	STAGE=local docker-compose run --rm poc-api alembic revision --autogenerate -m "create table"

migrate:
	STAGE=local docker-compose run --rm poc-api alembic upgrade head

restart-api:
	STAGE=local docker-compose restart poc-api poc-api-public
