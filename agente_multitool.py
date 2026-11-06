import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

from tools import (
    get_dragonball_character,
    get_character_transformations,
    get_dragonball_planet,
)

# Cargar variables de entorno desde .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Herramientas del agente
tools = [
    get_dragonball_character,
    get_character_transformations,
    get_dragonball_planet,
]

# Inicializamos el modelo en Groq (ultrarrápido y con soporte nativo de Tool Calling)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0,
)

# Creamos el agente ReAct multitool con LangGraph
agent = create_react_agent(llm, tools)


def preguntar(mensaje: str):
    """Envía un mensaje al agente y muestra la respuesta."""
    print(f"\n==========================================")
    print(f"Usuario: {mensaje}")
    print(f"==========================================")
    resultado = agent.invoke({"messages": [{"role": "user", "content": mensaje}]})
    respuesta_final = resultado["messages"][-1].content
    print(f"Agente: {respuesta_final}\n")
    return respuesta_final


if __name__ == "__main__":
    print("Iniciando Agente Multitool de Dragon Ball (Groq LLM)...")
    print("Herramientas disponibles:")
    for t in tools:
        print(f" - {t.name}: {t.description.strip().splitlines()[0]}")

    if len(sys.argv) > 1:
        consulta = " ".join(sys.argv[1:])
        preguntar(consulta)
    else:
        print("\nEscribe tu pregunta sobre Dragon Ball (o 'salir' para terminar):")
        while True:
            try:
                usuario_input = input("Tú > ").strip()
                if not usuario_input:
                    continue
                if usuario_input.lower() in ["salir", "exit", "quit"]:
                    print("¡Hasta luego!")
                    break
                preguntar(usuario_input)
            except KeyboardInterrupt:
                print("\nSaliendo...")
                break
