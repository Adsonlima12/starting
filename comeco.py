def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        print("⚠️ Erro: divisão por zero não permitida.")
        return None
    return x / y

def potencia(x, y):
    return x ** y

def calculadora():
    print("🧮 Calculadora Básica com Potência")
    print("Selecione uma operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (^)")

    opcao = input("Digite o número da operação (1 a 5): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = soma(num1, num2)
            simbolo = "+"
        elif opcao == "2":
            resultado = subtracao(num1, num2)
            simbolo = "-"
        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
            simbolo = "*"
        elif opcao == "4":
            resultado = divisao(num1, num2)
            simbolo = "/"
        elif opcao == "5":
            resultado = potencia(num1, num2)
            simbolo = "^"
        else:
            print("❌ Operação inválida.")
            return

        if resultado is not None:
            print(f"\nResultado: {num1} {simbolo} {num2} = {resultado:.2f}")
    except ValueError:
        print("⚠️ Entrada inválida. Certifique-se de digitar números.")

# Executa a calculadora
if __name__ == "__main__":
    calculadora()
