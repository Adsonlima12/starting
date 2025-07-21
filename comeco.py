def calculadora():
    print("Calculadora Básica em Python")
    print("Escolha uma operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    opcao = input("Digite o número da operação desejada (1-4): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = num1 + num2
            operador = "+"
        elif opcao == "2":
            resultado = num1 - num2
            operador = "-"
        elif opcao == "3":
            resultado = num1 * num2
            operador = "*"
        elif opcao == "4":
            if num2 == 0:
                print("⚠️ Erro: Divisão por zero não permitida.")
                return
            resultado = num1 / num2
            operador = "/"
        else:
            print("Opção inválida.")
            return

        print(f"\nResultado: {num1} {operador} {num2} = {resultado:.2f}")
    except ValueError:
        print("⚠Entrada inválida. Certifique-se de digitar números.")

calculadora()
