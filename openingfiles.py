poem=open('poem.txt')
print(poem)
#study
#for heard in poem:
 #   print(heard)
#study

#counting how many lines are
count=0
for line in poem:
    count=count+1
    print('line count:',count)

m=open('mail.txt','r')
reading=m.read()
print(len(reading))
print(reading[:20])