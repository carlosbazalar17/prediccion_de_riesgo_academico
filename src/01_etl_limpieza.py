import pandas as pd
import os
from pathlib import Path
from pandas.api.types import is_numeric_dtype

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Rutas
ruta_dataset = BASE_DIR / "data" / "raw" / "dataset.csv"
ruta_processed = BASE_DIR / "data" / "processed"
ruta_salida = ruta_processed / "estudiantes_limpio.csv"

# Crear carpeta de salida
os.makedirs(ruta_processed, exist_ok=True)

# Verificar existencia del dataset
if not ruta_dataset.exists():
    raise FileNotFoundError(f"No se encontró el archivo: {ruta_dataset}")

# Cargar dataset
df = pd.read_csv(ruta_dataset)

print("Dimensiones iniciales:", df.shape)

print("\nColumnas originales:")
print(df.columns)

# Normalizar nombres de columnas
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.replace("/", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("'", "", regex=False)
)

print("\nColumnas normalizadas:")
print(df.columns)

# Eliminar duplicados
df = df.drop_duplicates()

# Tratamiento de valores nulos
for col in df.columns:
    if is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# Renombrar variable objetivo
if "target" in df.columns:
    df = df.rename(columns={"target": "estado_academico"})
else:
    raise ValueError("No se encontró la columna target en el dataset.")

# Crear variable binaria de riesgo académico
# 1 = Dropout
# 0 = Enrolled o Graduate
df["riesgo_academico"] = df["estado_academico"].apply(
    lambda x: 1 if str(x).lower().strip() == "dropout" else 0
)

# Guardar dataset limpio
df.to_csv(ruta_salida, index=False, encoding="utf-8")

print("\nETL finalizado correctamente.")
print("Archivo guardado en:", ruta_salida)
print("Dimensiones finales:", df.shape)

print("\nDistribución de estado académico:")
print(df["estado_academico"].value_counts())

print("\nDistribución de riesgo académico:")
print(df["riesgo_academico"].value_counts())

print("\nPrimeras filas:")
print(df.head())