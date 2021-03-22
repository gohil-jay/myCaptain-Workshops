#Set Operations
set1 = set()
set2 = set()

# Adding elements into sets...
for i in range(1, 6): 
   set1.add(i) 
for i in range(3, 8): 
   set2.add(i) 
print("Set1:", set1) 
print("Set2:", set2) 
print("")

# Union operation.
set3 = set1 | set2
print("Union of Set1 and Set2:", set3)
print("")

# Intersection operation.
set4 = set1 & set2
print("Intersection of Set1 and Set2:", set4)
print("")

# Difference operation.
set5 = set1 - set2
print("Difference of Set1 and Set2:", set5)
print("")

# Symmetric difference operation.
set6 = set1 ^ set2
print("Symmetric difference of Set1 and Set2:", set6)
print("")

"""
Output-->

Set1: {1, 2, 3, 4, 5}
Set2: {3, 4, 5, 6, 7}

Union of Set1 and Set2: {1, 2, 3, 4, 5, 6, 7}

Intersection of Set1 and Set2: {3, 4, 5}

Difference of Set1 and Set2: {1, 2}

Symmetric difference of Set1 and Set2: {1, 2, 6, 7}
"""
