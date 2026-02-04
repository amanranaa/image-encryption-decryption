import cv2
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load Images
# -----------------------------
original = cv2.imread(r"D:\My Projects\image-encryption-decryption\image_encryption\input.jpg", 0)  # grayscale
decrypted = cv2.imread("decrypted_output.jpg", 0)

# Encrypted data visualization (optional)
encrypted = np.fromfile("encrypted_image.bin", dtype=np.uint8)

# -----------------------------
# Plot Histograms-
# -----------------------------
plt.figure(figsize=(12,5))

# Original Image Histogram
plt.subplot(1,3,1)
plt.hist(original.ravel(), bins=256)
plt.title("Original Image Histogram")

# Encrypted Image Histogram
plt.subplot(1,3,2)
plt.hist(encrypted, bins=256)
plt.title("Encrypted Image Histogram")

# Decrypted Image Histogram
plt.subplot(1,3,3)
plt.hist(decrypted.ravel(), bins=256)
plt.title("Decrypted Image Histogram")

plt.show()
