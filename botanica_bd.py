import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv('PASSWORD')

# Conexión a PostgreSQL
conn = psycopg2.connect(
    dbname="biologia_botanica",
    user="postgres",
    password=password,  # Se obtiene de .env
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Lista de palabras clave
palabras = [
    ("fotosíntesis", 98.5, "producción de energía, clorofila, luz solar"),
    ("célula vegetal", 97.0, "citoplasma, núcleo, pared celular"),
    ("clorofila", 96.2, "pigmento verde, fotosistema, energía solar"),
    ("flor", 94.7, "pétalos, reproducción, planta"),
    ("semilla", 93.5, "germinación, embrión, fruto"),
    ("raíz", 92.8, "absorción, anclaje, rizoma"),
    ("tallo", 91.6, "soporte, xilema, floema"),
    ("hoja", 90.9, "estoma, cloroplasto, fotosíntesis"),
    ("polinización", 89.8, "abeja, reproducción, floración"),
    ("germinación", 88.6, "crecimiento, semilla, humedad"),
    ("planta", 87.4, "organismo vegetal, flora"),
    ("ecosistema", 86.2, "hábitat, biodiversidad, bioma"),
    ("botánica", 85.0, "biología vegetal, taxonomía"),
    ("floración", 84.3, "estación, primavera, reproducción"),
    ("xilema", 83.0, "transporte, savia, conducción")
]

# Inserción de datos
cur.executemany("""
    INSERT INTO palabras_clave (palabra, porcentaje_identidad, sinonimos)
    VALUES (%s, %s, %s);
""", palabras)

conn.commit()
print(" Datos insertados correctamente.")

# Verificación
cur.execute("SELECT * FROM palabras_clave;")
for fila in cur.fetchall():
    print(fila)

cur.close()
conn.close()
