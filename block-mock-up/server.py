from flask import Flask, render_template
import datetime as dt
import requests


app = Flask(__name__)

@app.route("/")
def home_route():
    current_time = dt.datetime.now()
    current_year = current_time.year
    return render_template('index.html', year=current_year)


@app.route("/<name>")
def user_info_guess(name):
    # Get user age
    raw_age_name_data = requests.get(f"https://api.agify.io?name={name}")
    raw_age_name_data = raw_age_name_data.json()
    user_age = raw_age_name_data['age']
    # Get user gender
    raw_gender_data = requests.get(f"https://api.genderize.io?name={name}")
    raw_gender_data = raw_gender_data.json()
    user_gender = raw_gender_data["gender"]
    
    user_info = {"name": name, "age": user_age, "gender": user_gender}

    return render_template("gender-age.html", user_info=user_info)


if __name__ == "__main__":
    app.run(debug=True)