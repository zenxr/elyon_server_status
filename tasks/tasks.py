from celery import shared_task

from services import gamestatus_service

@shared_task
def update_server_status():
    '''
    Registers a task
    '''
    gamestatus_service.store_server_stats()