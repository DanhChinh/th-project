import tkinter as tk 

root = tk.Tk()
def handlerClick():
    global counter
    for i in range(10):
        for j in range(10):
            label = tk.Label(root, text=f"({counter})", width=5, height=2)
            counter+=1
            label.grid(row=i, column=j) 
            root.update_idletasks()
counter = 0
for i in range(10):
    for j in range(10):
        label = tk.Label(root, text=f"({counter})", width=5, height=2, bd=1)
        counter+=1
        label.grid(row=i, column=j)
btn = tk.Button(root,text="click",
    command = handlerClick)
btn.grid(row=11, column=5)
root.mainloop()