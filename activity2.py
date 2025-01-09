#file=open('newhorse.txt','x')
#file.close()

import os
if os.path.exists('carb.txt'):
    print('File does exsist')
else:
    print('file do not exsist')

file1=open('carb.txt','w')
file1.write('Hi I am a carb and a seafood')
file1.close()

#os.remove('octopus/octopus.txt')

os.rmdir('octopus')
