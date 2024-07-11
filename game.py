import tkinter as tk

class ChineseChess:
    def __init__(self, root):
        self.root = root
        self.root.title("Chinese Chess")
        self.root.geometry("1000x800")
        self.padding = 25
        self.width_cell =60
        self.r = int(0.375*self.width_cell)
        self.canvas = tk.Canvas(
            root, 
            width=self.padding*2 + self.width_cell*8, 
            height=self.padding*2 + self.width_cell*9, 
            bg="light yellow"
            )
        # self.canvas.place(x=0, y=0)
        self.turn = "red"
        self.canvas.pack()
        self.pieces = {}
        self.setup_board()
        self.setup_pieces()
        self.selected_piece = None
        self.valid_moves = {}
        # if self.turn == "black":
        #     self.ai_move()

    def setup_board(self):
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
    def setup_pieces(self):
        board = [   
                    ['chariot', 'horse','elephant','advisor','general','advisor','elephant','horse','chariot'],
                    ['','','','','','','','',''],
                    ['','cannon','','','','','','cannon',''],
                    ['soldier','','soldier','','soldier','','soldier','','soldier'],
                    ['','','','','','','','',''],
                    ['','','','','','','','',''],
                    ['soldier','','soldier','','soldier','','soldier','','soldier'],
                    ['','cannon','','','','','','cannon',''],
                    ['','','','','','','','',''],
                    ['chariot', 'horse','elephant','advisor','general','advisor','elephant','horse','chariot']
                ]

        padding = self.padding
        width_cell = self.width_cell
        r = self.r
        for y in range(10):
            for x in range(9):
                if board[y][x]:
                    self.create_piece(board[y][x], x, y, "black" if y<5 else "red")
                x0, y0 = padding + x * width_cell, padding + y * width_cell
                tag = f"cell{y}_{x}"
                cell_id = self.canvas.create_rectangle(x0 - r, y0 - r, x0 + r, y0 + r,outline="", fill="", tags = tag)
                self.canvas.tag_bind(tag, "<Button-1>", lambda e, x=x, y=y: self.on_cell_click(e, x, y))
                # self.canvas.lift(cell_id)

    def create_piece(self, name, x, y, color):
        name_dict = {
            "chariot": ["xe","車","俥"],
            "horse": ["mã", "馬","馬"],
            "elephant": ["tịnh", "象","相"],
            "advisor":["sĩ", "士","仕"],
            "general": ["tướng", "將","帥"],
            "cannon": ["pháo", "包","炮"],
            "soldier": ["tốt", "卒","兵"]
            }
        name_chinese = name_dict[name][1] #black
        if y>4:
            name_chinese = name_dict[name][2] #red
        x0, y0 = self.padding + x * self.width_cell, self.padding + y * self.width_cell
        r = self.r
        oval_id = self.canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, fill=color)
        text_id = self.canvas.create_text(x0, y0, text=name_chinese, fill="white",  font= 12)
        self.pieces[(x, y)] = {
            "oval_id":oval_id, 
            "text_id":text_id, 
            "name":name,
            "color":color,
            "name_vie":name_dict[name],
            "name_chinese":name_chinese
            }




    def on_cell_click(self, event, x, y):
        if not self.selected_piece and (x,y) not in self.pieces:
            return
        if not self.selected_piece:
            # Nếu chưa có quân cờ nào được chọn
            self.select_piece(x, y)
        elif self.selected_piece == (x, y):
            # Nếu click vào chính quân cờ đã chọn, bỏ chọn
            self.clear_selection()
        else: #self.selected_piece != (x,y)
            # Nếu có một quân cờ được chọn và click vào ô có thể di chuyển
            if (x, y) in self.valid_moves[self.selected_piece]:
                self.move_piece(self.selected_piece[0], self.selected_piece[1], x, y)
                self.clear_selection()
            else:
                # Nếu click vào quân cờ khác, chọn quân cờ khác
                self.clear_selection()
                self.select_piece(x, y)

    def select_piece(self, x, y):
        self.selected_piece = (x, y)
        oval_id = self.pieces[(x, y)].get("oval_id")
        self.canvas.itemconfig(oval_id, outline="blue", width=2)
        if (x, y ) not in self.valid_moves:
            print(x,y, "not in valid moves")
            self.valid_moves[(x, y)] = self.calculate_valid_moves(x, y)
        else:
            print(x,y, "exist")
        self.highlight_valid_moves((x, y))

    def clear_selection(self):
        if self.selected_piece:
            oval_id = self.pieces[self.selected_piece]["oval_id"]
            self.canvas.itemconfig(oval_id, outline="black", width=1)
        self.clear_valid_moves() #clear highlight
        self.selected_piece = None


    def highlight_valid_moves(self, key):
        padding = self.padding
        width = self.width_cell
        r = self.r
        for move in self.valid_moves[key]:
            #delete this line# if move not in self.pieces:
            x0, y0 = padding + move[0] * width, padding + move[1] * width
            self.canvas.create_rectangle(
                x0 - r, y0 - r, 
                x0 + r, y0 + r, 
                outline="green", 
                width=2, 
                tag="highlight"
                )

    def clear_valid_moves(self):
        self.canvas.delete("highlight")
    def move_piece(self, from_x, from_y, to_x, to_y):
        # print(f"move_piece({from_x}, {from_y}, {to_x}, {to_y})")
        from_piece = self.pieces.pop((from_x, from_y))
        if (to_x, to_y) in self.pieces:
            to_piece = self.pieces.pop((to_x, to_y))
            self.canvas.delete(to_piece["oval_id"])
            self.canvas.delete(to_piece["text_id"])

        oval_id, text_id = from_piece["oval_id"], from_piece["text_id"]
        x0, y0 = self.padding + to_x * self.width_cell, self.padding + to_y * self.width_cell
        r = self.r
        self.canvas.coords(oval_id, x0 - r, y0 - r, x0 + r, y0 + r)
        self.canvas.coords(text_id, x0, y0)
        self.canvas.lower(text_id)
        self.canvas.lower(oval_id)
        self.pieces[(to_x, to_y)] = from_piece
        self.selected_piece = (to_x, to_y)
        #xoa self.valid_moves
        self.valid_moves = {}
    def valid_moves_chariot(self, x, y):
        moves = []
        current_color = self.pieces[(x, y)].get("color")
        # Di chuyển theo hàng ngang và dọc
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx <= 8 and 0 <= ny <= 9:  # Bàn cờ Cờ Tướng có kích thước 10x9
                    # Nếu gặp quân cờ khác
                    if (nx, ny) in self.pieces:
                        other_piece = self.pieces[(nx, ny)]
                        other_color = other_piece.get("color")
                        if other_color != current_color:
                            moves.append((nx, ny))
                        break
                    moves.append((nx, ny))
                else:
                    break
        return moves
    def valid_moves_horse(self, x, y):
        moves = []
        current_color = self.pieces[(x, y)].get("color")
        horse_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        
        for dx, dy in horse_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 8 and 0 <= ny <=9:
                if dx == 2 and (x + 1, y) in self.pieces:
                    continue
                if dx == -2 and (x - 1, y) in self.pieces:
                    continue
                if dy == 2 and (x, y + 1) in self.pieces:
                    continue
                if dy == -2 and (x, y - 1) in self.pieces:
                    continue
                if (nx, ny) in self.pieces:
                    other_piece = self.pieces[(nx, ny)]
                    other_color = other_piece.get("color")
                    if other_color!= current_color:
                        moves.append((nx, ny))
                else:
                    moves.append((nx, ny))
        return moves
    def valid_moves_elephant(self, x, y):
        moves = []
        elephant_moves = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
        current_piece_color = self.pieces[(x, y)]["color"]
        min_x, max_x = 0, 8
        min_y, max_y = 0, 4
        if current_piece_color == "red":
            min_y, max_y = 5, 9
        for dx, dy in elephant_moves:
            nx, ny = x + dx, y + dy
            if min_x <= nx <= max_x and min_y <= ny <= max_y:
                if (nx, ny) in self.pieces:
                    other_piece_color = self.pieces[(nx, ny)]["color"]
                    if other_piece_color != current_piece_color:
                        moves.append((nx, ny))
                else:
                    moves.append((nx, ny))
        return moves
    def valid_moves_advisor(self, x, y):
        moves = []
        advisor_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        current_piece_color = self.pieces[(x, y)]["color"]
        min_x, max_x = 3, 5
        min_y, max_y = 0, 2
        if current_piece_color == "red":
            min_y, max_y = 7, 9
        for dx, dy in advisor_moves:
            nx, ny = x + dx, y + dy
            if min_x <= nx <= max_x and min_y <= ny <= max_y:
                if (nx, ny) in self.pieces:
                    other_piece_color = self.pieces[(nx, ny)]["color"]
                    if other_piece_color != current_piece_color:
                        moves.append((nx, ny))
                else:
                    moves.append((nx, ny))
        return moves
    def valid_moves_general(self, x, y):
        moves = []
        current_color = self.pieces[(x, y)].get("color")
        king_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_x,max_x = 3, 5
        min_y,max_y = 0, 2
        if current_color == "red":
            min_y, max_y = 7, 9
        for dx, dy in king_moves:
            nx, ny = x + dx, y + dy
            if min_x <= nx <= max_x  and min_y <= ny <= max_y:
                if (nx, ny) in self.pieces:
                    other_piece = self.pieces[(nx, ny)]
                    other_color = other_piece.get("color")
                    if other_color!= current_color:
                        moves.append((nx, ny))
                else:
                    moves.append((nx, ny))
        return moves
    def valid_moves_cannon(self, x, y):
        # print("valid_moves_cannon", x, y)
        return self.valid_moves_chariot( x, y)
    def valid_moves_soldier(self, x, y):
        moves = []
        current_color = self.pieces[(x, y)].get("color")
        soldier_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_x, max_x,min_y ,max_y = x,x,0,9
        if current_color == "red":
            min_y, max_y = min(y,0), max(y,0)
            if y<=4:
                min_x, max_x = 0,8
        else:
            min_y, max_y = min(y,9), max(y,9)
            if y>=5:
                min_x, max_x = 0,8
        for dx, dy in soldier_moves:
            nx, ny = x + dx, y + dy
            # print(f"{nx}, {ny} = {x} + {dx}, {y} + {dy}")
            # print(f"{min_x} <= {nx} <= {max_x}  and {min_y} <= {ny} <= {max_y}")
            if min_x <= nx <= max_x  and min_y <= ny <= max_y:
                if (nx, ny) in self.pieces:
                    other_piece = self.pieces[(nx, ny)]
                    other_color = other_piece.get("color")
                    if other_color!= current_color:
                        moves.append((nx, ny))
                else:
                    moves.append((nx, ny))
        return moves
    def calculate_valid_moves(self, x, y):
        piece_name = self.pieces[(x, y)].get("name")
        dict_moves = {
            "chariot": self.valid_moves_chariot,
            "horse": self.valid_moves_horse,
            "elephant": self.valid_moves_elephant,#
            "advisor":self.valid_moves_advisor,#
            "general": self.valid_moves_general,
            "cannon": self.valid_moves_cannon,#
            "soldier": self.valid_moves_soldier,#
            }
        return dict_moves[piece_name](x, y)
 



    def ai_move(self):
        root_node = Node(self.board_state(), self.turn)
        best_move = find_best_move(root_node)
        if best_move:
            self.move_piece(best_move[0], best_move[1])


    def board_state(self):
        board = [['' for _ in range(9)] for _ in range(10)]
        for (x, y), (oval, text) in self.pieces.items():
            board[x][y] = self.canvas.itemcget(text, "text")
        return board

root = tk.Tk()
game = ChineseChess(root)
root.mainloop()
