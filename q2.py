n = int(input("Informe o valor do número\n"))
fib = [0, 1]
indice = 1
# Utilizei programação dinâmica para fazer a sequência de fibonacci, pois para números grandes a recursão pode não ser a melhor escolha
while True:
    if fib[indice] == n:
        print("Pertence à sequência")
        break
    elif fib[indice] > n:
        print("Não pertence à sequência")
        break
    indice += 1
    fib.append(fib[indice-1]+fib[indice-2])