import shelve

shelf = shelve.open("sinkshelf")
del shelf['token']