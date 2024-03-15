Propósito:
Este script es una aplicación simple de lista de tareas implementada en Python utilizando la biblioteca Tkinter. Permite a los usuarios agregar tareas con fechas de vencimiento, ver tareas, editar detalles de tareas y agregar fechas de vencimiento a las tareas.
Uso:
		Ejecute el script.
		Utilice el botón "Agregar tarea" para añadir una nueva tarea. Ingrese la descripción de la tarea y la fecha de vencimiento cuando se le solicite.
		Haga clic en el botón "Ver tareas" para mostrar una lista de todas las tareas. Las tareas se muestran con sus descripciones y fechas de vencimiento, si están disponibles.
		Para editar una tarea, selecciónela de la lista y haga clic en el botón "Editar tarea". Modifique la descripción de la tarea según sea necesario.
		Para agregar o cambiar la fecha de vencimiento de una tarea, selecciónela de la lista y haga clic en el botón "Agregar fecha de vencimiento". Ingrese la nueva fecha de vencimiento cuand
o se solicite.
		Cierre la aplicación cuando haya terminado. Las tareas se guardan automáticamente en un archivo llamado "tasks.txt" al salir.

Funcionalidades:
1. Añadir una nueva tarea con su fecha de vencimiento.
2. Ver todas las tareas existentes con sus fechas de vencimiento.
3. Editar una tarea seleccionada.
4. Añadir una fecha de vencimiento a una tarea existente.

Módulos utilizados:
- sys: Proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y funciones que interactúan fuertemente con el intérprete.
- datetime: Proporciona clases para manipular fechas y horas.
- tkinter: Biblioteca estándar de Python para crear interfaces gráficas de usuario.
- simpledialog: Proporciona una clase para crear cuadros de diálogo simples.
- messagebox: Proporciona una clase para crear cuadros de mensaje.

Variables globales:
- TASKS_FILE: Nombre del archivo utilizado para almacenar las tareas.

Funciones:
1. load_tasks(): Carga las tareas existentes desde el archivo.
2. save_tasks(): Guarda las tareas en el archivo.
3. add_task(task_entry, task_listbox): Añade una nueva tarea con su fecha de vencimiento.
4. view_tasks(task_listbox): Muestra todas las tareas existentes con sus fechas de vencimiento.
5. edit_task(task_entry, task_listbox): Edita una tarea seleccionada.
6. add_due_date(task_listbox): Añade una fecha de vencimiento a una tarea existente.
7. enable_disable_edit_button(event, task_entry, edit_button): Habilita o deshabilita el botón de edición según el contenido del cuadro de entrada de la tarea.

El programa principal crea una interfaz de usuario con botones y cuadros de entrada para realizar las operaciones mencionadas anteriormente. 
Al finalizar, guarda las tareas en el archivo cuando el programa sale.

Purpose:
This script is a simple to-do list application implemented in Python using the Tkinter library. It allows users to add tasks with due dates, view tasks, edit task details, and add due dates to tasks.
Usage:
Run the script.
Use the "Add Task" button to add a new task. Enter the task description and due date when prompted.
Click the "View Tasks" button to display a list of all tasks. Tasks are shown with their descriptions and due dates if available.
To edit a task, select it from the list and click the "Edit Task" button. Modify the task description as needed.
To add or change the due date of a task, select it from the list and click the "Add Due Date" button. Enter the new due date when prompted.
Close the application when finished. Tasks are automatically saved to a file named "tasks.txt" upon exit.
Features:
		Add a new task with its due date.
		View all existing tasks with their due dates.
		Edit a selected task.
		Add a due date to an existing task
.
Modules used:
	•	sys: Provides access to some variables used or maintained by the interpreter and functions that interact strongly with the interpreter.
	•	datetime: Provides classes for manipulating dates and times.
	•	tkinter: Python's standard library for creating graphical user interfaces.
	•	simpledialog: Provides a class for creating simple dialog boxes.
	•	messagebox: Provides a class for creating message boxes.
Global variables:
	•	TASKS_FILE: Name of the file used for storing tasks.
Functions:
		load_tasks(): Loads existing tasks from the file.
		save_tasks(): Saves tasks to the file.
		add_task(task_entry, task_listbox): Adds a new task with its due date.
		view_tasks(task_listbox): Displays all existing tasks with their due dates.
		edit_task(task_entry, task_listbox): Edits a selected task.
		add_due_date(task_listbox): Adds a due date to an existing task.
		enable_disable_edit_button(event, task_entry, edit_button): Enables or disables the edit button based on the content of the task entry box.
The main program creates a user interface with buttons and entry boxes to perform the aforementioned operations.
Upon completion, it saves the tasks to the file when the program exits.
