import RFID_RW as rfid
from matriz import assign

print("Acerque la tarjeta al lector")
menu = "Menu Gestión de Puesto de trabajo \n\t1. Asignar Tarjeta a empleado.\n\t2. Leer tarjeta de empleado\n\t3. Salir\n> "

def main():
    ids = {
        1: "",
        2: "",
        3: "",
        4: "",
    }
    while True:
        print("¡Bienvenido!\n> Pasa tu tarjeta RFID para asignarte un puerto de trabajo\n> Pasa tu tarjeta RFID para liberar tu puesto de trabajo")
        id = rfid.read_id()
        print(ids)
        if id not in ids.values():
            # nuevo empleado, asignar puesto
            x = min(ids, key=ids.get)
            ids[x] = id
            assign(x, True)
        else:
            # empleado existente, liberar pueesto
            x = list(ids.keys())[list(ids.values()).index(id)]
            ids[x] = ""
            assign(x, False)

main()