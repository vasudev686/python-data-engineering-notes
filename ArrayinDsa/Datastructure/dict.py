# Dictionaries


# Dictionaries are the built-in data structure that store the collection of key-value pairs. Keys need to be immutable data types.

# Example code:-
# dictionary={
#     key1: value1,
#     key2: value2
# }

# dict() - > It is a built-in function that creates a new dictionary. It can be used to create an empty dictionary or to create a dictionary from an iterable of key-value pairs.

# Example code:-
# pizza = dict([('name', 'Pepperoni'), ('price', 10.99), ('toppings', ['pepperoni', 'cheese'])])

# * Bracket notation: You can access the value associated with a specific key using bracket notation. For example, to access the price of the pizza, you can use:
    

# dictionary[key]

# Common Dictionary Methods:
    # *get() - This method is used to retrieve the value associated with a specific key. It takes the key as an argument and returns the corresponding value. If the key does not exist in the dictionary, it returns None or a specified default value.
    
    
# Example code:-
# pizza = {
#     'name': 'Pepperoni',
#     'price': 10.99,
#     'toppings': ['pepperoni', 'cheese']
    
# }
# pizza.keys()
# pizza.values()
# pizza.items()
# pizza.clear()

# pop() Method: This method is used to remove a key-value pair from the dictionary based on the specified key. It takes the key as an argument and removes the corresponding key-value pair from the dictionary. If the key does not exist, it raises a KeyError.

#update() Method: This method is used to update the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs. It takes a dictionary or an iterable as an argument and adds the key-value pairs to the existing dictionary. If a key already exists, its value will be updated.

# Looping Over a Dictionary
# * Iterating Over Value:
#     if you need to iterate over the value in  a dictionary, you can write a for loop with value() to get all value of a dictionary
    
    
products={
    'laptop': 1000,
    'phone': 500,
    'tablet': 300
}
# for product in products.values():
#     print(product)

# * Iterating Over Key:
# for product in products.keys():
    # print(product)
    
    
# * Iterating Over Key-Value Pairs:
for product in products.items():
    print(product)
    
    
# enumerate() Function: This function is used to iterate over a sequence while keeping track of the index. It takes an iterable as an argument and returns an iterator that produces pairs of index and value for each item in the iterable.

# for index, product in enumerate(products.items()):
#     print(index, product)