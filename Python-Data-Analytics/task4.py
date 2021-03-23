#Importing necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Creating the minor dataset
data = {'Math-I':80, 'Chemistry':87, 'Comm. Skills':88, 'EME':74, 'EEE':95, 'PEHV':74, 'Workshop':88, 'EME':74, 'Sports-I':81}
course = list(data.keys())
marks = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(course, marks, color ='green', width = 0.4)
plt.show()
