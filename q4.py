sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros
print("Representação de cada estado:")
print(f"São Paulo: {round(100 * sp/total, 2)}%")
print(f"Rio de Janeiro: {round(100 * rj/total, 2)}%")
print(f"Minas Gerais: {round(100 * mg/total,2)}%")
print(f"Espírito Santo: {round(100 * es/total, 2)}%")
print(f"Outros: {round(100 * outros/total, 2)}%")

