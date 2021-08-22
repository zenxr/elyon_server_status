#!/bin/bash
python app.py &
python -m celery -A app.celery worker --loglevel=info &
python -m celery -A app.celery beat --loglevel=info
