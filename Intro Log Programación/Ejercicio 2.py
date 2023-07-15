# Ejercicio 1. Area y perimetro de círculo

# Importar Librerias o Bibliotecas: Son archivos que contienen funciones
import math

# ENTRADAS DE DATOS
# Declarar o crear variables
PI= 3.1416
radio= float(input("Ingresa el radio"))

# PROCESOS (Cálculos u operaciones matemáticas y/o Lógicas)
radioalcuadrado= pow (radio,2)
area= PI * radioalcuadrado
perimetro= 2 * PI * radio

# SALIDA DE DATOS
print ("El área del círculo es", round (area,2))
print ("El perímetro del círculo es", round (perimetro,2))
