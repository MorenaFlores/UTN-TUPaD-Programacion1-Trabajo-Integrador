import os

from funciones import limpiar_pantalla, pedir_opcion, mostrar_menu, pausar
from funciones import agregar_pais, actualizar_pais, buscar_pais
from funciones import filtrar_por_continente, filtrar_por_rango
from funciones import elegir_orden, ordenar_paises, mostrar_lista
from funciones import mostrar_estadisticas, preguntar_si_no, guardar_paises, leer_paises
from funciones import VERDE, AMARILLO, RESET

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV = os.path.join(CARPETA, "paises.csv")

paises = leer_paises(RUTA_CSV)


salir = False
while salir == False:
    limpiar_pantalla()
    mostrar_menu()
    opcion = pedir_opcion(0, 9)

    match opcion:
        case 1:
            agregar_pais(paises)
        case 2:
            actualizar_pais(paises)
        case 3:
            buscar_pais(paises)
        case 4:
            filtrar_por_continente(paises)
        case 5:
            filtrar_por_rango(paises, "poblacion", "población")
        case 6:
            filtrar_por_rango(paises, "superficie", "superficie")
        case 7:
            campo, descendente = elegir_orden()
            ordenados = ordenar_paises(paises, campo, descendente)
            mostrar_lista("Países ordenados", ordenados)
        case 8:
            mostrar_estadisticas(paises)
        case 9:
            mostrar_lista("Todos los países", paises)
        case 0:
            salir = True

    if salir == False:
        pausar()

if preguntar_si_no("¿Querés guardar los cambios en el CSV?"):
    guardar_paises(RUTA_CSV, paises)
    print(VERDE + "Cambios guardados en " + str(RUTA_CSV) + "." + RESET)
else:
    print(AMARILLO + "Los cambios no se guardaron." + RESET)
