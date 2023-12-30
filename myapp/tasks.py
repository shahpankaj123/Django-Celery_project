from celery import shared_task
from time import sleep


@shared_task
def sub(x,y):
    sleep(10)
    return x-y
