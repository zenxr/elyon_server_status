from celery import Celery
from .tasks import update_server_status

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    celery.autodiscover_tasks()
    setup_periodic_tasks(celery)
    return celery

def setup_periodic_tasks(celery_instance, **kwargs):
    '''
    Called after celery configuration is updated
    '''
    celery_instance.add_periodic_task(300.0, update_server_status.s(), name='add every 120')
