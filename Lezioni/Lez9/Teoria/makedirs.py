# Python program to explain os.makedirs() method
# importing os module
import os

# Leaf directory
directory = "prova3"

# Parent Directories
parent_dir = "/home/massimo/pippo/pluto/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'prova3'
os.makedirs(path)
print("Directory '% s' created" % directory)

# Directory 'pippo' and 'pluto' will
# be created too
# if it does not exists

# os.makedirs() method can be
# used to create a directory tre