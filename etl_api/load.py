import psycopg2
from datetime import date

def load_to_postgres(transformed_data):
    """ Inserts transformed data into PostgreSQL """
    conn = psycopg2.connect(
        dbname="etl_db",
        user="postgres",
        password="your_password",  # Change this to your actual password
        host="postgres_db",  # Use 'localhost' if running outside Docker
        port="5432"
    )
    cur = conn.cursor()

    for lang in transformed_data:
        cur.execute(
            """
            INSERT INTO etl_data (id, nombre_formateado, popularidad_categoria, 
                                  velocidad_categoria, eficiencia, fecha_procesamiento)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
            """,
            (lang["id"], lang["nombre_formateado"], lang["popularidad_categoria"], 
             lang["velocidad_categoria"], lang["eficiencia"], date.today())
        )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data successfully loaded into PostgreSQL!")
