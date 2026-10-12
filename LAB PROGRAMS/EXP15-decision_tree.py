
from sklearn.tree import DecisionTreeClassifier

# Training data
X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = [1, 1, 0, 0]

# Create and train the decision tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Get user input
a = int(input("Enter first feature (0 or 1): "))
b = int(input("Enter second feature (0 or 1): "))

# Predict output
result = model.predict([[a, b]])
print("Predicted class:", result[0])
