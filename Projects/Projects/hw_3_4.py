def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()  # Приводим корень к нижнему регистру

    for word in other_words:
        # Приводим к нижнему регистру для нечувствительности к регистру
        lower_word = word.lower()
        # Проверяем, содержит ли слово корень или корень содержит слово
        if root_word in lower_word or lower_word in root_word:
            same_words.append(word)  # Добавляем оригинальное слово

    return same_words

# Вызовы функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результата
print(result1)  # Ожидается ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидается ['Able', 'Disable']
