names=[]
eng=[]
mat=[]
engToppers=[]
f1=open("Marks.txt","r")
for i in range (0,26,1):
    
    info1=f1.readline()
    list1=info1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    eng.append(int(list2[1]))
    list2=list1[4].split(":")
    mat.append(int(list2[1]))
print(names)
print(eng)
print(mat)
maxEng=max(eng)
maxMat=max(mat)
print(maxEng)
print(maxMat)
for i in range (0,26,1):
    if(eng[i]==maxEng):
        engToppers.append(names[i])
print(f"{engToppers}: are the toppers in English with marks,{maxEng}")
print(engToppers,"are the toppers in English with marks",maxEng)
