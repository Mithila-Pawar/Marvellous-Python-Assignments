import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ( accuracy_score, confusion_matrix, classification_report, roc_auc_score,roc_curve)

file_path = "/mnt/data/d4d46b0d-d7b7-438a-877a-f8c16ac812c7.csv"
df = pd.read_csv(file_path, delimiter=';', quotechar='"')

categorical_cols = ['job', 'education', 'contact', 'poutcome']
df[categorical_cols] = df[categorical_cols].replace('unknown', 'missing')

X = df.drop("y", axis=1)
y = df["y"].map({'no': 0, 'yes': 1})

categorical_features = X.select_dtypes(include="object").columns.tolist()
numeric_features = X.select_dtypes(include=np.number).columns.tolist()

preprocessor = ColumnTransformer([ ("num", StandardScaler(), numeric_features),  ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier(random_state=42)
}

results = {}
for name, model in models.items():
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", model)
    ])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    y_proba = pipeline.predict_proba(X_test)[:, 1]

    results[name] = {
        "accuracy": accuracy_score(y_test, y_pred),
        "conf_matrix": confusion_matrix(y_test, y_pred),
        "report": classification_report(y_test, y_pred, output_dict=True),
        "roc_auc": roc_auc_score(y_test, y_proba),
        "fpr_tpr": roc_curve(y_test, y_proba)[:2]
    }

for name, res in results.items():
    print(f"=== {name} ===")
    print(f"Accuracy: {res['accuracy']:.4f}")
    print("Confusion Matrix:")
    print(res["conf_matrix"])
    print("\nClassification Report:")
    print(pd.DataFrame(res["report"]).transpose())
    print("=" * 60)
