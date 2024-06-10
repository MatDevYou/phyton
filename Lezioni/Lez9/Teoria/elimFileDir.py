import os
# File name
file = 'file1'
# File location
location = "/home/massimo/dir1/"
# Path
path = os.path.join(location, file)
print("path: ",path)
# Remove the file
# 'file1'
os.remove(path)