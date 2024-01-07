from celery import shared_task
from time import sleep


@shared_task
def sub(x,y):
    sleep(10)
    return x-y

@shared_task
def send_msg():
    print(f'hello hi {2+2}')

@shared_task
def send_msg1():
    print(f'hello bye {2+5}')    
