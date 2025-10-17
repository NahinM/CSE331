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
    seq = "bbac"
    i = 0
    for c in L:
        if seq[i]==c: i+=1
        if i==4: return True
    return False

SYMBOLS = "abc" # input your symbols
MAXDEPTH = 10 # input your choise of max string length
MYDFA = DFA(
    SYMBOLS, 
    [
        # input your table
    ],
    [] # input your final accepting states
)

print("starting Test For:")
MYDFA.makeGraph()
test()
print(f"Total test cases: {TOTAL}")
print(f"Passed: {PASSED}")
print(f"Failed: {TOTAL-PASSED}")