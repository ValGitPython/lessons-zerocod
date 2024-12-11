import tkinter as tk

# Создаём главное окно
root = tk.Tk()
root.title("Ваше имя")
root.geometry("270x150")

# Создаём виджеты
label = tk.Label(root, text="Введите ваше имя:")
label.place(x=70, y=20)

entry = tk.Entry(root)
entry.place(x=70, y=50)

# Определяем функцию
def exit_button_click():
    root.destroy()

def button_click():
    name = entry.get()
    label.config(text=f"Привет, {name}!")
    button.config(text="Закрыть", command=exit_button_click)

# Создаём кнопку
button = tk.Button(root, text="Нажмите", command=button_click)
button.place(x=90, y=80)

root.mainloop()