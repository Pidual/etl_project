from datetime import datetime

def transform_languages(languages):
    """Aplica las transformaciones al dataset de lenguajes de programación."""
    transformed_data = []

    for lang in languages:
        transformed_lang = {}

        # ID
        transformed_lang["id"] = str(lang.get("id", ""))

        # Convertir nombre a camelCase
        words = lang["nombre_formateado"].split(" ")
        transformed_lang["nombre_formateado"] = words[0].lower() + "".join(word.capitalize() for word in words[1:])

        # Clasificación de popularidad
        popularity = float(lang.get("eficiencia", 0))  # Assuming eficiencia stores popularity
        if popularity < 30:
            transformed_lang["popularidad_categoria"] = "Poco Usado"
        elif 30 <= popularity <= 70:
            transformed_lang["popularidad_categoria"] = "Moderado"
        else:
            transformed_lang["popularidad_categoria"] = "Muy Popular"

        # Clasificación de velocidad
        speed = float(lang.get("eficiencia", 0))  # Assuming eficiencia stores speed
        if speed < 40:
            transformed_lang["velocidad_categoria"] = "Lento"
        elif 40 <= speed <= 70:
            transformed_lang["velocidad_categoria"] = "Rápido"
        else:
            transformed_lang["velocidad_categoria"] = "Muy Rápido"

        # Índice de eficiencia
        transformed_lang["eficiencia"] = (popularity + speed) / 2

        # Fecha de procesamiento
        transformed_lang["fecha_procesamiento"] = datetime.today().strftime('%Y-%m-%d')

        transformed_data.append(transformed_lang)

    return transformed_data
