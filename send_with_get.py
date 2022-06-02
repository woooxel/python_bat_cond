import serial
import requests

wox = serial.Serial('COM3', 115200,stopbits=1) #Открыли порт

link = "http://sugwox.ru/temper/?temp0="
#http://sugwox.ru/temper/?temp0=50&temp1=700&voltage=10&current=100

while True:
    two_sensors = wox.readline().decode("utf-8")
    two_sensors = two_sensors.replace("\n","")
    st_two_sensors = two_sensors.split(",")
    st_two_sensors[3] = float(st_two_sensors[3])/440000
    print(st_two_sensors)
    requests.get(link+st_two_sensors[0]+"&temp1=700&voltage=10&current=100")

