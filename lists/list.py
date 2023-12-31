"""
Characteristics of a list:
1. A list is a collection of items in a particular order.
2. A list can contain items of different data types.
3. A list is mutable, meaning it can be changed.
4. A list is an ordered sequence of items.
5. A list can contain duplicate items.
6. A list can be empty.
"""


# Generating a list (array) of countries in East Africa
East_Africa = ['Kenya', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi']
print(East_Africa)

# Generating a list (array) of even numbers from 0 to 10
even_numbers = [0, 2, 4, 6, 8, 10]
print(even_numbers)

# Generating a list (array) of  a mix of data types
mix_data_types = [1, 4, 5, 'one', 'four', 'five']
print(mix_data_types)

# Generating an empty list (array)
empty_list = []
print(empty_list)

#Generating a list (array) of lists (arrays)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   
print(list_of_lists)

#Genrating a list using the list() function
names = 'Jam', 'Jan', 'Kin', 'Kan'
names_list = list(names)
print(names_list)

# Indexing
print(East_Africa[0])  # Kenya

# Negative indexing
print(East_Africa[-1])  # Burundi

# Slicing
print(even_numbers[0:3])  # [0, 2, 4]

# Appending in a list
odd_numbers = [1, 3, 5]
odd_numbers.append(7)
print(odd_numbers)