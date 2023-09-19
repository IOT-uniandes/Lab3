import RFID_RW as rfid

print("Acerque la tarjeta al lector")
menu = "Menu Gestión de Puesto de trabajo \n\t1. Asignar Tarjeta a empleado.\n\t2. Leer tarjeta de empleado"

def main():
    while True:
        option = input(menu)
        if option == "1":
            txt = input("Ingrese el nombre del empleado: \n")
            rfid.write(txt)
            print('Tarjeta Asignada a {}!'.format(rfid.read().rstrip()))

        elif option == "2":
            empleado = rfid.read()
            msgBienvenida = 'Bienvinid@ {}!'.format(empleado.rstrip())
            print(msgBienvenida)

main()