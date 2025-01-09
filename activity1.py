with open('horse.txt','w') as f:
    f.write('Hi I am Raza and 15 years old')
    f.close()

with open('horse.txt','r') as f:
    data=f.readlines()
    for lines in data:
        word=lines.split()
        print(word)
    f.close()