import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
import numpy as np

# Membaca dataset
data = pd.read_csv('restauran_cepat_saji.csv')

# Menampilkan lima baris pertama dataset
print("Lima baris pertama dataset:")
print(data.head())

# Menghitung korelasi antara jumlah pesanan dan harga total
correlation, p_value = pearsonr(data['jumlah_pesanan'], data['harga_total'])
print(f"\nKorelasi antara jumlah pesanan dan harga total: {correlation}")
print(f"P-value: {p_value}")

# Visualisasi scatter plot dengan garis regresi menggunakan seaborn
plt.figure(figsize=(10, 6))
sns.regplot(x='jumlah_pesanan', y='harga_total', data=data, scatter_kws={'color':'blue', 'alpha':0.5}, line_kws={'color':'red'})
plt.title('Scatter Plot Jumlah Pesanan vs Harga Total dengan Garis Regresi')
plt.xlabel('Jumlah Pesanan')
plt.ylabel('Harga Total (IDR)')
plt.grid(True)
plt.show()

# Membuat model regresi linier menggunakan sklearn
X = data[['jumlah_pesanan']]
y = data['harga_total']

model = LinearRegression()
model.fit(X, y)

# Koefisien dan Intersep
print(f"\nKoefisien regresi linier: {model.coef_[0]}")
print(f"Intersep regresi linier: {model.intercept_}")

# Prediksi harga total berdasarkan jumlah pesanan
data['predicted_harga_total'] = model.predict(X)

# Visualisasi scatter plot dengan garis regresi menggunakan matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(data['jumlah_pesanan'], data['harga_total'], color='blue', alpha=0.5, label='Actual Data')
plt.plot(data['jumlah_pesanan'], data['predicted_harga_total'], color='red', label='Regression Line')
plt.title('Scatter Plot Jumlah Pesanan vs Harga Total dengan Garis Regresi (Manual)')
plt.xlabel('Jumlah Pesanan')
plt.ylabel('Harga Total (IDR)')
plt.legend()
plt.grid(True)
plt.show()
