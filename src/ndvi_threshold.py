# code for NDVI index and percentage above 0.6
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to calculate NDVI
def calculate_ndvi(nir, red):
    # Avoid division by zero and invalid values
    ndvi = np.where((nir + red) == 0, 0, (nir - red) / (nir + red))
    return ndvi

# Load the stitched TIFF image
image_path = 'image.tif'

# Open the image using Pillow
image = Image.open(image_path)

# Assuming the image has multiple bands and is in 'RGBA' format or similar
# Convert the image to numpy array
image_array = np.array(image)

# Check the shape of the image to understand the bands
print(f"Image shape: {image_array.shape}")

# Assuming the NIR band is the fourth band and the Red band is the first band
# Adjust indices based on your specific image
nir_band = image_array[:, :, 3].astype(np.float32)
red_band = image_array[:, :, 0].astype(np.float32)

# Calculate NDVI
ndvi = calculate_ndvi(nir_band, red_band)
total_pixels = ndvi.size
above_0_6 = np.sum(ndvi > 0.6)
below_0_6 = np.sum(ndvi <= 0.6)

percent_above_0_6 = (above_0_6 / total_pixels) * 100
percent_below_0_6 = (below_0_6 / total_pixels) * 100

print(f"Percentage of NDVI values above 0.7: {percent_above_0_6:.2f}%")
print(f"Percentage of NDVI values below or equal to 0.7: {percent_below_0_6:.2f}%")
print('The average NDVI index of the image is ',(percent_above_0_6 + percent_below_0_6)/2)


# Display the NDVI result
plt.figure(figsize=(10, 10))
plt.title("NDVI Index")
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI value')
plt.show()
