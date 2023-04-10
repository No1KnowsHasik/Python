import numpy as np


def create_matr(dim, mode): #Создание квадратной матрицы
    if mode == 1:   #1 рандом
        temp = np.random.random((dim,dim))
        return np.around(temp,3)
    if mode == 2:   #2 нули                                        
        return np.full((dim, dim), 0)
    if mode == 3:   #3 число пользователя
        return np.full((dim, dim), int(input("Введите число которым заполнить матрицу: ")))
    else:
        return 0
    

def minor(arr,i,j): #Функция возвращет минор строки i и столбца j
    return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
               np.array(list(range(j))+list(range(j+1,arr.shape[1])))]

while True:
    print("""1-создать матрицу
2-посмотреть матрицу
3-минор
4-определитель
5-выход""")
    v1 = int(input("Что?: "))
    if v1 == 1:
        print("Режимы: 1-рандом 2-нули 3-custom")
        matr = create_matr(int(input("Введите размерность мартицы: ")),int(input("Выберете режим: ")))
    if v1 == 2:
        print(matr)
        input("Нажмите Enter чтобы продолжить")
    if v1 == 3:
        new_matr = minor(matr,int(input("Выберете строку: ")),int(input("Выберете столбец: ")))
        print(new_matr)
        input("Нажмите Enter чтобы продолжить")
    if v1 == 4:
        print(np.linalg.det(matr))
        input("Нажмите Enter чтобы продолжить")
    if v1 == 5:
        break



