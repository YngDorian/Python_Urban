first = 'Мама мыла раму'
second = 'Рамена мало было'

# 1 st
result = list(map(lambda x, y: x == y, first, second))

print(result)

#2nd
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                file.write(f"{item}\n")
    
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строка:', ['A', 'это', 'ужe', 'число', 5, 'в', 'списке'])

#3 rd
import random

class MysticBall:
    def __init__(self, words):
        self.words = words 

    def __call__(self):
        return random.choice(self.words)  

ball = MysticBall(['Да', 'Нет', 'Возможно', 'Определенно да', 'Не уверен'])
print(ball())  
