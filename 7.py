numero = int(input("Introduce un número entero positivo: "))

cuenta_atras = ", ".join(str(i) for i in range(numero, -1, -1))

print(f"Cuenta atrás: {cuenta_atras}")
