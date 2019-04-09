#File handling
#Print table of 1 to 10 in a file
a=open('table.txt','w')
for i in range(1,11):
    for k in range(1,11):
        h=i*k
        a.write(str(h)+'\t')
    a.write('\n')
a.close()

#File handling
#print table of 1 to 10 in a file by replacing multiple of 4 by H

a=open('modified_table.txt','w')
for i in range(1,11):
    for k in range(1,11):
        h=i*k
        if h%4==0:
            a.write("H\t")
        else:
            a.write(str(h)+'\t')
    a.write('\n')
a.close()
