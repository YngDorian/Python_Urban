def calculate_structure_sum(data):
    total = 0
    
    # Проверяем тип данных
    if isinstance(data, (list, tuple, set)):
        for item in data:
            total += calculate_structure_sum(item)  # Рекурсивный вызов
    elif isinstance(data, dict):
        for key, value in data.items():
            total += calculate_structure_sum(key)   # Рекурсивный вызов для ключей
            total += calculate_structure_sum(value) # Рекурсивный вызов для значений
    elif isinstance(data, str):
        total += len(data)  # Если это строка, добавляем её длину
    elif isinstance(data, (int, float)):
        total += data  # Если это число, добавляем его

    return total

# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый выход: 99
