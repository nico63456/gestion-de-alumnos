def crear_alumno(nombre, apellido, fecha_nacimiento, dni, tutor):
    return {
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha de nacimiento": fecha_nacimiento,
        "DNI": dni,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }

# Diccionario principal con la lista de alumnos
datos = {
    "Alumnos": []
}

def mostrar_alumnos():
    if not datos["Alumnos"]:
        print("\n📭 No hay alumnos registrados.")
        return

    for i, alumno in enumerate(datos["Alumnos"], 1):
        print(f"\n📘 Alumno #{i}")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")

def agregar_alumno():
    print("\n➕ Agregar nuevo alumno:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
    dni = input("DNI: ")
    tutor = input("Nombre del Tutor: ")
    nuevo_alumno = crear_alumno(nombre, apellido, fecha_nacimiento, dni, tutor)
    datos["Alumnos"].append(nuevo_alumno)
    print("✅ Alumno agregado con éxito.")

def modificar_alumno():
    mostrar_alumnos()
    if not datos["Alumnos"]:
        return

    try:
        indice = int(input("\nIngrese el número del alumno a modificar: ")) - 1
        alumno = datos["Alumnos"][indice]
    except (ValueError, IndexError):
        print("❌ Número inválido.")
        return

    print("\nCampos disponibles para modificar:")
    print("Nombre, Apellido, Fecha de nacimiento, DNI, Tutor, Notas, Faltas, Amonestaciones")
    campo = input("Campo a modificar: ")

    if campo not in alumno:
        print("❌ Campo no válido.")
        return

    if campo == "Notas":
        nueva_nota = float(input("Ingrese la nueva nota (se añadirá a la lista): "))
        alumno["Notas"].append(nueva_nota)
    elif campo in ["Faltas", "Amonestaciones"]:
        nuevo_valor = int(input(f"Ingrese el nuevo valor para {campo}: "))
        alumno[campo] = nuevo_valor
    else:
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
        alumno[campo] = nuevo_valor

    print("✅ Datos modificados correctamente.")

def expulsar_alumno():
    mostrar_alumnos()
    if not datos["Alumnos"]:
        return

    try:
        indice = int(input("\nIngrese el número del alumno a expulsar: ")) - 1
        expulsado = datos["Alumnos"].pop(indice)
        print(f"✅ Alumno {expulsado['Nombre']} {expulsado['Apellido']} expulsado.")
    except (ValueError, IndexError):
        print("❌ Número inválido.")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Mostrar alumnos")
        print("2. Agregar alumno")
        print("3. Modificar alumno")
        print("4. Expulsar alumno")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            mostrar_alumnos()
        elif opcion == "2":
            agregar_alumno()
        elif opcion == "3":
            modificar_alumno()
        elif opcion == "4":
            expulsar_alumno()
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")

# Ejecutar el programa
if __name__ == "_main_":
    menu()