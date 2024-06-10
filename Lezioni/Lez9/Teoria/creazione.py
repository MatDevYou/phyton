# Python program to explain os.mkdir() method
# importing os module
import os
# Directory
directory = "prova1"
# Parent Directory path
parent_dir = "/home/massimo"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'prova' in
# '/home / User '
os.mkdir(path)
print("Directory '% s' created" % directory)

# Directory
directory = "prova2"

# Parent Directory path
parent_dir = "/home/massimo/PythonProjects"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'prova2' in
# '/home / User / PythonProjects"'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)