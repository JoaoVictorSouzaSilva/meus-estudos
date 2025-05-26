import os
os.system('cls')
import random


question = str(input('Faça uma pergunta: '))
num = random.randint(1, 9)

print(f'Pergunta feita: /"{question}/"')
print('Resposta:')

if num == 8:
  print('Yes - definitely.')
elif num == 7:
  print('It is decidedly so.')
elif num == 6:
  print('Without a doubt.')
elif num == 5:
  print('Reply hazy, try again.')
elif num == 4:
  print('Ask again later.')
elif num == 3:
  print('Better not tell you now.')
elif num == 2:
  print('My sources say no.')
elif num == 1:
  print('Outlook not so good.')
else:
  print('Very doubtful')