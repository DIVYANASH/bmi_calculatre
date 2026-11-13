
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = ""

    if request.method == "POST":

        name = request.form["name"]
        age = int(request.form["age"])
        gender = request.form["gender"]

        weight = float(request.form["weight"])
        height = float(request.form["height"])

        activity = int(request.form["activity"])

        # Convert metres into centimetres
        height_cm = height * 100

        # BMI Calculation
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal Weight"

        elif bmi < 30:
            category = "Overweight"

        else:
            category = "Obese"

        # BMR Calculation
        if gender == "male":

            bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5

        else:

            bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

        # Activity Multiplier
        if activity == 1:
            calories = bmr * 1.2

        elif activity == 2:
            calories = bmr * 1.375

        elif activity == 3:
            calories = bmr * 1.55

        elif activity == 4:
            calories = bmr * 1.725

        else:
            calories = 0

        # Calorie Goals
        maintenance = calories
        weight_gain = calories + 300
        weight_loss = calories - 300

        result = {
            "name": name,
            "bmi": round(bmi, 2),
            "category": category,
            "bmr": round(bmr),
            "maintenance": round(maintenance),
            "weight_gain": round(weight_gain),
            "weight_loss": round(weight_loss)
        }

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
