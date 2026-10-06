
# Listas y diccionarios

semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

filas_Id = ["A","B","C","D","E"]


cartelera = {
    "Lunes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "2:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "4:30 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 3, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "5:30 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 5, "horario": "8:00 pm", "formato": "CXC"},
    ],
    "Martes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "5:00 pm", "formato": "4DX"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 1, "horario": "7:00 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 5, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "El Final", "sala": 4, "horario": "9:00 pm", "formato": "Normal"},
    ],
    "Miércoles": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "2:30 pm", "formato": "CXC"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "7:30 pm", "formato": "3D"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 2, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 3, "horario": "8:30 pm", "formato": "4DX"},
    ],
    "Jueves": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 2, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 3, "horario": "3:30 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 4, "horario": "8:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "2:00 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 5, "horario": "5:30 pm", "formato": "CXC"},
    ],
    "Viernes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 5, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 4, "horario": "7:00 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "5:30 pm", "formato": "CXC"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 3, "horario": "9:00 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 2, "horario": "2:30 pm", "formato": "4DX"},
    ],
    "Sábado": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 5, "horario": "8:30 pm", "formato": "3D"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "4:30 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 3, "horario": "7:30 pm", "formato": "CXC"},
    ],
    "Domingo": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "2:30 pm", "formato": "3D"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "7:00 pm", "formato": "CXC"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "8:30 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
    ],
}

asientos = {}

for dia in semana:
    for numero_sala in range(1, 6):
        matriz_asientos=[]

        for f in range(5):
            fila = [".",".",".",".",".","."]
            matriz_asientos.append(fila)
        asientos[f"{dia}-{numero_sala}"] = matriz_asientos

# Funcion de mostrar la cartelera


def mostrar_cartelera():
    print("\n~~~~~ Cartelera de la semana ~~~~~\n")
    dia = input("Ingresar día de interes: ").capitalize()

    if dia in cartelera:
        print(f"\nPelículas disponibles para {dia}:")
        for dataCartelera in cartelera[dia]:
            print(f" | Sala {dataCartelera['sala']}: {dataCartelera['pelicula']} - Horario: {dataCartelera['horario']} - Formato: {dataCartelera['formato']}")
    else:
        print("Dia no válido, vuelva a intentar !!")


# funcion mostrar los asientos


def mostrar_asientos(dia, sala):
    diaSeleccionado = f"{dia}-{sala}"
    
    if diaSeleccionado in asientos:
        matriz = asientos[diaSeleccionado]
        print(f"\n--- Vista previa de la sala: {sala} el {dia}, elige un asiento que tengas disponible")
        print("  1 2 3 4 5 6")
        for i in range(len(matriz)):
            fila_str = filas_Id[i] + " " + " ".join(matriz[i])
            print(fila_str)
    else:
        print("Reserva erronea.")


# Funcion de reservar


def reservar():
    dia = input("Día de la función: ").capitalize()

    while True:
        try:
            sala = int(input("Número de sala (1 a 5): "))
            if sala >= 1 and sala <= 5:
                break  # Si el número es válido, rompemos el while y seguimos
            else:
                print("Error: La sala debe ser un número entre el 1 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido, no letras.")

    reservacion = f"{dia}-{sala}"

    if reservacion not in asientos:
        print("Día o sala incorrectos.")
        return

    mostrar_asientos(dia, sala)
    
    asiento = input("Ingrese el asiento a reservar. \n\n Ej: A3): ").upper()
    if len(asiento) < 2:
        print("Formato de asiento inválido.")
        return
        
    letra = asiento[0]
    
    try:
        columna = int(asiento[1:]) - 1
    except ValueError:
        print("Asiento incorrecto.")
        return

    if letra in filas_Id and 0 <= columna < 6:
        fila_idx = filas_Id.index(letra)
        matriz = asientos[reservacion]
        
        if matriz[fila_idx][columna] == '.':
            nombre = input("Ingrese su nombre: ")
            matriz[fila_idx][columna] = 'X'
            print(f"Asiento {asiento} reservado correctamente para:\n --- {nombre}")
        else:
            print(f"Lo siento, el asiento {asiento} ya está reservado.")
    else:
        print("El asiento ingresado está fuera de rango.")


# funcion de cancelacion de la reservacion


def cancelar_reserva():
    dia = input("Día de la función: ").capitalize()

    try:
        sala = int(input("Número de sala (1 a 5): "))
    except ValueError:
        print("Número de sala no válido.")
        return

    reserva = f"{dia}-{sala}"
    if reserva not in asientos:
        print("Día o sala incorrectos.")
        return

    mostrar_asientos(dia, sala)
    
    asiento = input("Ingrese el asiento a cancelar (Ej: A3): ").upper()
    if len(asiento) < 2:
        print("Formato incorrecto.")
        return

    letra = asiento[0]
    try:
        columna = int(asiento[1:]) - 1
    except ValueError:
        print("Asiento inválido.")
        return

    if letra in filas_Id and 0 <= columna < 6:
        fila_idx = filas_Id.index(letra)
        matriz = asientos[reserva]
        
        if matriz[fila_idx][columna] == 'X':
            matriz[fila_idx][columna] = '.'
            print(f"¡Reserva del asiento {asiento} cancelada con éxito!")
        else:
            print(f"El asiento {asiento} ya se encuentra libre.")
    else:
        print("Asiento fuera de rango.")

def ver_disponibilidad():

    dia = input("Ingrese el día a consultar: ").capitalize()
    if dia in cartelera:
        print(f"\n--- DISPONIBILIDAD PARA EL DÍA {dia} ---")
        for funcion in cartelera[dia]:
            sala = funcion['sala']
            reservacion = f"{dia}-{sala}"
            matriz = asientos[reservacion]
            
            libres = 0
            ocupados = 0
            for fila in matriz:
                libres += fila.count('.')
                ocupados += fila.count('X')
            
            print(f"Sala {sala} {funcion['pelicula']} => Libres: {libres} | Ocupados: {ocupados}")
    else:
        print("Día no válido.")

def main():

    while True:
        print("""

|========================================================|
|======= CineMax - Sistema de Reservas de peliculas =====|
|========================================================|

        """)
        print("1. Ver cartelera de un día")
        print("2. Mostrar asientos de una función")
        print("3. Reservar asiento")
        print("4. Cancelar reserva")

        print("5. Ver disponibilidad\n")

        print("6. Salir\n")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_cartelera()
        elif opcion == '2':
            d = input("Día: ").capitalize()

            try:
                s = int(input("Sala (1-5): "))
                mostrar_asientos(d, s)
            except ValueError:
                print("Entrada inválida.")

        elif opcion == '3':
            reservar()
        elif opcion == '4':
            cancelar_reserva()
        elif opcion == '5':
            ver_disponibilidad()
        elif opcion == '6':
            print("¡Gracias por usar CineMax!")
            break
        else:
            print("Opción no válida. Intente del 1 al 6.")

main()