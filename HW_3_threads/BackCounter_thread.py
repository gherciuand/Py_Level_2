import threading
import time

count = 10
lock = threading.Lock()


class BackCounter(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global count

        while count > 0:
            lock.acquire()
            print(f"{self.name}>> {count}")
            lock.release()
            count -= 1
            time.sleep(0.1)


t1 = BackCounter("first ")
t2 = BackCounter("second ")
t3 = BackCounter("third ")

t1.start()
t2.start()
t3.start()
