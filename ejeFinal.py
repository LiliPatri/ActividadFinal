# Mostrar Lista de alumnos
def mostrar_lista_alumnos(alumnos):
    lista_alumnos = sorted(alumnos.keys())
    for alumno in lista_alumnos:
        print(alumno)

# Mostrar Lista de Notas
def mostrar_lista_notas(alumnos):
    lista_alumnos = sorted(alumnos.keys())
    for alumno in lista_alumnos:
        print(alumno + ": " + ", ".join(str(nota) for nota in alumnos[alumno]))

# Mostrar Lista de Promedios
def mostrar_lista_promedios(alumnos):
    lista_alumnos = sorted(alumnos.keys())
    for alumno in lista_alumnos:
        promedio = sum(alumnos[alumno]) / len(alumnos[alumno])
        print(alumno + ": " + str(promedio))

# Mostrar Nota Media
def mostrar_nota_media(alumnos):
    notas = []
    for alumno in alumnos:
        notas.extend(alumnos[alumno])
    nota_media = sum(notas) / len(notas)
    print("La nota media de todos los alumnos es:", nota_media)

# Mostrar Nota Media Aprobados
def mostrar_nota_media_aprobados(alumnos):
    notas_aprobados = []
    for alumno in alumnos:
        if all(nota >= 5 for nota in alumnos[alumno]):
            notas_aprobados.extend(alumnos[alumno])
    if notas_aprobados:
        nota_media_aprobados = sum(notas_aprobados) / len(notas_aprobados)
        print("La nota media de los alumnos aprobados es:", nota_media_aprobados)
    else:
        print("No hay alumnos aprobados")

# Mostrar Nota Media Suspendidos
def mostrar_nota_media_suspendidos(alumnos):
    notas_suspendidos = []
    for alumno in alumnos:
        if any(nota < 5 for nota in alumnos[alumno]):
            notas_suspendidos.extend(alumnos[alumno])
    if notas_suspendidos:
        nota_media_suspendidos = sum(notas_suspendidos) / len(notas_suspendidos)
        print("La nota media de los alumnos suspendidos es:", nota_media_suspendidos)
    else:
        print("No hay alumnos suspendidos")

# Menu
def main():
    alumnos = {}

    for i in range(20):
        nombre = input("Ingrese el nombre completo del alumno: ")
        notas = []
        while len(notas) < 3 or len(notas) > 6:
            notas = input("Ingrese las notas del alumno separadas por espacios (entre 3 y 6 notas): ").split()
            notas = [int(nota) for nota in notas if nota.isdigit()]
            if len(notas) < 3 or len(notas) > 6:
                print("Debe ingresar entre 3 y 6 notas")

        alumnos[nombre] = notas

    while True:
        print("\n--- MENÚ ---")
        print("a) Mostrar lista de alumnos")
        print("b) Mostrar lista de alumnos con notas")
        print("c) Mostrar lista de alumnos con promedios")
        print("d) Mostrar nota media de todos los alumnos")
        print("e) Mostrar nota media de los alumnos aprobados")
        print("f) Mostrar nota media de los alumnos suspendidos")
        print("g) Salir del programa")

        opcion = input("Ingrese una opción: ")

        if opcion == "a":
            mostrar_lista_alumnos(alumnos)
        elif opcion == "b":
            mostrar_lista_notas(alumnos)
        elif opcion == "c":
            mostrar_lista_promedios(alumnos)
        elif opcion == "d":
            mostrar_nota_media(alumnos)
        elif opcion == "e":
            mostrar_nota_media_aprobados(alumnos)
        elif opcion == "f":
            mostrar_nota_media_suspendidos(alumnos)
        elif opcion == "g":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
