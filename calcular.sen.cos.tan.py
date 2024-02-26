import math

gra = float(input("Digite quantos graus: "))

gras = math.sin(gra)
grac = math.cos(gra)
grat = math.tan(gra)

print("O resultado em SENO é {:.2f}".format(gras))
print("O resultado em COSENO é {:.2f}".format(grac))
print("O resultado em TANGENTE é {:.2f}".format(grat))