#!/usr/bin/python
import os
from multiprocessing import Process

def run_proc(name):
    print "chile processing %s (%s) Running...." % (name, os.getpid())

if __name__ == '__main__':
    print "parent process %s. " % os.getpid()
    for i in range(5) :
        p = Process(target=run_proc, args=(str(i),))
        print "process will start "
        p.start()
    p.join()
    print "process end!"








