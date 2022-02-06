import os
import numpy as np
import random
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([],[])

os.system('cls')
clear = lambda: os.system("cls")
i = 0
Numero = 0
Condicion = 0
K = random.randint(0, 1)
Tetai = random.randint(0, 2)
Tetaj = random.randint(0, 2)
Tetai= Tetai*np.pi
Tetaj= Tetaj*np.pi
datos1 = []
datos2 = []
datos3 = []
datos3.append(1)
datos3.append(2)
datos3.append(3)
print(datos3)
print(datos3[0])

Condiciones=[]
FrecuenciaInicial=[]
Frecuenciafianl=[]
Wo=[]

print("Ingrese el numero de osciladores ")
Numero = int(input())
clear()
print("el numero de osciladores sera de: ",Numero)
print("")

def CondicionesOscilador():
    for i in range (Numero):
        print("Seleccione la condicion del oscilador",i+1)
        print("")
        
        print("Para Wo = Wf y 0 rozamiento presione  1")
        print("Para Wo =/ Wf y 0 rozamiento presione  2")
        print("Para Wo = Wf y rozamiento menor a Wo presione  3")
        print("Para Wo =/ Wf y rozamiento menor a Wo presione  4")
        Condicion = int(input())
        print("Condicion", Condicion, "acepteda")
        Condiciones.append(Condicion)
        print(Condiciones)
CondicionesOscilador()

def Datos():
    for i in range(Numero):
        print("ingrese La frecuencia incial del oscilador")      
        FrecuenciaInicial.append(float(input()))
        
def init():
    ax.set_xlim(0, 20)
    ax.set_ylim(-1, 10)
    return ln,

def update(frame):
    'plt.plot([1, 2, 3, 4], [1, 2, 3, 4])'
    'plt.axis([0, 6, 0, 20])'
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig,update, frames=np.linspace(0, 6*np.pi,500), interval = 10, init_func= init , blit = True)
plt.show()

Datos()        
print("Finalizada")
