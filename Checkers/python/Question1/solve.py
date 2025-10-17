from .. import dfa
from dfa import *
import sys
sys.stdin = open("input.txt","r")

mydfa = DFA(
    "", # input your symbols
    [
        [1,0],
        [2,0],
        [3,0],
        [3,3]
    ],
    [0,1,2]
)

t = 1
t = int(input())
while t > 0:
    t-=1
    mydfa.runMachine(input())
