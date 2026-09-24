marks ={
    "jon":100,
    "ron":23,
    "shon":55,
    0:"sham"
}

# it will return all the key value pairs in the dictionary
print(marks.items())

# it will return all the keys in the dictionary
print(marks.keys())

# it update the value of the key value pair with passed value
# if the passed key value pair dosent exist in the dictionary then it will be appended
marks.update({"jon":50})

# it returns the corresponding value pair of the passed key
# both the things are not same
# if key dose not exist it will return null
print(marks.get("jon2")) # null
# if the key does not exist it will throw an error
print(marks["jon2"]) # error