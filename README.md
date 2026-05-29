# Predicción de Riesgo Académico

## 1. Descripción del proyecto

## 2. Objetivo del proyecto

## 3. Dataset utilizado

## 4. Estructura del proyecto

## 5. Flujo general del proceso

### 5.1 Limpieza y preparación de datos

El primer módulo del proyecto corresponde al proceso de **ETL y limpieza de datos**, implementado en el archivo `01_etl_limpieza.py`. Su finalidad es cargar el dataset original, preparar la información para las siguientes etapas del análisis y generar un archivo limpio que será utilizado posteriormente en el análisis exploratorio, entrenamiento del modelo y generación de predicciones.

El proceso inicia definiendo las rutas principales del proyecto mediante `Path`, lo que permite ubicar correctamente el archivo original `dataset.csv` dentro de la carpeta `data/raw/`. Asimismo, se establece como salida la carpeta `data/processed/`, donde se almacenará el archivo procesado `estudiantes_limpio.csv`.

Antes de cargar los datos, el módulo verifica que el archivo original exista. En caso contrario, se detiene la ejecución y muestra un error indicando que no se encontró el dataset. Esta validación evita errores posteriores durante el procesamiento.

Luego, el dataset es cargado con la librería `pandas`, mostrando inicialmente sus dimensiones y columnas originales. Posteriormente, se realiza una normalización de los nombres de las columnas, convirtiéndolos a minúsculas, eliminando espacios, reemplazando caracteres especiales y estandarizando su formato. Esto facilita el manejo de las variables dentro del código y evita problemas al referenciar columnas.

Después de normalizar las columnas, se eliminan registros duplicados para evitar que datos repetidos afecten el análisis o el entrenamiento del modelo. También se realiza el tratamiento de valores nulos: en las columnas numéricas, los valores faltantes son reemplazados por la mediana; mientras que en las columnas categóricas se utiliza la moda. Esta estrategia permite conservar los registros sin eliminar filas completas del dataset.

Una parte importante del proceso consiste en renombrar la variable objetivo `target` como `estado_academico`, con el fin de darle un nombre más descriptivo dentro del contexto del proyecto. A partir de esta variable, se crea una nueva columna llamada `riesgo_academico`, la cual transforma el problema en una clasificación binaria. En esta nueva variable, el valor `1` representa a los estudiantes en condición de abandono académico (`Dropout`), mientras que el valor `0` agrupa a los estudiantes que continúan matriculados (`Enrolled`) o que lograron graduarse (`Graduate`).

Finalmente, el dataset limpio es guardado en la ruta `data/processed/estudiantes_limpio.csv`. El módulo también imprime información de control, como las dimensiones finales del dataset, la distribución de la variable `estado_academico`, la distribución de la variable `riesgo_academico` y una vista preliminar de las primeras filas del archivo procesado.

### 5.2 Análisis exploratorio de datos

El segundo módulo del proyecto corresponde al **Análisis Exploratorio de Datos**, implementado en el archivo `02_eda.py`. Esta etapa tiene como finalidad revisar el comportamiento general del dataset limpio, obtener información descriptiva de las variables y generar gráficos que permitan comprender mejor la distribución de los estudiantes y su relación con el riesgo académico.

El módulo trabaja con el archivo `estudiantes_limpio.csv`, generado previamente durante la fase de limpieza y almacenado en la carpeta `data/processed/`. Además, se define una carpeta de salida en `reports/figuras/`, donde se guardan automáticamente todas las visualizaciones generadas durante el análisis.

Al iniciar el proceso, el script carga el dataset limpio mediante `pandas` y muestra información general del conjunto de datos, como sus dimensiones, primeras filas, estructura de columnas, tipos de datos, estadísticas descriptivas y cantidad de valores nulos por columna. Esta revisión permite comprobar que el archivo procesado se encuentra correctamente preparado para las etapas posteriores del proyecto.

También se analiza la distribución de las variables principales: `estado_academico` y `riesgo_academico`. La primera permite observar la cantidad de estudiantes según su situación académica, mientras que la segunda resume el problema en términos de riesgo, diferenciando entre estudiantes con posible abandono académico y estudiantes sin riesgo directo.

Como parte del análisis exploratorio, se generan siete gráficos principales. Estos gráficos permiten visualizar la distribución del estado académico, la distribución del riesgo académico, la edad de los estudiantes al momento de la matrícula, la nota de admisión según el estado académico, las unidades curriculares aprobadas en el primer y segundo semestre, y la matriz de correlación entre variables numéricas.

Los gráficos generados son almacenados automáticamente en la carpeta `reports/figuras/` con nombres ordenados del `01` al `07`, lo que facilita su posterior revisión y documentación. En este README general solo se describe el proceso de generación de las visualizaciones, mientras que la interpretación detallada de cada gráfico será desarrollada en un reporte específico.

Finalmente, este módulo permite obtener una visión inicial del comportamiento de los datos antes del entrenamiento del modelo, identificando patrones generales, posibles relaciones entre variables y diferencias relevantes entre los grupos de estudiantes.


### 5.3 Entrenamiento del modelo

El tercer módulo del proyecto corresponde al **entrenamiento del modelo predictivo**, implementado en el archivo `03_entrenamiento.py`. Esta etapa tiene como objetivo construir un modelo de clasificación que permita predecir si un estudiante presenta riesgo académico, tomando como referencia la variable binaria `riesgo_academico` generada durante la fase de limpieza.

El proceso inicia cargando el archivo `estudiantes_limpio.csv`, ubicado en la carpeta `data/processed/`. A partir de este dataset, se separan las variables predictoras y la variable objetivo. Las columnas `estado_academico` y `riesgo_academico` son excluidas del conjunto de entrada, mientras que `riesgo_academico` se utiliza como variable objetivo del modelo.

