from package.dfa import DFA
from package.nfa import NFA

MY_FA:DFA|NFA
Question:str


# Set your Question no:
Question = "19"

# Input your DFA|NFA:
# MY_FA = NFA(
#     "01",
#     [
#         [[0],[1]],
#         [[2,4],[1]],
#         [[3],[]],
#         [[2],[1]],
#         [[4],[]]
#     ],
#     [0,1,3,4]
# )

MY_FA = DFA(
    "01",
    [
        
    ],
    []
)