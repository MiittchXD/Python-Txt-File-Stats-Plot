""" 
    CIS 298 
    Winter 2019 
    Program 4
    
    Name: Mitchell Bartoszyk 
    Date: 4-16-2019

    Description: This program utilizes the matplotlib library to plot the frequency of all digits and characters in a text file. 
    For this assignment, we were to use the class syllabus as the input file. The program first stores all lines of the file in a 
    list. After this, the list is split by lines into sublists. After this, each sublist in the list is walked through, and if an 
    element in the list is a digit or character, it is concatenated with a list of all digits and characters in the input file.
    Next, I collect the stats for each character / digit. After this, pyplot 
    from Matplotlib is used to plot this data to a histogram. 
    
"""

import matplotlib.pyplot as plt

# Opens the txt file and reads in the lines 
syllabus = open("Syllabus.txt")
lines = syllabus.readlines()
syllabus.close()

my_list = []

# String of all numbers and letters in the input file 
nums_and_letters = ''

# Split by new lines and make all characters lowercase 
for line in lines:
    line = line.upper()
    my_list.append(line.split('\n'))

# Get all letters and numbers, add them to string nums_and_letters, which holds all nums and letters in the file 
for lst in my_list:
    for sub in lst:
        for elem in sub:
            if elem.isdigit():
                nums_and_letters += elem
            elif elem.isalpha():
                nums_and_letters += elem

# Stores the character as the key in a dict, and the frequency as the value 
my_count = {}

# Collects the stats for the letters and digits in the string 
for elem in nums_and_letters:
    if elem.isdigit():
        if elem in my_count:
            my_count[elem] += 1
        else:
            my_count[elem] = 1
    elif elem.isalpha():
        if elem in my_count:
            my_count[elem] += 1
        else:
            my_count[elem] = 1

# Stores the character as the key in a dict, and the frequency as the value 
sorted_my_count = {}

# Sorts the dictionary by key (character)
for key in sorted(my_count.keys()):
    sorted_my_count[key] = my_count[key]

# Graph labels
plt.title('Character / Digit Frequency in Syllabus')
plt.xlabel('Character / Digit')
plt.ylabel('Frequency')

# Plot info 
plt.bar(range(len(sorted_my_count.values())), list(sorted_my_count.values()), align='center')
plt.xticks(range(len(sorted_my_count.keys())), list(sorted_my_count.keys()))
plt.show()



