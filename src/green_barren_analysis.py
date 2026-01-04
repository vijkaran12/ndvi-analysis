import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(image_path, scale_factor=0.5):
    # Load the image
    image = cv2.imread(image_path)
    original_height, original_width = image.shape[:2]

    # Resize the image to speed up processing
    image = cv2.resize(image, (int(original_width * scale_factor), int(original_height * scale_factor)))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range for green color in HSV
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Calculate the area of green and barren regions
    green_area = np.sum(mask > 0)
    total_area = mask.shape[0] * mask.shape[1]
    barren_area = total_area - green_area

    # Plot the original image
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Plot the green mask
    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Green Area Mask')
    plt.axis('off')

    # Plot the pie chart
    plt.subplot(1, 3, 3)
    labels = 'Green Area', 'Barren Area'
    sizes = [green_area, barren_area]
    colors = ['green', 'brown']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Green and Barren Areas')

    plt.tight_layout()
    plt.show()

    # Print areas for debugging
    print(f"Green Area: {green_area} pixels ({green_area / total_area * 100:.2f}%)")
    print(f"Barren Area: {barren_area} pixels ({barren_area / total_area * 100:.2f}%)")

## Example usage with different images
image_paths = ['drone_image1.jpg', 'drone_image2.jpg', 'drone_image3.jpg']
for image_path in image_paths:
    print(f"Processing {image_path}")
    process_image(image_path)

