build:
	docker-compose build

start:
	docker-compose up -d

stop:
	docker-compose down

bash:
	docker-compose exec web /bin/bash

logs:
	docker-compose logs -f
