import random
user_win=0
computer_win=0
options=["rock","paper","scissor"]
while True:
    user_input=input("please choose rock/paper/scissor or Q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in ["rock","paper","scissor"]:
        print("please choose between rock/paper/scissor")
        continue
    random_number=random.randint(0,2)
    computer_choice= options [random_number]
    print("computer choose",computer_choice)

    if user_input == "rock" and computer_choice == "scissor":
        print("you won!")
        user_win += 1
        continue

    elif user_input == "paper" and computer_choice == "rock":
        print("you won!")
        user_win += 1
        continue

    elif user_input == "scissor" and computer_choice == "paper":
        print("you won!")
        user_win += 1
        continue
    elif user_input == "rock" and computer_choice == "rock":
        print("It's a tie")
        continue
    elif user_input == "paper" and computer_choice == "paper":
        print("It's a tie")
        continue
    elif user_input == "scissor" and computer_choice == "scissor":
        print("It's a tie")
        continue
    else:
        print("computer won")
        computer_win+=1

print("you won:",user_win)
print("computer won:",computer_win)
