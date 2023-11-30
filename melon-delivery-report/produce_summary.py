def print_report(files):
    '''Creates a report using txt files information'''
    day = 1

    for file in files:
        print(f"Day {day} ")
        content = open(file)
        for line in content:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]

            print(f"Delivered {count} {melon}s for total of ${amount}")
        content.close()
        day += 1


files = ["um-deliveries-day-1.txt",
         "um-deliveries-day-2.txt",
         "um-deliveries-day-3.txt"]

print_report(files)
