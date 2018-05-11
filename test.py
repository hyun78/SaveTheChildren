
def alphabet(s):
    for c in s:
        if (c>='0' and c<='9'):    
            return False
    return True

def checkfirst(s):
    return (s[0]==s[0].upper() and alphabet(s))

import re

f=open("test.txt", 'r')

lst = []
result=[]

for l in f:
    lst.append(l.strip())

f.close()

#print(lst)

prop=[]
#print(lst)

for e in lst:
    delimiters = ".", "!", "?", "\n"
    regexPattern = '|'.join(map(re.escape, delimiters))
    tmp = re.split(regexPattern, e)
    tmp = list(filter(None, tmp))
    #print(tmp)
    
    for t in tmp:
        deli = ",", " "
        reg = "|".join(map(re.escape, deli))
        ss=re.split(reg,t.strip())
        ss=list(filter(None, ss))
        #ss=t.strip().split()
        result=result+ss
        S=ss[1:]
        print(ss)
        #print(S)
        for s in S:
            if(checkfirst(s) and (not s in prop)):
                prop.append(s)

print(prop)
result = list(filter(lambda a: not a in prop, result))
print(result)
'''
print(lst)
print("!!!!!!!!!!!!!")
print(e)

for e in lst:
    for ee in e:
        if(ee in prop):
            lst.remove(ee)

print(lst)
'''

    
