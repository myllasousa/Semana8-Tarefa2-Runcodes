n = int(input(""))
d6 = n // 100000 % 10
d5 = n // 10000 % 10
d4 = n // 1000 % 10
d3 = n // 100 % 10
d2 = n // 10 % 10
d1 = n // 1 % 10

def soma():
    if 100000 > n >= 0:
        return d1 + d2 + d3 + d4 + d5 + d6
    else:
        return "-1"

resultado = soma()
print(resultado)
