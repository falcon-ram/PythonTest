import subprocess
''' Piping from one subprocess to another '''
p8 = subprocess.run(['cmd', '/c', 'type', 'test.txt'], 
    capture_output=True, text=True)
#print(p8.stdout)

p9 = subprocess.run('findstr /n test', 
    shell=True, capture_output=True, text=True, input=p8.stdout)

print(p9.stdout)