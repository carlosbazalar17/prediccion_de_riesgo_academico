import pandas as pd
import joblib
import os
from pathlib import Path

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Rutas
ruta_dataset = BASE_DIR / "data" / "processed" / "estudiantes_limpio.csv"
ruta_modelos = BASE_DIR / "models"
ruta_modelo = ruta_modelos / "modelo_dropout.pkl"
ruta_metricas = BASE_DIR / "reports" / "metricas_modelo.txt"

# Crear carpetas necesarias
os.makedirs(ruta_modelos, exist_ok=True)
os.makedirs(BASE_DIR / "reports", exist_ok=True)

# Cargar dataset limpio
df = pd.read_csv(ruta_dataset)

print("=" * 60)
print("ENTRENAMIENTO DEL MODELO PREDICTIVO")
print("=" * 60)

print("\nDimensiones del dataset:")
print(df.shape)

# Separar variables predictoras y objetivo
X = df.drop(columns=["estado_academico", "riesgo_academico"])
y = df["riesgo_academico"]

# Identificar variables numéricas
numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

print("\nCantidad de variables predictoras:", X.shape[1])
print("Cantidad de variables numéricas:", len(numeric_features))

# Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features)
    ],
    remainder="drop"
)

# Modelo
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced",
    max_depth=None
)

# Pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# División entrenamiento / prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTamaño de entrenamiento:", X_train.shape)
print("Tamaño de prueba:", X_test.shape)

print("\nDistribución en entrenamiento:")
print(y_train.value_counts())

print("\nDistribución en prueba:")
print(y_test.value_counts())

# Entrenar modelo
pipeline.fit(X_train, y_train)

# Predicciones
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]

# Métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_proba)

# Validación cruzada
cv_scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=5,
    scoring="f1"
)

# Resultados
print("\nMÉTRICAS DEL MODELO")
print("-" * 60)
print("Accuracy:", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1-score:", round(f1, 4))
print("ROC-AUC:", round(roc_auc, 4))
print("F1 promedio CV:", round(cv_scores.mean(), 4))

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# Guardar modelo
joblib.dump(pipeline, ruta_modelo)

# Guardar métricas en txt
with open(ruta_metricas, "w", encoding="utf-8") as f:
    f.write("MÉTRICAS DEL MODELO PREDICTIVO\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Dataset: {df.shape[0]} registros y {df.shape[1]} columnas\n")
    f.write(f"Modelo: Random Forest Classifier\n\n")
    f.write(f"Accuracy: {round(accuracy, 4)}\n")
    f.write(f"Precision: {round(precision, 4)}\n")
    f.write(f"Recall: {round(recall, 4)}\n")
    f.write(f"F1-score: {round(f1, 4)}\n")
    f.write(f"ROC-AUC: {round(roc_auc, 4)}\n")
    f.write(f"F1 promedio CV: {round(cv_scores.mean(), 4)}\n\n")
    f.write("Matriz de confusión:\n")
    f.write(str(confusion_matrix(y_test, y_pred)))
    f.write("\n\nReporte de clasificación:\n")
    f.write(classification_report(y_test, y_pred))

print("\nModelo guardado correctamente en:")
print(ruta_modelo)

print("\nMétricas guardadas en:")
print(ruta_metricas)