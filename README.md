# TP Integrador: Gestión de Datos de Países en Python

Trabajo Práctico Integrador de la materia **Programación 1** de la **Tecnicatura Universitaria en Programación a Distancia**.

El programa carga un dataset de países desde un archivo CSV y permite agregar, actualizar, buscar, filtrar, ordenar y obtener estadísticas, todo desde un menú en consola.

## Integrantes

- Estudiante 1: **Flores Ibarra Dafne**
- Estudiante 2: **Sanchez Tomas**

Participación: ambos integrantes participaron en el análisis de la consigna, el diseño de las funciones, la codificación, las pruebas, la documentación y la preparación de la demostración.

## Estructura del proyecto

```
integrador-programacion/
├── main.py                                               # estructura principal y menú
├── funciones.py                                          # todas las funciones del sistema
├── paises.csv                                            # dataset base (20 países)
├── informe_trabajo_integrador_flores_sanchez.pdf         # informe académico y técnico
├── TPI_GestionPaises.zip                                 # entrega comprimida
└── README.md
```

## Instrucciones de uso

1. Tener instalado **Python 3.x** (se usó Python 3.14).
2. Descargar o clonar el repositorio.
3. Abrir una terminal dentro de la carpeta del proyecto.
4. Ejecutar:

```
python main.py
```

En Windows también puede usarse `py main.py`.

El archivo `paises.csv` debe estar en la misma carpeta que `main.py`. El programa lo busca automáticamente al lado de `main.py`, así que funciona aunque abras la terminal en otra carpeta. Si no existe, avisa y arranca con la lista vacía. No se necesitan librerías externas: el menú usa colores con códigos ANSI incluidos en Python.

## Menú de opciones

```
1 - Agregar un país
2 - Actualizar población y superficie
3 - Buscar país por nombre
4 - Filtrar por continente
5 - Filtrar por rango de población
6 - Filtrar por rango de superficie
7 - Ordenar países
8 - Ver estadísticas
9 - Mostrar todos los países
0 - Salir
```

Al salir se pregunta si se quieren guardar los cambios en el CSV. Si se responde `s`, el archivo se sobrescribe con los datos actualizados.

## Ejemplos de entrada y salida

### Ejemplo 1: búsqueda parcial

Entrada:

```
Opción: 3
Ingresá el nombre completo o una parte: bras
```

Salida:

```
Resultados de la búsqueda
------------------------------------------------------------------------
NOMBRE                         POBLACIÓN    SUPERFICIE (km²)  CONTINENTE
------------------------------------------------------------------------
Brasil                       213,993,437           8,515,767  América
------------------------------------------------------------------------
```

### Ejemplo 2: filtro por rango de población

Entrada:

```
Opción: 5
Valor mínimo: 100000000
Valor máximo: 250000000
```

Salida (fragmento):

```
Países dentro del rango
------------------------------------------------------------------------
NOMBRE                         POBLACIÓN    SUPERFICIE (km²)  CONTINENTE
------------------------------------------------------------------------
Japón                        125,800,000             377,975  Asia
Brasil                       213,993,437           8,515,767  América
México                       128,455,567           1,964,375  América
...
```

### Ejemplo 3: estadísticas

Entrada:

```
Opción: 8
```

Salida:

```
ESTADÍSTICAS
Cantidad de países: 20
País con mayor población: China (1,412,000,000 hab.)
País con menor población: Chile (19,162,922 hab.)
Promedio de población: 234,750,111.15 hab.
Promedio de superficie: 3,189,305.95 km²

Países por continente:
  América: 8
  Asia: 5
  Europa: 3
  Oceanía: 1
  África: 3
```

### Ejemplo 4: validación de entradas

Entrada:

```
Opción: 1
Nombre: [Enter sin escribir]
Nombre: Portugal
Población: abc
Población: 500
Superficie en km²: 92000
Continente: Europa
```

Salida (fragmento):

```
Error: el campo no puede quedar vacío.
Error: ingresá un número entero válido.
País agregado correctamente.
```

## Enlaces

- Repositorio del proyecto: **https://github.com/MorenaFlores/UTN-TUPaD-Programacion1-Trabajo-Integrador.git**
- Video demostrativo: **https://drive.google.com/file/d/1BUhv4qgKvvHtp9ibah3Qgws5qLuYevv2/view**


## Entrega

El archivo `TPI_GestionPaises.zip` contiene el código fuente, el CSV, este README y el informe en PDF, según el formato solicitado en la consigna.
