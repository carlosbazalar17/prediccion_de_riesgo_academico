import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Ruta del archivo de predicciones
ruta_predicciones = BASE_DIR / "data" / "outputs" / "predicciones.csv"

# Configuración de página
st.set_page_config(
    page_title="Dashboard de Riesgo Académico",
    layout="wide"
)

st.title("Dashboard de Predicción de Riesgo Académico")

# Verificar archivo
if not ruta_predicciones.exists():
    st.error("No se encontró el archivo predicciones.csv. Ejecuta primero src/04_prediccion.py")
    st.stop()

# Cargar datos
df = pd.read_csv(ruta_predicciones)

# ==========================
# Etiquetas interpretables
# ==========================

mapa_genero = {
    0: "Femenino",
    1: "Masculino"
}

mapa_becario = {
    0: "No becario",
    1: "Becario"
}

mapa_deudor = {
    0: "No deudor",
    1: "Deudor"
}

mapa_pago = {
    0: "No está al día",
    1: "Está al día"
}

mapa_estado = {
    "Dropout": "Abandono",
    "Graduate": "Graduado",
    "Enrolled": "Matriculado"
}

if "gender" in df.columns:
    df["genero"] = df["gender"].map(mapa_genero)

if "scholarship_holder" in df.columns:
    df["condicion_beca"] = df["scholarship_holder"].map(mapa_becario)

if "debtor" in df.columns:
    df["condicion_deuda"] = df["debtor"].map(mapa_deudor)

if "tuition_fees_up_to_date" in df.columns:
    df["estado_pago_matricula"] = df["tuition_fees_up_to_date"].map(mapa_pago)

if "estado_academico" in df.columns:
    df["estado_academico_label"] = df["estado_academico"].map(mapa_estado)
    
st.markdown(
    """
    Este dashboard permite analizar estudiantes con posible riesgo académico
    utilizando un modelo predictivo entrenado con datos académicos, socioeconómicos
    y administrativos.
    """
)

# ==========================
# Filtros
# ==========================

st.sidebar.header("Filtros")

if "genero" in df.columns:
    genero = st.sidebar.selectbox(
        "Género",
        ["Todos"] + sorted(df["genero"].dropna().unique().tolist())
    )
else:
    genero = "Todos"

if "condicion_beca" in df.columns:
    beca = st.sidebar.selectbox(
        "Condición de beca",
        ["Todos"] + sorted(df["condicion_beca"].dropna().unique().tolist())
    )
else:
    beca = "Todos"

if "nivel_riesgo" in df.columns:
    nivel = st.sidebar.selectbox(
        "Nivel de riesgo",
        ["Todos"] + sorted(df["nivel_riesgo"].dropna().unique().tolist())
    )
else:
    nivel = "Todos"

df_filtrado = df.copy()

if genero != "Todos":
    df_filtrado = df_filtrado[df_filtrado["genero"] == genero]

if beca != "Todos":
    df_filtrado = df_filtrado[df_filtrado["condicion_beca"] == beca]

if nivel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["nivel_riesgo"] == nivel]

# ==========================
# KPIs
# ==========================

total_estudiantes = len(df_filtrado)
estudiantes_riesgo = int(df_filtrado["prediccion_riesgo"].sum())
porcentaje_riesgo = (
    estudiantes_riesgo / total_estudiantes * 100
    if total_estudiantes > 0
    else 0
)

probabilidad_promedio = (
    df_filtrado["probabilidad_riesgo"].mean()
    if total_estudiantes > 0
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total estudiantes", total_estudiantes)
col2.metric("Estudiantes en riesgo", estudiantes_riesgo)
col3.metric("% riesgo", f"{porcentaje_riesgo:.2f}%")
col4.metric("Probabilidad promedio", f"{probabilidad_promedio:.2f}")

# ==========================
# Gráficos
# ==========================

st.subheader("Distribución de niveles de riesgo")

if total_estudiantes > 0:
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    df_filtrado["nivel_riesgo"].value_counts().plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Nivel de riesgo")
    ax1.set_ylabel("Cantidad de estudiantes")
    ax1.set_title("Distribución de niveles de riesgo")
    st.pyplot(fig1)
else:
    st.warning("No hay datos para mostrar con los filtros seleccionados.")

st.subheader("Estado académico real vs predicción")

if total_estudiantes > 0:
    tabla_estado = pd.crosstab(
        df_filtrado["estado_academico"],
        df_filtrado["prediccion_riesgo"]
    )

    st.dataframe(tabla_estado)

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    tabla_estado.plot(kind="bar", ax=ax2)
    ax2.set_xlabel("Estado académico real")
    ax2.set_ylabel("Cantidad")
    ax2.set_title("Estado académico real vs predicción")
    st.pyplot(fig2)

# ==========================
# Ranking
# ==========================

st.subheader("Ranking de estudiantes con mayor riesgo académico")

columnas_mostrar = [
    "estado_academico",
    "prediccion_riesgo",
    "probabilidad_riesgo",
    "nivel_riesgo",
    "age_at_enrollment",
    "admission_grade",
    "genero",
    "condicion_beca",
    "condicion_deuda",
    "estado_pago_matricula",
    "curricular_units_1st_sem_approved",
    "curricular_units_2nd_sem_approved",
    "curricular_units_1st_sem_grade",
    "curricular_units_2nd_sem_grade"
]

columnas_existentes = [
    col for col in columnas_mostrar
    if col in df_filtrado.columns
]

ranking = df_filtrado.sort_values(
    by="probabilidad_riesgo",
    ascending=False
)

st.dataframe(ranking[columnas_existentes].head(30))

# ==========================
# Descarga
# ==========================

st.subheader("Descargar resultados")

csv = df_filtrado.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Descargar predicciones filtradas",
    data=csv,
    file_name="predicciones_filtradas.csv",
    mime="text/csv"
)