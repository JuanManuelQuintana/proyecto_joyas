import pulp
from pulp import LpMaximize, LpStatus, value

# Crear el problema de optimización
problema = pulp.LpProblem('Taller_Automoviles', LpMaximize)

# Variables de decisión
E = pulp.LpVariable('Electricistas', lowBound=0, upBound=30, cat='Integer')
M = pulp.LpVariable('Mecanicos', lowBound=0, upBound=20, cat='Integer')

# Función objetivo: maximizar beneficios
problema += 150 * E + 120 * M, "Beneficio_total"

# Restricciones
problema += M >= E, "Mecanicos_mayor_o_igual_que_electricistas"
problema += M <= 2 * E, "Mecanicos_no_mas_del_doble"

# Mostrar el modelo
print("Modelo de optimización:")
print(problema)

# Resolver el problema
estado = problema.solve()

# Mostrar resultados
if LpStatus[problema.status] == "Optimal":
    cantidad_e = round(value(E))
    cantidad_m = round(value(M))
    ganancia = 150 * cantidad_e + 120 * cantidad_m

    print("\n SOLUCIÓN ENCONTRADA:")
    print(f"Electricistas asignados: {cantidad_e}")
    print(f"Mecánicos asignados: {cantidad_m}")
    print(f"Ganancia total por jornada: €{ganancia}")
else:
    print("\n No se encontró una solución óptima.")
    print(f"Estado del modelo: {LpStatus[problema.status]}")