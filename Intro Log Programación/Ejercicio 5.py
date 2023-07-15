# Ejercicio 5 Valores de la formula general. X1

# Importar Librerias o Bibliotecas: Son archivos que contienen funciones
import math

# ENTRADAS DE DATOS
# Declarar o crear variables
valordea = float(input("Ingrese el valor de a: "))
valordeb = float(input("Ingrese el valor de b: "))
valordec = float(input("Ingrese el valor de c: "))

# PROCESOS (Cálculos u operaciones matemáticas y/o Lógicas)
X1= (-valordeb- math.sqrt((pow (valordeb,2))- (4*valordea*valordec)))/2*valordea
X2= (-valordeb+ math.sqrt((pow (valordeb,2))- (4*valordea*valordec)))/2*valordea

# SALIDA DE DATOS
print("El valor de X1 es", round(X1, 2))
print("El valor de X2 es", round(X2, 2))
