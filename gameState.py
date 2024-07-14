import copy
import numpy
class gameState:
    def __init__(self,board, turn):
        self.board = board
        self.turn = 'red'
        self.undoBoard = None
    def show(self):
        print('\nturn',self.turn)
        print(numpy.array(self.board))
    def move(self, fx,fy, tx,ty):
        #delete
        if not self.board[fx][fy]:
            print('No piece at starting position')
            return
        #delete_end
        self.undoBoard = copy.deepcopy(self.board)
        self.board[tx][ty] = self.board[fx][fy]
        self.board[fx][fy] = None
        self.turn = 'black' if self.turn =='red' else'red'
    def undo(self):
        if self.undoBoard:
            self.board = copy.deepcopy(self.undoBoard)
            self.turn = 'black' if self.turn =='red' else'red'
            self.undoBoard = None
        #delete
        else:
            print('No previous move to undo')
        #delete_end

def get_all_moves(state):
    moves = []
    for (x, y), piece in self.pieces.items():
        if piece[2] == color:
            moves.extend([(x, y, nx, ny) for nx, ny in self.calculate_valid_moves(x, y)])
    return moves

def find_best_move(state, depth):
    best_move = None
    best_value = float('-inf')
    for move in get_all_moves(state):
        '''
        self.make_move(move)
        move_value = self.minimax(depth - 1, float('-inf'), float('inf'), False)
        self.undo_move(move)
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

# board = [   
#     ['', '','','','general','','','',''],
#     ['','','','','','','','',''],
#     ['','','','','','','','',''],
#     ['','','','','','','horse','',''],
#     ['','','','','','','','',''],
#     ['','','','','','horse','','',''],
#     ['','','','','','','','',''],
#     ['','','','','','','','',''],
#     ['','','','','','','','',''],
#     ['', '','','','general','','','','']]
# firstState = gameState(board, 'red')
