import shutil

shutil.copyfile('app.log', 'app_backup.log')

with open('app.log', 'w') as f:
    f.truncate(0)
    
print("log eliminato correttamente")