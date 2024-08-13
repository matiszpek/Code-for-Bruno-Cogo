import matplotlib.pyplot as plt
import numpy as np

nom=input("lugar: ")

temperaturaI = input('Introduce la temperatura media de cada mes: ')
temperatura = [float(temp) for temp in temperaturaI.split('\t') if temp.strip()]

preciI = input('Introduce la precipitación media de cada mes: ')
preci = [float(pre) for pre in preciI.split('\t')]
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

promedio=0
maxtemp=0
maxpreci=0

promedio = sum(temperatura) / len(temperatura)

maxtemp = temperatura.index(max(temperatura))

maxpreci = preci.index(max(preci))

if maxtemp == maxpreci:
    plt.text(11, min(preci) - 10, 'Se refiere a una zona de llanura', fontsize=12, ha='center')
else:
    plt.text(11, min(preci) - 10, 'Se refiere a una zona de montaña', fontsize=12, ha='center')

if promedio >= 20:
    plt.text(11, min(preci) - 5, 'El clima es cálido', fontsize=12, ha='center')
elif promedio > 10:
    plt.text(11, min(preci) - 5, 'El clima es templado', fontsize=12, ha='center')
else:
    plt.text(11, min(preci) - 5, 'El clima es frío', fontsize=12, ha='center')

plt.text(0, max(temperatura) + 2, f'La temperatura promedio es:{promedio}',fontsize=10, ha='left', va='top')

norm_precip = plt.Normalize(min(preci), max(preci))
norm_temp = plt.Normalize(min(temperatura), max(temperatura))

preciC = plt.cm.Blues(norm_precip(preci))
preciCM = [preciC[i] for i in range(len(preci))]

tempC = plt.cm.Reds(norm_temp(temperatura))
tempCM = [tempC[i] for i in range(len(temperatura))]

plt.bar(meses, preci, color=preciCM, alpha=0.7, label='Precipitaciones')
plt.plot(meses, temperatura, color='red', marker='o', linestyle='-', label='Temperatura')

""" 
plt.plot(meses, temperatura, label='Temperatura')
plt.bar(meses, preci, alpha=0.5, label='Precipitaciones') """

plt.xlabel('Meses')
plt.ylabel('Temperatura / Precipitaciones')
plt.title(f'Climatograma de:{nom}')

plt.legend()

plt.show()
