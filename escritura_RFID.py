import RPi.GPIO as GPIO
import MFRC522
import signal
from mfrc522 import SimpleMFRC522

continue_reading = True

def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()
reader = SimpleMFRC522()

def griteRegistro():
    print("==========\nAgregar Registro \n ==========")
    nombres = input("Ingrese texto a escribir \n")
    print("Coloque el chip RFID sobre el lector")

    reader.write(text)
    print("Escritorio")
menu = "Menu de opciones \n\t1. Leer registros. \nIngrese la opciones que desea ejecutar\n"

def showTerminal():
    while True:
        option = input(menu)
        if option == "1":
            print("Leyendo Registro")
            readRFID()
        elif option == "2":
            griteRegistro()
        else:
            print("Opcion no valida")

showTerminal()