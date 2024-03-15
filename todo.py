import sys
import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

# Define el nombre del archivo para almacenar las tareas
TASKS_FILE = "tasks.txt"

# Carga las tareas almacenadas en el archivo
# Load the tasks stored in the file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Guarda las tareas en el archivo
# Saves the tasks to the file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task, due_date in tasks:
            file.write(f"{task}|{due_date}\n")

# Añade una nueva tarea con su fecha de vencimiento
# Add a new task with its due date
def add_task(task_entry, task_listbox):
    task = task_entry.get().strip()
    if task:
        due_date_str = tk.simpledialog.askstring("Agregar Tarea", "Ingrese la fecha de vencimiento (DD-MM-YYYY):")
        if due_date_str:
            try:
                due_date = datetime.datetime.strptime(due_date_str, "%d-%m-%Y").date()
                tasks.append((task, due_date))
                task_listbox.insert(tk.END, f"{len(tasks)}. {task} (Vence: {due_date.strftime('%d-%m-%Y')})")
                task_entry.delete(0, tk.END)
                messagebox.showinfo("Éxito", "Tarea agregada exitosamente.")
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha de vencimiento inválido. Por favor, use DD-MM-YYYY.")
    else:
        messagebox.showerror("Error", "La tarea no puede estar vacía. Por favor, ingrese una tarea válida.")

# Muestra todas las tareas existentes con sus fechas de vencimiento
# Displays all existing tasks with their due dates
def view_tasks(task_listbox):
    task_listbox.delete(0, tk.END)
    if not tasks:
        task_listbox.insert(tk.END, "No se encontraron tareas.")
    else:
        today = datetime.date.today()
        for index, (task, due_date) in enumerate(tasks, start=1):
            if due_date:
                days_left = (due_date - today).days
                if days_left == 0:
                    task_listbox.insert(tk.END, f"{index}. {task} (Vence hoy)")
                elif days_left < 0:
                    task_listbox.insert(tk.END, f"{index}. {task} (Tarde por {-days_left} días)")
                else:
                    task_listbox.insert(tk.END, f"{index}. {task} (Vence en {days_left} días)")
            else:
                task_listbox.insert(tk.END, f"{index}. {task}")

# Edita una tarea seleccionada
# Edits a selected task
def edit_task(task_entry, task_listbox):
    selected_index = task_listbox.curselection()
    if selected_index:
        task_number = int(selected_index[0])
        task_content, _ = tasks[task_number]
        new_task_content = task_entry.get()
        if new_task_content.strip() == "":
            new_task_content = task_content
        tasks[task_number] = (new_task_content, tasks[task_number][1])
        task_listbox.delete(task_number)
        task_listbox.insert(task_number, f"{task_number+1}. {new_task_content}")
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Tarea editada exitosamente.")
    else:
        messagebox.showerror("Error", "Por favor, seleccione una tarea para editar.")

# Añade una fecha de vencimiento a una tarea existente
# Adds a due date to an existing task
def add_due_date(task_listbox):
    selected_index = task_listbox.curselection()
    if selected_index:
        task_number = int(selected_index[0])
        due_date_str = tk.simpledialog.askstring("Agregar Fecha de Vencimiento", "Ingrese la fecha de vencimiento (YYYY-MM-DD):")
        if due_date_str:
            try:
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                tasks[task_number] = (tasks[task_number][0], due_date)
                task_listbox.delete(task_number)
                task_listbox.insert(task_number, f"{task_number+1}. {tasks[task_number][0]} (Vence: {due_date})")
                messagebox.showinfo("Éxito", "Fecha de vencimiento agregada exitosamente.")
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha de vencimiento inválido. Por favor, use YYYY-MM-DD.")
    else:
        messagebox.showerror("Error", "Por favor, seleccione una tarea para agregar una fecha de vencimiento.")

# Habilita o deshabilita el botón de edición según el contenido del cuadro de entrada de la tarea
# Enables or disables the edit button based on the content of the task entry box
def enable_disable_edit_button(event, task_entry, edit_button):
    if task_entry.get().strip() != "":
        edit_button.config(state=tk.NORMAL)
    else:
        edit_button.config(state=tk.DISABLED)

# Función principal del programa
# Main function of the program
def main():
    global tasks
    tasks = []
    for line in load_tasks():
        task_parts = line.split("|")
        if len(task_parts) == 2:
            task, due_date_str = task_parts
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            tasks.append((task, due_date))
        else:
            tasks.append((task_parts[0], None))

    root = tk.Tk()
    root.title("Lista de Tareas")

    task_label = tk.Label(root, text="Tarea:")
    task_label.grid(row=0, column=0, padx=5, pady=5)

    task_entry = tk.Entry(root)
    task_entry.grid(row=0, column=1, padx=5, pady=5)

    add_button = tk.Button(root, text="Agregar Tarea", command=lambda: add_task(task_entry, task_listbox))
    add_button.grid(row=0, column=2, padx=5, pady=5)

    view_button = tk.Button(root, text="Ver Tareas", command=lambda: view_tasks(task_listbox))
    view_button.grid(row=1, column=0, padx=5, pady=5)

    edit_button = tk.Button(root, text="Editar Tarea", command=lambda: edit_task(task_entry, task_listbox), state=tk.DISABLED)
    edit_button.grid(row=1, column=1, padx=5, pady=5)

    add_due_date_button = tk.Button(root, text="Agregar Fecha de Vencimiento", command=lambda: add_due_date(task_listbox))
    add_due_date_button.grid(row=1, column=2, padx=5, pady=5)

    task_listbox = tk.Listbox(root, width=50)
    task_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    task_entry.bind("<KeyRelease>", lambda event: enable_disable_edit_button(event, task_entry, edit_button))

    root.mainloop()

    # Guarda las tareas en el archivo al salir del programa
    # Save tasks to file when the program exits
    save_tasks()

if __name__ == "__main__":
    main()
