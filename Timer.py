from Counter import Counter
from time import sleep

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(12, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()

    def is_zero(self):
        if not self.hours.get_value():
            if not self.minutes.get_value():
                if not self.seconds.get_value():
                    return True

        return False

t = Timer(1, 30, 0)

print t.is_zero()
t.tick()
print t.is_zero()

while not t.is_zero():
    print t
    t.tick()
    sleep(0.02)