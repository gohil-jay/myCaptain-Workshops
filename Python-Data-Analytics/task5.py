#Importing necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Creating the dataset
data = {'7AM':4, '8AM':4.5, '9AM':4.5, '10AM':5, '11AM':5, '12PM':4.5, '1PM':4, '2PM':4.5, '3PM':3.5, '4PM':4, '5PM':4.5}
time = list(data.keys())
prod = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(time, prod, color ='green', width = 0.5)
plt.show()
