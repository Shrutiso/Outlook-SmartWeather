# 🌦️ Weather Intelligence System

A unified **AI-powered weather web application** that answers everyday practical questions like:

* **Will it rain today or tomorrow?** ☔
* **Will my clothes dry if I dry them outside?** 👕🌤️
* **Should I carry an umbrella?**
* **Which nearby places are good to travel today based on weather conditions?** ✈️

This project integrates **real-time weather intelligence**, **data-driven travel suggestions**, and **user-friendly insights** into **one single platform**, eliminating the need for multiple apps for the same information.

---

## 🚀 Motivation

In daily life, people often check multiple apps for:

* Temperature
* Rain forecast
* Humidity & wind
* Travel suggestions

Yet, **no single app answers simple real-life questions directly**, such as:

> *“Will my clothes dry today?”*
> *“Do I really need to carry an umbrella?”*

This application bridges that gap by converting **raw weather data into meaningful decisions**.

---

## 🧠 Key Features

### 🌡️ Current Weather Information

* Real-time temperature
* Humidity levels
* Wind speed
* Air Quality Index (AQI)

### 🌧️ Rain Prediction

* Hour-wise rain probability
* Tomorrow’s rain forecast
* Clear rain/no-rain insights (not just numbers)

### 👕 Clothes Drying Prediction

Uses:

* Humidity
* Wind speed
* Rain probability

To answer:

> **“Yes, good drying conditions”** or **“No, avoid drying clothes today”**

### 🧳 Travel Recommendation System

* Suggests suitable travel places
* Uses **historical + structured dataset** (via Pandas)
* Filters locations based on weather suitability

### 🔐 Secure Authentication

* Google OAuth Login
* Email verification using Google API
* Secure user sessions

### 🌐 Unified Platform

* Combines weather, rain logic, drying logic, and travel insights
* Avoids using multiple standalone apps

---

## 🛠️ Tech Stack

### Backend

* **Flask (Python)** – Web framework
* **Pandas** – Dataset handling & travel logic
* **Weather API** – Real-time weather data
* **OAuth 2.0 (Google API)** – Authentication & email verification

### Frontend

* **HTML5**
* **CSS3** (modern UI, glassmorphism-inspired design)

### Other Tools

* Git & GitHub
* REST APIs

---

## 🧩 System Architecture

```
User
 │
 │ Browser (UI)
 ▼
Flask Web Server
 │
 ├── Weather API (Real-time data)
 ├── Pandas Dataset (Travel places)
 ├── Rain Probability Logic
 ├── Clothes Drying Decision Logic
 └── Google OAuth Authentication
```

---

## 📊 Decision Logic (Simplified)

### Clothes Drying Logic

* Low rain probability
* Moderate humidity
* Adequate wind speed

➡️ **Good Drying Conditions**

### Umbrella Suggestion

* Rain probability > threshold

➡️ **Carry an umbrella**

---

## 📷 UI Preview

## Login Page with Google OAuth
 
## Interactive Weather Dashboard

 ## Rain probability charts

 
 ## Clothes drying insights




## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/weather-intelligence-system.git

# Navigate to project directory
cd weather-intelligence-system

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Access the app at:

```
http://127.0.0.1:5000
```

---

## 🔑 Environment Variables



```env
WEATHER_API_KEY=your_weather_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SECRET_KEY=your_flask_secret_key
```

---

## 📌 Problem Solved

✔ Eliminates checking multiple weather apps
✔ Converts weather data into **actionable insights**
✔ Helps users make **quick daily decisions**
✔ Combines **weather + travel + lifestyle intelligence**

---

## 🔮 Future Enhancements

* ML-based rain prediction
* Personalized drying recommendations
* Push notifications for rain alerts
* Mobile app version
* Voice-based weather assistant

---

## 👩‍💻 Author

**Shruti Somvanshi**
Data Science | Web Development | AI Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!

 
