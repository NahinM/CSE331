class NFA:
    def __init__(self,symbols:str, q0:list, table:list[list[list]], Fn:list[int]) -> None:
        self.symbols:str = symbols
        self.q0:list = q0
        self.map:dict = { c:int(i) for i,c in enumerate(symbols) }
        self.table:list[list[list]] = table
        self.F_States:list[bool] = [False]*len(table)
        for s in Fn: self.F_States[s] = True
    
    def runMachine(self,L:str) -> bool:
        from collections import deque
        states = deque()
        for qi in self.q0: states.append(qi)
        for c in L:
            for _ in range(len(states)):
                state_i = states.popleft()
                transition = self.map[c]
                for state in self.table[state_i][transition]: states.append(state)
        while states:
            if self.F_States[states.popleft()]: return True
        return False