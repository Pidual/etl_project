def transform_languages(languages):
        """Aplica las transformaciones al dataset de lenguajes de programación"""
        transformed_languages = []
        for lang in languages:
            if "name" in lang:
                # Convertir nombre a camelCase
                words = lang["name"].split(" ")
                lang["nombre_formateado"] = words[0].lower() + "".join(word.capitalize() for word in words[1:])

                # Clasificación de popularidad
                popularity = float(lang["popularity"])
                if popularity < 30:
                    lang["popularidad_categoria"] = "Poco Usado"
                elif 30 <= popularity <= 70:
                    lang["popularidad_categoria"] = "Moderado"
                else:
                    lang["popularidad_categoria"] = "Muy Popular"

                # Clasificación de velocidad
                speed = float(lang["speed"])
                if speed < 40:
                    lang["velocidad_categoria"] = "Lento"
                elif 40 <= speed <= 70:
                    lang["velocidad_categoria"] = "Rápido"
                else:
                    lang["velocidad_categoria"] = "Muy Rápido"

                # Índice de eficiencia
                lang["eficiencia"] = (popularity + speed) / 2

                # Eliminar claves innecesarias
                del lang["name"]
                del lang["popularity"]
                del lang["speed"]
                transformed_languages.append(lang)
            else:
                print(f"Advertencia: la clave 'name' no se encuentra en los datos del lenguaje: {lang}")
                # Aquí puedes decidir si quieres hacer algo más, como añadir un valor por defecto o saltar este elemento.
        return transformed_languages