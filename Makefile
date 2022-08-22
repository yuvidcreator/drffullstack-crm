manage=./manage.py
python=python3

runserver:
	$(python) $(manage) runserver 8000

collectstaic:
	$(python) $(manage) collectstatic

check:
	$(python) $(manage) check

install:
	pip install -r requirements.txt

migrate:
	$(python) $(manage) makemigrations  && $(python) $(manage) migrate

freeze:
	pip freeze > requirements.txt

shell:
	$(python) $(manage) shell_plus

reset-db:
	$(python) $(manage) reset_db
	make migrate

db-backup:
	$(python) $(manage) db_backup

superuser:
	$(python) $(manage) superuser

woker:
	celery -A venya worker -l info

beat:
	celery -A venya beat -l info
