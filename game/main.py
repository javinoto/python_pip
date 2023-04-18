import random

rounds = 1
user_wins = 0
computer_wins = 0
options = ('piedra', 'papel', 'tijera')    # Definimos tupla
computer_option = random.choice(options)   # Valor aleatorio


while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('user_wins: ', user_wins)
  print('computer_wins: ', computer_wins)
  
  user_option = input('piedra, papel o tijera: ')
  user_option = user_option.lower()
  
  if not user_option in options:         # Validar opcion
    print('Esa opción no es valida')
    continue

  print('-' * 30)
  print('User option: ', user_option)
  print('Computer option: ', computer_option)
  
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera, user ganó')
      user_wins += 1
    else:
      print('papel gana a piedra, computer ganó')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra, user ganó')
      user_wins += 1
    else:
      print('tijera gana a papel, computer ganó')
      computer_wins += 1
  elif user_option == 'tijera': 
    if computer_option == 'papel':
      print('tijera gana a papel, user ganó')
      user_wins += 1
    else:
      print('piedra gana a tijera, computer ganó')
      computer_wins += 1

  if computer_wins == 2:
    print('-' * 30)
    print('El rotundo ganador es la computadora')
    break

  if user_wins == 2:
    print('-' * 30)
    print('El rotundo ganador es el usuario')
    break
  
  rounds += 1
  print('-' * 30)