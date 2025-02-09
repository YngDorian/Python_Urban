class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message) 


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)  


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        self.__is_valid_vin(self.__vin)    
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')  
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True

try:
    car1 = Car("Toyota Camry", 1234567, "ABC123")  
    print("Автомобиль 1 создан успешно.")
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e)

try:
    car2 = Car("Honda Accord", "нечисло", "ABC123") 
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e)

try:
    car3 = Car("Nissan Leaf", 123456, 123456)  
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e)

try:
    car4 = Car("Tesla Model S", 12345678, "ABCD") 
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e)