Posteriormente, el módulo identifica las variables numéricas del dataset, ya que estas serán utilizadas como entradas para el entrenamiento. Para preparar los datos, se emplea un `ColumnTransformer` junto con `StandardScaler`, permitiendo estandarizar las variables numéricas antes de ingresar al modelo. Este paso ayuda a que las características tengan una escala comparable durante el proceso de aprendizaje.

El modelo seleccionado para esta etapa es un `RandomForestClassifier`, configurado con 300 árboles de decisión, una semilla aleatoria fija para garantizar reproducibilidad y el parámetro `class_weight="balanced"`, con el fin de considerar el posible desbalance entre estudiantes con riesgo y sin riesgo académico.

El flujo de preprocesamiento y modelo se integra mediante un `Pipeline`, lo que permite ejecutar de forma ordenada la transformación de los datos y el entrenamiento del clasificador. Luego, el dataset se divide en un conjunto de entrenamiento y un conjunto de prueba, utilizando el 80% de los datos para entrenamiento y el 20% para evaluación. Además, se aplica una división estratificada para conservar la proporción original de las clases en ambos subconjuntos.

Después de entrenar el modelo, se generan predicciones sobre el conjunto de prueba y se calculan diferentes métricas de evaluación, entre ellas: `accuracy`, `precision`, `recall`, `F1-score` y `ROC-AUC`. Estas métricas permiten analizar el rendimiento general del modelo, así como su capacidad para detectar correctamente los casos de riesgo académico.

Adicionalmente, se aplica validación cruzada con 5 particiones utilizando el `F1-score` como métrica principal. Esto permite obtener una evaluación más estable del desempeño del modelo y reducir la dependencia de una única división entre entrenamiento y prueba.

Como salida final, el modelo entrenado se guarda en la carpeta `models/` con el nombre `modelo_dropout.pkl`, utilizando la librería `joblib`. Asimismo, las métricas obtenidas, la matriz de confusión y el reporte de clasificación son almacenados en el archivo `reports/metricas_modelo.txt`, permitiendo documentar los resultados del entrenamiento para su posterior revisión.

En conjunto, este módulo constituye la parte central del proyecto, ya que permite construir y guardar el modelo que posteriormente será utilizado para generar predicciones de riesgo académico sobre nuevos datos o registros procesados.


### 5.4 Generación de predicciones

El cuarto módulo del proyecto corresponde a la **generación de predicciones**, implementado en el archivo `04_prediccion.py`. Esta etapa utiliza el modelo entrenado previamente para estimar el riesgo académico de los estudiantes y generar un archivo final con los resultados ordenados según la probabilidad de abandono.

El proceso inicia definiendo las rutas necesarias del proyecto. El módulo utiliza como entrada el dataset limpio `estudiantes_limpio.csv`, ubicado en la carpeta `data/processed/`, y el modelo entrenado `modelo_dropout.pkl`, almacenado en la carpeta `models/`. Además, se define como carpeta de salida `data/outputs/`, donde se guardará el archivo `predicciones.csv`.

Antes de ejecutar las predicciones, el script verifica que existan tanto el dataset limpio como el modelo entrenado. Si alguno de estos archivos no se encuentra disponible, el programa detiene la ejecución y muestra un mensaje de error. Esta validación permite asegurar que las etapas previas del flujo hayan sido ejecutadas correctamente.

Luego, el módulo carga el dataset procesado mediante `pandas` y recupera el modelo entrenado utilizando `joblib`. A partir del dataset, se separan las variables predictoras eliminando las columnas `estado_academico` y `riesgo_academico`, ya que estas corresponden a la variable original de referencia y a la variable objetivo del modelo.

Con el modelo cargado, se generan dos resultados principales para cada estudiante. Primero, se calcula la columna `prediccion_riesgo`, que indica si el modelo clasifica al estudiante como en riesgo académico o no. Segundo, se calcula la columna `probabilidad_riesgo`, que representa la probabilidad estimada de que el estudiante pertenezca a la clase de riesgo académico.

Para facilitar la interpretación de los resultados, el módulo crea una variable adicional llamada `nivel_riesgo`. Esta variable clasifica la probabilidad de riesgo en tres niveles: `Bajo`, `Medio` y `Alto`. Los estudiantes con probabilidad entre 0 y 0.4 son clasificados como riesgo bajo; aquellos con probabilidad entre 0.4 y 0.7 como riesgo medio; y los que se encuentran entre 0.7 y 1 como riesgo alto.

Posteriormente, los registros se ordenan de mayor a menor según la columna `probabilidad_riesgo`, permitiendo identificar rápidamente a los estudiantes que presentan mayor probabilidad de abandono académico. El resultado final se guarda en el archivo `data/outputs/predicciones.csv`.

Como salida informativa, el módulo muestra en consola los 15 estudiantes con mayor riesgo académico, incluyendo variables relevantes como el estado académico, la predicción del modelo, la probabilidad de riesgo, el nivel de riesgo, la edad al momento de matrícula, la nota de admisión y las unidades curriculares aprobadas en el primer y segundo semestre. También se muestra la distribución general de los niveles de riesgo generados.

En conjunto, este módulo permite transformar el modelo predictivo en una herramienta práctica para priorizar casos de seguimiento académico, ya que entrega un ranking interpretable de estudiantes según su probabilidad estimada de abandono.


### 5.5 Aplicación en Streamlit

## 6. Resultados generales

## 7. Tecnologías utilizadas

## 8. Instalación y ejecución

## 9. Archivos principales

## 10. Conclusiones generales
