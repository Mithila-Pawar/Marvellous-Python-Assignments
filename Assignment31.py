#Breast Cancer Classification
#Models Used: Decision Tree, Random Forest, Gradient Boosting
#Metrics: Accuracy, Confusion Matrix, ROC-AUC
#Dataset: sklearn.datasets.load_breast_cancer

from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import seaborn as sns

data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

exploration_breast_cancer = {
    "Shape": X.shape,
    "Feature Names": X.columns.tolist(),
    "Target Distribution": y.value_counts().to_dict(),
    "Target Labels": dict(enumerate(data.target_names))
}

X.describe().T, exploration_breast_cancer
