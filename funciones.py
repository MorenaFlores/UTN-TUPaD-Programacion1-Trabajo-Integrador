import os
import unicodedata

AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


# Ejercicio: limpiar la pantalla
def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Normalizar un texto para comparar nombres sin distinguir tildes ni mayúsculas
def normalizar_texto(texto):
    texto_normalizado = unicodedata.normalize("NFD", texto)
    texto_sin_tildes = "".join(
        caracter
        for caracter in texto_normalizado
        if unicodedata.category(caracter) != "Mn"
    )
    return texto_sin_tildes.casefold()


# Ejercicio: pedir un texto que no esté vacío
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print(ROJO + "Error: el campo no puede quedar vacío." + RESET)


# Ejercicio: pedir un número entero
def pedir_entero(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
            if numero < 0:
                print(ROJO + "Error: el número no puede ser negativo." + RESET)
            else:
                return numero
        except ValueError:
            print(ROJO + "Error: ingresá un número entero válido." + RESET)


# Ejercicio: pedir una opción de menú
def pedir_opcion(minimo, maximo):
    while True:
        texto = input("Opción: ").strip()
        try:
            opcion = int(texto)
            if opcion >= minimo and opcion <= maximo:
                return opcion
            print(ROJO + "Error: elegí una opción entre " +
                  str(minimo) + " y " + str(maximo) + "." + RESET)
        except ValueError:
            print(ROJO + "Error: ingresá un número." + RESET)


# Ejercicio: preguntar sí o no
def preguntar_si_no(mensaje):
    while True:
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta == "s" or respuesta == "si":
            return True
        if respuesta == "n" or respuesta == "no":
            return False
        print(ROJO + "Error: respondé con s o n." + RESET)


# Ejercicio: hacer una pausa
def pausar():
    input("\nPresioná Enter para continuar...")


# Ejercicio: leer los países desde el archivo CSV
def leer_paises(ruta_archivo):
    paises = []
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8-sig")
    except FileNotFoundError:
        print(AMARILLO + "Aviso: no se encontró " + ruta_archivo +
              ". Se empieza con la lista vacía." + RESET)
        return paises

    with archivo:
        encabezado = archivo.readline().strip()
        if encabezado != "nombre,poblacion,superficie,continente":
            print(ROJO + "Error: encabezado del CSV inválido. Se esperaba: nombre,poblacion,superficie,continente" + RESET)
            return paises

        numero_linea = 1
        for linea in archivo:
            numero_linea = numero_linea + 1
            datos = linea.strip().split(",")
            if len(datos) != 4:
                print(AMARILLO + "Fila " + str(numero_linea) +
                      " ignorada: cantidad de campos incorrecta." + RESET)
                continue

            nombre = datos[0].strip()
            continente = datos[3].strip()
            if nombre == "" or continente == "":
                print(AMARILLO + "Fila " + str(numero_linea) +
                      " ignorada: hay campos de texto vacíos." + RESET)
                continue

            try:
                poblacion = int(datos[1].strip())
                superficie = int(datos[2].strip())
            except ValueError:
                print(AMARILLO + "Fila " + str(numero_linea) +
                      " ignorada: población o superficie no son números." + RESET)
                continue

            if poblacion < 0 or superficie < 0:
                print(AMARILLO + "Fila " + str(numero_linea) +
                      " ignorada: los números no pueden ser negativos." + RESET)
                continue

            pais = {
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente,
            }
            paises.append(pais)

    print(VERDE + "Se cargaron " + str(len(paises)) +
          " países desde " + str(ruta_archivo) + "." + RESET)
    return paises


# Ejercicio: guardar los países en el archivo CSV
def guardar_paises(ruta_archivo, paises):
    archivo = open(ruta_archivo, "w", encoding="utf-8")
    with archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            fila = pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(
                pais["superficie"]) + "," + pais["continente"] + "\n"
            archivo.write(fila)


# Ejercicio: mostrar una lista de países
def mostrar_lista(titulo, lista):
    print("\n" + NEGRITA + AZUL + titulo + RESET)
    if len(lista) == 0:
        print(AMARILLO + "No hay países para mostrar." + RESET)
        return

    print("-" * 72)
    print(f"{'NOMBRE':<24}{'POBLACIÓN':>16}{'SUPERFICIE (km²)':>20}  CONTINENTE")
    print("-" * 72)
    for pais in lista:
        print(
            f"{pais['nombre']:<24}{pais['poblacion']:>16,}{pais['superficie']:>20,}  {pais['continente']}")
    print("-" * 72)


# Ejercicio: agregar un país
def agregar_pais(paises):
    print("\n" + NEGRITA + "ALTA DE PAÍS" + RESET)
    nombre = pedir_texto("Nombre: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(ROJO + "Ese país ya está cargado. No se agregó." + RESET)
            return

    poblacion = pedir_entero("Población: ")
    superficie = pedir_entero("Superficie en km²: ")
    continente = pedir_texto("Continente: ")

    pais_nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(pais_nuevo)
    print(VERDE + "País agregado correctamente." + RESET)


# Ejercicio: actualizar población y superficie de un país
def actualizar_pais(paises):
    print("\n" + NEGRITA + "ACTUALIZAR DATOS" + RESET)
    nombre = pedir_texto("Nombre del país a actualizar: ")

    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais

    if pais_encontrado is None:
        print(ROJO + "No se encontró un país con ese nombre." + RESET)
        return

    mostrar_lista("País seleccionado", [pais_encontrado])
    pais_encontrado["poblacion"] = pedir_entero("Nueva población: ")
    pais_encontrado["superficie"] = pedir_entero("Nueva superficie en km²: ")
    print(VERDE + "Datos actualizados correctamente." + RESET)


# Ejercicio: buscar un país por nombre
def buscar_pais(paises):
    print("\n" + NEGRITA + "BUSCAR PAÍS" + RESET)
    texto = pedir_texto("Ingresá el nombre completo o una parte: ")
    texto = texto.lower()

    resultados = []
    for pais in paises:
        if texto in pais["nombre"].lower():
            resultados.append(pais)

    mostrar_lista("Resultados de la búsqueda", resultados)


# Ejercicio: filtrar países por continente
def filtrar_por_continente(paises):
    print("\n" + NEGRITA + "FILTRAR POR CONTINENTE" + RESET)
    continente = normalizar_texto(pedir_texto("Continente: "))

    resultados = []
    for pais in paises:
        if normalizar_texto(pais["continente"]) == continente:
            resultados.append(pais)

    mostrar_lista("Países de ese continente", resultados)


# Ejercicio: filtrar países por un rango de valores
def filtrar_por_rango(paises, campo, etiqueta):
    print("\n" + NEGRITA + "FILTRAR POR RANGO DE " + etiqueta.upper() + RESET)
    minimo = pedir_entero("Valor mínimo: ")
    maximo = pedir_entero("Valor máximo: ")

    if minimo > maximo:
        print(ROJO + "Error: el mínimo no puede ser mayor que el máximo." + RESET)
        return

    resultados = []
    for pais in paises:
        valor = pais[campo]
        if valor >= minimo and valor <= maximo:
            resultados.append(pais)

    mostrar_lista("Países dentro del rango", resultados)


# Ejercicio: elegir el campo y el sentido del ordenamiento
def elegir_orden():
    print("\n" + NEGRITA + "ELEGIR ORDENAMIENTO" + RESET)
    print("1 - Nombre")
    print("2 - Población")
    print("3 - Superficie")
    opcion_campo = pedir_opcion(1, 3)

    if opcion_campo == 1:
        campo = "nombre"
    elif opcion_campo == 2:
        campo = "poblacion"
    else:
        campo = "superficie"

    print("1 - Ascendente")
    print("2 - Descendente")
    opcion_sentido = pedir_opcion(1, 2)

    if opcion_sentido == 1:
        descendente = False
    else:
        descendente = True

    return campo, descendente


# Ejercicio: ordenar países con el método de burbuja
def ordenar_paises(paises, campo, descendente):
    ordenados = []
    for pais in paises:
        ordenados.append(pais)

    cantidad = len(ordenados)
    for i in range(cantidad):
        for j in range(0, cantidad - i - 1):
            actual = ordenados[j][campo]
            siguiente = ordenados[j + 1][campo]
            if campo == "nombre":
                actual = actual.lower()
                siguiente = siguiente.lower()

            if descendente:
                cambiar = actual < siguiente
            else:
                cambiar = actual > siguiente

            if cambiar:
                auxiliar = ordenados[j]
                ordenados[j] = ordenados[j + 1]
                ordenados[j + 1] = auxiliar

    return ordenados


# Ejercicio: mostrar las estadísticas del dataset
def mostrar_estadisticas(paises):
    print("\n" + NEGRITA + AZUL + "ESTADÍSTICAS" + RESET)
    if len(paises) == 0:
        print(AMARILLO + "No hay datos para calcular estadísticas." + RESET)
        return

    total_poblacion = 0
    total_superficie = 0
    pais_mayor = paises[0]
    pais_menor = paises[0]
    continentes = {}

    for pais in paises:
        total_poblacion = total_poblacion + pais["poblacion"]
        total_superficie = total_superficie + pais["superficie"]

        if pais["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = pais
        if pais["poblacion"] < pais_menor["poblacion"]:
            pais_menor = pais

        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] = continentes[continente] + 1
        else:
            continentes[continente] = 1

    cantidad = len(paises)
    promedio_poblacion = total_poblacion / cantidad
    promedio_superficie = total_superficie / cantidad

    print("Cantidad de países: " + str(cantidad))
    print("País con mayor población: " +
          pais_mayor["nombre"] + " (" + f"{pais_mayor['poblacion']:,}" + " hab.)")
    print("País con menor población: " +
          pais_menor["nombre"] + " (" + f"{pais_menor['poblacion']:,}" + " hab.)")
    print("Promedio de población: " + f"{promedio_poblacion:,.2f}" + " hab.")
    print("Promedio de superficie: " + f"{promedio_superficie:,.2f}" + " km²")
    print("\nPaíses por continente:")
    for continente in continentes:
        print("  " + continente + ": " + str(continentes[continente]))


# Ejercicio: mostrar el menú principal
def mostrar_menu():
    print(NEGRITA + AZUL + "========================================" + RESET)
    print(NEGRITA + AZUL + "   GESTIÓN DE DATOS DE PAÍSES" + RESET)
    print(NEGRITA + AZUL + "========================================" + RESET)
    print("1 - Agregar un país")
    print("2 - Actualizar población y superficie")
    print("3 - Buscar país por nombre")
    print("4 - Filtrar por continente")
    print("5 - Filtrar por rango de población")
    print("6 - Filtrar por rango de superficie")
    print("7 - Ordenar países")
    print("8 - Ver estadísticas")
    print("9 - Mostrar todos los países")
    print("0 - Salir")
