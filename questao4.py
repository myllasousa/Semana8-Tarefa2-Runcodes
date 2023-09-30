def peso_ideal(altura, sexo):
    if sexo == 1:
        return (72.7 * altura) - 58
    elif sexo == 2:
        return (62.1 * altura) - 44.7

a = float(input(""))
s = float(input(""))

resultado = peso_ideal(a, s)
print(f'{resultado:.2f}')
