# 🌍 Haversine Calculator

A simple Python tool to calculate the great-circle distance between two points on the Earth using the **Haversine formula**.

---

## 📚 What is the Haversine Formula?

The Haversine formula determines the distance between two points on a sphere given their longitudes and latitudes. It's especially useful for calculating distances on Earth assuming it is a perfect sphere.

---

## 🧮 Formula

a = sin²(Δφ / 2) + cos(φ1) * cos(φ2) * sin²(Δλ / 2) c = 2 * atan2(√a, √(1 − a)) distance = R * c


Where:
- `φ` is latitude in radians  
- `λ` is longitude in radians  
- `Δφ` is the difference in latitude: `lat2 - lat1`  
- `Δλ` is the difference in longitude: `lon2 - lon1`  
- `R` is Earth's radius (mean radius = 6,371 km)

---

## 🚀 Features

- Accepts coordinates in degrees
- Returns distance in kilometers
- Simple command-line interface
- Lightweight (no external libraries)

---

## 🧰 Requirements

- Python 3.x

> ✅ No external dependencies required – uses only the Python standard library.

---

## 🛠️ Usage

### 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/haversine-calculator.git
cd haversine-calculator
