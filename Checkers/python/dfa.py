class DFA:
    def __init__(self,symbols:str,table:list[list],F_accStates:list) -> None:
        self.symbols = symbols
        self.map = { c:int(i) for i,c in enumerate(symbols) }
        self.table = table.copy()
        self.F_States = [False]*len(table)
        for s in F_accStates: self.F_States[s] = True
    
    def runMachine(self, L:str) -> bool:
        state:int = 0
        for c in L:
            t = self.map[c]
            state = self.table[state][t]
        return self.F_States[state]

    def makeGraph(self):
        print("the graph representation of your dfa is:")
        for si,states in enumerate(self.table):
            for i,s in enumerate(states):
                print(f"{si} {s} {self.symbols[i]}")
        print("\nPaste this graph at: https://mxwell.github.io/draw-graph/\n")

    def stateTable(self):
        print("The state table representation of your DFA:")
        print("symbols:",end='\t')
        for a in self.symbols: print(a,end='\t')
        for si,transitions in enumerate(self.table):
            print(f"state[{si}]-> ",end='\t')
            for t in transitions: print(t,end='\t')
            print('\n')