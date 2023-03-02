
#Creating a function to take a file and display a summary of inventory
def delivery_summary(file_name):
    """Retrieve a summary of inventory from a file.

    Arguments:
        - file_name (str): File name in format of um-deliveries-day-<day number>.txt

    Return:
        - (str) Summary of produce inventory
        - File for report
    """


    #Opening file with data
    the_file = open(file_name)

    #Retreiving the day number from file name and displaying
    day = file_name.split('-')
    day = (day[-1].split('.'))[0]

    print(f"Day {day}")

    #reading each line in file
    for line in the_file:
        #Removing whitespace and spereating each line by delimiter |
        line = line.rstrip()
        words = line.split('|')

        #Assigning each part of the line to a varibale to be use later in output
        melon_name = words[0]
        amount_melon = words[1]
        total_cost_melon = words[2]

        #Displays string of each line with variables values
        print(f"Delivered {amount_melon} {melon_name}s for a total of ${total_cost_melon}")

    #Closing file
    the_file.close()



