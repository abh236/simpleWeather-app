# 🌦️ PyQt5 Weather App

A beautiful and responsive desktop **Weather Application** built with **PyQt5**, powered by the [OpenWeatherMap API](https://openweathermap.org/api). Enter your city name to instantly get temperature, weather condition, and a corresponding emoji.

---

## 🚀 Features1

- Real-time weather info via OpenWeatherMap
- Temperature in Celsius
- Weather condition description
- Dynamic weather emojis (☀️ 🌦️ ❄️ etc.)
- Clear UI with Qt layouts and custom CSS styles
- Full error handling for various HTTP response codes.

---

## 🖥️ Screenshots

> *(Add a screenshot here once available)*  
![Weather App Screenshot](https://via.placeholder.com/500x300.png?text=Weather+App+Preview)

---

## 🛠️ Requirements

- Python 3.x
- PyQt5
- Internet connection (to fetch API data)
- OpenWeatherMap API key

### 🔧 Install Dependencies

```bash
pip install pyqt5 requests
🧪 How to Run
Clone this repository or download the code.

Replace the default api_key in the script with your own OpenWeatherMap API key.

python
Copy
Edit
api_key = "YOUR_API_KEY_HERE"
Run the app:

bash
Copy
Edit
python weather_app.py
🌍 API Information
This app uses OpenWeatherMap to fetch real-time weather data.

Endpoint used:

bash
Copy
Edit
https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}

🎨 UI & Layout
Built with QVBoxLayout for vertical stacking

Styled using Qt's setStyleSheet() for CSS-like customization

Dynamic emoji rendering using Unicode based on weather conditions

⚠️ Error Handling
The app gracefully handles:

City not found (404)

No internet connection

API authentication errors (401)

API rate limits and server errors

💡 Emojis Mapping
Weather Code Range	Emoji
200–232 (Thunder)	🌦️
300–321 (Drizzle)	🌧️
500–531 (Rain)	☁️
600–622 (Snow)	❄️
701–762 (Mist etc.)	☀️
800–804 (Clear/Clouds)	☀️
Others	😐

📁 Project Structure
bash
Copy
Edit
weather-app/
├── weather_app.py       # Main application code
├── README.md            # You're reading this!
