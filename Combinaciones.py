import itertools

def generar_combinaciones(longitud):
    caracteres = "0123456789"
    combinaciones = itertools.product(caracteres, repeat=longitud)
    return [''.join(comb) for comb in combinaciones]

def main():
    print("Generador de combinaciones numéricas")
    longitud = int(input("Ingrese la longitud de las combinaciones: "))

    if longitud < 1:
        print("La longitud debe ser al menos 1.")
        return

    combinaciones = generar_combinaciones(longitud)

    print(f"\nCombinaciones de longitud {longitud}:")
    for comb in combinaciones:
        print(comb)

if __name__ == "__main__":
    main()
