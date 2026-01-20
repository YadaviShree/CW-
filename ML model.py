import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load data
df = pd.read_csv('cleaned_data.csv')

# SIMPLE APPROACH: Use only numeric columns
print("Using only numeric columns for simplicity...")

# Select only numeric features
numeric_features = ['Engine HP', 'Engine Cylinders', 'highway MPG', 
                    'city mpg', 'Year', 'Popularity', 'Avg MPG']

# Check which features exist
available_features = [f for f in numeric_features if f in df.columns]
print(f"Available features: {available_features}")

X = df[available_features].copy()
y = df['MSRP']

# Handle missing values
X = X.fillna(X.median())
y = y.fillna(y.median())

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train simple model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
from sklearn.metrics import r2_score, mean_absolute_error
y_pred = model.predict(X_test)

print(f"\n✅ SUCCESS! Model trained.")
print(f"R² Score: {r2_score(y_test, y_pred):.3f}")
print(f"Mean Absolute Error: ${mean_absolute_error(y_test, y_pred):,.0f}")

# Feature importance
importance = pd.DataFrame({
    'feature': available_features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nFeature Importance:")
print(importance.to_string(index=False))