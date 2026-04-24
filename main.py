def main():
    print("Hello learners!")

    suma = addmultiplenumbers([5, 7, 9])
    producto = multiplymultiplenumbers([5, 7, 4,3])

   
    if isinstance(suma, float) and suma.is_integer():
        suma = int(suma)

    if isinstance(producto, float) and producto.is_integer():
        producto = int(producto)

    print("La Suma es:", suma)
    print("La Multiplicación es:", producto)
    print("¿4 es par?", isiteven(4))
    print("¿6.5 es entero?", isitaninteger(6.5))


def addmultiplenumbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def isitaninteger(num):
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())


def isiteven(num):
    return isitaninteger(num) and int(num) % 2 == 0


if __name__ == "__main__":
    main()