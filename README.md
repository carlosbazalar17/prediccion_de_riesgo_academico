# Predicción de Riesgo Académico

## 1. Descripción del proyecto
Este proyecto desarrolla un sistema de predicción de riesgo académico estudiantil utilizando técnicas de análisis de datos y machine learning. A partir de información académica, socioeconómica y administrativa de estudiantes, el modelo identifica posibles casos de abandono o bajo rendimiento, permitiendo priorizar acciones de seguimiento y apoyo académico.

## 2. Objetivo del proyecto
El objetivo principal es construir un modelo predictivo capaz de clasificar a los estudiantes según su nivel de riesgo académico. Para ello, se realiza un flujo completo de trabajo que incluye limpieza de datos, análisis exploratorio, entrenamiento del modelo, generación de predicciones y visualización de resultados mediante un dashboard interactivo.

## 3. Dataset utilizado
Se utiliza el dataset Predict Students Dropout and Academic Success, disponible en Kaggle. Este conjunto de datos contiene información de estudiantes universitarios, incluyendo variables como estado civil, modalidad de postulación, curso, calificaciones previas, situación económica, beca, deuda, edad de ingreso, unidades curriculares aprobadas, notas semestrales e indicadores macroeconómicos.

La variable objetivo original es target, la cual clasifica a los estudiantes en tres categorías:

Dropout: estudiante que abandonó.
Enrolled: estudiante matriculado.
Graduate: estudiante graduado.

Para este proyecto, se transforma en una variable binaria llamada riesgo_academico:

1: estudiante en riesgo académico.
0: estudiante sin riesgo académico crítico.

## 4. Estructura del proyecto
prediccion-riesgo-academico/ 
│
├── data/ 
│ ├── raw/ 
│ │ └── dataset.csv 
│ ├── processed/ 
│ │ └── estudiantes_limpio.csv 
│ └── outputs/ 
│ └── predicciones.csv 
│ ├── src/ 
│ ├── 01_etl_limpieza.py 
│ ├── 02_eda.py 
│ ├── 03_entrenamiento.py 
│ └── 04_prediccion.py 
│ ├── dashboard/ 
│ └── app_streamlit.py 
│ ├── models/ 
│ └── modelo_dropout.pkl 
│ ├── reports/ 
│ ├── figuras/ 
│ └── metricas_modelo.txt 
│ ├── requirements.txt 
├── README.md 
└── .gitignore

## 5. Flujo general del proceso
El proyecto sigue un flujo completo de ciencia de datos, desde la carga y limpieza del dataset hasta la visualización final de los resultados. El proceso está dividido en etapas para facilitar el mantenimiento y la comprensión.

### 5.1 Limpieza y preparación de datos

En esta etapa se carga el dataset original, se normalizan los nombres de las columnas, se eliminan duplicados y se tratan posibles valores nulos. Además, se transforma la variable objetivo target en una variable binaria llamada riesgo_academico, donde los estudiantes con estado Dropout son clasificados como estudiantes en riesgo.

También se generan archivos limpios dentro de la carpeta data/processed/, los cuales serán utilizados en las siguientes fases del proyecto.

### 5.2 Análisis exploratorio de datos
En el análisis exploratorio se revisan las dimensiones del dataset, los tipos de variables, la distribución de la variable objetivo y el comportamiento de las principales variables académicas. Se generan gráficos para analizar patrones relacionados con el abandono estudiantil, como edad de ingreso, nota de admisión, unidades curriculares aprobadas y distribución del riesgo académico.

Las visualizaciones se guardan en la carpeta reports/figuras/ para ser utilizadas posteriormente en el análisis, documentación o presentación del proyecto.

### 5.3 Entrenamiento del modelo
En esta etapa se entrena un modelo de clasificación utilizando machine learning. El dataset se divide en datos de entrenamiento y prueba, y se utiliza un modelo Random Forest para predecir si un estudiante presenta riesgo académico.

El modelo se evalúa mediante métricas como:

Accuracy
Precision
Recall
F1-score
ROC-AUC

Finalmente, el modelo entrenado se guarda en la carpeta models/ con el nombre modelo_dropout.pkl.

### 5.4 Generación de predicciones
Después del entrenamiento, se utiliza el modelo guardado para generar predicciones sobre los estudiantes del dataset. El sistema calcula la probabilidad de riesgo académico y asigna un nivel de riesgo, como bajo, medio o alto.

El resultado final se guarda en:

data/outputs/predicciones.csv

Este archivo contiene las predicciones, probabilidades y etiquetas interpretables que serán utilizadas en el dashboard.

### 5.5 Aplicación en Streamlit
Se desarrolla un dashboard interactivo con Streamlit para visualizar los resultados del modelo. La aplicación permite revisar indicadores principales, filtrar estudiantes por variables como género, condición de beca o nivel de riesgo, y consultar un ranking de estudiantes con mayor probabilidad de riesgo académico.

El dashboard facilita la interpretación de los resultados para usuarios no técnicos, permitiendo convertir las predicciones del modelo en información útil para la toma de decisiones.

## 6. Resultados generales

## 7. Tecnologías utilizadas
El proyecto utiliza las siguientes tecnologías y librerías:

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Streamlit
Git y GitHub

## 8. Instalación y ejecución
1. Clonar el repositorio

    git clone https://github.com/carlosbazalar17/prediccion_de_riesgo_academico.git

    cd prediccion-riesgo-academico

2. Crear entorno virtual

    python -m venv venv
   
4. Activar entorno virtual

En Windows:

    venv\Scripts\activate

En Linux o Mac:

    source venv/bin/activate
4. Instalar dependencias
    pip install -r requirements.txt
5. Colocar el dataset

Descargar el dataset desde Kaggle y colocarlo en la siguiente ruta:

    data/raw/dataset.csv
6. Ejecutar limpieza de datos
   
    python src/01_etl_limpieza.py
8. Ejecutar análisis exploratorio
   
    python src/02_eda.py
9. Entrenar el modelo
   
    python src/03_entrenamiento.py
10. Generar predicciones
    
    python src/04_prediccion.py
11. Ejecutar dashboard
    
    streamlit run dashboard/app_streamlit.py


## 9. Conclusiones generales
