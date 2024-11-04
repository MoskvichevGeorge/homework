import threading
import time


warriors = 100
warriors_lock = threading.Lock()

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        global warriors
        print(f"{self.name}, на нас напали!")

        while True:
            time.sleep(1)
            self.days += 1

            with warriors_lock:
                warriors -= self.power
                remaining_warriors = max(warriors, 0)

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {remaining_warriors} воинов.")

            if remaining_warriors <= 0:
                print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()

print("Все битвы закончились!")