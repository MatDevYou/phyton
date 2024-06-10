import os
os.chdir('/home/massimo/dir1/')
creaDir=os.popen('mkdir directory')
creaDir.close()
fd=os.popen('ls')
str=fd.read()
fd.close()
print(str)
