# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
def random_number():
    iterations = int(input("how many random number should be in the file between 1 and 1000? "))
    while True:
        try:
            if 1 <= iterations <= 1000:
                break
            else:
                print("please enter a number between 1 and 1000.")
        except ValueError:
           print("invalid input, please enter a valid integer.")

    with open("random_num.txt", "w") as f:
        for i in range(iterations):
            number = random.randint(1, 500)
            f.write(f"{number}\n")
    f.close()
    print(f"{iterations} numbers have been written into the random_num.txt file.")


random_number()