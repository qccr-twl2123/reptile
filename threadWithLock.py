#!/usr/bin/python
import threading
myLock = threading.RLock()
num = 0


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            myLock.acquire()
            print "%s locked, Number is %s" % (threading.current_thread().name, num)
            if num >= 4:
                print "%s released, Number is %s" % (threading.current_thread().name, num)
                myLock.release()
                break
            num += 1
            print "%s released, Number is %s" % (threading.current_thread().name, num)
            myLock.release()


if __name__ == '__main__':
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t1.start()
    t2.start()

