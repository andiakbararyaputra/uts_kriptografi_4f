# 🔐 AES File Encryption — Implementasi AES-256-CBC dengan Python

> Tugas 2 Mata Kuliah **Kriptografi**  
> Program Studi Informatika — **Universitas Muhammadiyah Makassar**

---

## 📋 Identitas

| | |
|---|---|
| **Nama** | Andi Akbar Arya Putra |
| **NIM** | 105841117924 |
| **No. Urut** | 3 |
| **Kelas** | 4F |
| **Mata Kuliah** | Kriptografi |
| **Universitas** | Universitas Muhammadiyah Makassar |

---

## 📖 Deskripsi

Program enkripsi dan dekripsi file teks (`.txt`) menggunakan algoritma **AES-256-CBC** (Advanced Encryption Standard) dengan library `pycryptodome`. Program menerima password dari pengguna, menurunkannya menjadi kunci 256-bit menggunakan SHA-256, lalu mengenkripsi/mendekripsi file secara biner.

---

## ⚙️ Cara Kerja AES

**AES (Advanced Encryption Standard)** adalah algoritma block cipher simetrik yang bekerja pada blok 128-bit. Setiap putaran enkripsi terdiri dari 4 operasi:

1. **SubBytes** — Substitusi setiap byte menggunakan tabel S-Box
2. **ShiftRows** — Pergeseran baris secara sirkular
3. **MixColumns** — Pencampuran kolom menggunakan Galois Field GF(2⁸)
4. **AddRoundKey** — XOR blok data dengan subkunci putaran

### Mode CBC (Cipher Block Chaining)

Setiap blok plaintext di-XOR dengan blok ciphertext sebelumnya sebelum dienkripsi. Blok pertama menggunakan **IV (Initialization Vector)** yang dibangkitkan secara acak.

```
Plaintext[i] XOR Ciphertext[i-1] → AES Encrypt → Ciphertext[i]
```

IV disimpan di 16 byte pertama file output sehingga bisa digunakan kembali saat dekripsi.

---

## 🛠️ Requirements

- Python 3.x
- [pycryptodome](https://pypi.org/project/pycryptodome/)

Install dependency:

```bash
pip install pycryptodome
```

---

## 🚀 Cara Penggunaan

### 1. Clone repository

```bash
git clone https://github.com/username/aes-file-encryption.git
cd aes-file-encryption
```

### 2. Jalankan program

```bash
python aes_enkripsi.py
```

Program akan otomatis:
- Membuat file contoh `sample.txt`
- Mengenkripsinya menjadi `sample_encrypted.enc`
- Mendekripsinya kembali menjadi `sample_decrypted.txt`
- Menampilkan perbandingan isi file sebelum dan sesudah enkripsi

---

## 📂 Struktur File

```
aes-file-encryption/
├── aes_enkripsi.py          # Source code utama
├── sample.txt               # File teks asli (dibuat saat program dijalankan)
├── sample_encrypted.enc     # File hasil enkripsi
├── sample_decrypted.txt     # File hasil dekripsi
└── README.md
```

---

## 📊 Contoh Output

```
=======================================================
  IMPLEMENTASI AES FILE ENCRYPTION  
=======================================================

[1] ENKRIPSI FILE
  File asli       : sample.txt
  File terenkripsi: sample_encrypted.enc
  Ukuran plaintext : 131 byte
  Ukuran ciphertext: 160 byte
  IV  (hex) : 771bbe15ecc5d20bbcdaacbc872b03c5
  Key (hex) : db9a5d5197ab18876ccc4ef4078b597d...

  Isi file SEBELUM enkripsi:
  Ini adalah file contoh untuk enkripsi AES.
  Nama   : Andi Akbar Arya Putra
  ...

  Isi file SETELAH enkripsi (hex dump):
  771bbe15ecc5d20bbcdaacbc872b03c5866311041ee844e2...

[2] DEKRIPSI FILE
  Hasil Dekripsi : Andiakbar121204
  Verifikasi file: BERHASIL ✓
=======================================================
```

---

## 🔑 Penjelasan Teknis

| Komponen | Detail |
|---|---|
| Algoritma | AES (Advanced Encryption Standard) |
| Mode | CBC (Cipher Block Chaining) |
| Panjang Kunci | 256-bit |
| Panjang Blok | 128-bit |
| IV | 16 byte acak (disimpan di awal file) |
| Padding | PKCS7 |
| Derivasi Kunci | SHA-256 dari password |
| Library | pycryptodome |

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan tugas akademik mata kuliah Kriptografi di Universitas Muhammadiyah Makassar.
