def calcular(matricula, nota1, nota2, nota3, media_exer):
    return (nota1 + (nota2 * 2) + (nota3 * 3) + media_exer) / 7

m = input("")
n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))
m_exer = float(input(""))

media = calcular(m, n1, n2, n3, m_exer)
print(m)
print(f'{media:.2f}')

def conceito(conceito):
    if media >= 9.0:
        return "A"
    elif 8.9 >= media >= 7.5:
        return "B"
    elif 7.4 >= media >= 6.0:
        return "C"
    elif 5.9 >= media >= 4.0:
        return "D"
    else:
        return "E"
c = conceito(conceito)
print(c)

if c == "A" or c == "B" or c == "C":
    print("Aprovado")
else:
    print("Reprovado")
