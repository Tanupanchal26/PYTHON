
def rem(L, word):
    n = [] 
    for item in L:
        if not(item == word):
            n.append(item.strip(word))
    return n


L = ["Tanya", "Urvi", "Lacki", "Ayan"]

print(rem(L, "Ayan"))