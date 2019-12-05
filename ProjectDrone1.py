#!/usr/bin/python
# -*- coding: utf-8 -*
from scipy.integrate import quad # модуль для интегрирования
import matplotlib.pyplot as plt # модуль для графиков
import numpy as np # модуль для операций со списками и массивами
T=np.pi; w=2*np.pi/T# период и круговая частота
def func(t):# анализируемая функция
         if t<np.pi:
                  p=np.cos(t)
         else:
                  p=-np.cos(t)
         return p
def func_1(t,k,w):# функция для расчёта коэффициента a[k]
         if t<np.pi:
                  z=np.cos(t)*np.cos(w*k*t)
         else:
                  z=-np.cos(t)*np.cos(w*k*t)
         return z
def func_2(t,k,w):#функция для расчёта коэффициента b[k]
         if t<np.pi:
                  y=np.cos(t)*np.sin(w*k*t)
         else:
                  y=-np.cos(t)*np.sin(w*k*t)
         return y
a=[];b=[];c=4;g=[];m=np.arange(0,c,1);q=np.arange(0,2*np.pi,0.01)# подготовка списков для численного анализа
a=[round(2*quad(func_1, 0, T, args=(k,w))[0]/T,3) for k in m]# интеграл для a[k], k -номер гармоники
b=[round(2*quad(func_2, 0, T, args=(k,w))[0]/T,3) for k in m]# интеграл для b[k], k -номер гармоники
plt.figure()
plt.title("Спектральный анализ \n Спектр амплитуд-A[k]")
A=np.array([(a[k]**2+b[k]**2)**0.5 for k in m])# численные значения амплитуды гармоник
plt.plot([m[1],m[1]],[0,A[1]],label='1 гармоника')
plt.plot([m[2],m[2]],[0,A[2]],label='2 гармоника')
plt.plot([m[3],m[3]],[0,A[3]],label='3 гармоника')
plt.xlabel("Номер гармоники")
plt.ylabel("Амплитуда")
plt.legend(loc='best')
plt.grid(True)
for k in m:#вычисление численных значений фазы
         if a[k]!=0:
                  g.append(-np.tanh(b[k]/a[k]))
         else:
                  g.append(-np.pi/2)# фаза когда тангенс равен бесконечности
plt.figure()
plt.title("Спектральный анализ \n Спектр фаз -g(k)")
plt.plot([m[1],m[1]],[0, g[1]],label='Фаза 1 гармоники')
plt.plot([m[2],m[2]],[0, g[2]],label='Фаза 2 гармоники')
plt.plot([m[3],m[3]],[0, g[3]],label='Фаза 3 гармоники')
plt.xlabel("Номер гармоники")
plt.ylabel("Фаза")
plt.legend(loc='best')
plt.grid(True)
plt.figure()
plt.title("Спектральный синтез - FK=A[k]*cos(w*k*t+g[k])")
FK=-np.array(a[0]/2)+np.array([0*t for t in q-1])#подготовка массива длячисленного синтеза
for k in m:
         FK=FK+np.array([A[k]*np.cos(w*k*t+g[k]) for t in q])# численный спектральный синтез
P=[func(t) for t in q]
plt.plot(q, P, label='f(t)')
plt.plot(q, FK, label='FK(t)')
plt.xlabel("Время t")
plt.ylabel("f(t),FK(t)")
plt.legend(loc='best')
plt.grid(True)
plt.show()