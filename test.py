import shelve


shelf = shelve.open("sinkshelf")
links = shelf['links']
newDict = dict(filter(lambda elem: elem[1] != None,links.items()))
print(len(newDict))