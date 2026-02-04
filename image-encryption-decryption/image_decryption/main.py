import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# -----------------------------
# Load Original Image (for shape)
# -----------------------------
original = cv2.imread(r"D:\My Projects\image-encryption-decryption\image_encryption\input.jpg")

if original is None:
    print("Original image not found!")
    exit()

# -----------------------------
# Enter SAME Key used in Encryption
# -----------------------------
key = b'your_16_byte_key'   # replace with your real key
with open("secret.key", "rb") as f:
    key = f.read()


# -----------------------------
# Read Encrypted File
# -----------------------------
with open("encrypted_image.bin", "rb") as f:
    iv = f.read(16)
    encrypted_data = f.read()

# -----------------------------
# Decrypt
# -----------------------------
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_bytes = unpad(cipher.decrypt(encrypted_data), AES.block_size)

# -----------------------------
# Convert Bytes to Image
# -----------------------------
decrypted_image = np.frombuffer(decrypted_bytes, dtype=np.uint8)
decrypted_image = decrypted_image.reshape(original.shape)

cv2.imwrite("decrypted_output.jpg", decrypted_image)

print("Decryption Successful!")
