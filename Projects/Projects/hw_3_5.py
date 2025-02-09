def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку

    # Если только одна цифра осталась, просто возвращаем её
    if len(str_number) == 1:
        return int(str_number)

    # Отделяем первую цифру и рекурсивно умножаем с оставшимися цифрами
    first = int(str_number[0])  # Берём первую цифру
    return first * get_multiplied_digits(int(str_number[1:]))  # Умножаем на результат рекурсии

# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24
