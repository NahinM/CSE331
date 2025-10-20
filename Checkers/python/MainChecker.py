from checkerFun_kkp_Fall25 import checker_kkp_fall25
from dfa import DFA
from test import *

def main():
    CHECKER_STATE = "run"
    
    print("wellcome to assignment checker\nPlease enter the question no you want to check")
    while CHECKER_STATE!="exit":
        inp = input("Question: ")
        CHECKER_STATE = inp
        if inp not in checker_kkp_fall25.keys():
            print("This question is not abailable please try again")
            continue
        mydfa = None
        with open(f"SolveHere/question{inp}.txt","r") as file:
            symbols = file.readline()[:-1]
            N = int(file.readline()[:-1])
            table = []
            for _ in range(N):
                table.append([int(t) for t in file.readline()[:-1].split(' ')])
            M = int(file.readline()[:-1])
            F_states = [int(f) for f in file.readline().split(' ')]
            mydfa = DFA(symbols, table, F_states)
        
        mydfa.makeGraph()
        test(mydfa, inp)


if __name__=="__main__":
    main()