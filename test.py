#Иванов, Таратун (Двойка № 5) ДЗ-3
#29-Mar-2023 
import numpy as np
l_col = -1 #длина матрицы
l_raw = 1  #высота матрицы




print("Введите уравнение в формате индексов через пробел")

matr = np.array(list(map(int,input().split(' ')))) #определяем размерность массива

print(matr)

while True: #Ввод матрицы
    val_of_line = input()
    if l_col +1 == l_raw:
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

resh_matr = matr[:,[l_col]]
new_matr =  np.delete(matr,l_col,axis=1) 

det_main = np.linalg.det(new_matr)
resh_matr = resh_matr.transpose()

temp = np.delete(new_matr,0 ,1)
temp = np.insert(temp,0,resh_matr, axis=1)
print("Матрица крамера")
print(temp)
#print(np.linalg.det(temp))
print(new_matr)
print(resh_matr)
