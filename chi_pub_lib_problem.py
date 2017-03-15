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
reader = csv.reader(file, delimiter='\t')
for line in reader:
    lib_list.append(line)


# Taking the labels ("Jan, Feb, etc." off of the list to make the numbers easier to work with.
headers = lib_list[0]
lib_list = lib_list[1:]
print("Lib list: ",end="")
print()
print("Headers list: ",end="")

# Sorting --> taking out the total visitors from each library location
lib_list.sort(key=itemgetter(-1))
print()

# Making the items in the list integers
for i in range(len(lib_list)):
    lib_list[i][-1] = int(lib_list[i][-1])


# The actual sorting process of picking out the top three libraries
lib_list.sort(key=itemgetter(-1))
print()
print("Top three most visited: " , end=" ")
print(lib_list[-3:])
print()


# Separating the values from the top three libraries into a list
top_three = []
top_three.append(lib_list[-3:])


# Building number lists to work with.
total_yearly = []
total_list = []
for line in file:
    words = split_line(line)
    total_list.append(words)


# Picks out the total visitors YEARLY for each chicago library each year and adds them to total_yearly list.
for i in range(len(lib_list)):
    total_yearly.append(lib_list[i][-1])
print()


# Getting the TOTAL number of visitors to chicago libraries YEARLY*******
total_visitors = 0
for i in range(len(total_yearly)):
    total_visitors += int(total_yearly[i])
print("Total visitors YEARLY:" , total_visitors)


# Finding and printing the TOP THREE visited libraries with all of the data per month
numthree = (lib_list[-3:])

names = []
for name in numthree:
    names.append(name[0])

#
total_monthly_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for lib in lib_list:
    for month in range(1, (len(total_monthly_list)) - 1):
        total_monthly_list[month] += int(lib[month + 1]) #lib[month+1]

print("Total_monthly_list = ", end=" ")
print(total_monthly_list)
################################GRAPHING#########################################
month_title = ["LOCATION" , "JANUARY" , "FEBRUARY" , "MARCH" , "APRIL" , "MAY" , "JUNE" , "JULY" , "AUGUST" , "SEPTEMBER" , "OCTOBER" , "NOVEMBER" ,"DECEMBER" , "YTD"]

topthreex = month_title[1:12]

topthreey = numthree[2][1:-1]
topthreey2 = numthree[1][1:-1]
topthreey3 = numthree[0][1:-1]
monthlyy = total_monthly_list

# **** Making the bar graph **** #
chinatown, = plt.plot(np.arange(len(topthreey)), topthreey, color= "darkgreen")
sulzer, = plt.plot(np.arange(len(topthreey2)), topthreey2, color= "orange")
harold, = plt.plot(np.arange(len(topthreey3)), topthreey3, color= "blue")
monthly, = plt.plot(np.arange(len(total_monthly_list)), monthlyy, color= "red")

chinatown.set_marker("*")
chinatown.set_markersize(5)
sulzer.set_marker("*")
sulzer.set_markersize(5)
harold.set_marker("*")
harold.set_markersize(5)
monthly.set_marker("*")
monthly.set_markersize(5)

# Labels the total bar on the x axis
plt.xticks(np.arange(len(topthreey)), month_title[1:], rotation=45)

# Labels
plt.title("Graph of Visitation of Chicago Libraries")
plt.xlabel("Name of Library")
plt.ylabel("Number of Visitors")

# Patches
chinatown_patch = mpatches.Patch(color = 'darkgreen', label = 'Chinatown Library')
sulzer_patch = mpatches.Patch(color = 'orange', label = 'Sulzer Regional Library')
harold_patch = mpatches.Patch(color = 'blue', label = 'Harold Washington Library')
total_patch = mpatches.Patch(color = 'red', label = 'Total visitors (to all chicago libraries)')

# Adding a key to the graph
plt.legend(handles= [chinatown_patch, sulzer_patch, harold_patch, total_patch],title = 'Library Name:', framealpha = 0.5, shadow = True)

# Limiting the axis
plt.axis([0,13, 0, 900000]) #(xmin, xmax, ymin, ymax)

plt.show()