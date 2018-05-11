
#input : string
#output : boolean
#description : check whether string contains alphabet.
def alphabet(s):
    for c in s:
        if (c>='0' and c<='9'):    
            return False
    return True

#input : string
#output : boolen
#description : check whether string's first letter is capital letter.
def checkfirst(s):
    return (s[0]==s[0].upper() and alphabet(s))

import re

f=open("test.txt", 'r')

lst = []

for l in f:
    lst.append(l.strip())

f.close()

#input : list of 덩어리
#output : list of 단어
#description : 겹치는 단어 제거
def remove_prop(lst):
    result=[]
    prop=[]
    for e in lst:
        delimiters = ".", "!", "?", "\n"
        regexPattern = '|'.join(map(re.escape, delimiters))
        tmp = re.split(regexPattern, e)
        tmp = list(filter(None, tmp))
        
        for t in tmp:
            deli = ",", " "
            reg = "|".join(map(re.escape, deli))
            ss=re.split(reg,t.strip())
            ss=list(filter(None, ss))
            #ss=t.strip().split()
            result=result+ss
            S=ss[1:]
            for s in S:
                if(checkfirst(s) and (not s in prop)):
                    prop.append(s)

    result = list(filter(lambda a: not a in prop, result))
    return result

result=remove_prop(lst)
print(result)

        
