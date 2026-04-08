# Python Classes and Object

# class - A class  is a blueprint for creating objects. It defines a  behavior an object will have through its attributes and methods.

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def bark(self):
#         print(f'{self.name.upper()} ')
        
        
# creating an object of the class
# Objects are the instance of a class They are created using the class name followed by parentheses. The __init__ method is called when an object is created and it initializes the attributes of the object.

# dog1 = Dog('Buddy', 3)
# dog2 = Dog('Max', 5)

# dog1.bark()  # Output: BUDDY
# dog2.bark()  # Output: MAX

# Calling the methods and Objects
# You can call methods on objects using the dot notation. For example, dog1.bark() calls the bark method on the dog1 object.

# Attributes
# Instance Attributes: Defined in __init__() using self. They are unique to each instance of the class.

# Class Attributes: Defined directly in the class body. They are shared among all instances of the class.
        
        
        # ======Example:-
        
# class Dog:
#     species = 'French Bulldog'  # Class attribute
    
#     def __init__(self,name):
#         self.name = name  # Instance attribute
        
# print(Dog.species)

# jack = Dog('Jack')
# print(jack.name)  # Output: Jack
# print(jack.species)  # Output: French Bulldog

# Methods
# Methods are functions defined within a class that describe the behaviors of an object. They can manipulate the attributes of the object and perform actions. Methods are defined using the def keyword and take self as the first parameter, which refers to the instance of the class.

# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
        
        
#     def describe(self):
#         print(f'This car is a {self.color} {self.model}.')
        
# my_car = Car('red', 'Toyota')
# my_car_2 = Car('blue', 'Honda')
# print(my_car.describe())
# print(my_car_2.describe())


# Dunder Magic Methods

# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
        
#     def __len__(self):
#         return self.pages
    
#     def __str__(self):
#         return f'{self.title} has {self.pages} pages.'
    
#     def __eq__(self, other):
#         return self.pages == other.pages
    
# Book1 = Book('Python Programming', 300)
# Book2 = Book('Data Structures', 300)
        
# print(len(Book1))  
# print(str(Book1))  
# print(Book1 == Book2) 


# Real World Example :- Shopping Cart

class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, item):
        self.items.append(item)
        
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} not found in the cart.')
            
            
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)
    
cart = Cart()
cart.add('Apple')
print(len(cart))  
print('Apple' in cart)  