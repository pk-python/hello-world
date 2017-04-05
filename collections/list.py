# List
sample_list = ["Raj",5,"Uday","Navya",9] #List can store both homogeneous and heterogeneous elements
# Creating a list with known size and unknown elements
sample_list2=[None]*5	# None denotes an unknown value in Python
# len(list) gives the length of list
print("2nd element in list ", sample_list[1], "last element of list ", sample_list[len(sample_list)-1])

# Iterating through list using for loop
# Using indexes
for index in range(0,len(sample_list)) :
    print("Element at ", index , " is ", sample_list[index])

# Using direct looping of list built in for
for elem in sample_list:
    print("Element is ", elem)

# To check whether an element exists in list or not
element = "Uday"

if element in sample_list:
    print("Element '", element, "' is in the list")
else:
    print("Element not found")

# Elements are indexed in negative values as well. For example list contains 0,1,2 as indexes
# they can also be accessed using indexes -3,-2,-1
print("List", sample_list) # can also print the list directly.

# Slicing in list
sub_list = sample_list[1:4] # slicing the list from indexes 1 to 3 i.e. (4-1)
print("List after slicing ", sub_list)

# List of Lists
airline_details=[["AI",8], ["EM",10],["BA",7]]
# Accessing an element from list in a list
print("Element in a list in a list", airline_details[2][1])

# Initializing List with initial values with a defined length
my_list = [0]*10 # creates a list with ten elements each having value as zero