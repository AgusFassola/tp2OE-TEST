
import matplotlib.pyplot as plt

equipos = ['Boca', 'River']
goles = [2,1]

plt.bar(equipos, goles)

plt.savefig('resultados/grafico.png')
