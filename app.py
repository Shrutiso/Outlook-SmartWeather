import requests
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

WEATHER_API_KEY = "024d1d98bdabbdf55727743213bacb43"

# ---------------- DATA ----------------
data = [

("Delhi", "Delhi", "Winter", 2500, "monuments,heritage",
 "India Gate, Red Fort, Qutub Minar, Lotus Temple, Humayun’s Tomb"),

("Agra", "Uttar Pradesh", "Winter", 2200, "monuments,heritage",
 "Taj Mahal, Agra Fort, Mehtab Bagh"),

("Jaipur", "Rajasthan", "Winter", 2400, "monuments,heritage",
 "Hawa Mahal, Amer Fort, City Palace, Jal Mahal"),

("Manali", "Himachal Pradesh", "Summer", 3500, "mountain,nature",
 "Solang Valley, Rohtang Pass, Hadimba Temple"),

("Shimla", "Himachal Pradesh", "Summer", 3200, "mountain,nature",
 "Mall Road, Jakhoo Temple, Kufri"),

("Goa", "Goa", "Winter", 4200, "beach,party",
 "Baga Beach, Calangute Beach, Fort Aguada"),

("Rishikesh", "Uttarakhand", "Winter", 2000, "religious,adventure",
 "Laxman Jhula, Ram Jhula, River Rafting"),

("Haridwar", "Uttarakhand", "Winter", 1800, "religious",
 "Har Ki Pauri, Ganga Aarti"),

("Ooty", "Tamil Nadu", "Summer", 3000, "mountain,garden",
 "Botanical Garden, Ooty Lake"),

("Mysuru", "Karnataka", "Winter", 2300, "heritage,garden",
 "Mysore Palace, Brindavan Gardens"),

("Andaman", "Andaman & Nicobar", "Winter", 5500, "beach,island",
 "Radhanagar Beach, Cellular Jail")
]

df = pd.DataFrame(
    data,
    columns=["City", "State", "Season", "Budget", "Category", "Attractions"]
)

# ---------------- WEATHER ----------------
def get_weather(city):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )
    r = requests.get(url)
    if r.status_code != 200:
        return None
    d = r.json()
    return {
        "temp": d["main"]["temp"],
        "humidity": d["main"]["humidity"],
        "condition": d["weather"][0]["description"]
    }

# ---------------- ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    city_data = None

    if request.method == "POST":
        city = request.form.get("city").strip()
        max_budget = request.form.get("budget")
        interest = request.form.get("interest")

        weather = get_weather(city)
        if not weather:
            weather = {"temp": "-", "humidity": "-", "condition": "unknown"}

        matched = df[df["City"].str.lower() == city.lower()]

        if not matched.empty:
            row = matched.iloc[0]

            # ✅ APPLY FILTERS
            if max_budget and row["Budget"] > int(max_budget):
                city_data = None
            elif interest and interest not in row["Category"]:
                city_data = None
            else:
                city_data = {
                    "city": row["City"],
                    "state": row["State"],
                    "budget": int(row["Budget"]),
                    "category": row["Category"],
                    "places": row["Attractions"].split(",")
                }

    return render_template("index.html",
                           weather=weather,
                           city_data=city_data)

if __name__ == "__main__":
    app.run(debug=True)
