build:
	chmod +x scripts/entrypoint.sh && docker-compose -f docker/docker-compose.yaml up

down:
	docker-compose -f docker/docker-compose.yaml down

build-database:
	python3 knowledgebase_building/build_knowledgebase.py

