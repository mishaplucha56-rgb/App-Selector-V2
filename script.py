import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


bg_path = resource_path("bg.png")

def open_github():
    webbrowser.open_new("https://github.com")

def open_browser():
    webbrowser.open_new("http://google.com")

def open_gemini():
    webbrowser.open_new("https://gemini.google.com")

root = tk.Tk()

root.geometry("600x600")
root.title("My App")

root.resizable(False, False)

script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, "bg.png")

# 2. Безопасная загрузка через Pillow под размер окна 600x600
pil_image = Image.open(bg_path)
pil_image = pil_image.resize((600, 600))
bg_photo = ImageTk.PhotoImage(pil_image)

# 3. Фон приложения
bg = tk.Label(root, image=bg_photo)
bg.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(root, text="App Selector", font=("Arial", 30, "bold"), bg="Black", fg="Green")
label.pack()

btn = tk.Button(
    root,
    text='Open Terminal',
    command = lambda: os.system("start cmd"),
    bg = "#1E1E1E",
    fg = "green",
    font = ("Segoe UI", 25, "bold"),
    wraplength=180,
    justify="center")


btn.place(x = 50, y = 70, width = 150, height = 100)


btn1 = tk.Button(
    root,
    text="Open Google",
    command=open_browser,
    bg="#001c8c",
    fg="yellow",
    font=("Arial", 25, "bold"),
    wraplength=180,
    justify="center"
)

btn1.place(x = 395, y = 70, width = 150, height = 100)

btn2 = tk.Button(
    root,
    text="Open Discord",
    command= lambda: os.system("start Discord:"),
    bg="#25108f",
    fg="#ffffff",
    font=("Arial", 25, "bold"),
    wraplength=180,
    justify="center"
)

btn2.place(x = 395, y = 200, width = 150, height = 100)

btn3 = tk.Button(
    root,
    text='Open Gemini',
    command = lambda: open_gemini(),
    bg = "#000000",
    fg = "#1f134f",
    font = ("Segoe UI", 25, "bold"),
    wraplength=180,
    justify="center")


btn3.place(x = 50, y = 200, width = 150, height = 100)

btn3 = tk.Button(
    root,
    text='Open Steam',
    command=lambda: os.system("start steam:"),
    bg = "#0c145c",
    fg = "white",
    font = ("Segoe UI", 25, "bold"),
    wraplength=180,
    justify="center")


btn3.place(x = 50, y = 330, width = 150, height = 100)

btn4 = tk.Button(
    root,
    text="Open Github",
    command= lambda: open_github(),
    bg="#000000",
    fg="#232324",
    font=("Arial", 25, "bold"),
    wraplength=180,
    justify="center"
)

btn4.place(x = 395, y = 330, width = 150, height = 100)

btn_auto =   tk.Button(
    root,
    text = "Start Up?",
    command = lambda: os.system(f'copy "{sys.executable}" "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"'),
    bg = "#000000",
    fg = "green",
    font = ("Segoe UI", 25, "bold"),
)

btn_auto.place(x=225, y=500, width=150, height=40)

root.mainloop()

