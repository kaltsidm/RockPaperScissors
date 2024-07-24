rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
x = random.randint(0, 2)
list1 = [rock, paper, scissors]
computer_choice = x
your_choice = int(input('Which is you choice? (0 for rock/1 for paper/2 for scissors): '))
if your_choice == 0 and computer_choice == 0 or your_choice == 1 and computer_choice == 1 or your_choice == 2 and computer_choice == 2:
  print(list1[your_choice])
  print('Computer chose:')
  print(list1[x])
  print('It is a draw')
elif your_choice == 0 and computer_choice == 1:
  print(list1[your_choice])
  print('Computer chose:')
  print(list1[x])
  print('You lose')
elif your_choice == 0 and computer_choice == 2:
  print(list1[your_choice])
  print('Computer chose:')
  print(list1[x])
  print('You win')
elif your_choice == 1 and computer_choice == 0:
  print(list1[your_choice])
  print('Computer chose:')
  print(list1[x])
  print('You win')
elif your_choice == 1 and computer_choice == 2:
  print(list1[your_choice])
  print('Computer chose:')
  print(list1[x])
  print('You lose')
elif your_choice == 2 and computer_choice == 0:
  print(list1[your_choice])
  print('Computer chose:')
  print(list1[x])
  print('You lose')
elif your_choice == 2 and computer_choice == 1:
  print(list1[your_choice])
  print('Computer chose:')
  print(list1[x])
  print('You win')  
