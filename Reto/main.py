import RFID_RW as rfid
from matriz import assign, clean

print("Acerque la tarjeta al lector")
menu = "Menu Gestión de Puesto de trabajo \n\t1. Asignar Tarjeta a empleado.\n\t2. Leer tarjeta de empleado\n\t3. Salir\n> "

def main():
    ids = {
        1: "",
        2: "",
        3: "",
        4: "",
    }
    clean()
    while True:
        print("¡Bienvenido!\n> Pasa tu tarjeta RFID para asignarte un puerto de trabajo\n> Pasa tu tarjeta RFID para liberar tu puesto de trabajo")
        id = rfid.read_id()
        if not list(ids.values()).__contains__(f"{id}"):
            # nuevo empleado, asignar puesto
            x = min(ids, key=ids.get)
            ids[x] = f"{id}"
        else:
            # empleado existente, liberar pueesto
            x = list(ids.keys())[list(ids.values()).index(id)]
            ids[x] = ""

        assign([k for k, v in ids.items() if v != ""])
        
        print(ids)

main()