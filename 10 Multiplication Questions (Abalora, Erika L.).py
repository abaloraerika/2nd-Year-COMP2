import random

# Initialize the score
score = 0

# Loop to generate 10 multiplication questions
for num in range(1, 11):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    multiplication = x * y
    answer = int(input(f"Question # {num}: {x} x {y} = "))
    if answer == multiplication:
        print("Your answer is correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {multiplication}.")

# Print the final score
print(f"Your final score is {score}/10.")
