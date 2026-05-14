# Intelligent-Climate-Control
This project is an IoT-based Climate Monitoring and Crop Prediction System designed to monitor environmental conditions in real time and provide intelligent agricultural insights.
## Features
- ✅ Real-time temperature & humidity monitoring
- ✅ Crop recommendation system
- ✅ Raspberry Pi Pico W integration
- ✅ DHT22 sensor support
- ✅ Secure sensor authentication using auth keys
- ✅ REST API architecture
- ✅ Weather API integration
- ✅ SQLite database support
- ✅ Responsive React dashboard
- ✅ Real-time alerts & monitoring
- ✅ Scalable modular sensor architecture
## Prediction Logic
The crop recommendation engine uses:

- Euclidean Distance
- Cosine Similarity

to compare current environmental conditions with historical crop datasets and recommend the most suitable crops.
## Tech Stack
### 🎨 Frontend
- React.js
- Tailwind CSS
- JavaScript
### ⚙️ Backend
- Node.js
- Express.js
### 🗄️ Database
- SQLite
### 🔌 Hardware
- Raspberry Pi Pico W
- DHT22 Sensor
### 📚 Libraries & APIs
- Axios
- CSV Parser
- QRCode Generator
- OpenWeather API
## System Architecture
DHT22 Sensor → Raspberry Pi Pico W → Node.js Backend → SQLite Database → Recommendation Engine → React Dashboard
## Project Structure
```bash
Intelligent-Climate-Control/
│
├── weather-server/
│   ├── server.js
│   ├── cropRecommendation.js
│   ├── deviceServer.js
│   ├── insertCSVDataIntoDB.js
│   ├── connecteddevices.js
│   ├── database.db
│   ├── Crop_recommendation.csv
│   └── package.json
│
├── pico_code.py
├── README.md
└── .gitignore
```
# ⚡ Installation & Setup

## 📥 Clone Repository

```bash
git clone https://github.com/your-username/intelligent-climate-control.git

cd intelligent-climate-control
```

---

# 🔧 Backend Setup

```bash
cd weather-server

npm install
```

---

# ▶️ Run Server

```bash
npm start
```

Server runs on:

```bash
http://localhost:5000
```

---

# 🔑 Environment Variables

Create a `.env` file inside the `weather-server/` directory.

```env
WEATHER_API_KEY=your_openweather_api_key
PORT=5000
```

---

# 🔌 Raspberry Pi Pico Setup

Upload the `pico_code.py` file to the Raspberry Pi Pico W using Thonny IDE.

Install the required MicroPython libraries:

```python
import machine
import dht
import requests
```

Connect:
- DHT22 Sensor
- Wi-Fi enabled Raspberry Pi Pico W

Then run:

```python
pico_code.py
```

The Pico W will:
- Read temperature and humidity
- Send sensor data to backend APIs
- Push updates every 5 minutes
