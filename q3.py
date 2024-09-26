import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

menor = 0 # O menor valor de faturamento ocorrido em um dia do mês;
maior = 0 # O maior valor de faturamento ocorrido em um dia do mês;
dias = 0 # Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
soma = 0.0 # A soma do valor do faturamento para calcular a média
dias_considerados = 0 # O valor de dias considerados para calcular a média

for item in dados:
    valor = item['valor']
    
    if maior < valor :
        maior = valor
    if valor > 0:
        soma += valor
        dias_considerados += 1

menor = maior
for item in dados:
    valor = item['valor']
    if menor > valor and valor > 0:
        menor = valor
    if valor > (soma/dias_considerados):
        dias += 1

print(f"Menor faturamento em dia do mês (diferente de 0): {menor}")
print(f"Maior faturamento em dia do mês: {maior}")
print(f"{dias} dias no mês tiveram o valor de faturamento superior a média mensal")

