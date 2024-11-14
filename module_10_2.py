import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemy = 100
        i = 0
        while(enemy > 0):
            enemy-=self.power
            i+=1
            print(f"{self.name} сражается {i} дней(дня), осталось {enemy} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {i} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
