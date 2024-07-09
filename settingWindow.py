import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
# Danh sách các chủ đề
themes = [
    "superhero", "flatly", "darkly", "cyborg", "cosmo", "journal", "litera", 
    "lumen", "lux", "materia", "minty", "pulse", "sandstone", "simplex", 
    "sketchy", "slate", "solar", "spacelab", "united", "yeti"
]

def change_theme(event):
    pass



def open_new_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    new_window.focus_set()  # Đặt cửa sổ mới làm cửa sổ được focus
    combobox = ttk.Combobox(new_window, values=themes, textvariable=theme_var, state="readonly")
    combobox.pack(pady=20)
    selected_theme = theme_combobox.get()
    style.theme_use(selected_theme)
    

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def on_select(event):
    selected_theme = theme_var.get()
    style = Style(theme=selected_theme)
    combobox.configure(style=f"{selected_theme}.TCombobox")

root = tk.Tk()
root.title("Combobox with Different Styles")

# Tạo danh sách các chủ đề
themes = [
    "superhero", "flatly", "darkly", "cyborg", "cosmo", "journal",
    "litera", "lumen", "lux", "materia", "minty", "pulse", "sandstone",
    "simplex", "sketchy", "slate", "solar", "spacelab", "united", "yeti"
]

# Tạo một biến để lưu trữ chủ đề chọn
theme_var = tk.StringVar(value=themes[0])

# Tạo ComboBox
combobox = ttk.Combobox(root, values=themes, textvariable=theme_var, state="readonly")
combobox.pack(pady=20)

# Đăng ký sự kiện khi chọn chủ đề
theme_var.trace_add("write", on_select)

# Khởi tạo Combobox với style mặc định
style = Style(theme="superhero")
combobox.configure(style="superhero.TCombobox")

root.mainloop()




# Tạo đối tượng Style từ ttkbootstrap với chủ đề mặc định
    # style = Style(theme="superhero")
    # Tạo Combobox với các chủ đề
    # theme_combobox = ttk.Combobox(root, values=themes)
    # theme_combobox.set("superhero")  # Đặt chủ đề mặc định
    # theme_combobox.pack(pady=20)

    # Gán sự kiện thay đổi chủ đề khi chọn một chủ đề từ Combobox
    # theme_combobox.bind("<<ComboboxSelected>>", change_theme)


