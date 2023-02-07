import random
name =input("Hello! What is your name? ")
print("Well,", name,", I am thinking of a number between 1 and 20.")
print("Take a guess")
count = 0
number = random.randint(1, 20)
print(number)
while count<20:
    num = int(input())
    count += 1
    if num == number:
        print("Good job,", name, "! You guessed my number in", count ,"guesses!")
        break
    elif num < number:
        print("Your guess is too low.")
        print("Take a guess.")
        continue
    elif num > number:
        print("Your guess is too high.")
        print("Take a guess.")
        continue