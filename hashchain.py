# import the hashlib library for performing hashing functions
import hashlib

# Create an initial test string
some_string = "Hello World!"

# Create an MD5 hash object
hash = hashlib.md5()

# Update our hash object with the string
hash.update(some_string)

# Print out our hash in hex format
print (hash.hexdigest())
