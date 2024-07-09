# House Price Prediction

Proyek ini bertujuan untuk memprediksi harga rumah di tiga wilayah utama Jabodetabek: Jakarta, Depok, dan Tangerang. Model prediksi dibuat menggunakan Regresi Linear dan diimplementasikan ke dalam API menggunakan Flask.

## Dataset

Dataset ini terdiri dari beberapa fitur berikut:
- `Location`: Lokasi rumah (Jakarta, Depok, Tangerang)
- `Land Size`: Luas tanah dalam meter persegi
- `Building Size`: Luas bangunan dalam meter persegi
- `Num Rooms`: Jumlah kamar
- `Num Floors`: Jumlah lantai
- `Price ($)`: Harga rumah dalam dolar

## Pembuatan Dataset Sintetis

```python
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
locations = ['Jakarta', 'Tangerang', 'Depok']
land_size = np.random.randint(50, 200, 10000)  # in square meters
building_size = np.random.randint(50, 200, 10000)  # in square meters
num_rooms = np.random.randint(2, 10, 10000)
num_floors = np.random.randint(1, 4, 10000)
location = np.random.choice(locations, 10000)

# Encode locations as numerical values
location_dict = {'Jakarta': 0, 'Tangerang': 1, 'Depok': 2}
location_encoded = [location_dict[loc] for loc in location]

# Adjust building_size to be not larger than land_size with a gap
gap = 12
building_size = np.where(building_size >= land_size, land_size - gap, building_size)

# Generate house prices
price = (land_size * 5000) + (building_size * 10000) + (num_rooms * 100000) + (num_floors * 50000) + (np.array(location_encoded) * 100000) + np.random.randint(0, 100000, 10000)

# Create DataFrame
df = pd.DataFrame({
    'Location': location,
    'Land Size': land_size,
    'Building Size': building_size,
    'Num Rooms': num_rooms,
    'Num Floors': num_floors,
    'Price ($)': price
})

# Map locations to numerical values
df['Location'] = df['Location'].map(location_dict)
