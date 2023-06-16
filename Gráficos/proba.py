import matplotlib.pyplot as plt
import numpy as np

# Definir los límites de tiempo
tiempo_inicio = 17 * 60 - 9  # Convertir las 17:00 a minutos y restar 9 minutos
tiempo_fin = 17 * 60 + 9  # Convertir las 17:00 a minutos y sumar 9 minutos

# Crear un array de valores de tiempo para graficar
x = np.linspace(tiempo_inicio, tiempo_fin, 100)

# Calcular los valores de tiempo máximo y mínimo de llegada
tiempo_max = x + 9
tiempo_min = x - 9

# Crear el gráfico
fig, ax = plt.subplots()

# Graficar las funciones de tiempo máximo y mínimo
ax.plot(x, tiempo_max, label='Tiempo máximo de llegada')
ax.plot(x, tiempo_min, label='Tiempo mínimo de llegada')

# Etiquetas de los ejes
ax.set_xlabel('Tiempo de llegada de Ana')
ax.set_ylabel('Tiempo de llegada')

# Título del gráfico
ax.set_title('Funciones de tiempo máximo y mínimo de llegada')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.show()