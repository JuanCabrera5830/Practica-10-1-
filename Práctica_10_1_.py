def suma_iterativa(n):
    suma = 0
    # Mientras n sea mayor que 9, seguimos sumando los d�gitos
    while n > 9:
        suma += n % 10  # Sumar el �ltimo d�gito de n
        n //= 10        # Actualizar n eliminando el �ltimo d�gito
    # Agregar el �ltimo d�gito restante
    suma += n  # Esto suma n si n es menor o igual a 9
    return (suma + n)  # Devolver la suma total de los d�gitos

def main():
    numero = int(input("Introduce un numero entero: "))
    resultado = suma_iterativa(numero)
    print(f"La suma de los digitos de {numero} es: {resultado}")

if __name__ == "__main__":
    main()