import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Load CSV
data = pd.read_csv(r"C:\Users\CHIRANTH M\Desktop\Python_projects\Python\imports_project\student.csv")

# Step 2: Show dataset
print("Columns in CSV:", data.columns)
print(data.head())

# Step 3: Use correct column names (case-sensitive!)
X = data[['Hrs']]      # Feature (hours studied)
y = data['Score']      # Target (score)

# Step 4: Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 5: Print slope and intercept
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)

# Step 6: Predict example (e.g., score for 5 hrs)
pred = model.predict([[5]])
print("Predicted score for 5 hrs:", pred[0])

# Step 7: Plot data & regression line
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Linear Regression - Student Performance")
plt.legend()
plt.show()
