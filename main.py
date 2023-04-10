from sympy import *

a = Symbol("a")
b = Symbol("b")
c = Symbol("c")


x = eval(input("Введите функцию: "))
av = float(input("А: "))
a_delta = float(input("▲А: "))
bv = float(input("B: "))
b_delta = float(input("▲B: "))
cv = float(input("C: "))
c_delta = float(input("▲C: "))


delta_a = x.diff(a) #производная функции по a
delta_b = x.diff(b) #производная функции по b
delta_c = x.diff(c) #производная функции по c

aa = abs(delta_a.subs({a:av, b:bv, c:cv}))
bb = abs(delta_b.subs({a:av, b:bv, c:cv}))
cc = abs(delta_c.subs({a:av, b:bv, c:cv}))

pred_pogr = aa*a_delta + bb*b_delta + cc*c_delta

x_verh = x.subs({a:av+a_delta, b:bv+b_delta, c:cv+c_delta})
x_niz = x.subs({a:av-a_delta, b:bv-b_delta, c:cv-c_delta})
x_sred = x.subs({a:av, b:bv, c:cv})
abs_pogr = (x_verh-x_niz)/2

print("Верхнее значение: ", x_verh)
print("Нижнее значение: ", x_niz)
print("Значение: ", x_sred)
print("Предельная абсолютная погрешность: ", pred_pogr)
print("Абсолютная погрешность: ", abs_pogr)
print("Относительная погрешность: ", abs_pogr/x_sred)
print("Предельная относительная погрешность: ", pred_pogr/x_sred)