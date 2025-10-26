def question1(L:str) -> bool:
    zero = 0
    for c in L:
        if c=='0':zero+=1
        else: zero=0
        if zero>=3: return False
    return True

def question2(L:str) -> bool:
    sub = "bbac"
    i = 0
    for c in L:
        if sub[i]==c: i+=1
        if i==4: return True
    return False

def question3a(L:str) -> bool:
    if len(L)<2: return False
    return L[0]!=L[len(L)-1]

def question3b(L:str) -> bool:
    if L=="": return False
    return L[0]==L[len(L)-1]

def question4a(L:str) -> bool:
    if len(L)<4: return False
    return L[-4:]=="0101"

def question4b(L:str) -> bool:
    if len(L)<4: return False
    return L[-4:]=="yxxy"

def question5a(L:str) -> bool:
    return len(L)%4==2

def question5b(L:str) -> bool:
    one = 0
    for c in L: one+=(c=='1')
    return one%4==2

def question6(L:str) -> bool:
    if L=="": return True
    return int(L,2)%5==0

def question7a(L:str) -> bool:
    zero = 0
    for c in L:
        if c=='#':return False
        zero+=(c=='0')
    return zero%3!=0

def question7b(L:str) -> bool:
    return False

def question8(L:str) -> bool:
    if len(L)<2: return False
    if L[-2:]!="cb": return False
    return "ba" not in L

def question9(L:str) -> bool:
    one = 0
    zero = 0
    for c in L:
        if c=='0': zero+=1
        else: one+=1
        if zero>=3: return True
    return one==2
    

def question10a(L:str) -> bool:
    if len(L)<2: return False
    return L[len(L)-2]=='a'

def question10b(L:str) -> bool:
    if len(L)<3: return False
    return L[len(L)-3]=='1'

def question11(L:str) -> bool:
    if len(L)<2: return False
    a=0
    b=0
    for c in L:
        if c=='a': a+=1
        else: b+=1
    if L[len(L)-1]=='a': return a>=2
    return b>=2

def question12(L:str) -> bool:
    one=0
    zero=0
    for c in L:
        if c=='1': one+=1
        else: zero+=1
    return abs(one-zero)%3==0

def question13a(L:str) -> bool:
    i = 0
    for c in L:
        if i==2 and c!='1': return False
        i = (i+1)%3
    return True

def question14a(L:str) -> bool:
    total = 0
    if len(L)<2: return False
    for i in range(len(L)-1):
        if L[i]=='a' and L[i+1]=='b': total+=1
        if total>=2: return False
    return total==1

def question15(L:str) -> bool:
    total = 0
    for i in range(len(L)-1):
        if L[i]=='0' and L[i+1]=='0': total+=1
        if total>=2: return True
    return False

def question16a(L:str) -> bool:
    total = 0
    for i in range(len(L)-1):
        if L[i]=='0' and L[i+1]=='0': total+=1
        if total>2: return False
    return total==2

def question17(L:str) -> bool:
    zero = 0
    L = L[-1::-1]
    while zero<len(L) and L[zero]!='1': zero+=1
    return zero==len(L) or zero%2==0

def question18(L:str) -> bool:
    if len(L)==0: return True
    if len(L)==1: return L=='a'
    i = 0
    while i<len(L)-1:
        if L[i]=='b' and L[i+1]!='a': return False
        i+=1
    return L[i]!='b'

def question19(L:str) -> bool:
    i=0
    while i<len(L) and L[i]!='1': i+=1
    zero = 0
    while i<len(L):
        if L[i] == '0': zero+=1
        else:
            if zero&1: return False
            zero = 0
        i+=1
    return True

def question20(L:str) -> bool:
    one,zero = 0,0
    for c in L:
        if c=='0':
            zero+=1
            one = 0
        else:
            one+=1
            zero = 0
        if zero>=2: return False
        if one>=2: return True
    return True

def question21(L:str) -> bool:
    zero,one = 0,0
    for c in L:
        if c=='0':
            zero+=1
            one = 0
        else: one+=1
        if zero>=2: return False
        if one>=2: return True
    return True

def question22(L:str) -> bool:
    L = L[-1::-1]
    i = 0
    while i<len(L) and L[i]=='1': i+=1
    if i==len(L): return True
    zero = 0
    while i<len(L) and L[i]=='0':
        zero+=1
        i+=1
    if i==len(L) or zero>=2: return True
    one = 0
    while i<len(L) and L[i]=='1':
        i+=1
        one+=1
    if i==len(L): return True
    return one%2==0
    
def question23a(L:str) -> bool:
    i = 0
    while i<len(L) and L[i]=='1': i+=1
    one = 0
    while i<len(L):
        if L[i]=='0': one = 0
        else: one+=1
        i+=1
        if i<len(L) and L[i]=='0' and one%3==0: return True
    return False
        
def question24a(L:str) -> bool:
    i = 0
    zero,one = 0,0
    while i<len(L) and L[i]=='0':
        i+=1
        zero+=1
    if zero&1==0: return False
    while i<len(L) and L[i]=='1':
        i+=1
        one+=1
    if one&1==0: return False
    if zero+one != len(L): return False
    return True


checker_kkp_fall25 = {
    "1": question1,
    "2":question2,
    "3a":question3a,
    "3b":question3b,
    "4a":question4a,
    "4b":question4b,
    "5a":question5a,
    "5b":question5b,
    "6":question6,
    "7a":question7a,
    "7b":question7b,
    "8":question8,
    "9":question9,
    "10a":question10a,
    "10b":question10b,
    "11":question11,
    "12":question12,
    "13a":question13a,
    "14a":question14a,
    "15":question15,
    "16a":question16a,
    "17":question17,
    "18":question18,
    "19":question19,
    "20":question20,
    "21":question21,
    "22":question22,
    "23a":question23a,
    "24a":question24a
}
