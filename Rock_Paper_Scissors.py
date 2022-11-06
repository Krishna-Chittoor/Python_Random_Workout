import random

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

#Write your code below this line 👇

print(rock)
print(paper)
print(scissors)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player_choice == 0:
  print ("You chose Rock")
elif player_choice ==1:
  print ("You chose Paper")
elif player_choice ==2:
  print ("You chose Scissors")
else:
  print ("Please enter the right choice 0, 1 or 2")

computer_choice = random.randint(0,2)

if computer_choice == 0:
  print ("Computer chose Rock")
elif computer_choice ==1:
  print ("Computer chose Paper")
elif computer_choice == 2:
  print ("Computer chose Scissors")
else:
  print ("Choice is not right")

if (player_choice == computer_choice):
  print ("It's a draw")
elif(player_choice ==0):
  if (computer_choice == 1):
    print ("Paper wins against rock. Hence computer Win")
  elif (computer_choice ==2):
    print ("Rock wins against scissors. Hence You Win")

elif (player_choice == 1):
  if (computer_choice == 0):
    print ("Paper wins against rock. Hence You Win")
  elif (computer_choice ==2):
    print ("Scissors win against paper. Hence Computer Win")

elif (player_choice == 2):
  if (computer_choice == 0):
    print ("Rock wins against scissors. Hence Computer Win")
  elif (computer_choice ==1):
    print ("Scissors win against paper. Hence You Win")
