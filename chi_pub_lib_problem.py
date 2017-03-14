# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend, label axes, title the graph.

import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import numpy as np

def split_line(line):
        return re.findall('[A-Za-z0-9]+(?:\'[A-Za-z0-9]+)?', line)

lib_list = []
file = open("chilib_visitors_2016")

reader = csv.reader(file, delimiter='\t')
for line in reader:
    lib_list.append(line)

# Taking the labels ("Jan, Feb, etc. off of the list to make the numbers easier to work with.
headers = lib_list[0]
lib_list = lib_list[1:]
print("Lib list: ",end="")
print(lib_list)
print("Headers list: ",end="")
print(headers)
print()

# Building number lists to work with.
total_yearly = []
total_list = []
for line in file:
    words = split_line(line)
    total_list.append(words)

# Picks out the total visitors for each chicago library each year and adds them to total_yearly list.
for i in range(len(lib_list)):
    total_yearly.append(lib_list[i][-1])
print("Total visitors yearly for each library: ",end="")
print(total_yearly)
print()

'''
highest = []
for i in total_yearly:
    if total_yearly[i] > total_yearly[i+1]:
        highest.append(total_yearly[i+1])
print(highest)
'''

# Organizing and formatting the list
def print_list(total_yearly):
    for item in total_yearly:
        print("{:3}".format(item), end=", ")
    print()

# For comparison
print("UNSORTED: " , end="")
print_list(total_yearly)
print()

# *** Not sorting properly... ***
print("SORTED: " , end="")
total_yearly.sort()
print(total_yearly)

# Getting the TOTAL number of visitors to chicago libraries
total_visitors = 0
for i in range(len(total_yearly)):
    total_visitors += int(total_yearly[i])
print()
print("Total visitors:" , total_visitors)


################################GRAPHING#########################################
total_y = [int(total_visitors), 1353311, 297123, 283611]
total_x_label = ["Total (Yearly)", "Hardold Washington Library" , "Chinatown Library", "Woodson Regional Library"]



# Making the bar graph
total, = plt.bar(np.arange(len(total_y)), total_y, 0.1)

# Labels the total bar on the x axis
plt.xticks(np.arange(len(total_y)), total_x_label, rotation=45)

# Labels
plt.title("Graph of Visitation of Chicago Libraries")
plt.xlabel("Library Name")
plt.ylabel("Number of Visitors")

# Details
total.set_color("darkgreen")

# *************
#plt.axis([0, 1000000, 0, 50]) #(xmin, xmax, ymin, ymax)

# Key


plt.show()

'''
#Trying to selection sort the list of yearly totals
def select_sort(total_yearly):
    for currentpos in range(len(total_yearly)):
        smallpos = currentpos
        for scanpos in range(currentpos + 1, len(total_yearly)):
            if total_yearly[scanpos] < total_yearly[smallpos]:
                smallpos = scanpos
        value = total_yearly[smallpos]
        total_yearly[smallpos] = total_yearly[currentpos]
        total_yearly[currentpos] = value
    return total_yearly

print()
print("SELECTION SORT: " , end="")
select_sort(total_yearly)
print_list(total_yearly)
'''