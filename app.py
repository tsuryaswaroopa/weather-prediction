from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("weather_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        humidity = float(request.form["humidity"])
        pressure = float(request.form["pressure"])
        wind = float(request.form["wind"])

    except ValueError:
        return "Please enter valid numeric values."

    # Validation
    if humidity < 0 or humidity > 1:
        return "Humidity should be between 0 and 1."

    if pressure < 800 or pressure > 1200:
        return "Pressure should be between 800 and 1200 mb."

    if wind < 0:
        return "Wind speed cannot be negative."

    prediction = model.predict([[humidity, pressure, wind]])

    temp = round(prediction[0], 2)

    # Weather condition
    if temp >= 35:
        condition = "Very Hot 🔥"

    elif temp >= 25:
        condition = "Sunny ☀️"

    elif temp >= 15:
        condition = "Pleasant 🌤️"

    elif temp >= 5:
        condition = "Cool 🌥️"

    else:
        condition = "Cold ❄️"

    return render_template(
        "result.html",
        prediction=temp,
        humidity=humidity,
        pressure=pressure,
        wind=wind,
        condition=condition
    )


if __name__ == "__main__":
    app.run(debug=True)