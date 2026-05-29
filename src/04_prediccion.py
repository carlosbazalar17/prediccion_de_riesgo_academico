import pandas as pd
import joblib
import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Rutas
ruta_dataset = BASE_DIR / "data" / "processed" / "estudiantes_limpio.csv"
ruta_modelo = BASE_DIR / "models" / "modelo_dropout.pkl"
ruta_outputs = BASE_DIR / "data" / "outputs"
ruta_predicciones = ruta_outputs / "predicciones.csv"

# Crear carpeta de salida
os.makedirs(ruta_outputs, exist_ok=True)

# Verificar archivos necesarios
if not ruta_dataset.exists():
    raise FileNotFoundError(f"No se encontró el dataset limpio: {ruta_dataset}")

if not ruta_modelo.exists():
    raise FileNotFoundError(f"No se encontró el modelo entrenado: {ruta_modelo}")

# Cargar datos y modelo
df = pd.read_csv(ruta_dataset)
modelo = joblib.load(ruta_modelo)

print("=" * 60)
print("GENERACIÓN DE PREDICCIONES")
print("=" * 60)

print("\nDimensiones del dataset:")
print(df.shape)

# Separar variables predictoras
X = df.drop(columns=["estado_academico", "riesgo_academico"])

# Generar predicción y probabilidad
df["prediccion_riesgo"] = modelo.predict(X)
df["probabilidad_riesgo"] = modelo.predict_proba(X)[:, 1]

# Crear etiqueta interpretativa
df["nivel_riesgo"] = pd.cut(
    df["probabilidad_riesgo"],
    bins=[0, 0.4, 0.7, 1],
    labels=["Bajo", "Medio", "Alto"],
    include_lowest=True
)

# Ordenar de mayor a menor riesgo
df_ranking = df.sort_values(by="probabilidad_riesgo", ascending=False)

# Guardar archivo final
df_ranking.to_csv(ruta_predicciones, index=False, encoding="utf-8")

print("\nPredicciones generadas correctamente.")
print("Archivo guardado en:")
print(ruta_predicciones)

print("\nTop 15 estudiantes con mayor riesgo académico:")
print(
    df_ranking[
        [
            "estado_academico",
            "prediccion_riesgo",
            "probabilidad_riesgo",
            "nivel_riesgo",
            "age_at_enrollment",
            "admission_grade",
            "curricular_units_1st_sem_approved",
            "curricular_units_2nd_sem_approved"
        ]
    ].head(15)
)

print("\nDistribución de niveles de riesgo:")
print(df_ranking["nivel_riesgo"].value_counts())