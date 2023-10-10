"""
1. Sets contain unique items, do not allow duplicates.
2. Sets are unordered.
3. Sets are mutable.
4. Sets are unindexed.
5. Sets can contain any data type.
6. Sets can be empty.
7. Sets cannot be nested.
"""

# Generating a set of cities in Kenya
cities = ('Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret')
print(cities)

# Generating a set of even numbers from 0 to 20
even_numbers = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
print(even_numbers)

# Empty set
empty_set = set()
print(empty_set)

# Length of a set
print(len(cities))

# type()
odd_numbers = {1, 3, 5}
print(type(odd_numbers))

# Accessing items in a set
odd_numbers = {1, 3, 5, 7, 9}

for number in odd_numbers:
    print(number)

# Checking presence of an item in a set
colors = {'blue', 'white', 'black', 'yellow', 'red'}
print('blue' in colors)

# Changing items in a set - You cannot change items in a set

# Adding items to a set
colors = {'blue', 'white', 'black', 'yellow', 'red'}
colors.add('magenta')
print(colors)

# Adding multiple items to a set from a set
east_africa = {'Kenya', 'Uganda', 'Tanzania'}
west_africa = {'Nigeria', 'Ghana', 'Benin'}
countries = east_africa.union(west_africa)
print(countries)

# Adding multiple items to a set from a set (2)
east_africa = {'Kenya', 'Uganda', 'Tanzania'}
east_africa.update(['Rwanda', 'Burundi'])
print(east_africa)

# Adding multiple items to a set from a list
west_africa = {'Nigeria', 'Ghana', 'Benin'}
others = ['Liberia', 'Sierra Leone']
west_africa.update(others)
print(west_africa)

# Removing items from a set - Method 1
colors = {'blue', 'white', 'black', 'yellow', 'red'}
colors.remove('red')
print(colors)

# Removing items from a set - Method 2
colors = {'blue', 'white', 'black', 'yellow', 'red'}
colors.discard('blue')
print(colors)

# Removing items from a set - Method 3, removes a random item
even_numbers = {0, 2, 4, 6, 8, 10}
even_numbers.pop()
print(even_numbers)

# Removing all items from a set
even_numbers = {0, 2, 4, 6, 8, 10}
even_numbers.clear()
print(even_numbers)

# Deleting a set
even_numbers = {0, 2, 4, 6, 8, 10}
del even_numbers
#print(even_numbers)

# Loops in sets
fruits = {'mango', 'kiwi', 'banana', 'apple', 'orange'}
for each in fruits:
    print(each)

# Joining sets
continents_1 = {'Africa', 'Asia', 'Australasia'}
continents_2 = {'Europe', 'North America', 'South America'}

continents = continents_1.union(continents_2)
print(continents)

# Joining sets (2)
continents = continents_1.update(continents_2)
print(continents_1)
