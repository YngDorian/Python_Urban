class Vehicle:
    __COLOR_VARIANTS = ["Красный", "Синий", "Зеленый", "Черный", "Белый"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
            print(f'Цвет успешно сменен на {new_color}.')
        else:
            print(f'Нельзя сменить цвет на {new_color}.')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Максимальное количество пассажиров

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

# Создаём объект класса Sedan
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'Синий')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Красный')  # Правильный цвет
vehicle1.set_color('Фиолетовый')  # Неправильный цвет

# Изменяем владельца
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
