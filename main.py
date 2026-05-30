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

selection = [rock, paper, scissors]

computer_choice = random.randint(0, len(selection) - 1)

print(("Welcome to Rock Papers Scissors vs a Computer!\n"
       "What do you choose?"))
player_choice_str = input("Select 0 for rock, 1 for paper, and 2 for scissors: ")
if not player_choice_str.isdigit() or int(player_choice_str) > 2 or int(player_choice_str) < 0:
    print("You ran away. You lose!")
    exit()

player_choice = int(player_choice_str)

print(selection[player_choice])
print(f"Computer chose: \n{selection[computer_choice]}")

if player_choice == computer_choice:
    print("It's a draw!")
# Scenarios where the player chooses the option right before the computer's choice in the list(all losing options)
elif player_choice + 1 == computer_choice:
    print("You lose!")
else:
    # Accounting for the scenario where the player chooses scissors and the computer chooses rock
    if player_choice + 1 == computer_choice + 3:
        print("You lose!")
    # In all other scenarios, the player wins
    else:
        print("You win!")
