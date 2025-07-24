from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

def get_data():
    data = load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df, data

def prepare_data(df):
    X = df.drop('target', axis=1)
    y = df['target']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.3, random_state=42)

def train_model(X_train, y_train, k=5):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    return model

def test_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return acc, report, y_pred

def main():
    df, data_info = get_data()
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train, k=5)

    accuracy, report, predictions = test_model(model, X_test, y_test)

    print("=== Wine Classifier using KNN ===\n")
    print(f"Accuracy: {accuracy*100:.2f}%\n")
    print("Classification Report:")
    print(report)

if __name__== "_main_":
    main()