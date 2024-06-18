import pandas as pd
import matplotlib.pyplot as plt

# Membaca dataset
data = pd.read_csv('restauran_cepat_saji.csv')

# Menampilkan lima baris pertama dataset
print("Lima baris pertama dataset:")
print(data.head())

# Menampilkan informasi umum tentang dataset
print("\nInformasi umum tentang dataset:")
print(data.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data.describe())

# Menghitung total pendapatan untuk setiap item menu
total_pendapatan_per_item = data.groupby('menu_item')['harga_total'].sum()
print("\nTotal pendapatan untuk setiap item menu:")
print(total_pendapatan_per_item)

# Membuat plot jumlah pesanan yang diberikan per item menu
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
jumlah_pesanan_per_item = data['menu_item'].value_counts()
jumlah_pesanan_per_item.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Jumlah Pesanan per Item Menu')
plt.xlabel('Item Menu')
plt.ylabel('Jumlah')

# Membuat scatter plot hubungan antara jumlah pesanan dan harga total
plt.subplot(2, 2, 2)
plt.scatter(data['jumlah_pesanan'], data['harga_total'], color='blue', alpha=0.5)
plt.title('Scatter Plot Jumlah Pesanan vs Harga Total')
plt.xlabel('Jumlah Pesanan')
plt.ylabel('Harga Total (IDR)')

# Membuat histogram distribusi harga total
plt.subplot(2, 2, 3)
plt.hist(data['harga_total'].dropna(), bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram Distribusi Harga Total')
plt.xlabel('Harga Total (IDR)')
plt.ylabel('Frekuensi')

# Membuat box plot harga total
plt.subplot(2, 2, 4)
plt.boxplot(data['harga_total'].dropna())
plt.title('Box Plot Harga Total')
plt.ylabel('Harga Total (IDR)')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()

# Menghitung rata-rata jumlah pesanan per pelanggan
rata_rata_pesanan_per_pelanggan = data.groupby('pelanggan')['jumlah_pesanan'].mean()
print("\nRata-rata jumlah pesanan per pelanggan:")
print(rata_rata_pesanan_per_pelanggan)
