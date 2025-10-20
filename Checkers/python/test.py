from dfa import *
from checkerFun_kkp_Fall25 import *
SYMBOLS_TEST = ""
MAXLENGTH = 8
MY_DFA:DFA
CHECKER_NAME:str = ""
TOTAL = 0
PASSED = 0

def L_genarator(L:str = "", d=0):
    global TOTAL,PASSED,MAXLENGTH,SYMBOLS_TEST,CHECKER_NAME
    TOTAL+=1
    LHS = MY_DFA.runMachine(L)
    RHS = checker_kkp_fall25[CHECKER_NAME](L)
    if LHS!=RHS:
        print(f"{L} -Not Accepted")
        print(f"    Your machine:{"accepted" if LHS else "rejected"}, Should be:{"accepted" if RHS else "rejected"}")
    else: PASSED+=1
    if d==MAXLENGTH: return
    for c in SYMBOLS_TEST: L_genarator(L+c,d+1)

def test(dfa:DFA,checkerFun:str) -> None:
    global SYMBOLS_TEST,CHECKER_NAME,MY_DFA,TOTAL,PASSED,MAXLENGTH
    TOTAL=PASSED=0
    SYMBOLS_TEST = dfa.symbols
    MY_DFA = dfa
    CHECKER_NAME = checkerFun
    if len(SYMBOLS_TEST)<=2:
        MAXLENGTH = 18
    elif len(SYMBOLS_TEST)<=3:
        MAXLENGTH = 11
    print(f"starting test for question{checkerFun}")
    L_genarator()
    print(f"Total {TOTAL} test cases")
    print(f"Passed {PASSED} cases")
    print(f"Failed: {TOTAL-PASSED}")