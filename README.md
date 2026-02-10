# Submission Akhir Belajar Machine Learning by DICODING

**Kreator:** Achmad_Rahman_M  
**Dataset yang digunakan:** bank_transactions_data_edited

# Tujuan Project

Tujuan dari project ini adalah untuk mengelompokkan nasabah berdasarkan pola transaksi keuangan mereka menggunakan algoritma K-Means Clustering, kemudian membangun model klasifikasi (Decision Tree) yang mampu memprediksi cluster nasabah baru berdasarkan fitur-fitur seperti jumlah transaksi, saldo akun, durasi transaksi, dan lainnya. Model klasifikasi berhasil mencapai akurasi 99.59% dalam memprediksi cluster nasabah. Project ini berhasil diselesaikan dan diterima oleh tim reviewer Dicoding, serta memperoleh sertifikat resmi sebagai bukti kelulusan.

# 📦 Packages & Instalasi

## Requirement Sistem

- **Python:** 3.8 atau lebih tinggi
- **Operating System:** Windows, macOS, atau Linux

## Daftar Package yang Digunakan

| Package        | Versi  | Fungsi                            |
| -------------- | ------ | --------------------------------- |
| `pandas`       | 3.0.0  | Data manipulation dan analysis    |
| `numpy`        | 2.4.2  | Numerical computing               |
| `matplotlib`   | 3.10.8 | Data visualization                |
| `seaborn`      | 0.13.2 | Statistical data visualization    |
| `scikit-learn` | 1.5.2  | Machine learning library          |
| `yellowbrick`  | 1.5    | ML visualization                  |
| `joblib`       | 1.5.3  | Model serialization & persistence |
| `setuptools`   | 82.0.0 | Python packaging utilities        |

## Cara Instalasi

### 1. Setup Virtual Environment (Recommended)

**Untuk Windows:**

```bash
# Buat virtual environment
python -m venv .venv

# Aktivasi virtual environment
.venv\Scripts\activate
```

**Untuk macOS/Linux:**

```bash
# Buat virtual environment
python3 -m venv .venv

# Aktivasi virtual environment
source .venv/bin/activate
```

### 2. Install Semua Package

**Opsi A: Install secara individual**

```bash
pip install pandas==3.0.0
pip install numpy==2.4.2
pip install matplotlib==3.10.8
pip install seaborn==0.13.2
pip install scikit-learn==1.5.2
pip install yellowbrick==1.5
pip install joblib==1.5.3
pip install setuptools==82.0.0
```

**Opsi B: Install dengan satu command**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn==1.5.2 yellowbrick joblib setuptools
```

**Opsi C: Dari requirements.txt (jika tersedia)**

```bash
pip install -r requirements.txt
```

### 3. Verifikasi Instalasi

Jalankan command berikut untuk memastikan semua package terinstall dengan baik:

```bash
python -c "import pandas; import numpy; import matplotlib; import seaborn; import sklearn; import yellowbrick; import joblib; print('✅ Semua package berhasil terinstall!')"
```

## Running the Project

### Untuk Jupyter Notebook:

```bash
# Install jupyter (kalau belum)
pip install jupyter

# Jalankan jupyter
jupyter notebook

