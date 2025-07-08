import pulp
from pulp import LpMaximize, LpStatus, value

# Crear el problema
problema = pulp.LpProblem('Taller_Autos_Mejorado', LpMaximize)

# Variables de trabajadores internos
E_int = pulp.LpVariable('Electricistas_Internos', lowBound=0, upBound=30, cat='Integer')
M_int = pulp.LpVariable('Mecanicos_Internos', lowBound=0, upBound=20, cat='Integer')

# Variables de trabajadores contratados externamente
E_ext = pulp.LpVariable('Electricistas_Externos', lowBound=0, upBound=10, cat='Integer')
M_ext = pulp.LpVariable('Mecanicos_Externos', lowBound=0, upBound=10, cat='Integer')

# Totales
E = E_int + E_ext
M = M_int + M_ext

# Función objetivo: beneficio total = ingresos - costos de contratación
beneficio_total = (150 * E) + (120 * M) - (80 * E_ext) - (70 * M_ext)
problema += beneficio_total, "Beneficio_neto"

# Restricciones del negocio
problema += M >= E, "Mecanicos_mayor_o_igual"
problema += M <= 2 * E, "Mecanicos_no_mas_del_doble"

# Resolver
estado = problema.solve()

# Mostrar resultados
if LpStatus[problema.status] == "Optimal":
    print("\n SOLUCIÓN ÓPTIMA ENCONTRADA:\n")
    print(f"Electricistas internos: {round(value(E_int))}")
    print(f"Electricistas externos: {round(value(E_ext))}")
    print(f"Mecánicos internos: {round(value(M_int))}")
    print(f"Mecánicos externos: {round(value(M_ext))}")
    print(f"Electricistas totales: {round(value(E))}")
    print(f"Mecánicos totales: {round(value(M))}")
    print(f"Beneficio neto: €{round(value(problema.objective))}")
else:
    print("No se encontró una solución óptima.")
    print(f"Estado del modelo: {LpStatus[problema.status]}")
