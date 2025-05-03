with open('jagur.txt','w') as a:
    a.write('Hi I am Jagur and a predetor')
    a.close()

with open('jagur.txt','r') as a:
    data=a.readlines()
    for lines in data:
        word=lines.split()
        print(word)
    a.close()


# new work

#file=open('dolphine.txt','x')
#file.close()

import os
if os.path.exists('none.txt'):
    print('File does exsist')
else:
    print('file do not exsist')

file1=open('none.txt','w')
file1.write('Hi I am a none and a nothing')
file1.close()

#os.remove('mono/mono.txt')

#os.rmdir(mono)
