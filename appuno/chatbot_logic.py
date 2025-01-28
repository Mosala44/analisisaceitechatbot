import nltk
from nltk.chat.util import Chat, reflections

from datetime import datetime

# Lista de preguntas del chatbot
preguntas = [
    "Número de camión:",
    "Motor (mt1 o mt2): ",
    "Número de muestra: ",
    "Tipo de pauta: Ingresa el tipo de inspección (por horas de operación).",
    "Horas componente: ",
    "Fecha análisis: (formato dd/mm/yyyy).",
    "Cambio de aceite: ¿Se realizó cambio de aceite? (Sí o No).",
    "Lubricante: ",
    "Horómetro: ",
    "Fecha de la muestra: Ingresa la fecha en que se tomó la muestra (formato dd/mm/yyyy).",
    "Componente:.",
    "Viscosidad: Ingresa el estado del aceite (NORMAL o ACCIÓN REQUERIDA).",
    "Agua %: (N o porcentaje encontrado)",
    "CFe: Ingresa ",
    "Fe (Hierro): ",
    "Cu (Cobre): ",
    "Pb (Plomo): ",
    "Al (Aluminio): ",
    "Sn (Estaño): ",
    "Cr (Cromo): ",
    "Ni (Níquel): ",
    "Si (Silicio): ",
    "Na (Sodio): "
]

# Lógica del chatbot para hacer preguntas
pregunta_actual = 0  # Índice para controlar la pregunta actual

def obtener_respuesta_usuario(input_usuario):
    global pregunta_actual

    # Verificar si hay más preguntas por hacer
    if pregunta_actual < len(preguntas):
        pregunta_actual += 1
        return preguntas[pregunta_actual - 1]  # Devolver la siguiente pregunta
    else:
        return "Gracias, he terminado de hacer todas las preguntas."

# Función para mostrar respuestas y preguntas en el chatbot
def iniciar_chatbot():
    print("¡Hola humano! Soy un chatbot para análisis de aceite.")
    print("Por favor, responde las siguientes preguntas:")
    
    # Empezamos con la primera pregunta
    respuesta = obtener_respuesta_usuario("")

    while respuesta != "Gracias, he terminado de hacer todas las preguntas.":
        print(respuesta)
        respuesta_usuario = input("Tu respuesta: ")

        # Continuar con la siguiente pregunta
        respuesta = obtener_respuesta_usuario(respuesta_usuario)

    print("\nGracias, he terminado de hacer todas las preguntas.")

# Iniciar el chatbot
if __name__ == "__main__":
    iniciar_chatbot()
