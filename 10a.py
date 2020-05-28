"""а) Дан файл f, компоненти якого є цілими числами. Отримати в файлі g всі
компоненти файлу f що є простими числами. Простим називається число, що більше за 1
та не має інших дільників, окрім 1 та самого себе)"""


def get_integers():
    with open("C:\\Users\\Toma\Desktop\\NewFold\\f.txt") as file_start:
        for integer in file_start:
            integers = integer.split()
    file_start.close()
    return integers


def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


data = get_integers()
with open("C:\\Users\\Toma\Desktop\\NewFold\\g.txt", "w") as file_end:
    for i in data:
        if is_prime(int(i)) == True:
            file_end.write(i + ' ')
file_end.close()