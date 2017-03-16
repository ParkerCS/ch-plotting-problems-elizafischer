#1 Import csv, numpy, and matplotlib.plot
#2 Open the chi_life_expectancy.txt file
#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.
# Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list) to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])
#7  Label your axes
#8  Add a title
#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org
#11  Comment your code as always.

import csv
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import matplotlib.patches as mpatches

file = open("chi_life_expectancy.txt", "r")

# Putting the file in a list
life_exp = []
reader = csv.reader(file, delimiter = '\t')
for line in reader:
    life_exp.append(line)
#print(life_exp)


# Taking the labels off of the front of list to make the numbers easier to work with.
headers = life_exp[0]
life_exp = life_exp[1:]
print("Life expectancy list: ",end="")
#print(life_exp)
print("Headers list: ",end="")
print(headers, "\n")

# Sorting low--> high
life_exp.sort(key=itemgetter(8))
print("Sorted life expectancy list: " , end=" ")
print(life_exp, "\n")


# Iterating through the list and taking out the neighborhood names (and appending them to a new list)
neighborhood_list = []
for i in range(len(life_exp)):
    neighborhood_list.append(life_exp[i][1])
print("Neighborhood names: " , neighborhood_list[1:] , "\n")

# Iterating through and picking out the life expectancy for each neighborhood in 2010
life_exp_2010 = []
for i in range(1,len(life_exp)):
    life_exp_2010.append(float(life_exp[i][8]))
print("Life expectancy in 2010, lowest to highest: " , life_exp_2010, "\n")

life_exp_2000 = []
for i in range(1,len(life_exp)):
    life_exp_2000.append(float(life_exp[i][5]))
print("Life expectancy in 2000, lowest to highest: " , life_exp_2000, "\n")

life_exp_1990 = []
for i in range(1,len(life_exp)):
    life_exp_1990.append(float(life_exp[i][2]))
print("Life expectancy in 1990, lowest to highest: " , life_exp_1990, "\n")


################################GRAPHING#########################################
# Plotting
plt.figure(tight_layout = True, figsize = [12,5])

#plotting 2010
line1, = plt.plot(np.arange(len(life_exp_2010)), life_exp_2010, color = "orange")
plt.xticks(np.arange(len(life_exp_2010)-1), neighborhood_list[1:], rotation=90)
line1.set_marker("*")
line1.set_markersize(5)

# plotting 2000
line2, = plt.plot(np.arange(len(life_exp_2000)), life_exp_2000, color = "green")
line2.set_marker("*")
line2.set_markersize(5)

# Plotting 1990
line3, = plt.plot(np.arange(len(life_exp_1990)), life_exp_1990, color = "black")
line3.set_marker("*")
line3.set_markersize(5)


# Labeling
plt.title("Life Expectancy by Chicago Neighborhood")
plt.xlabel("Neighborhoods")
plt.ylabel("Life Expectancy in Years")

# Key
patch_2010 = mpatches.Patch(color = "orange", label = "2010")
patch_2000 = mpatches.Patch(color = "green", label = "2000")
patch_1990 = mpatches.Patch(color = "black", label = "1990")


plt.legend(handles = [patch_2010, patch_2000, patch_1990],title = 'Life Expectancy by Year:', framealpha = 0.5, shadow = True)

# Details
#plt.axis([0, 90, 0, 80]) #(xmin, xmax, ymin, ymax)

plt.show()