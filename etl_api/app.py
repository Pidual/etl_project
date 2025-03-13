import psycopg2
from flask import Flask, jsonify
from extract import extract_languages
from transform import transform_languages

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return psycopg2.connect(
        dbname="etl_db",
        user="postgres",
        password="your_password",  # 🔴 Replace with the correct password
        host="postgres_db",  # ✅ Docker service name (must match docker-compose)
        port="5432"
    )

@app.route("/api/extract", methods=["GET"])
def extract_data():
    data = extract_languages()
    return jsonify(data)

@app.route("/api/transform", methods=["GET"])
def transform_data():
    raw_data = extract_languages()
    transformed_data = transform_languages(raw_data)
    return jsonify(transformed_data)

@app.route("/api/load", methods=["POST"])
def load_data():
    raw_data = extract_languages()
    transformed_data = transform_languages(raw_data)

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO etl_data (id, nombre_formateado, popularidad_categoria, velocidad_categoria, eficiencia, fecha_procesamiento)
    VALUES (%s, %s, %s, %s, %s, CURRENT_DATE)
    ON CONFLICT (id) DO NOTHING;
    """

    for lang in transformed_data:
        cur.execute(query, (
            lang["id"],  # Ensure your extracted data has an "id" field
            lang["nombre_formateado"],
            lang["popularidad_categoria"],
            lang["velocidad_categoria"],
            lang["eficiencia"]
        ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Data successfully loaded into PostgreSQL!"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
