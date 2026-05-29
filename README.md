# Predicción de Riesgo Académico

## 1. Descripción del proyecto

## 2. Objetivo del proyecto

## 3. Dataset utilizado

## 4. Estructura del proyecto

## 5. Flujo general del proceso

### 5.1 Limpieza y preparación de datos
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

### 5.4 Generación de predicciones
### 5.5 Aplicación en Streamlit

## 6. Resultados generales

## 7. Tecnologías utilizadas

## 8. Instalación y ejecución

## 9. Archivos principales

## 10. Conclusiones generales
