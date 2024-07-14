import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
    
class ChineseChess:
    def __init__(self, root):
        self.root = root
        self.root.title("Chinese Chess")
        # self.root.geometry("1000x800")
        self.padding = 25
        self.width_cell =60
        self.id_line = None
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
        # print("getValue:", evaluate_board(self.pieces))

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
        board = [   
                    ['', '','','','general','','','',''],
                    ['','','','','','','','',''],
                    ['','','','','','','','',''],
                    ['','','','','','','horse','',''],
                    ['','','','','','','','',''],
                    ['','','','','','horse','','',''],
                    ['','','','','','','','',''],
                    ['','','','','','','','',''],
                    ['','','','','','','','',''],
                    ['', '','','','general','','','','']
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
                self.canvas.tag_bind(tag, "<Button-1>", lambda e, x=x, y=y: self.handle_left_click(e, x, y))
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




    def handle_left_click(self, event, x, y):
        if self.turn == "black":
            return

        if not self.selected_piece and (x,y) not in self.pieces:
            return
        # fix loi 
        # if not self.select_piece and  self.pieces[(x,y)]["color"] != self.turn:
        #     return
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
                self.selected_piece = (x,y)
                self.clear_selection()
            else:
                # Nếu click vào quân cờ khác, chọn quân cờ khác
                self.clear_selection()
                self.select_piece(x, y)

    def select_piece(self, x, y):
        self.selected_piece = (x, y)
        oval_id = self.pieces[(x, y)].get("oval_id")
        self.canvas.itemconfig(oval_id, outline="blue", width=2)
        self.canvas.update()
        if (x, y ) not in self.valid_moves:
            self.valid_moves[(x, y)] = get_valid_moves(self.pieces, x, y)
        else:
            print(x,y, "exist")
        self.highlight_valid_moves((x, y))

    def clear_selection(self):
        # print("clear_selection", self.selected_piece)
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
    def draw_line(self,x,y,xx,yy):
        x = self.padding + x* self.width_cell
        y = self.padding + y* self.width_cell
        xx = self.padding + xx* self.width_cell
        yy = self.padding + yy* self.width_cell
        # self.canvas.delete(self.id_line)  # delete old line if exists
        if self.id_line:
            self.canvas.delete(self.id_line)
            self.id_line = None
        self.id_line =  self.canvas.create_line(x, y, xx, yy, fill="green", width=4)
        self.canvas.update()


 
    def move_piece(self, from_x, from_y, to_x, to_y):
        # print(f"move_piece({from_x}, {from_y}, {to_x}, {to_y})")
        self.draw_line(from_x, from_y, to_x, to_y)
        from_piece = self.pieces.pop((from_x, from_y))
        if (to_x, to_y) in self.pieces:
            to_piece = self.pieces.pop((to_x, to_y))
            #fix moves outboart list
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
        # self.selected_piece = (to_x, to_y)
        #xoa self.valid_moves
        self.valid_moves = {}
        if self.turn == "red":
            self.turn = "black"
            self.canvas.update()
            self.AI_move()
        else:
            self.turn = "red"






    def get_all_moves(self, color):
        # Hàm trả về tất cả các nước đi hợp lệ của màu quân cờ
        # print("get_all_moves",self.pieces.items())
        moves = []
        for (x, y), piece in self.pieces.items():
            if piece["color"] == color:
                moves.extend([(x, y, nx, ny) for nx, ny in self.calculate_valid_moves(x, y)])
        # from_x, from_y, to_x, to_y = random.choice(moves)
        # print(from_x, from_y, to_x, to_y)
        # self.move_piece(from_x, from_y, to_x, to_y)
        return moves

    def make_move(self, move):
        # Hàm thực hiện một nước đi
        from_x, from_y, to_x, to_y = move
        self.move_piece(from_x, from_y, to_x, to_y)

    def undo_move(self, move):
        # Hàm hoàn tác một nước đi
        from_x, from_y, to_x, to_y = move
        self.move_piece(to_x, to_y, from_x, from_y)

    def is_game_over(self):
        # Hàm kiểm tra xem trò chơi đã kết thúc hay chưa
        # Bạn cần triển khai hàm này dựa trên luật chơi cờ tướng
        return False


    def AI_move(self):
        print("AI move")
        first_node = Node(self.turn, self.pieces )
        min_node = Node("min", {})
        min_node.inf_min = True
        max_node = Node("max", {})
        max_node.inf_max = True
        best_node = alphabeta(first_node, 3, min_node, max_node, True)
        affterroot = find_affterroot(best_node)
        # print(affterroot.counter)
        # print(affterroot.get_value())
        (x,y,z,t) = affterroot.fromTo
        self.move_piece(x,y,z,t)
        print("Player move")

def find_affterroot(node):
    if node.parent.parent == None:
        return node 
    return node.parent
def setUpBoard(root):
    board = ttk.Labelframe(
        root,
        bootstyle="info",
        width = 500,
        height = 600,
        text = 'board'
        )
    board.place(x=10, y=10)
    return board

def setUpRemote(root):
    pass

root = tk.Tk()
root.title("Chess")
root.geometry("1000x800")
root.attributes("-topmost", True)

board = setUpBoard(root)
remote = setUpRemote(root)
root.mainloop()
