import matplotlib.pyplot as plt

lenguajes = ["C", "C++", "Java", "Python"]
usuarios = [50,30,70,100]

plt.pie(usuarios, labels = lenguajes, autopct='%1.2f%%')
plt.title(label = "Preferencia Actual Lenguajes",
          loc = "center",
          color = "Blue")

plt.show()