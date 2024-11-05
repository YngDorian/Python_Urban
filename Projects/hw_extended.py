grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
name_students = list(students)
name_students = sorted(name_students)
my_dict = dict(zip(name_students, grades))
print(my_dict)