import tkinter as tk

VERSION = "1.0.2"



root = tk.Tk()
root.title("Calculator 1.0.2")
root.geometry("400x500")

# экран
entry = tk.Entry(root, font=("Arial", 24), justify="right", bg="white", fg="black", bd=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0),
]

def calculate():
    try:
        result = eval(entry.get())  # вычисляем строку ("2+3*4")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")

def clear():
    entry.delete(0, tk.END)

def on_click(t):
    entry.insert(tk.END, t)

def on_enter(e):
        e.widget['background'] = '#45a049'

def on_leave(e):
        e.widget['background'] = '#4CAF50'
# создаём кнопки
for (text, row, col) in buttons:
    if text == "=":
    
    
        button = tk.Button(root, text=text, font=("Arial", 14),
                           bg="#4CAF50", fg="white",
                           width=5, height=2, command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 14),
                           bg="#F44336", fg="white",
                           width=5, height=2, command=clear)
    else:
        button = tk.Button(root, text=text, font=("Arial", 14),
                           bg="#e0e0e0", fg="white",
                           width=5, height=2, command=lambda t=text: on_click(t))

    button.grid(row=row, column=col, sticky="nsew")

# равномерное распределение строк и колонок
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()