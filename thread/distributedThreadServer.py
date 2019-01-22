#!/usr/bin/python
import random, time, Queue
from multiprocessing.managers import BaseManager
# 1.建立 task_queue和 result_queue用于存放任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()


class QueueManager(BaseManager):
    pass


# 将创建的两个队列注册在网络上,利用register
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

manager = QueueManager(address=('', 8001), authkey='abc')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()
