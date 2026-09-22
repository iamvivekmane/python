a = "tiger is here and is there"

print(len(a))

# returns true if the string starts with the passed argument otherwise false
print(a.startswith('ti'))

# returns true if the string ends with the passed argument otherwise false
print(a.endswith('rw'))

# it capitalizes the first letter of the string, not the first letter of all the words in the string but only the first letter of entire string.
print(a.capitalize())

# it capitalizes the first letter all the words in the string.
print(a.title())

# it returns the first occurence of the argument in the string 
index = a.find('h')
print(index)

# it replaces all the occurences of the first argument in the string with the second argument
newString = a.replace('is','his')
print(newString)