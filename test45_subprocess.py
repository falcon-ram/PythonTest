import subprocess

#subprocess.run(['cmd', '/c', 'dir'])
p1 = subprocess.run('dir', shell=True)
print(p1)
print(p1.args)
print(p1.returncode)
print(p1.stdout)

print()
print('*******************************')
p2 = subprocess.run(['cmd', '/c', 'dir'], capture_output=True)
print(p2.stdout)
#converting to string
print(p2.stdout.decode())

print()
print('*******************************')
# automatically converts the output to a string
p3 = subprocess.run(['cmd', '/c', 'dir'], capture_output=True, text=True)
print(p3.stdout)

print()
print('*******************************')
# using stdout=subprocess.PIPE instead of capture_output=True
# this is what Python does internally when capture_output=True
p4 = subprocess.run(['cmd', '/c', 'dir'], stdout=subprocess.PIPE, text=True)
print(p4.stdout)

print()
print('***** sending output to file ***********')
with open('output.txt', 'w') as f:
    p5 = subprocess.run(['cmd', '/c', 'dir'], stdout=f, text=True)

print()
print('*******************************')
# what happens when there is an error
p6 = subprocess.run(['cmd', '/c', 'dir', 'dne'], capture_output=True, text=True)
print(p6.returncode)
print(p6.stderr)

print()
print('*******************************')
# error checking when running subprocess
# p7 = subprocess.run(['cmd', '/c', 'dir', 'dne'],
#  capture_output=True, text=True, check=True) # now Python throws an error
# print(p7.returncode)
# print(p7.stderr)

print()
print('*******************************')
# Piping the error to dev NULL
p8 = subprocess.run(['cmd', '/c', 'dir', 'dne'],
 stderr=subprocess.DEVNULL) # this is for ignoring the error
print(p8.returncode)
print(p8.stderr)

