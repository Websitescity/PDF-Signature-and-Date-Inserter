import sys
from typing import Optional, Tuple, List
import fitz
from PIL import Image
from datetime import datetime

def add_signature_and_date(pdf_path: str, signature_image_path: str, output_path: str,
                           signature_position: Optional[Tuple[int, int]] = None,
                           date_position: Optional[Tuple[int, int]] = None,
                           pages: Optional[List[int]] = None) -> None:
    """
    Add signature image and current date to specified pages of a PDF document.

    Args:
        pdf_path: Path to the input PDF file.
        signature_image_path: Path to the signature image file.
        output_path: Path to save the modified PDF file.
        signature_position: Optional. Position to place the signature image (x, y).
        date_position: Optional. Position to place the date string (x, y).
        pages: Optional. List of page numbers to apply changes. If None, applies to all pages.

    Returns:
        None
    """
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Open the image file and resize it if needed
    signature_img = Image.open(signature_image_path)
    signature_img_width, signature_img_height = signature_img.size

    # Calculate the date string
    current_date = datetime.now().strftime("%Y-%m-%d")

    # If no pages specified, apply changes to all pages
    if pages is None:
        pages = range(len(pdf_document))

    for page_num in pages:
        if page_num < 0 or page_num >= len(pdf_document):
            print(f"Page number {page_num} is out of range. Skipping.")
            continue

        page = pdf_document[page_num]
        # Load the image onto the PDF page if signature position is provided
        if signature_position:
            page.insert_image(signature_position[0], signature_position[1], signature_image_path)
        # Add date string if date position is provided
        if date_position:
            page.insert_text((date_position[0], date_position[1]), current_date, fontsize=12)

    # Save the modified PDF to a new file
    pdf_document.save(output_path)
    pdf_document.close()

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py <pdf_path> <signature_image_path> <output_path> [<signature_x> <signature_y> [<date_x> <date_y>]] <page_numbers>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    signature_image_path = sys.argv[2]
    output_path = sys.argv[3]
    signature_position = None if len(sys.argv) < 7 else (int(sys.argv[4]), int(sys.argv[5]))
    date_position = None if len(sys.argv) < 9 else (int(sys.argv[6]), int(sys.argv[7]))
    page_numbers = [int(page_num) for page_num in sys.argv[-1].split(",")]

    add_signature_and_date(pdf_path, signature_image_path, output_path, signature_position, date_position, page_numbers)
