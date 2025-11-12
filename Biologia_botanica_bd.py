import sqlite3

# ---------------------------------------------
# Conexión a la base de datos SQLite
# ---------------------------------------------
conn = sqlite3.connect("botanica.db")
cur = conn.cursor()

# ---------------------------------------------
# Crear tabla (si no existe)
# ---------------------------------------------
cur.execute("""
CREATE TABLE IF NOT EXISTS palabras_clave (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT UNIQUE,
    porcentaje_identidad REAL,
    sinonimos TEXT
);
""")

# ---------------------------------------------
# Lista ampliada de palabras clave de Biología y Botánica
# ---------------------------------------------
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
    ("xilema", 83.0, "transporte, savia, conducción"),
    ("floema", 82.7, "nutrientes, azúcares, transporte"),
    ("antera", 81.5, "polen, estambre, flor"),
    ("estambre", 81.0, "polen, flor, reproducción masculina"),
    ("pistilo", 80.6, "óvulo, estigma, ovario"),
    ("polen", 80.1, "grano, fertilización, flor"),
    ("óvulo", 79.8, "ovario, gameto, reproducción"),
    ("mitosis", 79.2, "división celular, cromosomas, células hijas"),
    ("meiosis", 78.9, "reproducción sexual, gametos, cromosomas"),
    ("citoplasma", 78.0, "orgánulos, célula, membrana"),
    ("ADN", 77.6, "ácido desoxirribonucleico, genética, cromosomas"),
    ("ARN", 77.1, "ácido ribonucleico, síntesis de proteínas, transcripción"),
    ("genética", 76.8, "herencia, genes, ADN"),
    ("mutación", 75.9, "variación, ADN, evolución"),
    ("evolución", 75.2, "selección natural, adaptación, especies"),
    ("reino vegetal", 74.8, "plantas, flora, fotosíntesis"),
    ("taxonomía", 74.0, "clasificación, especies, biología"),
    ("bioma", 73.4, "ecosistema, clima, vegetación"),
    ("biodiversidad", 73.1, "variedad, especies, ecosistema"),
    ("simbiogénesis", 72.6, "evolución, endosimbiosis, mitocondria"),
    ("endosimbiosis", 72.2, "mitocondria, cloroplasto, célula eucariota"),
    ("autótrofos", 71.8, "fotosíntesis, energía solar, carbono"),
    ("heterótrofos", 71.4, "nutrición, organismos, energía"),
    ("micorriza", 70.9, "hongo, raíz, simbiosis"),
    ("hongos", 70.5, "micelio, esporas, descomposición"),
    ("algas", 70.1, "acuáticas, clorofila, fotosíntesis"),
    ("morfología vegetal", 69.7, "estructura, órganos, planta"),
    ("fisiología vegetal", 69.3, "procesos vitales, metabolismo, hormonas"),
    ("transpiración", 69.0, "agua, hojas, evaporación"),
    ("estoma", 68.6, "intercambio gaseoso, hoja, cloroplasto"),
    ("cloroplasto", 68.3, "orgánulo, fotosíntesis, energía solar"),
    ("savias", 68.0, "nutrientes, transporte, floema"),
    ("adaptación", 67.5, "supervivencia, evolución, entorno"),
    ("descomposición", 67.0, "nutrientes, reciclaje, hongos"),
    ("reproducción vegetal", 66.5, "sexual, asexual, flores"),
    ("reproducción asexual", 66.0, "brotación, estolones, esquejes"),
    ("reproducción sexual", 65.5, "polinización, fecundación, semillas")
]

# ---------------------------------------------
# Insertar datos (sin duplicar)
# ---------------------------------------------
cur.executemany("""
INSERT OR IGNORE INTO palabras_clave (palabra, porcentaje_identidad, sinonimos)
VALUES (?, ?, ?)
""", palabras)

conn.commit()
print("✅ Base de datos actualizada con nuevas palabras clave.")

# ---------------------------------------------
# Mostrar resultados
# ---------------------------------------------
cur.execute("SELECT * FROM palabras_clave ORDER BY id ASC;")
for fila in cur.fetchall():
    print(fila)

# ---------------------------------------------
# Cerrar conexión
# ---------------------------------------------
cur.close()
conn.close()
