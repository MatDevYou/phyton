#utilizzato per rimuovere directory vuota
import os

# Directory name
directory = "dirA"
# Parent Directory
parent = "/home/massimo/dir1/"

# Path
path = os.path.join(parent, directory)

# Remove the Directory
# "dirA"
print(os.rmdir(path))
