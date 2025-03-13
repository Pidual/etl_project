from neo4j import GraphDatabase
from datetime import datetime

#  Conexión a Neo4j SIN autenticación
NEO4J_URI = "bolt://neo4j_db:7687"

def connect_neo4j():
    """ Crea una conexión a Neo4j """
    return GraphDatabase.driver(NEO4J_URI)  # Sin usuario ni contraseña

def extract_languages():
    """ Extrae los datos de lenguajes de programación de Neo4j y los formatea """
    query = """
    MATCH (l:Lenguaje) 
    RETURN l.id AS id, l.nombre AS nombre, l.popularidad AS popularidad, 
           l.velocidad AS velocidad, l.paradigma AS paradigma, 
           l.año_creacion AS año_creacion,
           datetime() AS fecha_procesamiento
    """
    with connect_neo4j() as driver:
        with driver.session() as session:
            result = session.run(query)
            data = []
            for record in result:
                lang = record.data()
                # Categorizar popularidad y velocidad
                popularidad_categoria = "Muy Popular" if lang['popularidad'] > 80 else "Popular" if lang['popularidad'] > 50 else "Poco Popular"
                velocidad_categoria = "Rápido" if lang['velocidad'] > 70 else "Moderado" if lang['velocidad'] > 40 else "Lento"
                # Simulación de eficiencia (puedes ajustar esto según tus datos)
                eficiencia = lang['popularidad'] * 0.7 + lang['velocidad'] * 0.3
                # Formatear la fecha
                fecha_procesamiento = lang['fecha_procesamiento'].to_native().strftime('%Y-%m-%d')
                data.append({
                    "id": lang['id'],
                    "nombre_formateado": lang['nombre'],
                    "popularidad_categoria": popularidad_categoria,
                    "velocidad_categoria": velocidad_categoria,
                    "eficiencia": eficiencia,
                    "fecha_procesamiento": fecha_procesamiento
                })
            return data