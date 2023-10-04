"""
1. Defined using key and value pairs
2. Are unordered
3. Keys are unique
4. Keys are immutable
"""

# Creating a dictionary
employee_ranks = {1 : 'CEO', 2 : 'Director', 3 : 'Manager'}
print(employee_ranks)

# Creating an empty dictionary
empty_dict = {}
print('An empty dictionary', empty_dict)

# Creating a dictionary using dict() method
employee_ranks = dict({1 : 'CEO', 2 : 'Director', 3 : 'Manager'})
print(employee_ranks)

# Nested dictionaries
companies = {1 : 'Amazon', 2 : 'Apple',
             3 :{4 : 'Meta', 5 : 'Netflix'}}

print(companies)

# Adding elements / insertion
companies[6] = 'Google'
print(companies)

# Accessing elements in a dictionary
print(companies[2])

# Accessing using the .get() method
print(companies.get(1))

# Accessing elements in a nested dict
print(companies[3][4])

countries = {'East' : 'Kenya', 'South' : 'South Africa', 'West' : 'Nigeria'}
print(countries)

# Generating a copy of the dictionary
countries_copy = dict.copy(countries)
print(countries_copy)

# Listing a tupple for each key value pair
print(dict.items(countries))

# An output of the dictionary keys
print(dict.keys(countries))

# Updating a dictionary
countries_updated = countries.update({'North' : 'Egypt'}) 
print(countries_updated)

# An output of the values
print(dict.values(countries))

# Removing an element with specified key
countries_removed = countries_updated.pop({'North'})
print(countries_removed)