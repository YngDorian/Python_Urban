calls = 0

def count_calls():
    global calls  # Используем глобальную переменную
    calls += 1   # Увеличиваем счетчик
    return calls

def string_info(string):
    My_tuple = (len(string), string.upper(), string.lower())
    count_calls()  # Счетчик увеличивается при каждом вызове
    return My_tuple

def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]  # Приводим все элементы списка к нижнему регистру
    count_calls()  # Увеличиваем счетчик вызовов

    # Проверяем, содержится ли строка в списке
    return string in list_to_search

print(string_info('Capybara'))  # Пример вызова функции string_info
print(string_info('Armageddon'))  # Пример вызова функции string_info

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)  # Вывод общего числа вызовов
