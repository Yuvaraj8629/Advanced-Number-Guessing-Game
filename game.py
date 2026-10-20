import random
print("=" * 35)
print("   NUMBER GUESSING GAME")
print("=" * 35)
name = input("Enter your name: ").strip()
print(f"\nWelcome, {name}!")
print("\nChoose your difficulty:")
print("1. Easy   (1-20, 10 attempts)")
print("2. Medium (1-50, 7 attempts)")
print("3. Hard   (1-100, 5 attempts)")
choice = input("\nEnter your choice (1/2/3): ").strip()
if choice == "1":
    max_number = 20
    attempts = 10
elif choice == "2":
    max_number = 50
    attempts = 7
elif choice == "3":
    max_number = 100
    attempts = 5
else:
    print("Invalid choice! Starting Medium mode.")
    max_number = 50
    attempts = 7
secret_number = random.randint(1, max_number)
score = 100
attempts_used = 0
print(f"\nGuess a number between 1 and {max_number}.")
print(f"You have {attempts} attempts.")
while attempts_used < attempts:
    guess_text = input("\nEnter your guess: ").strip()
    if not guess_text.isdigit():
        print("Please enter a valid positive number!")
        continue
    guess = int(guess_text)
    if guess < 1 or guess > max_number:
        print(f"Enter a number from 1 to {max_number}.")
        continue
    attempts_used += 1
    if guess == secret_number:
        print(f"\nCorrect, {name}! You won!")
        score = max(0, 100 - (attempts_used - 1) * 10)
        print(f"Your score: {score}")
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
    remaining = attempts - attempts_used
    print(f"Attempts remaining: {remaining}")
else:
    print("\nGame over!")
    print(f"The correct number was {secret_number}.")
    score = 0
print("\nThanks for playing!")
print(f"Player: {name}")
print(f"Final score: {score}")