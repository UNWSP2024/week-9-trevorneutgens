# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    try:
        with open("numbers.txt", "r") as f:
            number_total = 0
            content = f.readlines()

        for number in content:
            try:
                number = int(number.strip())
                number_total += number
            except ValueError:
                print("invalid data, an item in numbers.txt file is not a valid integer.")

    except IOError:
        print("could not read the file.")

    print(f"the sum of all the numbers in the numbers.txt file is {number_total}.")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()