"""
"""

from typing import List, Tuple

class BoardProblem:
    def __init__(self, name: str, board: List[List[int]], start: Tuple[int, int], target: Tuple[int, int]):
        self.name = name
        self.board = board
        self.start = start
        self.target = target
        self.n = len(board)

    def __str__(self):
        return f"Board: {self.name} of ({self.n} x {self.n}), start: {self.start}, target: {self.target}"
    
simple_board = BoardProblem(
    name="simple board 5x5", 
    board=[[1, 4, 7, 2, 6], [12, 1, 2, 2, 6], [1, 4, 70, 2, 6], [0, 6, 0, 2, 0], [1, 4, 7, 2, 6]]
    start = (0, 0), 
    target=(4, 4)
)