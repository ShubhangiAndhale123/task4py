import random

while True:
  user_input = input("Enter your choice(rock,paper,scissors)")
  possible_choices = ["rock","paper","scissors"]
  computer_input = random.choice(possible_choices)

  print(f"you chose{user_input},computer chose{computer_input}")


  if user_input == computer_input:
      print(f"It's drow as both selected {user_input}")
  elif user_input == "rock":
      if computer_input == "scissors":
          print("user wins,rocs will break scissors")
      else:
          print("user lose,paper will cover rock")
  elif user_input == "paper":
      if computer_input == "rock":
          print("user wins,paper will cover rock")
      else:
          print("user lose,scissors will cut paper")
  elif user_input == "scissor":
      if computer_input == "paper":
          print("user wins,scissors will cut paper")
      else:
          print("user lose,rock will break scissors")

  play_again = input("do you want to play again? (y/n):")
  if play_again.lower() !="y":
      break

print("game over")


