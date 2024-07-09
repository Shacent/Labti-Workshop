# House Price Prediction

Shacent mengalami kesulitan dalam memprediksi harga rumah di tiga daerah utama Jabodetabek: Jakarta, Depok, dan Tangerang. Untuk membantu Shacent, kami akan membuat aplikasi yang mampu memprediksi harga rumah berdasarkan beberapa fitur input seperti lokasi, luas tanah, luas bangunan, banyaknya ruangan, dan banyaknya lantai.
Proyek ini bertujuan untuk memprediksi harga rumah di tiga wilayah utama Jabodetabek: Jakarta, Depok, dan Tangerang. Model prediksi dibuat menggunakan Regresi Linear dan diimplementasikan ke dalam API menggunakan Flask.

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
