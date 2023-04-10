import numpy as np

matr = np.array([[1,2,3],[2,-1,2],[1,1,5]])
mm = [1,6,-1]
det_main = np.linalg.det(matr)
if det_main == 0:
    print("определитель матрицы равен нулю")

zxc = ["X","Y","Z"]

for i in range(3):
    print(matr[i,0],"x + ",matr[i,1],"y + ",matr[i,2],"z ","= " , mm[i],sep="")

def deter(matr,raw,resh):
    temp = np.delete(matr,raw ,1)
    temp = np.insert(temp,raw,resh, axis=1)
    print("Матрица крамера", zxc[raw])
    print(temp)
    return np.linalg.det(temp)


print("Вот наша матрица")
print(matr)
print("Вот наше решение ур-ний")
print(mm)

for i in range(3):
    tt = deter(matr,i,mm)
    print("Определитель матрицы крамера", zxc[i], tt)
    print(zxc[i], " = ",tt/det_main)





