import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('path_to_your_image.jpg')

# Convert the image from BGR (OpenCV default) to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Extract the red and green channels
# Assume NIR is the red channel and RED is the green channel for demonstration purposes
nir_channel = image[:, :, 0]  # Red channel
red_channel = image[:, :, 1]  # Green channel

# Convert to float32 for precision
nir_channel = nir_channel.astype(np.float32)
red_channel = red_channel.astype(np.float32)

# Calculate NDVI
ndvi = (nir_channel - red_channel) / (nir_channel + red_channel + 1e-10)  # Add a small number to avoid division by zero

# Normalize NDVI to the range 0-1 for visualization purposes
ndvi_normalized = cv2.normalize(ndvi, None, 0, 1, cv2.NORM_MINMAX)

# Display the original image and the NDVI image
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('NDVI Image')
plt.imshow(ndvi_normalized, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.axis('off')

plt.tight_layout()
plt.show()

