import os
os.system('cls')

num1 = int(input('Digite o primeiro Número: '))
num2 = int(input('Digite o segundo Número: '))

if num1 >= num2:
    print(f'O primeiro Número é o maior. ({num1})')
else:
    print(f'O segundo Número é o maior. ({num2})')