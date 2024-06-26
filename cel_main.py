from celery import Celery
import time

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def TaskQueue(message):
    print("TaskQueue1: {0}".format(message))
    return "QUEUE DONE."

@app.task
def write_log(logs):
    print("Writing Logs2: {0}".format(logs))
    return "LOGS WRITTEN."