import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Rutas
ruta_dataset = BASE_DIR / "data" / "processed" / "estudiantes_limpio.csv"
ruta_figuras = BASE_DIR / "reports" / "figuras"

# Crear carpeta para figuras
os.makedirs(ruta_figuras, exist_ok=True)

# Cargar dataset limpio
df = pd.read_csv(ruta_dataset)

print("=" * 60)
print("ANÁLISIS EXPLORATORIO DE DATOS")
print("=" * 60)

print("\nDimensiones del dataset:")
print(df.shape)

print("\nPrimeras filas:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nDistribución del estado académico:")
print(df["estado_academico"].value_counts())

print("\nDistribución del riesgo académico:")
print(df["riesgo_academico"].value_counts())

# ==========================
# Gráfico 1: Estado académico
# ==========================

plt.figure(figsize=(7, 4))
sns.countplot(data=df, x="estado_academico")
plt.title("Distribución del estado académico")
plt.xlabel("Estado académico")
plt.ylabel("Cantidad de estudiantes")
plt.tight_layout()
plt.savefig(ruta_figuras / "01_distribucion_estado_academico.png")
plt.close()

# ==========================
# Gráfico 2: Riesgo académico
# ==========================

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="riesgo_academico")
plt.title("Distribución de riesgo académico")
plt.xlabel("Riesgo académico")
plt.ylabel("Cantidad de estudiantes")
plt.tight_layout()
plt.savefig(ruta_figuras / "02_distribucion_riesgo_academico.png")
plt.close()

# ==========================
# Gráfico 3: Edad al matricularse
# ==========================

plt.figure(figsize=(7, 4))
sns.histplot(data=df, x="age_at_enrollment", bins=20, kde=True)
plt.title("Distribución de edad al momento de matrícula")
plt.xlabel("Edad al matricularse")
plt.ylabel("Cantidad de estudiantes")
plt.tight_layout()
plt.savefig(ruta_figuras / "03_distribucion_edad.png")
plt.close()

# ==========================
# Gráfico 4: Nota de admisión por estado académico
# ==========================

plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x="estado_academico", y="admission_grade")
plt.title("Nota de admisión según estado académico")
plt.xlabel("Estado académico")
plt.ylabel("Nota de admisión")
plt.tight_layout()
plt.savefig(ruta_figuras / "04_admission_grade_estado.png")
plt.close()

# ==========================
# Gráfico 5: Unidades aprobadas 1er semestre
# ==========================

plt.figure(figsize=(8, 4))
sns.boxplot(
    data=df,
    x="estado_academico",
    y="curricular_units_1st_sem_approved"
)
plt.title("Unidades aprobadas en el 1er semestre según estado académico")
plt.xlabel("Estado académico")
plt.ylabel("Unidades aprobadas 1er semestre")
plt.tight_layout()
plt.savefig(ruta_figuras / "05_unidades_aprobadas_1er_semestre.png")
plt.close()

# ==========================
# Gráfico 6: Unidades aprobadas 2do semestre
# ==========================

plt.figure(figsize=(8, 4))
sns.boxplot(
    data=df,
    x="estado_academico",
    y="curricular_units_2nd_sem_approved"
)
plt.title("Unidades aprobadas en el 2do semestre según estado académico")
plt.xlabel("Estado académico")
plt.ylabel("Unidades aprobadas 2do semestre")
plt.tight_layout()
plt.savefig(ruta_figuras / "06_unidades_aprobadas_2do_semestre.png")
plt.close()

# ==========================
# Gráfico 7: Matriz de correlación
# ==========================

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(14, 10))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False)
plt.title("Matriz de correlación de variables numéricas")
plt.tight_layout()
plt.savefig(ruta_figuras / "07_matriz_correlacion.png")
plt.close()

print("\nEDA finalizado correctamente.")
print("Figuras guardadas en:", ruta_figuras)