import tkinter as tk 
from gameState import makeInitGameState
from rule import get_valid_moves
class ChessBoard:
    def __init__(self, root, state):
        self.gameState = state
        self.padding = 25
        self.width_cell = 60
        self.r = int(0.375 * self.width_cell)
        self.canvas = tk.Canvas(
            root, 
            width=self.padding*2 + self.width_cell*8, 
            height=self.padding*2 + self.width_cell*9, 
            bg="light yellow"
            )
        self.selected = None
    def draw_board(self):
        self.canvas.pack()
        # Vẽ bàn cờ
        # Ve hàng
        padding = self.padding
        width_cell = self.width_cell
        x_start = padding
        x_end = padding + 8*width_cell
        y_start1 = padding
        y_end1 = padding + 4*width_cell
        y_start2 = padding+ 5*width_cell
        y_end2 = padding+ 9*width_cell
        
        for i in range(10):  
            y = padding + i*width_cell
            self.canvas.create_line(x_start, y, x_end, y)
        #Vẽ cột
        for i in range(9):
            x = padding + i*width_cell
            self.canvas.create_line(x,y_start1, x,y_end1)
            self.canvas.create_line(x,y_start2, x,y_end2)
        # Vẽ cung tướng
        self.canvas.create_line(
            padding+3*width_cell, padding,
            padding+5*width_cell, padding+2*width_cell
            )
        self.canvas.create_line(
            padding+5*width_cell, padding,
            padding+3*width_cell, padding+2*width_cell
            )
        self.canvas.create_line(
            padding+3*width_cell, padding+7*width_cell,
            padding+5*width_cell, padding+9*width_cell
            )
        self.canvas.create_line(
            padding+5*width_cell, padding+7*width_cell,
            padding+3*width_cell, padding+9*width_cell
            )
    def draw_pieces(self):
        pieces = self.gameState.pieces
        name_dict = {
            "chariot": ["xe","車","俥"],
            "horse": ["mã", "馬","馬"],
            "elephant": ["tịnh", "象","相"],
            "advisor":["sĩ", "士","仕"],
            "general": ["tướng", "將","帥"],
            "cannon": ["pháo", "包","炮"],
            "soldier": ["tốt", "卒","兵"]
            }
        for (row,col), piece in pieces.items():
            name = name_dict[piece['name']][1]
            if piece['color'] == 'red':
                name = name_dict[piece['name']][2]
            x0 = self.padding +  col* self.width_cell 
            y0 = self.padding + row * self.width_cell
            r = self.r
            tag = f"chessman{row}_{col}"
            self.canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, fill=piece['color'], tags = tag)
            self.canvas.create_text(x0, y0, text=name, fill="white",  font= 12, tags = tag)
    def add_event(self):
        print("Player move")
        width_cell = self.width_cell
        padding = self.padding
        r  = self.r
        for row in range(10):
            for col in range(9):
                x0 = padding + col * width_cell
                y0 = padding + row * width_cell
                tag = f"cell{row}_{col}"
                cell_id = self.canvas.create_rectangle(x0 - r, y0 - r, x0 + r, y0 + r,outline="", fill="", tags = tag)
                self.canvas.tag_bind(tag, "<Button-1>", lambda e, row=row, col=col: self.handle_left_click(e, row, col))
    def draw_valid_moves(self):
        self.clear_valid_moves()
        padding = self.padding
        width = self.width_cell
        r = self.r
        moves = self.gameState.player_valid_moves[self.selected]
        for move in moves:
            #delete this line# if move not in self.pieces:
            y0, x0 = padding + move[0] * width, padding + move[1] * width
            self.canvas.create_rectangle(
                x0 - r, y0 - r, 
                x0 + r, y0 + r, 
                outline="green", 
                width=2, 
                tag="highlight"
                )
    def clear_valid_moves(self):
        self.canvas.delete("highlight")
        '''
        handle this function
    def handle_left_click(self, event, row, col):
        if not self.selected:
            self.selected = (row, col)
            self.draw_valid_moves()
        else:
            hand
        '''
    def move(self,best_move):
        (row, col, newrow, newcol) = best_move
        from_tag = f"chessman{row}_{col}"
        to_tag = f"chessman{newrow}_{newcol}"

        (to_oval_id, to_text_id) = self.canvas.find_withtag(to_tag)
        if to_oval_id:
            self.canvas.delete(to_oval_id)
            self.canvas.delete(to_text_id)
        (oval_id, text_id) = self.canvas.find_withtag(from_tag)
        x0, y0 = self.padding + newcol * self.width_cell, self.padding + newrow * self.width_cell
        r = self.r
        self.canvas.coords(oval_id, x0 - r, y0 - r, x0 + r, y0 + r)
        self.canvas.coords(text_id, x0, y0)
        self.draw_line(col, row, newcol, newrow)
    def draw_line(self, x, y, xx, yy ):
        x = self.padding + x* self.width_cell
        y = self.padding + y* self.width_cell
        xx = self.padding + xx* self.width_cell
        yy = self.padding + yy* self.width_cell
        # self.canvas.delete(self.id_line)  # delete old line if exists
        (line_id ) = self.canvas.find_withtag('line')
        if line_id:
            self.canvas.delete(line_id)
        line_id = self.canvas.create_line(x, y, xx, yy, fill="green", width=4, tags = 'line')
        self.canvas.lower(line_id)

    def AI_move(self):
        print("AI_move")
        state = self.gameState
        best_move = state.find_best_move(1)
        newState = self.gameState.makeChild(best_move)
        self.gameState = newState #logic
        self.move(best_move) #ui
        self.gameState.get_dict_valid_moves() #logic
        for (x, y), piece in self.gameState.player_valid_moves.items():
            print((x,y), piece)

        self.add_event() #ui

gameState = makeInitGameState()
root = tk.Tk()
root.attributes("-topmost", True)
board = ChessBoard(root, gameState)
board.draw_board()
board.draw_pieces()
if gameState.turn == 'red':
    board.get_player_valid_moves()
    board.add_event()
else:
    board.AI_move()
root.mainloop()
