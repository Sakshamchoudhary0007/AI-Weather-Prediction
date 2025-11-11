# AI-Weather-Prediction
Flask-based AI Weather Forecasting App using OpenWeather API &amp; Chart.js

# 🌦️ AI Weather Prediction

### A Flask-based AI Weather Forecasting Web Application 🌍  

This project uses **Python Flask**, **OpenWeatherMap API**, and **Chart.js** to display real-time and AI-analyzed weather forecasts for any city across the world.  
It also includes AI logic (using NumPy) to predict temperature trends and visualize data dynamically using interactive charts.  

---

## 🧠 Features

- 🌍 **Global City Search** with auto-suggestions using a world cities dataset  
- 🌦️ **7-Day Forecast** with daily temperature, humidity, and wind speed  
- 💡 **AI Trend Analysis** for detecting warming or cooling patterns  
- 📊 **Dynamic Charts** using Chart.js for temperature and wind visualization  
- 🌑 **Modern Dark UI** with responsive design  
- ⚡ **Real-Time API Integration** via OpenWeatherMap  

---

## 🧰 Tech Stack

| Layer | Technology |
|:------|:------------|
| **Frontend** | HTML, CSS (Dark Theme), JavaScript, Chart.js |
| **Backend** | Python (Flask Framework) |
| **AI Logic** | NumPy (Linear Trend Analysis) |
| **API** | OpenWeatherMap API |
| **Dataset** | `cities.json` (Global City List for Auto-Suggest) |

---

## 🧩 System Workflow

```mermaid
flowchart TD
A[User Enters City Name] --> B[Flask App Calls OpenWeather API]
B --> C[Fetch Real-time Weather Data (JSON)]
C --> D[AI Logic Processes Weekly Trends]
D --> E[Generate Charts and Predictions]
E --> F[Display on Dashboard (HTML + Chart.js)]


🚀 How to Run This Project

1️⃣ Clone the repository

git clone https://github.com/Sakshamchoudhary0007/AI-Weather-Prediction.git


2️⃣ Install dependencies

pip install flask requests numpy


3️⃣ Run the Flask app

python app.py


4️⃣ Open in browser

http://127.0.0.1:5050/


🧑‍💻 Developer Info

Developed By:
Saksham Seervi
🎓 MCA (AI & ML), University Institute of Computing

📚 References

🌐 OpenWeatherMap API

🧠 NumPy

⚙️ Flask

📊 Chart.js

🌍 Global Cities Dataset

⭐ Show Your Support

If you like this project, don’t forget to ⭐ star the repository and share it with others!