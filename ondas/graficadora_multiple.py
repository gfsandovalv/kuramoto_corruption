import numpy as np
import matplotlib.pyplot as plt

# condiciones inicales péndulo

pen_0 = 1000 # [⁰] amplitud inicial en grados
pen_0 *= np.pi/180 # [radianes] grados -> radianes
phi_0 = 10 # [radianes] fase inicial
l = 10 # [m] longitud de la cuerda
g = 9.8


omega = np.sqrt(g/l) # frecuencia de oscilación
def pen(t):
    return pen_0 *np.cos(omega*t+phi_0)


tempo = np.linspace(0,10,int(1E3))
outPen = pen(tempo)
plt.plot(tempo,outPen)
plt.ylabel('Frecuencia Angular')
plt.xlabel('Tiempo [s]')
plt.show()
