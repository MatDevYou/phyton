import os
file = "/home/massimo/dir1/"
result = os.path.exists(file)
print(result)
file = "/home/massimo/dir1/filechenonesiste"
result = os.path.exists(file)
print(result)