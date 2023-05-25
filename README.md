# Image-Resizer-Python

This Python script allows you to resize images with different heights and widths. It provides the flexibility to add multiple sizes for resizing. Currently, one size is added, and you can add more sizes by modifying the `sizes` list variable like this: `sizes = [(640, 480), (120, 120)]`.

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library) module

## Installation

1. Clone this repository or download the `image_resizer.py` file.
2. Install the required dependencies by running the following command:
   ```shell
   pip install Pillow
   ```

## Usage

1. Open the `image_resizer.py` file in a text editor.
2. Modify the `folder_path` variable to the actual path of the folder containing the images you want to resize.
3. Adjust the `sizes` list to specify the desired new sizes of the images. You can add as many sizes as needed.
4. Optionally, update the `prefix` variable to set a custom prefix for the renamed files.
5. Optionally, create a new variable called `destination_folder` and set it to the desired destination folder path. You can change the folder path in the for loop to use this variable.
6. Save the changes.

7. Run the script by executing the following command:
   ```shell
   python image_resizer.py
   ```

   The script will iterate through all the image files in the specified folder with the extensions `.jpg`, `.png`, and `.jpeg`. It will resize each image to the specified sizes and save them with the new file names, incorporating the custom prefix and size information.

8. After the script finishes, you will see the message `All images resized successfully and renamed with custom prefix!` indicating that the resizing and renaming process is complete.

## Customization Options

- **Adding Sizes:** You can add additional sizes for resizing by modifying the `sizes` list variable in the script.
- **Changing Destination Folder:** Create a new variable called `destination_folder` and set it to the desired folder path. Modify the for loop to use this variable as the destination folder path.
- **Custom Names:** You can add custom names to the resized images by updating the `prefix` variable in the script.

## License

This project is licensed under the [MIT License](LICENSE).
