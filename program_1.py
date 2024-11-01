# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    try:
        with open('names.txt', 'r') as file:
            list_of_lines = file.readlines()
            num_of_lines = len(list_of_lines)
            print(f'there are {num_of_lines} names in this file.')
    except Exception as e:
        print(f"an error occurred: {e}")

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()