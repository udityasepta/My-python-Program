import random
print("This is the Number guessing game please choose a value to get you won in this game!")
print("choose  value between 1 - 50 high and low value ...")

low = int(input("Enter the Number of Low "))
High = int(input("Enter the Number of high "))

num = random.randint(low, High)
print(f"The number is between {low} and {High}")

ch =7 
gc =0
while gc < ch:
    gc += 1
    guess = int(input("Enter the number to guess "))
    
    
    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break
    elif gc >= ch and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')  

