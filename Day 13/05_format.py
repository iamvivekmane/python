# in the code written nowadays it is not used much we use fstring instead

# both are the same
a = '{} is a good {}'.format('shubham','man')
a = '{0} is a good {1}'.format('shubham','man')

# if we want to change the indexes then we can give it in the brackets
b = '{1} is a good {0}'.format('shubham','man')

print(a)
print(b)