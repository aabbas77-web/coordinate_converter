# 🌍 Coordinate Converter Tool
# By Dr. Ali Abbas
# aabbas7@gmail.com
# 2025

A minimal web tool to convert geospatial coordinates between:
- **WGS84/Elipsoid** (latitude, longitude, altitude)
- **UTM40S/Orthometric** (easting, northing, altitude)

Includes geoid correction for accurate altitude transformation.

---

## ⚙️ Features
✅ Convert coordinates between systems  
✅ Adjust altitude using geoid height from `.tif` file  
✅ Lightweight HTML+JS frontend and Python (Flask) backend

---

## 🚀 Quick Start

1️⃣ Place the geoid file (`us_nga_egm84_30.tif`) in the project folder.

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Run the backend:
```bash
python app.py
```

4️⃣ Open `index.html` in your browser.

---

## 📦 Project Structure
```
/ (root)
 ├── app.py
 ├── index.html
 ├── us_nga_egm84_30.tif
 ├── requirements.txt
 └── .gitignore
```

---

## 📌 Notes
- Make sure Flask runs locally or adjust the frontend API URL.
- `.gitignore` excludes cache, compiled files, and large binary files.

---

## 🧭 License
MIT – feel free to use, modify, and share.

⭐ If you like this project, consider giving it a star!
