import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # исправлено на _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
            return

        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def get_cords(self):
        return self._cords

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        return self.sound if self.sound else "No sound"

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        # Используйте random для генерации случайного числа от 1 до 4
        num_eggs = random.randint(1, 4)
        return f"Here are {num_eggs} eggs for you"

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] += abs(dz) * self.speed / 2  # Уменьшает z-координату

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

# Пример использования
if __name__ == "__main__":
    duckbill = Duckbill(speed=3)
    duckbill.move(2, 3, -1)
    print(duckbill.get_cords())
    print(duckbill.attack())
    print(duckbill.speak())
    print(duckbill.lay_eggs())

db = Duckbill(10)



print(db.live)

print(db.beak)



db.speak()

db.attack()



db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()



db.lay_eggs()

