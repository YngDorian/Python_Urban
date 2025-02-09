Mylist = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while Mylist[i] >= 0:
    if Mylist[i] > 0:
        print(Mylist[i])
    elif Mylist[i] < 0:
        break
    i = i +1
