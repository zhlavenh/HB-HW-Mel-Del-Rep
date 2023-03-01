# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

def produce_summary(file_name):

    the_file = open(file_name)

    day = file_name.split('-')
    day = (day[-1].split('.'))[0]

    print(f"Day {day}")

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon_name = words[0]
        amount_melon = words[1]
        total_cost_melon = words[2]

        print(f"Delivered {amount_melon} {melon_name}s for a total of ${total_cost_melon}")

    the_file.close()

produce_summary("um-deliveries-day-2.txt")

