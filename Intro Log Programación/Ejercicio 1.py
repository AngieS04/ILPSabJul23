# Ejercicio 1. Calificaciones

# Importar Librerias o Bibliotecas: Son archivos que contienen funciones
import math

# ENTRADAS DE DATOS
# Declarar o crear variables
calificación1= float(input("Ingresa la primer calificación: "))
calificación2= float(input("Ingresa la segunda calificación: "))
calificación3= float(input("Ingresa la tercer calificación: "))


# PROCESOS (Cálculos u operaciones matemáticas y/o Lógicas)
suma= calificación1 + calificación2 + calificación3
división= suma / 3

# SALIDA DE DATOS
print("el promedio de las calificaciones es:", round(división,2))

