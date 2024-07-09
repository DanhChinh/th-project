import tkinter as tk
from tkinter import Menu

def on_open():
    print("Open selected")

def on_save():
    print("Save selected")

def on_exit():
    root.quit()

root = tk.Tk()
root.title("Context Menu Example")

# Tạo context menu
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Open", command=on_open)
context_menu.add_command(label="Save", command=on_save)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=on_exit)

# Hàm hiển thị context menu
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

# Bind chuột phải để hiển thị context menu
root.bind("<Button-3>", show_context_menu)

# Thêm một Label để dễ dàng test context menu
label = tk.Label(root, text="Right-click to show context menu")
label.pack(pady=50, padx=50)

root.mainloop()
