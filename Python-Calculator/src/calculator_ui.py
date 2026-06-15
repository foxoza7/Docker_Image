# calculator_ui.py

"""
Este archivo contiene la interfaz gráfica de la calculadora.

Buena práctica:
La interfaz gráfica se mantiene separada de la lógica matemática.
Este archivo solo se encarga de ventanas, botones, colores y eventos.
"""

# Importamos tkinter para crear la interfaz gráfica
import tkinter as tk

# Importamos messagebox para mostrar errores en ventanas emergentes
from tkinter import messagebox

# Importamos la lógica matemática desde otro archivo
from calculator_logic import CalculatorLogic


class CalculatorApp:
    """
    Clase principal de la interfaz gráfica.

    Esta clase crea la ventana, la pantalla, los botones
    y conecta las acciones del usuario con la lógica matemática.
    """

    def __init__(self, root):
        """
        Constructor de la aplicación.

        Se ejecuta automáticamente cuando creamos CalculatorApp(root).
        """

        # Guardamos la ventana principal como atributo de la clase
        self.root = root

        # Creamos una instancia de la lógica matemática
        self.calculator_logic = CalculatorLogic()

        # Configuramos la ventana
        self.setup_window()

        # Creamos la pantalla donde se escriben los números
        self.create_display()

        # Creamos los botones
        self.create_buttons()

        # Creamos el texto inferior
        self.create_footer()

    def setup_window(self):
        """
        Configura las propiedades principales de la ventana.
        """

        self.root.title("Professional Python Calculator")
        self.root.geometry("380x560")
        self.root.resizable(False, False)
        self.root.config(bg="#1e1e2f")

    def create_display(self):
        """
        Crea la pantalla de entrada de la calculadora.
        """

        self.display = tk.Entry(
            self.root,
            font=("Arial", 24),
            bg="#2d2d44",
            fg="white",
            bd=0,
            justify="right",
            insertbackground="white"
        )

        self.display.pack(
            padx=20,
            pady=25,
            fill="x",
            ipady=15
        )

    def create_buttons(self):
        """
        Crea todos los botones de la calculadora usando una matriz.

        Buena práctica:
        Usar una lista de listas evita crear cada botón manualmente.
        """

        self.buttons_frame = tk.Frame(
            self.root,
            bg="#1e1e2f"
        )

        self.buttons_frame.pack()

        # Matriz que representa las filas y columnas de botones
        buttons = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["√", "0", ".", "="],
            ["(", ")", "^", ""]
        ]

        # Recorremos cada fila
        for row_index, row in enumerate(buttons):

            # Recorremos cada botón dentro de la fila
            for column_index, button_text in enumerate(row):

                # Si hay un espacio vacío, no creamos botón
                if button_text == "":
                    continue

                self.create_single_button(button_text, row_index, column_index)

    def create_single_button(self, text, row, column):
        """
        Crea un botón individual.

        Recibe:
            text: texto del botón.
            row: fila donde se ubicará.
            column: columna donde se ubicará.
        """

        # Color por defecto para números
        background_color = "#3a3a5c"
        text_color = "white"

        # Color especial para operadores
        if text in ["+", "-", "×", "÷", "=", "^"]:
            background_color = "#ff8c42"

        # Color especial para acciones
        if text in ["C", "⌫", "%", "√"]:
            background_color = "#5c6bc0"

        # Creamos el botón
        button = tk.Button(
            self.buttons_frame,
            text=text,
            font=("Arial", 18, "bold"),
            bg=background_color,
            fg=text_color,
            bd=0,
            width=5,
            height=2,
            activebackground="#7070a8",
            activeforeground="white",
            cursor="hand2",
            command=lambda: self.handle_button_click(text)
        )

        # Ubicamos el botón en la cuadrícula
        button.grid(
            row=row,
            column=column,
            padx=6,
            pady=6
        )

    def handle_button_click(self, text):
        """
        Decide qué acción ejecutar según el botón presionado.
        """

        if text == "C":
            self.clear_display()

        elif text == "⌫":
            self.delete_last_character()

        elif text == "=":
            self.calculate_result()

        elif text == "√":
            self.calculate_square_root()

        elif text == "%":
            self.calculate_percentage()

        else:
            self.add_text_to_display(text)

    def add_text_to_display(self, text):
        """
        Agrega texto al final de la pantalla.
        """

        self.display.insert(tk.END, text)

    def clear_display(self):
        """
        Limpia completamente la pantalla.
        """

        self.display.delete(0, tk.END)

    def delete_last_character(self):
        """
        Borra el último carácter escrito.
        """

        current_text = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current_text[:-1])

    def calculate_result(self):
        """
        Envía la expresión matemática a la lógica y muestra el resultado.
        """

        expression = self.display.get()
        result = self.calculator_logic.calculate_expression(expression)
        self.show_result(result)

    def calculate_square_root(self):
        """
        Calcula la raíz cuadrada del número actual.
        """

        value = self.display.get()
        result = self.calculator_logic.square_root(value)
        self.show_result(result)

    def calculate_percentage(self):
        """
        Calcula el porcentaje del número actual.
        """

        value = self.display.get()
        result = self.calculator_logic.percentage(value)
        self.show_result(result)

    def show_result(self, result):
        """
        Muestra el resultado en pantalla o una ventana de error.
        """

        if "Error" in result:
            messagebox.showerror("Error", result)
            return

        self.clear_display()
        self.display.insert(0, result)

    def create_footer(self):
        """
        Crea el texto inferior de la aplicación.
        """

        footer = tk.Label(
            self.root,
            text="Professional Calculator | Python + Tkinter 🧮",
            bg="#1e1e2f",
            fg="#b8b8d1",
            font=("Arial", 10)
        )

        footer.pack(pady=12)