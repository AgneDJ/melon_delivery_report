'''Creates a report using txt files information'''
print("Day 1")  # prints out string
# opens txt file and defines it as a variable "the_file"
the_file = open("um-deliveries-day-1.txt")
for line in the_file:  # iterating through every line in variable the_file
    line = line.rstrip()  # removes any empty line
    # each line contains one string, so with split method code is splitting that one string into list with multiple strings, which are separated with |
    words = line.split('|')

    # variable melon defined as first member of the words list
    melon = words[0]
    # variable count defined as second member of the words list
    count = words[1]
    # variable amount defined as third member of the word list
    amount = words[2]

    # prints out a string with values of variables in it
    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()  # closes the file


print("Day 2")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
