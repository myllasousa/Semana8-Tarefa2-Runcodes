def par_impar():
    n = int(input(""))
    if n % 2 == 0:
        return n + 5
    else:
        return n + 8

resultado = par_impar()
print(resultado)
