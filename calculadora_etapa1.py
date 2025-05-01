# Etapa 1 - Implementação das operações básicas

numero1 = float(input("Digite o primeiro número: ")) # pega o número digitado - em String - e o transforma em float
operador = input("Digite o operador (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: ")) # pega o número digitado - em String - e o transforma em float

# Passo 2: Realizar a operação correspondente

# Usa o if como forma mais básica de cálculo a partir do operador
if operador  == '+':
    resultado = numero1 + numero2

elif operador  == '-':
    resultado = numero1 - numero2

elif operador  == '*':
    resultado = numero1 * numero2

elif operador  == '/':
    resultado = numero1 / numero2

else:
    resultado = "Operador Inválido" # caso o operador seja qualquer coisa diferente dos 04 básicos

# Passo 3: Exibir o resultado

print("Resultado:", resultado)

# Pontos de atenção

#1. Se os valores do número 1 e 2 forem letras ou qualquer outra coisa diferente de um número,
#   haverá um erro durante a tentativa de conversão do valor digitado em float.

#2. Se o valor numérico for uma vírgula ao invés de um ponto, haverá outro erro durante a conversão do float.

#3. Haverá erro na divisão por zero.