build:
	cd infra
	docker-compose up -d
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py createsuperuser
	docker-compose exec web python manage.py collectstatic --no-input