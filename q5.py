str = input("Informe a string desejada para inverter a ordem dos caracteres\n")
str_reserse = ""
j = len(str) - 1
while j > -1:
    str_reserse += str[j]
    j -= 1

print(str_reserse)