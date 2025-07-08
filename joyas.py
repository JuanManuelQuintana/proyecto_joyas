import pulp
from pulp import LpMaximize, LpStatus, value

# Crear el problema
problema = pulp.LpProblem('Problema_joyas', LpMaximize)

# Variables de decisión
x = pulp.LpVariable('A', lowBound=0, cat='Integer')
y = pulp.LpVariable('B', lowBound=0, cat='Integer')

# Función objetivo
problema += 40*x + 50*y  # Beneficio Total

# Restricciones
problema += x + 1.5*y <= 750  # Oro
problema += 1.5*x + y <= 750  # Plata

# Mostrar el modelo formulado
print("Modelo de optimización:")
print(problema)

# Resolver el problema
estado = problema.solve()

# Verificar si se obtuvo una solución óptima
if LpStatus[problema.status] == "Optimal":
    cantidad_a = round(value(x))
    cantidad_b = round(value(y))
    ganancia = 40 * cantidad_a + 50 * cantidad_b

    print("\n SOLUCIÓN ENCONTRADA:")
    print(f"Joyas tipo A: {cantidad_a}")
    print(f"Joyas tipo B: {cantidad_b}")
    print(f"Ganancia total: ${ganancia}")
else:
    print("\n No se encontró una solución óptima.")
    print(f"Estado del modelo: {LpStatus[problema.status]}")
