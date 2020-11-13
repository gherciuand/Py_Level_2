import random
#Definim clasa
class RandomInteger:
    def __init__(self): #setam variabile
        self.n = 1
        self.c = 1

    def __next__(self): #setam pasul
        self.n = random.randint(1, 1000)
        if self.c <= 10:
            self.c += 1
            return self.n
        else:
            raise StopIteration

    def __iter__(self): # iteram pe sine insusi
        return self


ri = RandomInteger()
for i in ri:
    print(i)
