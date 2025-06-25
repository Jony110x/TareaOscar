def calculadora():
    """
    Realiza operaciones matemáticas básicas: suma, resta, multiplicación y división.
    """
    print("--- Calculadora Sencilla ---")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("--------------------------")

    while True:
        operacion = input("Selecciona una operación (1/2/3/4) o 'salir' para terminar: ").lower()

        if operacion == 'salir':
            print("¡Hasta luego!")
            break

        if operacion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingresa números válidos.")
                continue

            if operacion == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif operacion == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif operacion == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif operacion == '4':
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: No se puede dividir por cero.")
        else:
            print("Operación inválida. Por favor, selecciona una opción válida (1/2/3/4) o 'salir'.")

if __name__ == "__main__":
    calculadora()