import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load the Data
def load_data():
    data = pd.DataFrame
    ({
        'Wether': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy','Sunny', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny','Rainy', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild','Mild', 'Mild', 'Hot', 'Mild', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool','Mild', 'Mild', 'Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Mild', 'Cool'],
        'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes','Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes','Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
    })
    return data

def prepare_data(data):
    le_wether = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    data['Wether'] = le_wether.fit_transform(data['Wether'])
    data['Temperature'] = le_temp.fit_transform(data['Temperature'])
    data['Play'] = le_play.fit_transform(data['Play'])

    features = data[['Wether', 'Temperature']]
    target = data['Play']
    return features, target, le_play

def train_model(features, target, k=3):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(features, target)
    return model

def predict(model, le_play, input_wether, input_temp):
    le_wether = LabelEncoder().fit(['Sunny', 'Overcast', 'Rainy'])
    le_temp = LabelEncoder().fit(['Hot', 'Cool', 'Mild'])
    
    encoded_input = [[le_wether.transform([input_wether])[0], le_temp.transform([input_temp])[0]]]
    prediction = model.predict(encoded_input)
    result = le_play.inverse_transform(prediction)
    return result[0]

def check_accuracy(data, k=3):
    features, target, le_play = prepare_data(data)
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.5, random_state=42)

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    return accuracy

data = load_data()
features, target, le_play = prepare_data(data)
model = train_model(features, target, k=3)

wether_input = 'Sunny'
temp_input = 'Mild'
result = predict(model, le_play, wether_input, temp_input)
print(f"Prediction for Wether = {wether_input}, Temperature = {temp_input} ➤ Play: {result}")

for k in range(1, 6):
    acc = check_accuracy(data, k)
    print(f"Accuracy with K={k}: {acc*100:.2f}%")