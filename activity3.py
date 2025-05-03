inputfile=open('leo.txt','r')
outputfile=open('leo2.txt','w')

lines_seen_so_far=set()
for line  in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)
inputfile.close()
outputfile.close()