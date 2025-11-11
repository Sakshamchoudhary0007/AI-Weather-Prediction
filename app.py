# =====================================
# 🌦️ AI Weekly Weather Predictor (with Charts + Debug)
# Developed by: Saksham Seervi
# =====================================

from flask import Flask, render_template, request
import requests
import numpy as np
from datetime import datetime

app = Flask(__name__)

# ---------- FUNCTION TO FETCH WEATHER DATA ----------
def get_weather_data(city):
    api_key = "46a4e6460eb4fe34a8d3c7abaa0df68b"  # ✅ Your working API key
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    
    print("📡 Fetching from:", base_url)  # Debug line
    res = requests.get(base_url).json()
    print("🟢 API RESPONSE CODE:", res.get("cod"))  # Debug line

    # Check for invalid city or API issue
    if res.get("cod") != "200":
        print("⚠️ API Error:", res)
        return None, False

    # ---------- CURRENT WEATHER ----------
    current = res["list"][0]
    current_temp = current["main"]["temp"]
    current_humidity = current["main"]["humidity"]
    current_wind = current["wind"]["speed"]
    current_desc = current["weather"][0]["description"].title()

    # ---------- WEEKLY FORECAST ----------
    forecast = []
    added_days = set()

    for entry in res["list"]:
        date_txt = entry["dt_txt"]
        day_name = datetime.strptime(date_txt, "%Y-%m-%d %H:%M:%S").strftime("%a")

        # Take one record per day (7 days max)
        if day_name not in added_days and len(forecast) < 7:
            added_days.add(day_name)
            forecast.append({
                "day": day_name,
                "temp": round(entry["main"]["temp"], 1),
                "humidity": entry["main"]["humidity"],
                "wind": entry["wind"]["speed"],
                "condition": entry["weather"][0]["description"].title()
            })

    # ---------- AI LOGIC ----------
    temps = [d["temp"] for d in forecast]
    slope = np.polyfit(range(len(temps)), temps, 1)[0]

    if slope > 0.3:
        week_trend = "Warming Week 🌞"
    elif slope < -0.3:
        week_trend = "Cooling Week 🌧️"
    else:
        week_trend = "Stable Weather 🌤️"

    wind_avg = np.mean([d["wind"] for d in forecast])
    if wind_avg > 20:
        wind_trend = "Windy Week 💨"
    elif wind_avg < 5:
        wind_trend = "Calm Week 🌈"
    else:
        wind_trend = "Normal Breeze 🌬️"

    # ---------- RETURN DATA ----------
    return {
        "city": city.capitalize(),
        "current_temp": current_temp,
        "current_humidity": current_humidity,
        "current_wind": current_wind,
        "current_desc": current_desc,
        "forecast": forecast,
        "week_trend": week_trend,
        "wind_trend": wind_trend
    }, True


# ---------- FLASK ROUTES ----------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    city = request.form['city']
    result, success = get_weather_data(city)
    if not success:
        return render_template('index.html', error="City not found or API issue.")
    current_time = datetime.now().strftime("%A, %d %B %Y | %I:%M %p")
    return render_template('result.html', current_time=current_time, **result)


# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True, port=5001)

