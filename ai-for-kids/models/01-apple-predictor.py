# Simple AI using Machine Learning

from sklearn.tree import DecisionTreeClassifier

# Training Data
# [weight, smoothness]
# Apple  = 0
# Banana = 1

features = [
    [150, 1],   # Apple
    [170, 1],   # Apple
    [120, 0],   # Banana
    [110, 0]    # Banana
]

labels = [0, 0, 1, 1]

# Create AI Model
model = DecisionTreeClassifier()

# Train the model
model.fit(features, labels)

# New fruit to predict
prediction = model.predict([[140, 1]])

# Output result
if prediction[0] == 0:
    print("Apple")
else:
    print("Banana")