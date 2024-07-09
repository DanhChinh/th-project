import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from tkinter import PhotoImage
import logic
from functools import partial
# import time


def handleLeftClick(event):
    if event.widget.cget("state")=="disabled":
        return
    global selected_old, selected_new
    # x, y = event.x, event.y
    # print(f"Button clicked at ({x}, {y})")
    selected_old = selected_new
    selected_new = event.widget
    selected = selected_new
    if selected_new is selected_old:
        if selected_new.cget("bd") == 1:
            selected_new.config(bd=5)
        else:
            selected_new.config(bd=1)
            selected = None
            print("Cancel")
    else:
        if selected_old:
            selected_old.config(bd=1)
        selected_new.config(bd=5)
    if selected:
        print(f"Tinh nuoc di o vi tri [{selected.row}][{selected.col}]")
        # validMove(node, selected.row, selected.col)
        # move(node, selected.row, selected.col,)
        # player()
def on_open():
    print("Open selected")
def on_save():
    print("Save selected")
def on_cancel():
    context_menu.unpost()
def handleRightClick(event):

    print("Right click")
    buttonChessman = event.widget
    # if buttonChessman.cget("state")=="disabled":
    #     return
    # context_menu.delete(0, 'end')
    # context_menu.unpost()
    context_menu.post(event.x_root, event.y_root)
def computer():
    '''
    dung trong co up
    neu may di, may chi can tim ra nuoc di tot nhat, 
    viec thuc hien thay doi vi tri tren ban co nen duoc nguoi dung thao tao
    '''
    for i in range(5):
        print(f"Computer call...{i}")
        time.sleep(1)
    print("done")
    move(node, 1,1,1,1)
def move(node, start_row, start_col, end_row, end_col):
   print(f"move: {start_row}.{start_col}->{end_row}.{end_col}") 


'''
render khi nao:
    khi chuyen doi luot choi
render cai gi:
    render ban co va lable luot di
'''
def render(node):
    global lableShowTurn

    if node.isPlayerTurn:
        lableShowTurn.config(text="Lượt đi: Người")
    else:
        lableShowTurn.config(text="Lượt đi: Máy")


    space = 67
    xx=69
    yy=69
    buttonState = "disabled"
    if node.isPlayerTurn:
        buttonState = "normal"
    for row in range(10):
        for col in range(9):
            if node.board[row][col]:
                button = tk.Button(canvas)
                button.config(
                    text=node.board[row][col].name,
                    width=5,height=2,padx=0,pady=0,
                    fg="white",
                    state = buttonState,
                    bg = node.board[row][col].color)
                button.row = row
                button.col = col
                button.chessman = node.board[row][col]
                if node.isPlayerTurn:
                    button.bind("<Button-1>", handleLeftClick)
                    button.bind("<Button-3>", handleRightClick)#partial(handleRightClick, parentWidget = canvas))

                button.place(x=xx-23, y=yy-23)

            xx += space
        xx = 69
        yy += space
def togleTurn(event, node):
    
    node.isPlayerTurn = not node.isPlayerTurn
    event.widget.config(text = f"isPlayerTurn: {node.isPlayerTurn}")
    render(node)
def motion_handler(event):
    x, y = event.x, event.y
    print(f"Mouse moved to ({x}, {y})")
def handleClickBtStart(event):
    global gameState
    if selected_option.get() == "Nguoi":
        gameState.isPlayerTurn = True
    else:
        gameState.isPlayerTurn = False
    btn = event.widget
    btn.config(state = "disabled")
    radioChoseTurn1.config(state = "disabled")
    radioChoseTurn2.config(state = "disabled")
    btn.unbind("<Button-1>")
    render(gameState)
def setTheme(style,theme):
    global gameState
    style.theme_use(theme)
    render(gameState)
#____________________________________________________________________________________
gameState = logic.gameState
selected_old = None
selected_new = None
root = tk.Tk()
root.title("Game Cờ Tướng ")
root.geometry("1200x800")
background_image = PhotoImage(file="chessboard.png")
style = Style(theme='superhero')

#setting




#container1: board_____________________________
# Tạo Canvas với kích thước bằng với hình ảnh
canvas = tk.Canvas(root, 
    width=background_image.width(), 
    height=background_image.height()
    )
canvas.place(x=0,y=0)
# Vẽ hình ảnh lên Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
labelComputer = ttk.Label(canvas, 
    text="Computer", 
    bootstyle = 'inverse-dark'
    )
labelComputer.place(x=0,y=0)
labelPlayer = ttk.Label(canvas, 
    text="Player", 
    bootstyle = 'inverse-danger'
    )
labelPlayer.place(x=0,y=background_image.height()-24)

#frameController: ______________________________

frameController = ttk.Frame(root, 
    width=480, 
    # bootstyle = "light",
    height=background_image.height()
    )
frameController.place(x=700,y=0)

#frameCrlstart
frameStart = ttk.Labelframe(frameController, 
    width=480,
    height = 60,
    bootstyle = "success",
    text="Start" 
    )
frameStart.place(x=0,y=5)

labelChoseTurn = ttk.Label(frameStart,
    text = "Đi trước: ",)
labelChoseTurn.place(x=10,y=5)
selected_option = tk.StringVar()
selected_option.set("Nguoi")
radioChoseTurn1 = ttk.Radiobutton(frameStart,
    bootstyle="info", 
    text="Người", 
    variable=selected_option, 
    value="Nguoi"
    )
radioChoseTurn1.place(x=100,y=5)
radioChoseTurn2 = ttk.Radiobutton(frameStart, 
    bootstyle="info",
    text="Máy", 
    variable=selected_option, 
    value="May"
    )
radioChoseTurn2.place(x=185,y=5)
buttonStart = ttk.Button(frameStart,
    bootstyle="info",
    text="Bắt đầu"
    )
buttonStart.bind("<Button-1>", handleClickBtStart)
buttonStart.place(x=260,y=0)
#frameInformation
frameInformation = ttk.Labelframe(frameController,
    bootstyle="success",
    text = "Information",
    width = 480,
    height=150
    )
frameInformation.place(x=0,y=70)
lableShowTurn = ttk.Label(frameInformation,
    text="Lượt đi:   "
    )
lableShowTurn.place(x=5,y=5)

# buttonTogle = tk.Button(root,text=f"isPlayerTurn: {gameState.isPlayerTurn}")
# buttonTogle.bind("<Button-1>",partial(togleTurn,node=gameState))
# buttonTogle.place(x=700,y=100)

#frameSetting
frameSetting = ttk.Labelframe(frameController,
    bootstyle="success",
    text="Settings",
    width = 480,
    height=150
    )
frameSetting.place(x=0,y=500)


themes = [
    "superhero", "darkly", "cyborg", "cosmo", "journal", 
    "litera", "minty", "pulse", "sandstone", "simplex"
]
theme_choice = tk.StringVar()
theme_choice.set("superhero")
for idx, choice in enumerate(themes):
    rb = ttk.Radiobutton(frameSetting, 
        text=choice, 
        value=choice, 
        variable=theme_choice,
        command = lambda: setTheme(style,theme_choice.get())
        )
    rb.grid(row=idx//4, 
        column=idx%4, 
        padx=10, 
        pady=10
        )
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Open", command=on_open)
context_menu.add_command(label="Save", command=on_save)
context_menu.add_separator()
context_menu.add_command(label="Cancel", command=on_cancel)
# root.bind("<Motion>", motion_handler)
root.mainloop()






