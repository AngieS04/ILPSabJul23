# Ejemplo 2. Operaciones Matemáticas

# Importar Librerias o Bibliotecas: Son archivos que contienen funciones
import math

# ENTRADAS DE DATOS
# Declarar o crear variables
número1= float(input("Ingresa un número: "))
número2= float(input("Ingresa otro número: "))

# PROCESOS (Cálculos u operaciones matemáticas y/o Lógicas)
suma = número1 + número2
resta = número1 - número2
multiplicación = número1 * número2
división = número1 / número2

potencia1 = número1 ** número2
potencia2 = pow (número1, número2)
cuadrado = pow(número1, 2)
cubo = pow(número2, 3)

raíz_cuadrada1 = math.sqrt(9)
raíz_cuadrada2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)
módulo_resíduo = número1 % número2

# SALIDA DE DATOS
print("la suma es =", round(suma,2)) 
print ("la suma es = " + str(suma)) #CONCATENACIÓN (Unir dos o mas textos en una sola cadena)
# CASTEO: Convertir un tipo de dato a otro tipo de dato.
print(f"la suma es = {suma}")

print("la resta es =", resta)
print("la multiplicación es =", multiplicación)
print("la división es =", división)

print("la potencia 1 es =", potencia1)
print("la potencia 2 es =", potencia2)

print("el cuadrado es =", cuadrado)
print("el cubo es =", cubo)
print("la raíz cuadrada1 es =", math.sqrt(9))
print("la raíz cuadrada2 es =", pow(9, 1/2))
print("la raíz cúbica es =", pow(27, 1/3))
print("el módulo o residuo es =", módulo_resíduo)