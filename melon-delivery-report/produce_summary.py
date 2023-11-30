def print_report(files):
    '''Creates a report using txt files information'''
    day = 1  # keeps track of day

    for file in files:  # iterates through all file names
        print(f"Day {day} ")  # prints out the day
        # opens the file and assigns it to a variable named "content"
        content = open(file)
        for line in content:  # iterates through each line in file
            # removes every white space (new line) on the right and reassigns it to the line
            line = line.rstrip()
            # splits each line with a separator and creates a list of words
            words = line.split('|')

            melon = words[0]  # first word assigns to a variable named melon
            count = words[1]  # second word assigns to a variable named count
            amount = words[2]  # third word assigns to a variable named amount

            # prints out a f string containing values of those variables
            print(f"Delivered {count} {melon}s for total of ${amount}")
        content.close()  # closes file
        day += 1  # add one day to a day


# list of file names to read
files = ["um-deliveries-day-1.txt",
         "um-deliveries-day-2.txt",
         "um-deliveries-day-3.txt"]

print_report(files)  # calls the function with file names
