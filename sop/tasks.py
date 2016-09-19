from __future__ import absolute_import

from celery import shared_task


@shared_task
def add(x, y):
    print ("\n\n****** task add")
    return x + y


@shared_task
def mul(x, y):
    print ("\n\n****** task mul")
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)