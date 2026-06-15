import os
import tkinter as tk
from calculator_ui import CalculatorApp

def calculadora_consola():
    """
    Toda la lógica de tu calculadora en modo texto (CLI).
    Esta función se encarga de pedir datos y mostrar resultados.
    """
    print("\n--- CALCULADORA MODO TEXTO ---")
    try:
        num1 = float(input("Escribe el primer número: "))
        op = input("Escribe la operación (+, -, *, /): ")
        num2 = float(input("Escribe el segundo número: "))
        
        if op == '+': res = num1 + num2
        elif op == '-': res = num1 - num2
        elif op == '*': res = num1 * num2
        elif op == '/': res = num1 / num2 if num2 != 0 else "Error: División por 0"
        else: res = "Operación no válida"
        
        print(f"Resultado: {res}\n")
    except ValueError:
        print("Error: Por favor, ingresa solo números válidos.")

def main():
    """
    Esta es tu función 'Traffic Cop'.
    Decide qué camino tomar basándose en el entorno.
    """
    # Verificamos si estamos en un entorno con pantalla
    if os.environ.get('DISPLAY') is None:
        # Estamos en Docker (o un servidor)
        calculadora_consola()
    else:
        # Estamos en Windows/Escritorio
        root = tk.Tk()
        CalculatorApp(root)
        root.mainloop()

if __name__ == "__main__":
    main()