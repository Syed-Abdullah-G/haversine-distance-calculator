# 🌍 Haversine Calculator

A simple Python tool to calculate the great-circle distance between two points on the Earth using the **Haversine formula**.

## 📚 What is the Haversine Formula?

The Haversine formula determines the distance between two points on a sphere given their longitudes and latitudes. It is particularly useful for calculating distances on Earth assuming a spherical shape.

## 🧮 Formula

\[
a = \sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right)
\]
\[
c = 2 \cdot \text{atan2}\left(\sqrt{a}, \sqrt{1-a}\right)
\]
\[
\text{distance} = R \cdot c
\]

Where:
- \( \phi \) is latitude in radians,
- \( \lambda \) is longitude in radians,
- \( R \) is Earth's radius (mean = 6,371 km).

---

## 🚀 Features

- Accepts coordinates in degrees
- Returns distance in kilometers or miles
- Simple CLI interface
- Optional conversion to miles

---

## 🧰 Requirements

- Python 3.x

No external dependencies are required (uses only the standard library).

---

## 🛠️ Usage

### 🔧 Installation

Clone the repo:
```bash
git clone https://github.com/yourusername/haversine-calculator.git
cd haversine-calculator
