a = "cloudfront"

# first is the starting index and the second one is the last index it will return the string starting from the first index and till the last index -1
newString = a[0:5] 

print(a)
print(newString)


# negative slicing
# both are same
print(a[-7:-1])     
print(a[3:9])

# both are same
# if the second argument is not given then it will be length -1 by default
# if the first argument is not given then it is 0 by default
print(a[0:])
print(a[:10])

# slicing with jumping indexes.
print(a[0:10:3]) 