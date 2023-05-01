import matplotlib.pyplot as plt

habitantes = [120000, 80000, 3000000, 40000, 500000]
ciudades = ["Mendoza", "Ushuaia", "Buenos Aires", "Tres arroyos", "Cordoba"]

plt.title(label="Grafico de Habitantes por Ciudad", fontsize = 20, color = "blue")
plt.xlabel("Ciudades")
plt.ylabel("Poblacion")

plt.bar(ciudades, habitantes, color = "green", width = 1)

plt.show()