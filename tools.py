import requests
from langchain_core.tools import tool

BASE_URL = "https://dragonball-api.com/api"


@tool
def get_dragonball_character(name: str) -> str:
    """Busca información detallada de un personaje de Dragon Ball por su nombre (ej: 'Goku', 'Vegeta', 'Piccolo').
    Retorna raza, género, ki, ki máximo, afiliación y descripción.
    """
    print(f"Llamando get_dragonball_character con name='{name}'")
    try:
        url = f"{BASE_URL}/characters?name={name}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data:
            return f"No se encontró ningún personaje con el nombre '{name}'."

        # Puede retornar una lista de personajes que coincidan
        char = data[0] if isinstance(data, list) else data
        return (
            f"Personaje: {char.get('name')}\n"
            f"- Raza: {char.get('race', 'Desconocida')}\n"
            f"- Género: {char.get('gender', 'Desconocido')}\n"
            f"- Ki base: {char.get('ki', 'N/A')}\n"
            f"- Ki máximo: {char.get('maxKi', 'N/A')}\n"
            f"- Afiliación: {char.get('affiliation', 'N/A')}\n"
            f"- Descripción: {char.get('description', 'Sin descripción')}"
        )
    except Exception as e:
        return f"Error al consultar el personaje '{name}': {e}"


@tool
def get_character_transformations(name: str) -> str:
    """Obtiene todas las transformaciones disponibles de un personaje de Dragon Ball (ej: 'Goku', 'Vegeta', 'Freezer')
    junto con el nivel de Ki asociado a cada una.
    """
    print(f"Llamando get_character_transformations con name='{name}'")
    try:
        # Primero buscamos el ID del personaje por su nombre
        search_url = f"{BASE_URL}/characters?name={name}"
        search_res = requests.get(search_url, timeout=10)
        search_res.raise_for_status()
        search_data = search_res.json()

        if not search_data:
            return f"No se encontró ningún personaje con el nombre '{name}' para ver sus transformaciones."

        char_summary = search_data[0] if isinstance(search_data, list) else search_data
        char_id = char_summary.get("id")

        # Consultamos el endpoint detallado por ID que contiene las transformaciones
        detail_url = f"{BASE_URL}/characters/{char_id}"
        detail_res = requests.get(detail_url, timeout=10)
        detail_res.raise_for_status()
        detail_data = detail_res.json()

        transformations = detail_data.get("transformations", [])
        if not transformations:
            return f"{detail_data.get('name', name)} no tiene transformaciones registradas en la base de datos."

        result = [f"Transformaciones de {detail_data.get('name', name)} ({len(transformations)} en total):"]
        for t in transformations:
            result.append(f"- {t.get('name')}: Ki = {t.get('ki', 'N/A')}")

        return "\n".join(result)
    except Exception as e:
        return f"Error al consultar las transformaciones de '{name}': {e}"


@tool
def get_dragonball_planet(name: str) -> str:
    """Busca información sobre un planeta del universo de Dragon Ball (ej: 'Tierra', 'Namek', 'Vegeta').
    Indica si está destruido, su descripción e historia.
    """
    print(f"Llamando get_dragonball_planet con name='{name}'")
    try:
        url = f"{BASE_URL}/planets?name={name}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data:
            return f"No se encontró información sobre el planeta '{name}'."

        planet = data[0] if isinstance(data, list) else data
        destruido = "Sí" if planet.get("isDestroyed") else "No"
        return (
            f"Planeta: {planet.get('name')}\n"
            f"- ¿Destruido?: {destruido}\n"
            f"- Descripción: {planet.get('description', 'Sin descripción')}"
        )
    except Exception as e:
        return f"Error al consultar el planeta '{name}': {e}"
