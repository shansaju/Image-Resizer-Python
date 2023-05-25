from PIL import Image
import os

folder_path = r"D:\Ras\Dataset\nonbio"
# Replace with the actual path to your folder
sizes = [(640, 480)]  # List of desired new sizes of the image
prefix = "nonbiodata"  # Replace with the desired prefix for the renamed files


for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):  # Check for image file extension
        # Open the image file
        img = Image.open(os.path.join(folder_path, filename))

        # Resize the image to each of the sizes
        for size in sizes:
            img_resized = img.resize(size)
            if img_resized.mode == "RGBA" or img_resized.mode == "P":
                img_resized = img_resized.convert("RGB")

            # Construct the new file name with custom prefix and size information
            new_filename = f"{prefix}_resized_{size[0]}x{size[1]}_{filename}"
            new_filename = os.path.splitext(new_filename)[0] + os.path.splitext(filename)[1]

            # Save the resized image with the new file name
            img_resized.save(os.path.join(folder_path, new_filename))

print("All images resized successfully and renamed with custom prefix!")
