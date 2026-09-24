# hindi english dictionary
encyclo = {
    "namaste": "hello",
    "dhanyavaad": "thank you",
    "paani": "water",
    "khaana": "food",
    "ghar": "house",
    "kitaab": "book",
    "school": "school",
    "dost": "friend",
    "pyaar": "love"
}

inp = input("Enter the hindi word : ")
print(inp, " : ",encyclo.get(inp))