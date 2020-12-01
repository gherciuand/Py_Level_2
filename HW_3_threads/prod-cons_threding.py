from threading import Thread, RLock, Condition
from time import sleep
from random import random

mobilePhones = [{"brand": "Apple", "model": "iPhone XIII"}]
lock = RLock()
condition = Condition(lock)


class Producer(Thread):
    def __init__(self, brand):
        Thread.__init__(self)
        self.brand = brand

    def run(self):
        global mobilePhones
        lock.acquire()
        sleep(random())

        mobilePhones.append({"brand": self.brand, "model": "iPhone XII"})
        print(f'Factory {self.brand} produced a phone')

        #condition.notify(5)
        lock.release()


class Consumer(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(random())
        lock.acquire()
        global mobilePhones
        mobile = mobilePhones.pop()
        print(f" {self.name} takes >>> PHONE: {mobile['brand']} | {mobile['model']}")
        print(f' remain in stock {mobilePhones}')
        #condition.wait()
        lock.release()


factory = Producer("Apple")
cons = Consumer("Andrei")
cons_2 = Consumer("Ion")
#cons_3 = Consumer("Dima")

cons.start()
cons_2.start()
#cons_3.start()
factory.start()
