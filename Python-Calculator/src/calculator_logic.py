# calculator_logic.py

"""
Este archivo contiene la lógica matemática de la calculadora.

Buena práctica:
La lógica de negocio debe estar separada de la interfaz gráfica.
Así el código es más fácil de leer, probar y mantener.
"""

# Importamos math para usar operaciones matemáticas como raíz cuadrada
import math


class CalculatorLogic:
    """
    Clase encargada únicamente de realizar cálculos.

    Buena práctica:
    Esta clase no sabe nada de botones, colores o ventanas.
    Solo recibe datos, calcula y devuelve resultados.
    """

    def calculate_expression(self, expression: str) -> str:
        """
        Calcula una expresión matemática completa.

        Ejemplo:
        "5 + 3 * 2" devuelve "11"

        Recibe:
            expression: operación escrita como texto.

        Devuelve:
            Resultado como texto.
        """

        try:
            # Reemplazamos símbolos visuales por símbolos que Python entiende
            expression = expression.replace("×", "*")
            expression = expression.replace("÷", "/")
            expression = expression.replace("^", "**")

            # Evaluamos la expresión matemática
            # Nota: eval se usa aquí porque es un proyecto académico/simple.
            # En proyectos reales se debe validar mejor por seguridad.
            result = eval(expression)

            # Convertimos el resultado a texto para mostrarlo en pantalla
            return str(result)

        except ZeroDivisionError:
            # Controlamos el caso especial de división entre cero
            return "Error: división entre cero"

        except Exception:
            # Controlamos cualquier operación inválida
            return "Error: operación inválida"

    def square_root(self, value: str) -> str:
        """
        Calcula la raíz cuadrada de un número.

        Recibe:
            value: número como texto.

        Devuelve:
            Resultado como texto.
        """

        try:
            # Convertimos el valor recibido a número decimal
            number = float(value)

            # No se permite raíz cuadrada de números negativos en este ejemplo
            if number < 0:
                return "Error: número negativo"

            # Calculamos la raíz cuadrada
            result = math.sqrt(number)

            return str(result)

        except Exception:
            # Si el usuario escribe algo inválido, devolvemos error
            return "Error: valor inválido"

    def percentage(self, value: str) -> str:
        """
        Convierte un número en porcentaje.

        Ejemplo:
        50 devuelve 0.5
        """

        try:
            # Convertimos el texto a número
            number = float(value)

            # Calculamos el porcentaje dividiendo entre 100
            result = number / 100

            return str(result)

        except Exception:
            return "Error: valor inválido"