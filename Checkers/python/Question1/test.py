import sys
sys.path.append('..') # make sure you are at the correct dir to run the test
from dfa import *

TOTAL:int = 0
PASSED:int = 0
MYDFA:DFA
SYMBOLS:str = ""
MAXDEPTH:int = 0

def test(L:str="",d:int=0):
    global TOTAL,PASSED,MYDFA,MAXDEPTH
    TOTAL+=1
    LHS,RHS = MYDFA.runMachine(L),genaralSolve(L)
    if(LHS!=RHS):
        print(f"{L} -> Not Accepted; Your Machine: {"accepted" if LHS else "rejected"}, Should be: {"accepted" if RHS else "rejected"}")
    else: PASSED+=1
    if(d==MAXDEPTH): return
    for c in SYMBOLS: test(L+c,d+1)

def genaralSolve(L:str):
    zero = 0
    for c in L:
        if c=='0':
            zero+=1
        else: zero=0
        if zero>=3: return False
    return True

SYMBOLS = "01"
MAXDEPTH = 17
MYDFA = DFA(
    SYMBOLS, 
    [
        [1,0],
        [2,0],
        [3,0],
        [3,3]
    ],
    [0,1,2]
)

print("starting Test For:")
MYDFA.makeGraph()
test()
print(f"Total test cases: {TOTAL}")
print(f"Passed: {PASSED}")
print(f"Failed: {TOTAL-PASSED}")