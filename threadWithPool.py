#!/usr/bin/python
import os, time, random
from multiprocessing import Pool

def run_task(name):
    print "task  (%s) pid (%s) runing" % (name, os.getpid())
    time.sleep(random.random() * 3)
    print 'task %s end.' % name

if __name__ == '__main__':
    print "parent process %s runing" % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i, ))

    print "waiting for all process is done"
    p.close()
    p.join()
    print "end"



