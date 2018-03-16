"""
This file contains a list of method references for a dictionary
"""

# initialize a dictionary
stuff = {
    'name': 'Zed',
    'age': 35,
    'height': 4 * 12
}

# set key to value
stuff['hair_color'] = 'black'

# check if key is in dict
print 'hair_color' in stuff # true

# delete key and its value from dict. Raises KeyError if key is not in map
del stuff['hair_color']
print 'hair_color' in stuff # false

# return an iterator over the keys of the dictionary, this is a shortcut for iterkeys()
iterator = iter(stuff)

# return a copy of the dictionary's list of (key, value) pairs
print "items are: ",
print stuff.items()

# clear all items from the dictionary
# stuff.clear()

# update the dictionary with key value pairs or another dictionary, return None
a = {'a': 1}
b = {'b': 2}
a.update(b) # a = {'a': 1, 'b': 2}
a.update(c=3, d=4)

# if key is in dictionary. remvoe and return its value, else return default 
stuff.pop('height')

# you can also build a dictionary directly from sequence of key value pairs
new_stuff = dict([('sape', 4139), ('guido', 4217), ('jack', 4098)])

# you can also create dictionaries with dict comprehension
new_stuff_2 = {x: x**2 for x in [2, 4, 6]} # {2: 4, 4: 16, 6: 36}

# access an item in dictionary by key
print stuff['name']

# delete a key value pair from dictionary
del stuff['height']
print stuff

# get a list of keys in the dictionary
print stuff.keys()

# check if a key is in dictionary
print 'name' in stuff
print 'height' in stuff


# loop over a dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v

# check number of items in dictionary
len(knights)