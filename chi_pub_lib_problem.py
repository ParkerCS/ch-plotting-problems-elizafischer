# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.
# Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend, label axes, title the graph.
from operator import itemgetter
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import numpy as np


def split_line(line):
        return re.findall('[A-Za-z0-9]+(?:\'[A-Za-z0-9]+)?', line)

# Organizing and formatting a list
def print_list(list):
    for item in list:
        print("{:3}".format(item), end=", ")
    print()


lib_list = []
file = open("chilib_visitors_2016")
extra_list = []
reader = csv.reader(file, delimiter='\t')
for line in reader:
    lib_list.append(line)
    extra_list.append(line)



# Taking the labels ("Jan, Feb, etc." off of the list to make the numbers easier to work with.
headers = lib_list[0]
lib_list = lib_list[1:]
print("Lib list: ",end="")
#print(lib_list)

print()
print("Headers list: ",end="")
print(headers)
print()


# Sorting
# taking out the total visitors from each library location
#print("SORTED: ", end=" ")
lib_list.sort(key=itemgetter(-1))
#print(lib_list)
print()


# Making the items in the list integers
for i in range(len(lib_list)):
    lib_list[i][-1] = int(lib_list[i][-1])


# the actual sorting process of picking out the top three libraries
lib_list.sort(key=itemgetter(-1))
print()
print("Top three most visited: " , end=" ")
print(lib_list[-3:])
print()


# Separating the values from the top three libraries into a list
top_three = []
top_three.append(lib_list[-3:])
print(top_three)


# Building number lists to work with.
total_yearly = []
total_list = []
for line in file:
    words = split_line(line)
    total_list.append(words)


# Picks out the total visitors YEARLY for each chicago library each year and adds them to total_yearly list.
for i in range(len(lib_list)):
    total_yearly.append(lib_list[i][-1])
#print("Total visitors yearly for each library: ",end="")
#print(total_yearly)
print()


# Getting the TOTAL number of visitors to chicago libraries YEARLY*******
total_visitors = 0
for i in range(len(total_yearly)):
    total_visitors += int(total_yearly[i])
print("Total visitors:" , total_visitors)


# Finding and printing the TOP THREE visited libraries with all of the data per month
print("Top three most visited NAMES from greatest to smallest: " , end=" ")
#print(lib_list)
numthree = (lib_list[-3:])

names = []
for name in numthree:
    names.append(name[0])
#print(names)



''''''
# finding the total each month
jan_tot = []
feb_tot = []
mar_tot = []
apr_tot = []
may_tot = []
jun_tot = []
jul_tot = []
aug_tot = []
sep_tot = []
oct_tot = []
nov_tot = []
dec_tot = []

for i in range(len(jan_tot)):
    jan_tot[i]= int(jan_tot[i])

for i in range(len(lib_list)):
    jan_tot.append(lib_list[i][1])
    feb_tot.append(lib_list[i][2])
    mar_tot.append(lib_list[i][3])
    apr_tot.append(lib_list[i][4])
    may_tot.append(lib_list[i][5])
    jun_tot.append(lib_list[i][6])
    jul_tot.append(lib_list[i][7])
    aug_tot.append(lib_list[i][8])
    sep_tot.append(lib_list[i][9])
    oct_tot.append(lib_list[i][10])
    nov_tot.append(lib_list[i][11])
    dec_tot.append(lib_list[i][12])

jan = 0
for i in range(len(jan_tot)):
    jan = jan_tot[0] + jan_tot[i]

print()
print("Jan List = ", jan_tot)
print()
print("Jan =", jan)
################################GRAPHING#########################################
# ORDER : Jan tot - dec tot, top 3, total yearly

topthreex = headers[1:12]

topthreey = numthree[2][1:-1]
topthreey2 = numthree[1][1:-1]
topthreey3 = numthree[0][1:-1]

#total_y = [int(total_visitors), 1353311, 297123, 283611]
#total_x_label = [numone, numtwo, numthree, "Total (Yearly)"]


# **** Making the bar graph **** #
chinatown, = plt.plot(np.arange(len(topthreey)), topthreey)
sulzer, = plt.plot(np.arange(len(topthreey2)), topthreey2)
harold, = plt.plot(np.arange(len(topthreey3)), topthreey3)


# Labels the total bar on the x axis
plt.xticks(np.arange(len(topthreey)), topthreex, rotation=45)

# Labels
plt.title("Graph of Visitation of Chicago Libraries")
plt.xlabel("Name of Library")
plt.ylabel("Number of Visitors")

# Details
#chinatown.set_color("darkgreen")

# ************* #
#plt.axis([0, 1000000, 0, 50]) #(xmin, xmax, ymin, ymax)

# Key

plt.show()
