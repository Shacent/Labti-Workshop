# House Price Prediction

Shacent mengalami kesulitan dalam memprediksi harga rumah di tiga daerah utama Jabodetabek: Jakarta, Depok, dan Tangerang. Untuk membantu Shacent, kami akan membuat aplikasi yang mampu memprediksi harga rumah berdasarkan beberapa fitur input seperti lokasi, luas tanah, luas bangunan, banyaknya ruangan, dan banyaknya lantai.
Proyek ini bertujuan untuk memprediksi harga rumah di tiga wilayah utama Jabodetabek: Jakarta, Depok, dan Tangerang. Model prediksi dibuat menggunakan Regresi Linear dan diimplementasikan ke dalam API menggunakan Flask.

## Tujuan
Membuat model Linear Regression yang dapat memprediksi harga rumah dengan akurasi tinggi berdasarkan dataset, dengan fokus pada fitur-fitur yang relevan.

## Langkah-Langkah
1. **Persiapan Data**
   - Mengimpor pustaka yang diperlukan
   - Mengimpor datasets
   - Melakukan pembersihan data termasuk penanganan outlier, data kosong, dan duplikat

2. **Eksplorasi Data**
   - Menggunakan teknik visualisasi untuk memahami distribusi data
   - Menampilkan statistik deskriptif dari dataset

3. **Membangun Model**
   - Memisahkan dataset menjadi fitur dan target
   - Membagi data menjadi set latih dan uji
   - Melatih model Linear Regression
   - Mengevaluasi model menggunakan metrik seperti R-Squared (R²)

## Dataset

Dataset ini terdiri dari beberapa fitur berikut:
- `Location`: Lokasi rumah (Jakarta, Depok, Tangerang)
- `Land Size`: Luas tanah dalam meter persegi
- `Building Size`: Luas bangunan dalam meter persegi
- `Num Rooms`: Jumlah kamar
- `Num Floors`: Jumlah lantai
- `Price ($)`: Harga rumah dalam dolar

# Using the POST API

```JSON
{
    "Location": "Jakarta",
    "Land Size": 150,
    "Building Size": 100,
    "Num Rooms": 3,
    "Num Floors": 2
}
```
## Output 
```JSON
{
    "prediction": 2199640.180737771
}
```
