import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# FUNGSI ENKRIPSI FILE (AES-CBC)
def encrypt_file(input_path: str, output_path: str, password: str) -> dict:
    """
    Mengenkripsi file menggunakan AES-256-CBC.
    Menyisipkan IV (16 byte) di awal file terenkripsi.
    """
    # Turunkan kunci 256-bit dari password menggunakan SHA-256
    key = hashlib.sha256(password.encode()).digest()

    # Bangkitkan IV acak (16 byte)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_path, "rb") as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_path, "wb") as f:
        f.write(iv + ciphertext)          # Simpan IV diikuti ciphertext

    return {
        "plaintext_size": len(plaintext),
        "ciphertext_size": len(iv + ciphertext),
        "iv_hex": iv.hex(),
        "key_hex": key.hex(),
    }

# FUNGSI DEKRIPSI FILE (AES-CBC)
def decrypt_file(input_path: str, output_path: str, password: str) -> dict:
    """
    Mendekripsi file hasil enkripsi AES-256-CBC.
    Membaca IV dari 16 byte pertama file.
    """
    key = hashlib.sha256(password.encode()).digest()

    with open(input_path, "rb") as f:
        data = f.read()

    iv         = data[:16]           # Ambil IV dari 16 byte pertama
    ciphertext = data[16:]           # Sisa adalah ciphertext

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_path, "wb") as f:
        f.write(plaintext)

    return {
        "ciphertext_size": len(data),
        "plaintext_size":  len(plaintext),
        "iv_hex": iv.hex(),
    }

# DEMO / MAIN
if __name__ == "__main__":
    # Buat file teks contoh
    sample_path   = "contoh.txt"
    encrypted_path = "contoh.enc"
    decrypted_path = "contoh.txt"

    PASSWORD = "AndiAkbar105841117924"

    with open(sample_path, "w") as f:
        f.write(
            "Ini adalah file contoh untuk enkripsi AES.\n"
            "Nama   : Andi Akbar Arya Putra\n"
            "NIM    : 105841117924\n"
            "Kelas  : 4F\n"
            "Algoritma: AES-256-CBC\n"
        )

    print("=" * 55)
    print("  IMPLEMENTASI AES FILE ENCRYPTION  ")
    print("=" * 55)

    # ─── Enkripsi ───
    print("\n[1] ENKRIPSI FILE")
    enc_info = encrypt_file(sample_path, encrypted_path, PASSWORD)
    print(f"  File asli       : {sample_path}")
    print(f"  File terenkripsi: {encrypted_path}")
    print(f"  Ukuran plaintext : {enc_info['plaintext_size']} byte")
    print(f"  Ukuran ciphertext: {enc_info['ciphertext_size']} byte")
    print(f"  IV  (hex) : {enc_info['iv_hex']}")
    print(f"  Key (hex) : {enc_info['key_hex']}")

    print("\n  Isi file SEBELUM enkripsi:")
    with open(sample_path, "r") as f:
        print("  " + f.read().replace("\n", "\n  ").rstrip())

    print("\n  Isi file SETELAH enkripsi (hex dump, 64 byte pertama):")
    with open(encrypted_path, "rb") as f:
        raw = f.read(64)
    print("  " + raw.hex())

    # ─── Dekripsi ───
    print("\n[2] DEKRIPSI FILE")
    dec_info = decrypt_file(encrypted_path, decrypted_path, PASSWORD)
    print(f"  File terenkripsi : {encrypted_path}")
    print(f"  File hasil dekripsi: {decrypted_path}")
    print(f"  Ukuran ciphertext: {dec_info['ciphertext_size']} byte")
    print(f"  Ukuran plaintext : {dec_info['plaintext_size']} byte")

    print("\n  Isi file SETELAH dekripsi:")
    with open(decrypted_path, "r") as f:
        print("  " + f.read().replace("\n", "\n  ").rstrip())

    # Verifikasi
    with open(sample_path, "rb") as f1, open(decrypted_path, "rb") as f2:
        match = f1.read() == f2.read()
    print(f"\n  Verifikasi file: {'BERHASIL ✓' if match else 'GAGAL ✗'}")
    print("=" * 55)
