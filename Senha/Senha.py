import os
os.system('cls')

Senha = input('Digite sua Senha: ')

SenhaC = input('Confirme sua Senha novamente: ') 

if Senha != SenhaC:
    print('Senha Incorreta, tente novamente.')
else:
    print('Senha Correta!')