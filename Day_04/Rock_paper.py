
import  random
choice = ["rock","paper","scissor"]

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

computer_choice = random.choice(choice)
print(computer_choice)
player_choice  = input("your choice rock / paper / scissor \n")

#display the choice of  player
if player_choice == "rock" :
    print("your choice \n rock")
    print(rock)
elif player_choice == "paper" :
    print("your choice \n paper")
    print(paper)
else:
    print("your choice \n scissor")
    print(scissor)


# display the choice of computer

if computer_choice == "rock" :
    print("computer choice \n rock")
    print(rock)
elif computer_choice == "paper" :
    print("computer choice \n paper")
    print(paper)
else:
    print("computer choice \n scissor")
    print(scissor)



#logic for win , lose and draw
if computer_choice == player_choice :
    print(" game draw ")

elif computer_choice == "rock" :
    if player_choice == "paper" :
        print("you own")
    elif player_choice == "scissor" :
        print("you lose")
    else:
        print("you lose")
elif computer_choice == "paper" :
    if player_choice == "rock" :
        print("you lose")
    elif player_choice == "scissor" :
        print("you win")
elif computer_choice == "scissor" :
    if player_choice == "rock":
        print("you won")
    elif player_choice == "paper" :
        print("you lose")