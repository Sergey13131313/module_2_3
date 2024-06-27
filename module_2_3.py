# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до
# тех пор, пока не встретите отрицательное или не закончится список
# (выход за границу).

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
size = len(my_list)

while True:
    if count < size and my_list[count] >= 0:
        if my_list[count] > 0:
            print(my_list[count])
            count += 1
        elif my_list[count] == 0:
            count += 1
            continue
    else:
        break