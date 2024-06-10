import os,stat
file = "/home/massimo/dir1/file1"
statinfo = os.stat(file)
mode = statinfo.st_mode
print(stat.S_ISREG( mode ))
print(stat.S_IMODE( mode ))