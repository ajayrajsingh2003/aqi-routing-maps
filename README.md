# AQI Routing Maps

This project introduces a health-aware routing system that integrates real-time data from the **Azure Maps API** (Air Quality, Weather, and Routes). Instead of guiding commuters only along the fastest path, the system identifies cleaner and safer alternatives by evaluating pollution exposure along each route.

Designed primarily to support respiratory disease patients and pollution-sensitive groups, the system demonstrates how navigation can evolve from being purely efficiency-driven to **health- and environment-conscious**.

-  Generates routes that minimize exposure to harmful pollutants (helpful in **daily commuting** or **wildfire evacuations**).  
-  Encourages sustainable, green commuting practices.  
-  Supports smart city initiatives by integrating health metrics into mobility solutions.  

Ultimately, this work highlights how pollution-sensitive navigation can improve **daily commuting safety and comfort**, while also serving as a framework for future intelligent mobility in smart cities.

---

##  Recognition & Impact
- Featured in the **New Jersey Big Data Alliance (NJBDA) 2025** Research Work (**Under Review**).  
- 🥇 **First Prize** at Data Science Showcase SPU (2024).  

**Academic Affiliation**  
Saint Peter's University – Data Science Institute, Jersey City, NJ, USA  

---

## Gallery (Click to View LinkedIn Posts)

| Data Science Showcase Winner @ SPU 2024 | NJBDA Research Presentation |
|-----------------------------------------|-------------------------------|
| [![Data Science Showcase](assets/Data%20Science%20Showcase%20Win.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7270277314288967680/) <br> [![With Professor](assets/Data%20Science%20Showcase%20with%20Professor.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7270277314288967680/) | [![NJBDA Conference](assets/NJBDA%20Conference.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7330083180433002496/) <br> [![Research Presentation](assets/NJBDA%20Research%20Presntation%20.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7330083180433002496/) |

| Guest Lecture (Exchange Program, India) | |
|-----------------------------------------|---|
| [![Student Exchange](assets/Student%20exchange%20Program%20INDIA.jpeg)](https://your-link.com) | [![Exchange Presentation](assets/Student%20Exchange%20Program%20Presentation.jpeg)](https://your-link.com) |

---
## Development Team
- [**Ajay Raj Singh**](https://www.linkedin.com/in/connectwithajayrajsingh/)  
- [**Yaswanth Pati**](https://www.linkedin.com/in/yaswanthpati/)  
- [**Dr. Sharath Kumar Jagannathan**](https://www.linkedin.com/in/sharathkumarj/)  

---

## Live Demo
- 🌐 **Website** → View Live (Update Soon) 
- 🎥 **Video Walkthrough** → Watch on YouTube (Update Soon)
- 📄 **NJBDA Journal Reference** → Read More  (https://njbda.org/2025symposium/#)

---

##  Project Highlights
- Real-time **AQI + Weather** integrated with routing  
- Personalized **health-safe routes**  
- Built on **Azure Maps APIs** (Routes, Weather, AQI)  
- Interactive **Web interface for visualization**  
- Future extension → **Mobile App**  

---

## Repository Structure
```
AQI Routing Maps/
│
├── README.md                # Clear project overview, setup, demo links
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignore .venv, cache files etc
│
├── assets/                     # Core source code
│   ├── NJBDA Research Presentation.jpg ...  # Images of Presentations at various platforms
│   
├── src/                     # Core source code
│   ├── main.py              # Entry point
│   ├── allAPI.py            # Unified API handler
│   ├── airQualityAPI.py     # AQI data fetcher
│   ├── weatherAPI.py        # Weather data fetcher
│   ├── routesAPI.py         # Routing (Azure Maps)
│   ├── subscriptionKeysAzure.py
│   ├── urls.py              # All used URLs (Azure Maps)
│
├── data/                    # Sample inputs/outputs
│   ├── route_json_2_alternatives.txt
│   ├── sample_aqi.json
│   ├── sample_weather.json
│   └── sample_route.json
│
├── docs/                    # Documentation & presentations
│   ├── system_architecture.png
│   ├── presentation.pdf
│
└── demo/                    # Website & media
    └──screenshots/
       ├── spu_university_to_journal_square_path_station_aqi_routing.jpeg
    
```
---

## System Architecture

**How the Algorithm Works**  
1. **Fetch Routes** → Query Azure Maps for multiple routes.  
2. **Extract Coordinates** → Get lat/long for route segments.  
3. **Fetch AQI & Weather** → Pull pollutant levels for each segment.  
4. **Fuse Data** → Interpolate AQI values along route.  
5. **Exposure Calculation** → Estimate AQI/weather exposure.  
6. **Cost Function** → `Cost = β * Distance + γ * AQI Exposure`.  
7. **Select Route** → Choose lowest-cost (healthier if γ is high).  
8. **Display** → Show *Fastest Route* vs *Health-Safe Route* on map.  

---

## Installation & Setup

```bash
# Clone repo
git clone https://github.com/ajayrajsingh2003/AQI-Routing-Maps.git
cd AQI-Routing-Maps

# Setup virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run project
python src/main.py
```
---

# References & Publication

- Featured in NJBDA Journal (2025) – Under Review.
-  Built with Azure Maps API (Routes, Weather, Air Quality).

## Future Work

- Mobile App Integration (Flutter / React Native)
- Real-time alert system for high pollution events
- Integration with wearable health sensors

## Authors

**Ajay Raj Singh** – Data Engineer / Data Scientist

**Special thanks to mentors & NJBDA community.**