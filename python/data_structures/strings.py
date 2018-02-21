"""
This file details the python string module

"""
import string

print "String Constants"
print string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
print string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print string.digits # 0123456789
print string.hexdigits # 0123456789abcdefABCDEF
print string.letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print string.lowercase # abcdefghijklmnopqrstuvwxyz
print string.octdigits # 01234567
print string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print string.printable # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print string.uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print string.whitespace # 

# string format examples
# access arguments by position
print '{0}, {1}, {2}'.format('a', 'b', 'c')
print '{}, {}, {}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format(*'abc')
print '{0}{1}{0}'.format('abra', 'cad')

# access arguments by name
print 'Names: {james}, {roger}'.format(james='hello', roger='world')

print 'repr() shows quotes: {!r}; str() doesn\'t: {!s}'.format('test1', 'test2')

# return a copy of word with only its first character capitalized
print string.capitalize('word')

print string.find('string to search from', 'from')
# return -1 if sub string is not found
print string.find('string to search from', 'from', 3, 6) # start from index 3, end at index 6

# like .find() but find the highest index
print string.rfind('hello world hello', 'hello')

# like find but raise ValueError exception when substring is not found
print string.index('testing', 'test')

print string.count('hello world hello world hello world', 'hello')

print string.lower("LOWERCASE")
print string.upper("UPPERCASE")

print string.split('hello world hello world hello world', ' ')

print string.join(('hello', 'world'), '=')

print string.strip('   fdsf    ')

# pad a numberic string on the left with zero digits until the given width is met
print string.zfill('453', 8)

# replace all occurences of old with new
print string.replace('hello old', 'old', 'new')
