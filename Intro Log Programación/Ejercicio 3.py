# Ejercicio 3. Edad de una persona

# Importar Librerias o Bibliotecas: Son archivos que contienen funciones
import math

# ENTRADAS DE DATOS
# Declarar o crear variables
añoactual = float (input("Ingresa el año actual"))
añodenac= float (input("Ingresa tu año de nacimiento"))

# PROCESOS (Cálculos u operaciones matemáticas y/o Lógicas)
Edad= añoactual - añodenac

# SALIDA DE DATOS
print ("tu edad es", round (Edad,2))
