#!/usr/bin/python
# -*- coding: utf-8 -*
import matplotlib.pyplot as plt 
import numpy as np
import numpy.fft 
T=np.pi;z=T/16; m=[k*z for k in np.arange(0,16,1)];arg=[];q=[]#  16 отсчётов на период в пи
def f(t):# анализируемая функция
         if t<np.pi:
                  p=np.cos(t)
         else:
                  p=-np.cos(t)
         return p
v=[f(t) for t in m]
F=np.fft.rfft(v, n=None, axis=-1) # прямое быстрое преобразование Фурье в частотную область
A=[((F[i].real)**2+(F[i].imag)**2)**0.5 for i in np.arange(0,7,1)]#модуль амплитуды
for i in np.arange(0,7,1):# определение фазы
         if F[i].imag!=0:
                  t=(-np.tanh((F[i].real)/(F[i].imag)))
                  arg.append(t)                  
         else:
                arg.append(np.pi/2)
plt.figure()
plt.title("Спектральный анализ с использованием  прямого БПФ ")
plt.plot(np.arange(0,7,1),arg,label='Фаза')
plt.plot(np.arange(0,7,1),A,label='Амплитуда')
plt.xlabel("Частота")
plt.ylabel("Фаза,Амплитуда")
plt.legend(loc='best')
plt.grid(True)
for i in np.arange(0,9,1):
         if i<=7:
                  q.append(F[i])
         else:
                  q.append(0)
h=np.fft.irfft(q, n=None, axis=-1)# обратное быстрое преобразование Фурье во временную область
plt.figure()
plt.title("Спектральный синтез с использованием  обратного БПФ ")
plt.plot(m, v,label='Исходная функция')
plt.plot(m, h,label='Синтезированная функция')
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.legend(loc='best')
plt.grid(True)          
plt.show()

