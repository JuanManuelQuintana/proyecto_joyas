import pulp
from pulp import LpMaximize, LpStatus, value

# Crear el problema
problema = pulp.LpProblem('Problema_joyas_ampliado', LpMaximize)

# Variables de decisión
A = pulp.LpVariable('Joyas_tipo_A', lowBound=0, cat='Integer')
B = pulp.LpVariable('Joyas_tipo_B', lowBound=0, cat='Integer')
C = pulp.LpVariable('Joyas_tipo_C', lowBound=0, cat='Integer')

# Función objetivo: maximizar ganancia
problema += 40 * A + 50 * B + 100 * C, "Ganancia_total"

# Restricciones de materiales
problema += A + 1.5 * B + 1 * C <= 750, "Oro"
problema += 1.5 * A + 1 * B + 1 * C <= 750, "Plata"
problema += 1 * C <= 100, "Diamantes"

# Mostrar el modelo
print("Modelo de optimización:")
print(problema)

# Resolver
estado = problema.solve()

# Verificar resultados
if LpStatus[problema.status] == "Optimal":
    a = round(value(A))
    b = round(value(B))
    c = round(value(C))
    ganancia = 40 * a + 50 * b + 100 * c

    print("\n SOLUCIÓN ENCONTRADA:")
    print(f"Joyas tipo A: {a}")
    print(f"Joyas tipo B: {b}")
    print(f"Joyas tipo C: {c}")
    print(f"Ganancia total: ${ganancia}")
else:
    print("\n No se encontró una solución óptima.")
    print(f"Estado del modelo: {LpStatus[problema.status]}")