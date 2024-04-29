# PDF Signature and Date Inserter

![Logo](catSign.jpeg)


## Overview
This Python script allows you to easily add a signature image and current date to specified pages of a PDF document. It provides a convenient way to sign PDF files electronically and add the date alongside the signature.

## Features
- Inserts a signature image onto specified pages of a PDF document.
- Adds the current date below the signature image.
- Supports specifying the position of the signature and date on the page.
- Works with both single-page and multi-page PDF files.

## Usage
### Running Locally with Python
1. Install the required dependencies by running:
   ```
   pip install PyMuPDF pillow
   ```

2. Run the script using the following command format:
   ```
   python script.py <pdf_path> <signature_image_path> <output_path> [<signature_x> <signature_y> [<date_x> <date_y>]] <page_numbers>
   ```

   - `<pdf_path>`: Path to the input PDF file.
   - `<signature_image_path>`: Path to the signature image file.
   - `<output_path>`: Path to save the modified PDF file.
   - `<signature_x>` and `<signature_y>`: Optional. X and Y coordinates to place the signature image on the page.
   - `<date_x>` and `<date_y>`: Optional. X and Y coordinates to place the date string on the page.
   - `<page_numbers>`: Comma-separated list of page numbers or ranges (e.g., "0,1,2" or "0-3") to apply changes. If omitted, changes will be applied to all pages.

### Running Inside a Docker Container
1. Build the Docker image by running:
   ```
   docker build -t pdf-signature-date .
   ```

2. Run the script inside a Docker container using the following command format:
   ```
   docker run --rm \
       -v $(pwd)/example.pdf:/app/example.pdf \
       -v $(pwd)/signature.png:/app/signature.png \
       -v $(pwd)/output.pdf:/app/output.pdf \
       pdf-signature-date \
       /app/example.pdf /app/signature.png /app/output.pdf 100 100 200 200 0,1,2
   ```

   - Replace `example.pdf` and `signature.png` with your actual file names.
   - After execution, the modified PDF will be available as `output.pdf` in the current directory.

## Why Use This Script?
- **Efficiency**: Quickly sign multiple pages of a PDF file with a signature image and date.
- **Customization**: Specify the position of the signature and date on each page.
- **Automation**: Easily integrate this script into your workflow or scripts for automated document signing tasks.
- **Flexibility**: Supports both single-page and multi-page PDF files, as well as selective page modification.

