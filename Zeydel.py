#Иванов, Таратун (Двойка № 5) ДЗ-3
#29-Mar-2023
import numpy as np
l_col = -1 #длина матрицы
l_raw = 1  #высота матрицы
otvet = []

def deter(matr,raw,resh): #определитель матрицы Крамера
    temp = np.delete(matr,raw ,1)
    temp = np.insert(temp,raw,resh, axis=1)
    print("Матрица крамера ", "X", raw+1, sep="")
    print(temp)
    return np.linalg.det(temp)

print("Введите уравнение в формате индексов через пробел")
matr = np.array(list(map(int,input().split(' '))))
print(matr)

while True: #Ввод матрицы
    val_of_line = input()
    if l_col == l_raw:
        print("Вы ввели лишнюю строку")
        break
    if val_of_line != "":
        temp = list(map(int,val_of_line.split(' ')))
        matr = np.vstack([matr,temp])
        print(matr)
    else:
        break
    l_col = len(matr)
    l_raw = len(matr[0])

for i in range(l_col): #Вывод матрицы
    print()
    for j in range(l_raw-1):
        if matr[i,j+1] < 0:
            print(matr[i,j],"x",j+1, sep = "", end="")
        else:
            print(matr[i,j],"x",j+1, sep = "", end="")
            if j < l_raw-2:
                print("+", sep="", end="")
    print("=", matr[i,l_raw-1],end="",sep = "")
print("\n")
resh_matr = matr[:,[l_col]]
resh_matr = resh_matr.transpose()
new_matr =  np.delete(matr,l_col,axis=1)
det_main = np.linalg.det(new_matr)

for i in range(l_col):
    tt = deter(new_matr,i,resh_matr)
    print("Определитель матрицы Крамера ","X",i+1," = ", round(tt,2),"\n", sep ="")
    otvet.append(round(tt/det_main,2))

for i in range(len(otvet)):
    print("X", i+1, " = ", otvet[i], sep = "")


eps = 0.01
max_iter = 5

if not np.all(np.linalg.eigvals(A) > 0):
    print("Матрица не является положительно определенной")
else:
    n = A.shape[0]
    x = x0.copy()
    delta = eps + 1
    num_iter = 0
    while delta > eps and num_iter < max_iter:
        x_new = np.zeros(n)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        delta = np.max(np.abs(x - x_new))
        x = x_new.copy()
        num_iter += 1

    if num_iter == max_iter:
        print("Метод Зейделя не сошелся за заданное число итераций")
    else:
        print("Решение системы:", x)
