#================Sets===============#


# *Sets: Sets are the built-in data structure in python that do not allow duplicate values.
# sets are mutableand unordered, which mean that their element are not stored in any specific order so you cannot use indices or keys to access them. also sets can only contain value of immutable data types such as numbers, strings, and tuples.


# * Defining a Set: You can define a set using curly braces {} or the built-in set() function. For example:
# my_set = {1, 2, 3, 4, 5}

# my_set = {}


# Common Set Methods

# my_set.add(6) # This method is used to add an element to the set. If the element already exists in the set, it will not be added again.

# my_set.remove(3) # This method is used to remove an element from the set. If the element does not exist in the set, it raises a KeyError.
# Mathematical Set Operations


my_set = {1,2,3,4,5}
your_set = {2,3,4,5}

print(my_set | your_set) # Union of two sets
print(my_set & your_set) # Intersection of two sets
print(my_set - your_set) # Difference of two sets


print(your_set.issubset(my_set))
print(my_set.issuperset(your_set))

print(my_set.isdisjoint(your_set))

