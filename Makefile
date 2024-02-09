.PHONY: init
init: ingestor-init api-init

.PHONY: ingestor-init
ingestor-init:
	docker compose --profile ingestor up -d
	cd ./test_infra/; ./seed_moto.sh

.PHONY: api-init
api-init:
	docker compose --profile api up -d
	cd ./test_infra/; ./seed_moto.sh
	docker compose cp test_infra/seed_db_data.sql db:/tmp/seed_db_data.sql
	docker compose exec db sh -c 'cat /tmp/seed_db_data.sql | psql postgres://postgres:postgres@127.0.0.1:5432/cryoet'

.PHONY: clean
clean:
	docker compose --profile '*' down

.PHONY: ingestor-test
ingestor-test:
	docker compose exec ingestor pytest -vvv -s .