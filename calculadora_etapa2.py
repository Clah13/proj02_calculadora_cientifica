# Etapa 2 - Refatoração com Funções para Operações Básicas

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

num1 = float(input("Digite o primeiro número: ")) # pega o número digitado - em String - e o transforma em float
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: ")) # pega o número digitado - em String - e o transforma em float

# Usa o if como forma mais básica de cálculo a partir do operador
if operador  == '+':
    resultado = adicionar(num1, num2)

elif operador  == '-':
    resultado = subtrair(num1, num2)

elif operador  == '*':
    resultado = multiplicar(num1, num2)

elif operador  == '/':
    resultado = dividir(num1, num2)

else:
    print("Operador Inválido!") # caso o operador seja qualquer coisa diferente dos 04 básicos
    resultado = None

if resultado is not None: # Apresenta a mensagem apenas se não houver deteccção de erros
    print(f"O resultado é {resultado}")

# Pontos de atenção - Se mantém em relação ao item anterior.

#1. Se os valores do número 1 e 2 forem letras ou qualquer outra coisa diferente de um número,
#   haverá um erro durante a tentativa de conversão do valor digitado em float.

#2. Se o valor numérico for uma vírgula ao invés de um ponto, haverá outro erro durante a conversão do float.

#3. Haverá erro na divisão por zero.