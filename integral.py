from sympy import *
import matplotlib.pyplot as plt
import numpy as np

##################################################################################################################
x = Symbol("x")
y = []
fx = eval(input("Введите функцию "))
upper = float(input("Введите вернхний предел "))
lower = float(input("Введите нижниый пердел "))
n_iter = int(input("Введите к-во итерраций "))
step = (upper-lower)/n_iter
fig,axs = plt.subplots(4)
x_for_plot = []
y_for_plot = []

#Графики функции#######################################################################################################
for j in range(1000):
    x_for_plot.append(lower+j*((upper-lower)/1000))
    y_for_plot.append(fx.subs({x:lower+j*((upper-lower)/1000)}))

axs[3].plot(x_for_plot,y_for_plot)
axs[2].plot(x_for_plot,y_for_plot)
axs[1].plot(x_for_plot,y_for_plot)
axs[0].plot(x_for_plot,y_for_plot)

#Метод левых прямоугольников ######################################################################################
x_plot = []
y_plot = []

for i in range(n_iter):
    y.append(fx.subs({x:lower+i*step}))
    axs[0].scatter(lower+i*step,fx.subs({x:lower+i*step}),color='#50ab59')
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(fx.subs({x:lower+(i)*step}))
    y_plot.append(fx.subs({x:lower+(i)*step}))
    axs[0].plot(x_plot,y_plot,color='black')
    x_plot.clear()
    y_plot.clear()
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(0)
    y_plot.append(0)
    axs[0].plot(x_plot,y_plot,color='black')

cc = step * sum(y)
print("Левые прямоугольники = ", cc)

#reboot
y = []
x_plot = []
y_plot = []

#Метод правых прямоугольников #########################################################################################
for i in range(n_iter):
    y.append(fx.subs({x:lower+(i+1)*step}))
    axs[1].scatter(lower+i*step,fx.subs({x:lower+i*step}),color="#FF00FF")
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(fx.subs({x:lower+(i+1)*step}))
    y_plot.append(fx.subs({x:lower+(i+1)*step}))
    axs[1].plot(x_plot,y_plot,color='black')
    x_plot.clear()
    y_plot.clear()
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(0)
    y_plot.append(0)
    axs[1].plot(x_plot,y_plot,color='black')


cc = step * sum(y)
print("Правые прямоугольники = ",cc)

#reboot
y = []
x_plot = []
y_plot = []

#Метод средних прямоугольников##############################################################################################
for i in range(n_iter):
    y.append(fx.subs({x:lower+i*step+step/2}))

    axs[2].scatter(lower+i*step+step/2,fx.subs({x:lower+i*step+step/2}),color="#00BFFF")
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(fx.subs({x:lower+i*step+step/2}))
    y_plot.append(fx.subs({x:lower+i*step+step/2}))
    axs[2].plot(x_plot,y_plot,color='black')
    x_plot.clear()
    y_plot.clear()
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(0)
    y_plot.append(0)
    axs[2].plot(x_plot,y_plot,color='black')

cc = step * sum(y)
print("Средние прямоугольники = ", cc)

#reboot
y = []
x_plot = []
y_plot = []
cc = 0
#Метод трапеций############################################################################################################################

for i in range(n_iter+1):
    y.append(fx.subs({x:lower+i*step}))

    axs[3].scatter(lower+i*step,fx.subs({x:lower+i*step}),color="#FF0000")
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(fx.subs({x:lower+(i)*step}))
    y_plot.append(fx.subs({x:lower+(i+1)*step}))
    axs[3].plot(x_plot,y_plot,color='black')
    x_plot.clear()
    y_plot.clear()
    x_plot.append(lower+(i)*step)
    x_plot.append(lower+(i+1)*step)
    y_plot.append(0)
    y_plot.append(0)
    axs[3].plot(x_plot,y_plot,color='black')

for j in range(len(y)-1):
    cc += (y[j]+y[j+1])/2*step

print("Трапеция = ", cc)
plt.show()
