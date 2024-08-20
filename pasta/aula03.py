nome = 'Nicole'
idade = 16

print(nome)
print(f'O nome é {nome}')

peso = input('Digite seu peso: ')

num1 = input('Digite o primeiro numero: ')
num1 = int(num1)

num2 = int(input('Digite o segundo numero: '))

# operadoress matemáticos
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
divi = num1 / num2
divi_inteira = numn1 // num2
expo = num1 ** num2
modulo = num1 % num2 # resto da divisão

# FIXME: Operadores comparativos
print('Operadores comparativos')
print(num1 > num2)  # maior que
print(num1 - num2)  # menor que
print(num1 == num2)  # igualdade
print(num1 != num2) # diferente
print(num1 <= 100)  # menor ou igual
'''
print(num1 <= 100 and num2 <=100 and (num1 + num2) > 100)

'''
# FIXME: Operadores matemáticos
print('Operadores matemáticos no print')
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

# Atribuicão de valores
num1 += 1
num1 -= 1
num1 /= 1
num1 *= 1

print(f'Soma: {soma}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {divi}')
print(f'Divisão arredondada: {divi:.2f}')
print(f'Divisão inteira: {divi_inteira}')
print(f'Expónenciação: {expo}')
print(f'Resto da divisão: {modulo}')
print()
print(f'O numero digitado + 1 é: {num1}')
