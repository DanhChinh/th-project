import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import logic
from functools import partial
import time
def handleClick(event):
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
        player()
def computer():
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
        lableShowTurn.config(text="Lượt đi: Người",bg="#006400",fg="#FFFAFA",font=24, width=15)
    else:
        lableShowTurn.config(text="Lượt đi: Máy",fg="#006400",bg="#FFFAFA",font=24, width=15)


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
                    button.bind("<Button-1>", handleClick)

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
    radio1.config(state = "disabled")
    radio2.config(state = "disabled")
    btn.unbind("<Button-1>")
    render(gameState)

#____________________________________________________________________________________
gameState = logic.gameState
root = tk.Tk()
root.title("Game Cờ Tướng ")
root.geometry("1200x800")
background_image = PhotoImage(file="chessboard.png")

#container1: board_____________________________
# Tạo Canvas với kích thước bằng với hình ảnh
canvas = tk.Canvas(root, width=background_image.width(), 
    height=background_image.height())
canvas.place(x=0,y=0)
# Vẽ hình ảnh lên Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
labelComputer = tk.Label(canvas, text="Computer",bg='black',fg='white')
labelComputer.place(x=0,y=0)
labelPlayer = tk.Label(canvas, text="Player", bg='red',fg='white')
labelPlayer.place(x=0,y=background_image.height()-25)

selected_old = None
selected_new = None
#frameController: ______________________________

frameController = tk.Frame(root, width=480, 
    height=background_image.height(),
    bg="#4682B4",
    relief=tk.SUNKEN)
frameController.place(x=700,y=0)
#
frameController1 = tk.Frame(frameController, width=470, 
    height = 40,
    relief=tk.SUNKEN)
frameController1.place(x=5,y=5)
labelChoseTurn = tk.Label(frameController1,text = "Đi trước: ")
labelChoseTurn.place(x=10,y=5)
selected_option = tk.StringVar()
selected_option.set("Nguoi")
radio1 = tk.Radiobutton(frameController1, text="Người", variable=selected_option, value="Nguoi")
radio1.place(x=100,y=5)
radio2 = tk.Radiobutton(frameController1, text="Máy", variable=selected_option, value="May")
radio2.place(x=185,y=5)
buttonStart = tk.Button(frameController1,text="Bắt đầu",height=1)
buttonStart.bind("<Button-1>", handleClickBtStart)
buttonStart.place(x=260,y=3)
#
buttonTogle = tk.Button(root,text=f"isPlayerTurn: {gameState.isPlayerTurn}")
buttonTogle.bind("<Button-1>",partial(togleTurn,node=gameState))
buttonTogle.place(x=700,y=100)

lableShowTurn = tk.Label(frameController,text="Luot di:   ")
lableShowTurn.config(bg="#006400",fg="#FFFAFA",font=24,width=15)
lableShowTurn.place(x=5,y=60)

labelTimer = tk.Label(root,text="")
labelTimer.place(x=270,y=360)
# root.bind("<Motion>", motion_handler)
root.mainloop()






