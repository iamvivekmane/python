# remove a given word from a list and strip it at the same time.
items = ["  apple ", "banana  ", " cherry", "  banana", "date "]
def remove_word(l,word):
    clean = []
    for item in l:
        clean.append(item.strip())
    for item in clean:
        if(item == word):
            clean.remove(word)
    return clean
result = remove_word(items, "banana")
print(result)