# Buka file notebook:
# - [Clustering]_Submission_Akhir_BMLP_Achmad_Rahman_M.ipynb
# - [Klasifikasi]_Submission_Akhir_BMLP_Achmad_Rahman_M.ipynb
```

### Untuk VS Code:

```bash
# Install extension "Jupyter" di VS Code
# Buka file .ipynb
# Jalankan cells (Run All untuk menjalankan semua cell)
```

## Catatan Penting

- ⚠️ **scikit-learn versi 1.5.2** digunakan untuk kompatibilitas dengan yellowbrick
- ⚠️ Jika menggunakan Python 3.14+, pastikan setuptools terinstall untuk mengatasi error `distutils`
- ✅ Virtual environment sangat disarankan untuk menghindari conflict dengan package lain

## Troubleshooting

**Error: distutils not found**

```bash
pip install setuptools
```

**Error: yellowbrick compatibility**

```bash
# Uninstall scikit-learn versi lama
pip uninstall scikit-learn
# Install versi yang compatible
pip install scikit-learn==1.5.2
```

**Error: Module not found**

```bash
# Pastikan virtual environment sudah activated
# Reinstall packages
pip install -r requirements.txt
```

---

# Insight yang Dihasilkan dari Analisis Clustering (610 sampel - 4 kategori cluster)

## Cluster 0: Pengguna Moderat dengan Aktivitas Terukur (610 sampel)

- **TransactionAmount** : 0.1479 → Jumlah transaksi rendah hingga sedang
- **TransactionDate** : 943.7 → Periode transaksi pertengahan (sudah cukup lama)
- **TransactionDuration** : 0.3741 → Durasi transaksi sedang
- **AccountBalance** : 0.3303 → Saldo akun menengah
- **LoginAttempts** : 0.0270 → Usaha login rendah
- **CustomerAge** : 0.4344 → Usia pengguna pertengahan

**Analisis:** Cluster ini mencakup pengguna dengan profil moderat yang memiliki aktivitas transaksi stabil namun tidak terlalu sering. Mereka memiliki saldo akun yang cukup dan jarang melakukan login ulang. Pengguna dalam segmen ini mungkin sudah memiliki kepercayaan terhadap layanan dan menggunakan sistem dengan percaya diri. Mereka cocok untuk program retensi dan edukasi produk tambahan.

## Cluster 1: Pengguna Aktif dengan Frekuensi Tinggi (604 sampel)

- **TransactionAmount** : 0.1670 → Jumlah transaksi tertinggi
- **TransactionDate** : 1577.1 → Periode transaksi cukup baru (pengguna aktif lebih lama)
- **TransactionDuration** : 0.3873 → Durasi transaksi sedang
- **AccountBalance** : 0.3302 → Saldo akun serupa dengan Cluster 0
- **LoginAttempts** : 0.0232 → Usaha login terendah
- **CustomerAge** : 0.4401 → Usia rata-rata sedikit lebih tinggi

**Analisis:** Pengguna cluster ini adalah segmen paling aktif dengan volume transaksi tertinggi. Meskipun usaha login mereka rendah, frekuensi transaksi mereka menunjukkan engagement yang tinggi. Mereka adalah pengguna setia yang telah beradaptasi dengan platform dan melakukan transaksi dengan lancar. Strategi terbaik adalah memberikan penawaran eksklusif berbasis transaksi dan program loyalitas untuk mempertahankan engagement mereka.

## Cluster 2: Pengguna Baru dengan Saldo Tinggi (599 sampel)

- **TransactionAmount** : 0.1516 → Jumlah transaksi sedang
- **TransactionDate** : 2204.2 → Periode transaksi paling baru (pengguna terbaru)
- **TransactionDuration** : 0.3816 → Durasi transaksi sedang
- **AccountBalance** : 0.3453 → Saldo akun tertinggi
- **LoginAttempts** : 0.0321 → Usaha login tertinggi
- **CustomerAge** : 0.4327 → Usia pengguna pertengahan

**Analisis:** Cluster ini berisi pengguna baru yang menunjukkan inisiatif tinggi dengan usaha login paling sering dan saldo akun tertinggi. Mereka merupakan early adopter yang enthusiastik terhadap platform digital banking. Saldo awal yang tinggi menunjukkan potensi nilai transaksi besar. Rekomendasi strategis adalah memberikan onboarding interaktif, fitur premium, program referral, dan promosi khusus untuk membangun loyalitas jangka panjang.

## Cluster 3: Pengguna Lama dan Loyal (607 sampel)

- **TransactionAmount** : 0.1531 → Jumlah transaksi sedang
- **TransactionDate** : 314.3 → Periode transaksi paling lama (pengguna paling veteran)
- **TransactionDuration** : 0.3657 → Durasi transaksi terendah
- **AccountBalance** : 0.3349 → Saldo akun tinggi
- **LoginAttempts** : 0.0367 → Usaha login tertinggi kedua
- **CustomerAge** : 0.4133 → Usia pengguna terendah

**Analisis:** Cluster ini merepresentasikan pengguna veteran terlama dengan pengalaman platform paling matang. Durasi transaksi mereka paling singkat menunjukkan efisiensi maksimal dalam menggunakan layanan. Usaha login tinggi menunjukkan engagement konsisten, dan mereka memiliki saldo akun yang stabil. Pengguna ini adalah aset berharga dengan potensi high lifetime value. Strategi terbaik adalah program loyalitas eksklusif, early access fitur baru, dedicated customer service, dan reward premium untuk mempertahankan kepuasan dan advocacy mereka.
