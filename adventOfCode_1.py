list=[]
with open("C:\\Users\\12055\\Desktop\\DSA_python\\adventOfCode.txt") as file:
    for line in file:
        list.append(line)
#print(list)
list2=[]
for str in list:
    l=len(str)
    i,j=0,l-1
    while(ord(str[i]) not in range(48,58)):
        i+=1
    while(ord(str[j]) not in range(48,58)):
        j-=1
    num=(ord(str[i])-48)*10+(ord(str[j])-48)
    list2.append(num)
#print(list2)
print(sum(list2))