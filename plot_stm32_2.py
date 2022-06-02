
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
import serial
import pylab

wox = serial.Serial('COM3', 115200,stopbits=1)

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []
y_vals_t2 =[]
y_vals_voltage = []
y_vals_current = []


index = count()


def takeSer():  #Эту функцию заменить на считывалку из серийного порта.
    two_sensors = wox.readline().decode("utf-8")
    two_sensors = two_sensors.replace("\n", "")
    st_two_sensors = two_sensors.split(",")
    st_two_sensors[3] = float(st_two_sensors[3]) / 220000
    print(st_two_sensors)
    return st_two_sensors


def animate(i):
    x_vals.append(next(index))
    y_vals.append(int(takeSer()[0]))
    y_vals_t2.append(int(takeSer()[1]))
    y_vals_voltage.append(float(takeSer()[2]))
    y_vals_current.append(float(takeSer()[3]))


    pylab.subplot(2,2,1)
    pylab.plot(x_vals, y_vals)
    pylab.title("Температура аккумулятора")

    pylab.subplot(2, 2, 2)
    pylab.plot(x_vals, y_vals_t2)
    pylab.title("Температура помещения")

    pylab.subplot(2, 2, 3)
    pylab.plot(x_vals, y_vals_voltage)
    pylab.title("Напряжние аккумулятора")

    pylab.subplot(2, 2, 4)
    pylab.plot(x_vals, y_vals_current)
    pylab.title("Ток аккумулятора")



ani = FuncAnimation(plt.gcf(), animate, interval= 1000)  #get currect figure #interval 1 second


#plt.tight_layout()
plt.show()