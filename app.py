from flask import Flask, render_template
from celery import Celery
import os
import json

from config import configuration
from tasks.celery import make_celery
from services import gamestatus_service

app = Flask(__name__)

# Celery configuration
app.config['CELERY_BROKER_URL'] = configuration.CELERY_BROKER_URL
app.config['CELERY_RESULT_BACKEND'] = configuration.CELERY_RESULT_BACKEND
celery = make_celery(app)

def main():
    app.run(host='0.0.0.0', port=configuration.APP_PORT)

@app.route("/")
def index():
    status = gamestatus_service.get_server_stats()
    return render_template('index.html', status = json.loads(status))

if __name__ == '__main__':
    main()