# image-encryption-decryption
# 🔐 Image Encryption using AES in Python

A cybersecurity project that demonstrates how digital images can be securely encrypted and decrypted using the Advanced Encryption Standard (AES) algorithm. The project ensures confidentiality of image data and prevents unauthorized access.

---

## 📖 Project Description

Image Encryption is the process of converting an image into an unreadable format using cryptographic techniques.  
Only users with the correct secret key can decrypt and view the original image.

This project:
- Encrypts an image using AES (128-bit key)
- Saves the encrypted data
- Decrypts the image back using the same key
- Demonstrates histogram analysis for security validation

---

## 🚀 Features

- AES-128 Encryption
- Secure key generation and storage
- Image encryption & decryption
- Histogram analysis
- Simple and easy-to-understand code

---

## 🛠️ Technologies Used

- Python  
- OpenCV  
- NumPy  
- PyCryptodome  
- Matplotlib  

---

## 📂 Project Structure
image-encryption-decryption/
│
├── image_encryption
   ├── main.py
   ├── input.jpg
├── image_decryption
   ├── main.py
├── histogram_analysis
   ├── histogram.py
   
├── encrypted_image.bin
├── decrypted_output.jpg
├── secret.key



---

## ⚙️ Installation

Install required libraries:

```bash
pip install opencv-python numpy pycryptodome matplotlib

