import sys

board = [['xe', 'ma','tinh','si','tuong','si','tinh','ma','xe'],
['','','','','','','','',''],
['','phao','','','','','','phao',''],
['tot','','tot','','tot','','tot','','tot'],
['','','','','','','','',''],
['','','','','','','','',''],
['tot','','tot','','tot','','tot','','tot'],
['','phao','','','','','','phao',''],
['','','','','','','','',''],
['xe', 'ma','tinh','si','tuong','si','tinh','ma','xe']]




#cach luu tru 1
class Chessman:
    def __init__(self, name, color, row, col, isUp):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        self.isUp = isUp


for i in range(10):
    for j in range(9):
        if board[i][j]:
            color = "red"
            if i<5:
                color = "black"
            board[i][j] = Chessman(board[i][j], color, i, j, True)
        else:
            board[i][j] = None


class Node:
    def __init__(self, board, isPlayerTurn, selected=None ,parent=None):
        self.board = board
        self.isPlayerTurn = isPlayerTurn
        self.childrens = []
        self.validMoveDict = {}
        self.selected = selected
        self.parent = parent
    def getValue(self):
        return 0

def validMove(Node, row, col):
    pass
        

gameState = Node(board, True)
gameState.selectedIndex = [0, 0]
gameState.validMoveDict = {
    "00":[[1,0],[2,0]],
    "01":[[1,1],[2,1]]}