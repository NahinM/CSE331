class DFA:
    def __init__(self,symbols,table,fState) -> None:
        self.SYMBOLS = symbols
        self.TABLE = table
        self.FINAL_STATES = [False]*len(table)
        for f in fState:
            self.FINAL_STATES[f] = True
        self.map = { c:i for i,c in enumerate(symbols)}

    def makeGraph(self):
        print("Graph representation of the DFA:")
        for s,state in enumerate(self.TABLE):
            for i,t in enumerate(state):
                print(f"{s} {t} {self.SYMBOLS[i]}")
        print("\nCopy & Past this graph at: https://mxwell.github.io/draw-graph/")
    
    def runMachine(self, L):
        state = 0
        for c in L:
            t = self.map[c]
            state = self.TABLE[state][t]
        return self.FINAL_STATES[state]