up:
	docker-compose up

down:
	docker-compose down

run:
	make up

wipe:
	make down
	make wipe-containers
	make wipe-images

wipe-containers:
	make down
	-bash wipe-containers.sh

wipe-images:
	make down
	-bash wipe-images.sh

shell:
	docker run -it new-mexico-docker-app fish
