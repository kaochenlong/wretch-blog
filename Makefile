server:
	uv run python manage.py runserver

migrate:
	uv run python manage.py migrate

migrations:
	uv run python manage.py makemigrations

shell:
	uv run python manage.py shell
