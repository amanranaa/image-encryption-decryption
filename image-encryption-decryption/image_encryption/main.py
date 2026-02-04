import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# -----------------------------
# Step 1: Load the Image
# -----------------------------
image = cv2.imread(r"D:\My Projects\image-encryption-decryption\image_encryption\input.jpg")
image_bytes = image.tobytes()

# -----------------------------
# Step 2: Generate AES Key
# -----------------------------
key = get_random_bytes(16)  # 16 bytes = 128-bit key
with open("secret.key", "wb") as f:
    f.write(key)
cipher = AES.new(key, AES.MODE_CBC)

# -----------------------------
# Step 3: Encrypt the Image
# -----------------------------
ciphertext = cipher.encrypt(pad(image_bytes, AES.block_size))

# Save encrypted data
with open("encrypted_image.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(ciphertext)

print("Encryption Completed!")

# -----------------------------
# Step 4: Decryption Process
# -----------------------------
with open("encrypted_image.bin", "rb") as f:
    iv = f.read(16)
    encrypted_data = f.read()

cipher_dec = AES.new(key, AES.MODE_CBC, iv=iv)
decrypted_bytes = unpad(cipher_dec.decrypt(encrypted_data), AES.block_size)

# Convert bytes back to image
decrypted_image = np.frombuffer(decrypted_bytes, dtype=np.uint8).reshape(image.shape)

# Save decrypted image
cv2.imwrite("decrypted_output.jpg", decrypted_image)

print("Decryption Completed!")
