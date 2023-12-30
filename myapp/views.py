from django.shortcuts import render
from Django_celery.celery import add
from .tasks import sub
from celery.result import AsyncResult


def home(request):
    print(add.delay(10,20))
    print(sub.delay(10,20))
    return render(request,'index.html')

def About(request):
    result=add.delay(10,50)
    return render(request,'about.html',{'result':result})

def Result(request,Task_id):
    result=AsyncResult(Task_id)
    return render(request,'result.html',{'result':result})


def Contact(request):
    print("Result")
    return render(request,'contact.html')

