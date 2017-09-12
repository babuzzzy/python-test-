import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of thing to buy
shoplist = ['apple','mango','carrot']

# Write to the file
f = open(shoplistfile,'wb')
# Dump the object to a file

pickle.dump(shoplist, f)
f.close()

del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print storedlist
