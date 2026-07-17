import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "weatherHistory.csv")

df = pd.read_csv(csv_path)
# Select features and target
X = df[['Humidity', 'Pressure (millibars)', 'Wind Speed (km/h)']]
y = df['Temperature (C)']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and weather_model.pkl saved successfully")