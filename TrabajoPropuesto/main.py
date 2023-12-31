import RFID_RW as rfid
from matriz import paint

print("Acerque la tarjeta al lector")
menu = "Menu Gestión de Puesto de trabajo \n\t1. Asignar Tarjeta a empleado.\n\t2. Leer tarjeta de empleado\n\t3. Salir\n> "

def main():
    while True:
        option = input(menu)
        if option == "1":
            info = ""
            info += input("Ingrese el nombre del empleado: \n") + ","
            info += input("Ingrese el apellido del empleado: \n") + ","
            info += input("Ingrese el cargo de trabajo del empleado: \n") + ","
            info += input("Ingrese el código del empleado: \n") + ","
            info += input("Ingrese la edad del empleado: \n")

            # write json as string
            rfid.write(info)
            txt = rfid.read()
            print("Tarjeta Asignada a {}!".format(txt))
            paint('Tarjeta Asignada a {}!'.format(txt))

        elif option == "2":
            empleado = rfid.read()
            empleado = empleado.split(",")
            msgBienvenida = f'Bienvinido/a {empleado[0]} {empleado[1]}, codigo: {empleado[3]}, cargo: {empleado[2]}, edad: {empleado[4]}'
            print(msgBienvenida)
            paint(msgBienvenida)

        elif option == "3":
            exit()

main()