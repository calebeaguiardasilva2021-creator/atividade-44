# Tabuada Automática
# Peça um número e exiba a tabuada de 1 a 10 usando for.

tabuada = int(input("Digite algum número para saber a tabuada: "))

for i in range(1,11):
    print(f"{tabuada} x {i} = {tabuada * i}")

