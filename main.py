from random import randint

max_guesses = {
  'e': 10,
  'h': 5
}

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.")
number = randint(1, 100)
difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ")

if difficulty == 'e' or difficulty == 'h':
  remaining_guesses = max_guesses[difficulty]
  has_correctly_guessed = False
  
  while remaining_guesses > 0:
    print(f"You have {remaining_guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
      has_correctly_guessed = True
      print(f"You got it! The answer was {guess}")
      break
    elif guess > number:
      print("Too high.")
      remaining_guesses -= 1
    elif guess < number:
      print("Too low.")
      remaining_guesses -= 1
    else:
      print("Please enter a valid value.")

  if not has_correctly_guessed:
    print("You've run out of guesses, you lose.")

else: 
  print("Please enter a valid value.")
