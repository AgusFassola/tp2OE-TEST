
import pandas as pd

df = pd.read_csv('datos/resultados.csv')

estadisticas = {}

for _, fila in df.iterrows():

    local = fila['equipo_local']
    visitante = fila['equipo_visitante']

    goles_local = fila['goles_local']
    goles_visitante = fila['goles_visitante']

    if local not in estadisticas:
        estadisticas[local] = 0

    if visitante not in estadisticas:
        estadisticas[visitante] = 0

    if goles_local > goles_visitante:
        estadisticas[local] += 3

    elif goles_local < goles_visitante:
        estadisticas[visitante] += 3

    else:
        estadisticas[local] += 1
        estadisticas[visitante] += 1

print(estadisticas)
