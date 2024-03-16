import tkinter as tk  # Import the tkinter module for GUI creation / Importa el módulo tkinter para la creación de la GUI
import math  # Import the math module for mathematical operations / Importa el módulo math para operaciones matemáticas

# Initialize the main window / Inicializa la ventana principal
root = tk.Tk()
root.title("Advanced Calculator")  # Set the title of the window / Establece el título de la ventana

# Create an entry widget for displaying input and output / Crea un widget de entrada para mostrar la entrada y salida
display = tk.Entry(root, width=20, font=("Arial", 14))
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)  # Place the display widget / Coloca el widget de visualización

# Define buttons for basic arithmetic operations / Define los botones para operaciones aritméticas básicas
buttons = [
    ('AC', 1, 0), ('+/-', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('Adv', 5, 3)
]

# Define buttons for advanced operations / Define los botones para operaciones avanzadas
advanced_buttons = [
    ('!', 6, 0), ('sqrt', 6, 1), ('^', 6, 2)
]

# Dictionary to keep track of advanced operation buttons / Diccionario para realizar un seguimiento de los botones de operaciones avanzadas
advanced_button_dict = {}

# Function to toggle visibility of advanced operation buttons / Función para alternar la visibilidad de los botones de operaciones avanzadas
def toggle_advanced_operations():
    global advanced_button_dict
    if not advanced_button_dict:
        for (text, row, col) in advanced_buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),
                               command=lambda text=text: button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            advanced_button_dict[text] = button
    else:
        for button in advanced_button_dict.values():
            button.grid_forget()
        advanced_button_dict = {}

# Function to handle button clicks / Función para manejar los clics de botones
def button_click(value):
    current_text = display.get()  # Get current text from display / Obtiene el texto actual de la visualización
    
    # Clear the display / Borra la pantalla
    if value == "AC":
        display.delete(0, tk.END)
        
    # Evaluate the expression in the display / Evalúa la expresión en la pantalla
    elif value == "=":
        try:
            if current_text:
                result = eval(current_text)
                display.delete(0, tk.END)  # Clear the display / Borra la pantalla
                display.insert(tk.END, result)  # Display the result / Muestra el resultado
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Division by zero")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            
    # Calculate factorial / Calcula el factorial
    elif value == "!":
        try:
            num = float(current_text)
            result = math.factorial(int(num))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ValueError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid input")
        except OverflowError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Result too large")
            
    # Calculate square root / Calcula la raíz cuadrada
    elif value == "sqrt":
        try:
            num = float(current_text)
            if num < 0:
                display.delete(0, tk.END)
                display.insert(tk.END, "Error: Invalid input")
            else:
                result = math.sqrt(num)
                display.delete(0, tk.END)
                display.insert(tk.END, result)
        except ValueError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid input")
            
    # Insert exponentiation operator / Inserta el operador de exponenciación
    elif value == "^":
        display.insert(tk.END, "**")
        
    # Toggle sign / Alterna el signo
    elif value == "+/-":
        if current_text.startswith("-"):
            current_text = current_text[1:]
        else:
            current_text = "-" + current_text
        display.delete(0, tk.END)
        display.insert(tk.END, current_text)
        
    # Toggle visibility of advanced operations / Alterna la visibilidad de las operaciones avanzadas
    elif value == "Adv":
        toggle_advanced_operations()
        
    # Handle digit input and operators / Maneja la entrada de dígitos y operadores
    else:
        if value.isdigit() or value == '.':
            display.insert(tk.END, value)
        else:
            if current_text and current_text[-1] in ['+', '-', '*', '/', '%', '^']:
                display.delete(len(current_text) - 1, tk.END)
            display.insert(tk.END, value)

# Function to handle keyboard events / Función para manejar eventos de teclado
def on_key(event):
    key = event.char
    if key.isdigit() or key in ['+', '-', '*', '/', '.', '%', '^']:
        button_click(key)
    elif key == '\x08':  # Backspace key / Tecla de retroceso
        current_text = display.get()
        if current_text:
            display.delete(len(current_text) - 1, tk.END)

# Create buttons and bind their click events / Crea botones y vincula sus eventos de clic
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),
                       command=lambda text=text: button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)

# Bind keyboard events to the window / Vincula eventos de teclado a la ventana
root.bind('<Key>', on_key)

# Start the GUI event loop / Inicia el bucle de eventos de la GUI
root.mainloop()
