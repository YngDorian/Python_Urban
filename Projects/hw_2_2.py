Values = input("Введите три целых числа: ").split(" ")
First = Values[0]
Second = Values[1]
Third = Values[2]
if type(First) or type(Second) or type(Third) != int:
    print("Введены не целые числа")
    exit()
if First == Second == Third:
    print(3)
elif First== Second or Second == Third or Third == First:
    print(2)
elif First != Second != Third:
    print(0)