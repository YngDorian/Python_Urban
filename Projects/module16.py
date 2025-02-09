my_dict = {1: 34, 2: 88, 3: 97}
print(my_dict)
print("Exist: ", my_dict[1])
print("Exist: ", my_dict.get('4'))
my_dict.update({
    4: 108,
    5: 198
})
my_dict.pop(4)
print(my_dict)
my_set = {1, 2.99, 'sdhfsd', 1, 2.99, 'sdhfsd'}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.remove(1)
print(my_set)