import tkinter as tk

# Функции
def add_task():
    task = task_entry.get()
    if task:
        frame.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = frame.curselection()
    if selected_task:
        frame.delete(selected_task)

def notice_task():
    selected_task = frame.curselection()
    if selected_task:
        frame.itemconfig(selected_task, {'bg': "dark green", 'fg': "GhostWhite"})

# Основное окно
root = tk.Tk()
root.title("Daily Planner")
root.geometry("383x620+100+50")
root.resizable(False, False)

# Заголовок
task_label = tk.Label(root, text="СПИСОК ЗАДАЧ:", font=("Arial", 12, "italic"))
task_label.grid(row=0, column=0, columnspan=3, sticky="n")

# Список для выбора элементов
frame = tk.Listbox(root, bg="white", width=60, height=30)
frame.grid(row=2, column=0, columnspan=3, sticky="n", ipadx=6, ipady=2, padx=4, pady=4)

# Поле ввода текста
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=3, column=0, columnspan=3, sticky="nsew", ipadx=6, ipady=2, padx=4, pady=4)

# Кнопки
add_task_button = tk.Button(root, text="+ добавить", command=add_task, font=("Arial", 12), fg="DarkBlue")
add_task_button.grid(row=4, column=0, ipadx=6, ipady=6, padx=4, pady=4)

ok_button = tk.Button(root, text="выполнено", command=notice_task, font=("Arial", 12), fg="dark green")
ok_button.grid(row=4, column=1, ipadx=6, ipady=6, padx=4, pady=4)

del_task_button = tk.Button(root, text="удалить", command=delete_task, font=("Arial", 12), fg="dark red")
del_task_button.grid(row=4, column=2, ipadx=6, ipady=6, padx=4, pady=4)

# Запуск главного цикла
root.mainloop()
