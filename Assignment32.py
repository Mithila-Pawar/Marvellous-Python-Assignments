import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

fake_df = pd.read_csv('/mnt/data/Fake.csv')
true_df = pd.read_csv('/mnt/data/True.csv')

fake_df['label'] = 0  
true_df['label'] = 1  

df = pd.concat([fake_df, true_df], ignore_index=True)
df = df[['text', 'label']].dropna()

X = df['text']
y = df['label']

tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
X_tfidf = tfidf.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

log_reg = LogisticRegression(max_iter=1000)
tree_clf = DecisionTreeClassifier()

log_reg.fit(X_train, y_train)
tree_clf.fit(X_train, y_train)

log_pred = log_reg.predict(X_test)
tree_pred = tree_clf.predict(X_test)

hard_voting = VotingClassifier(estimators=[
    ('lr', log_reg), ('dt', tree_clf)], voting='hard')
soft_voting = VotingClassifier(estimators=[
    ('lr', log_reg), ('dt', tree_clf)], voting='soft')

hard_voting.fit(X_train, y_train)
soft_voting.fit(X_train, y_train)

hard_pred = hard_voting.predict(X_test)
soft_pred = soft_voting.predict(X_test)

def evaluate_model(name, y_true, y_pred):
    print(f"\n------- {name} -------")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))

evaluate_model("Logistic Regression", y_test, log_pred)
evaluate_model("Decision Tree", y_test, tree_pred)
evaluate_model("Hard Voting Classifier", y_test, hard_pred)
evaluate_model("Soft Voting Classifier", y_test, soft_pred)

def plot_cm(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

plot_cm(y_test, log_pred, "Logistic Regression")
plot_cm(y_test, tree_pred, "Decision Tree")
plot_cm(y_test, hard_pred, "Hard Voting")
plot_cm(y_test, soft_pred, "Soft Voting")
