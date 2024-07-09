from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Muat model yang sudah dilatih
model = joblib.load('linear_regression_model.pkl')

# Mapping lokasi dari string ke nilai numerik
location_dict = {'Jakarta': 0, 'Tangerang': 1, 'Depok': 2}

@app.route('/predict', methods=['POST'])
def predict():
    # Mendapatkan data dari request
    data = request.get_json()
    
    # Ekstrak fitur dari data
    location_str = data['Location']
    location = location_dict.get(location_str, -1)  # Default ke -1 jika lokasi tidak ditemukan
    
    if location == -1:
        return jsonify({'error': 'Invalid Location'}), 400
    
    land_size = data['Land Size']
    building_size = data['Building Size']
    num_rooms = data['Num Rooms']
    num_floors = data['Num Floors']
    
    # Buat array fitur
    features = np.array([[location, land_size, building_size, num_rooms, num_floors]])
    
    # Buat prediksi
    prediction = model.predict(features)
    
    # Mengembalikan hasil prediksi sebagai JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
