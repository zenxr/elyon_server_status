import os

APP_PORT = os.getenv('PORT', 8000)
REDIS_HOST = os.getenv('REDIS_HOST', None)
REDIS_PORT = os.getenv('REDIS_PORT', None)
if REDIS_HOST and REDIS_PORT:
    CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'
else:
    CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

server_info = {
    "servers" : {
        "leticia" : "49.236.159.67",
        "arquina" : "49.236.159.66"
    },
    "port" : "7801"
}