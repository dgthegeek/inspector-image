# Steganography and Metadata Extraction Tool

## Description

This program is designed to extract metadata from images and reveal hidden information using steganography techniques. It demonstrates basic image recognition approaches and the concept of steganography.

## What is Steganography?

Steganography is the practice of concealing information within other non-secret data or files. In the context of digital images, it involves hiding data within the image file in ways that are not immediately apparent. This can include embedding text in the least significant bits of pixel data or hiding information in metadata fields.

## How the Program Works

The program uses two main functionalities:

1. Metadata Extraction (-map option):
   - Uses the `exifread` library to read EXIF metadata from the image.
   - Extracts and displays GPS coordinates if available.

2. Steganography Detection (-steg option):
   - Searches for hidden PGP keys in the image.
   - Checks both metadata and image content for the PGP key.

## Usage

To use the program, follow these steps:

1. Ensure you have Python installed on your system.
2. Install required libraries:
   ```
   pip install Pillow exifread
   ```
3. Run the program with one of the following commands:

   For metadata extraction:
   ```
   python inspector_image.py -map path/to/image.jpeg
   ```

   For steganography detection:
   ```
   python inspector_image.py -steg path/to/image.jpeg
   ```

## Example Output

```
$ python inspector_image.py -map image.jpeg
Lat/Lon: (32.0) / (34.0)

$ python inspector_image.py -steg image.jpeg
-----BEGIN PGP PUBLIC KEY BLOCK-----
[pgp key content]
-----END PGP PUBLIC KEY BLOCK-----
```

## Notes

- This tool is for educational purposes only.
- Always ensure you have permission before analyzing images that are not your own.
- The effectiveness of steganography detection may vary depending on the methods used to hide the information.