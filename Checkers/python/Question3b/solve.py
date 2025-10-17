from .. import dfa
from dfa import *
import sys
sys.stdin = open("input.txt","r")

mydfa = DFA(
    "", # input your symbols
    [
        # input your table
    ],
    [] # input your final accepting states
)

t = 1
t = int(input())
while t > 0:
    t-=1
    mydfa.runMachine(input())
