from package.dfa import DFA
from package.nfa import NFA

MY_FA:DFA|NFA
Question:str


# Set your Question no:
Question = "1"

# Input your DFA|NFA:

# MY_FA = NFA(
#     "01", # input symbols
#     [], # input all the starting states q0
#     [
#         [[],[]],
#     ],
#     [] #input accepting final states
# )

MY_FA = DFA(
    "01", # input symbols
    [
        [] # input transition states
    ],
    []  #input accepting final states
)