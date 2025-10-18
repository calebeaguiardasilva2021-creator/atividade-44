# Tabuada Automática
# Peça um número e exiba a tabuada de 1 a 10 usando for.
numeros = []
for i in range(1,11):
    numeros = int(input("Digite algum número: "))
    print(f"""{numeros} x 1 = {numeros * 1}
{numeros} x 2 = {numeros * 2}
{numeros} x 3 = {numeros * 3}
{numeros} x 4 = {numeros * 4}
{numeros} x 5 = {numeros * 5}
{numeros} x 6 = {numeros * 6}
{numeros} x 7 = {numeros * 7}
{numeros} x 8 = {numeros * 8}
{numeros} x 9 = {numeros * 9}
{numeros} x 10 = {numeros * 10}""")
    break