import RFID_RW as rfid
import json

print("Acerque la tarjeta al lector")
menu = "Menu Gestión de Puesto de trabajo \n\t1. Asignar Tarjeta a empleado.\n\t2. Leer tarjeta de empleado\n\t3. Salir\n> "

def main():
    while True:
        option = input(menu)
        if option == "1":
            info = dict()
            info["name"] = input("Ingrese el nombre del empleado: \n")
            info["surname"] = input("Ingrese el apellido del empleado: \n")
            info["labor"] = input("Ingrese el cargo de trabajo del empleado: \n")
            info["code"] = input("Ingrese el código del empleado: \n")
            info["age"] = input("Ingrese la edad del empleado: \n")

            # write json as string
            rfid.write(json.dumps(info))
            print('Tarjeta Asignada a {}!'.format(rfid.read()))

        elif option == "2":
            empleado = rfid.read()
            print("string",empleado)
            empleado = json.loads(empleado)
            msgBienvenida = f'Bienvinid@ {empleado["name"]} {empleado["surname"]}!, código: {empleado["code"]}, cargo: {empleado["labor"]}, edad: {empleado["age"]}'
            print(msgBienvenida)

        elif option == "3":
            exit()

main()