# Etapa 3 - Validação da entrada do usuário

def adicionar(n1, n2):
    # Retorna a soma de dois números
    return n1 + n2

def subtrair(n1, n2):
    # Retorna a diferença de dois números
    return n1 - n2

def multiplicar(n1, n2):
    # Retorna a o produto de dois números
    return n1 * n2

def dividir(n1, n2):
    # Retorna o quociente da divisão de dois números
    return n1 / n2



try: # validação de possíveis erros no preenchimento
    num1_str = input("Digite o primeiro número: ")
    operador = input("Digite o operador (+, -, *, /): ")
    num2_str = input("Digite o segundo número: ")

    # Passo 1: verificar se os números inseridos são válidos.
    # A validação é realizada verificando se os números são dígitos. Antes disso, realiza um tratamento para desconsiderar o ponto, caso exista.
    if not num1_str.replace('.', '', 1).isdigit() or not num2_str.replace('.','', 1).isdigit():
        raise ValueError("Por favor, insira números válidos.")
    else:
        num1 = float(num1_str) # transformação da string para float para seguir com as demais operações
        num2 = float(num2_str) # transformação da string para float para seguir com as demais operações
    
    # Passo 2: verificar se o operador inserido é válido.
    if operador in ['+', '-', '*', '/']: # insere os operadores válidos em uma lista. Ele valida se o operador está dentro da lista ou não

        #Passo 4: chamar a função correspondente, dependendo do operador escolhido.
        if operador  == '+':
            resultado = adicionar(num1, num2)

        elif operador  == '-':
            resultado = subtrair(num1, num2)

        elif operador  == '*':
            resultado = multiplicar(num1, num2)

        elif operador  == '/':
            #Considerar a divisão por zero aqui

            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            else:
                resultado = dividir(num1, num2)
    
        # Passo 5: Exibir o resultado.

        print(f"O resultado é: {resultado}")

    else:
        # Passo 3: Exibir mensagens de erro apropriadas.
        raise ValueError("Operador inválido. Use +, -, *, ou /.")

except ValueError as e: #Possíveis exceções durante a execução do bloco try
    print(f"Erro: {e}")

except ZeroDivisionError as e: # Possíveis exceções durante a execução do bloco try
    print(f"Erro: {e}")

except Exception as e: # Exceção genérica para englobar erros não mapeados
    print(f"Ocorreu um erro inesperado: {e}")


# Pontos de atenção

# 1. Todos os erros identificados anteriormente agora são capturados dentro do bloco try except.
