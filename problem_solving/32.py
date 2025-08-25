import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("D:\student-por.csv", sep=",", quotechar='"')

# ----------------------
# 1) Data Cleaning & Preprocessing
# ----------------------

# Check for missing values
print("Missing values per column:\n", data.isnull().sum())

# Convert numerical columns to correct dtype (already mostly int/float)
num_cols = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel",
            "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]
data[num_cols] = data[num_cols].apply(pd.to_numeric, errors='coerce')

# Drop duplicates if any
data = data.drop_duplicates()

print("\nData shape after cleaning:", data.shape)

# ----------------------
# 2) Exploratory Data Analysis (EDA)
# ----------------------

# Histograms
plt.figure(figsize=(12, 6))
for i, col in enumerate(["age", "studytime", "absences", "G1", "G2", "G3"]):
    plt.subplot(2, 3, i+1)
    plt.hist(data[col], bins=15, color="skyblue", edgecolor="black")
    plt.title(f"Histogram of {col}")
plt.tight_layout()
plt.show()

# Scatter plot with regression line (studytime vs G3)
plt.figure(figsize=(8, 6))
sns.regplot(x="studytime", y="G3", data=data, scatter_kws={"alpha":0.5}, line_kws={"color":"red"})
plt.title("Study Time vs Final Grade (G3)")
plt.show()

# Box plots (Grades by Sex)
plt.figure(figsize=(8, 6))
sns.boxplot(x="sex", y="G3", hue="sex", data=data, palette="Set2", legend=False)
plt.title("Final Grade (G3) Distribution by Sex")
plt.show()

# Box plot (Absences by Sex)
plt.figure(figsize=(8, 6))
sns.boxplot(x="sex", y="absences", hue="sex", data=data, palette="Set3", legend=False)
plt.title("Absences Distribution by Sex")
plt.show()
