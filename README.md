# Image Editing Script

This repository contains a Python script that automates the process of editing images using the Python Imaging Library (PIL), specifically the `Pillow` module. The script applies a sharpening filter, converts images to grayscale, and saves the edited images to a specified output folder.

## Prerequisites

Before using the script, ensure you have the following installed on your system:

1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **Pillow library**: Install the Pillow library by running:

   ```bash
   pip install pillow
   ```

## Script Overview

The script performs the following steps:

1. Iterates through all image files in the `./imgs` directory.
2. Opens each image file using Pillow.
3. Applies a sharpening filter to the image.
4. Converts the image to grayscale.
5. Saves the edited image in the `./editedimgs` directory with a new filename format: `original_filename_edited.jpg`.
6. 
## Usage

1. Place all the images you want to edit into the `./imgs` directory.
2. Run the script:

   ```bash
   python photoeditor.py
   ```

3. The edited images will be saved in the `./editedimgs` directory.

## Notes

- Ensure the `./imgs` and `./editedimgs` directories exist before running the script. If they do not exist, create them manually or modify the script to handle directory creation.
- The script processes all files in the `./imgs` directory. Ensure that only valid image files are placed there to avoid errors.

## Customization

You can modify the script to apply different filters or transformations. For example:

- To adjust brightness or contrast, use the `ImageEnhance` module.
- To resize images, use the `resize` method.
- To add other effects, explore the `ImageFilter` module.

Refer to the [Pillow documentation](https://pillow.readthedocs.io/en/stable/) for more details.

## License

This script is open-source and available under the MIT License. Feel free to use and modify it as needed.

