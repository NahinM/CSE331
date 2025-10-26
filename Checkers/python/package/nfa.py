class NFA:
    def __init__(self,symbols:str, table:list[list[list]], Fn:list[int]) -> None:
        self.symbols:str = symbols
        self.map:dict = { c:int(i) for i,c in enumerate(symbols) }
        self.table:list[list[list]] = table
        self.F_States:list[bool] = [False]*len(table)
        for s in Fn: self.F_States[s] = True
    
    def runMachine(self,L:str) -> bool:
        from collections import deque
        states = deque()
        states.append(0)
        for c in L:
            for _ in range(len(states)):
                for state in self.table[states.popleft()][self.map[c]]: states.append(state)
        while states:
            if self.F_States[states.popleft()]: return True
        return False