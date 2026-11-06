# 🐉 Agente Multitool - Dragon Ball API

Agente inteligente autónomo desarrollado con **LangGraph** y **LangChain**, integrado con **Groq** (`llama-3.3-70b-versatile`) para realizar consultas especializadas y en tiempo real a la [Dragon Ball API](https://dragonball-api.com).

El agente utiliza un patrón **ReAct** (Reasoning + Acting) para interpretar las preguntas del usuario, elegir de forma dinámica las herramientas adecuadas y sintetizar la información solicitada.

---

## 🛠️ Herramientas Integradas (Tools)

Ubicadas en [`tools.py`](tools.py):

1. **`get_dragonball_character(name: str)`**: Consulta información detallada de cualquier personaje (raza, género, ki base, ki máximo, afiliación y descripción biográfica).
2. **`get_character_transformations(name: str)`**: Recupera todas las transformaciones de un personaje y su nivel de Ki específico.
3. **`get_dragonball_planet(name: str)`**: Consulta datos de planetas del universo Dragon Ball (descripción, estado de destrucción y habitantes notables).

---

## 📁 Estructura del Proyecto

```text
Agente-Multitool/
├── agente_multitool.py    # Ciclo de ejecución del agente ReAct (LangGraph + Groq)
├── tools.py               # Definición de herramientas con decorador @tool de LangChain
├── requirements.txt       # Librerías necesarias (langchain, langgraph, langchain-groq, etc.)
├── .env                   # Variables de entorno locales (API keys - no versionado)
├── .gitignore             # Filtros para seguridad y entornos virtuales
└── README.md              # Documentación técnica del módulo
```

---

## ⚙️ Configuración y Requisitos

1. **Python**: Versión 3.10 o superior.
2. **Groq API Key**: Obtén una clave gratuita en [console.groq.com](https://console.groq.com).

---

## 📦 Instalación

1. Clona el repositorio y navega a la carpeta:
   ```bash
   git clone https://github.com/Mariogarluu/Agente_multitool.git
   cd Agente_multitool
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu archivo `.env` en la raíz del proyecto:
   ```env
   GROQ_API_KEY=tu_api_key_de_groq_aqui
   ```

---

## 🚀 Ejecución del Agente

Inicia el agente interactivo por consola:

```bash
python agente_multitool.py
```

### Ejemplos de consultas compatibles:
- *"¿Cuál es el Ki máximo de Goku y qué transformaciones tiene?"*
- *"Dime detalles sobre el planeta Vegeta y si está destruido."*
- *"Compara las razas y poderes entre Piccolo y Vegeta."*
