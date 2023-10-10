"""
Characteristics of tuples:
1. A collection of items in a particular order.
2. Can contain items of different data types.
3. Immutable, meaning it cannot be changed.
4. An ordered sequence of items.
5. Can contain duplicate items.
6. Can be empty.
7. Can be nested.
"""

# Generating a tuple of cities in Kenya
cities = ('Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret')
print(cities)

# Generating a tuple of even numbers from 0 to 20
even_numbers = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
print(even_numbers)

# Generating a tuple of a mix of data types
mix_tuples = (4, 8, 20, 'two', 'four', 'twenty')
print(mix_tuples)

# Generating an empty tuple
empty_tuple = ()
print(empty_tuple)

# One item tuple
one_item_tuple = ('mango',)
print(one_item_tuple)

# type() function
print(type(one_item_tuple))

# Length of a tuple
odd_numbers = (1, 3, 5, 7, 9, 11)
print(len(odd_numbers))

# Accessing items in a tuple
odd_numbers = (1, 3, 5, 7, 9, 11)
print(odd_numbers[1])

# Accessing items in a tuple - Negative indexing
odd_numbers = (1, 3, 5, 7, 9, 11)
print(odd_numbers[-1])

# Accessing items in a tuple - Range indexing
odd_numbers = (1, 3, 5, 7, 9, 11)
print(odd_numbers[1:5])

# Changing tuple values - Tuples are immutable

# Adding items to a tuple - Tuples are immutable
# Convert the tuple into a list, add items, then convert back to a tuple
odd_numbers = (1, 3, 5, 7, 9, 11)
odd_numbers_list = list(odd_numbers)
odd_numbers_list.append(13)
odd_numbers = tuple(odd_numbers_list)
print(odd_numbers)

# Removing items from a tuple - Tuples are immutable
# Convert the tuple into a list, remove items, then convert back to a tuple
odd_numbers = (1, 3, 5, 7, 9, 11)
odd_numbers_list = list(odd_numbers)
odd_numbers_list.remove(11)
odd_numbers = tuple(odd_numbers_list)
print(odd_numbers)

# Joining tuples
letters_1 = ('a', 'b', 'c', 'd', 'e')
letters_2 = ('f', 'g', 'h', 'i', 'j')
letters = letters_1 + letters_2
print(letters)

# Multiply tuples
letters = ('a', 'b', 'c')
letters = letters * 3
print(letters)