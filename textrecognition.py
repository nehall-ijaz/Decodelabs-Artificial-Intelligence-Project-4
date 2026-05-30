# ==========================================
# AI PROJECT 4 - TEXT RECOGNITION SYSTEM
# DecodeLabs Internship Project
# ==========================================

import os
from PIL import Image
import pytesseract

# Optional:
# Uncomment and update path if Tesseract is not in system PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    """
    Extract text from an image using OCR.
    """

    if not os.path.exists(image_path):
        print("Error: Image file not found.")
        return None

    try:
        image = Image.open(image_path)

        extracted_text = pytesseract.image_to_string(image)

        return extracted_text

    except Exception as e:
        print(f"Error: {e}")
        return None


def save_text(text, output_file="recognized_text.txt"):
    """
    Save extracted text to a text file.
    """

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"\nText saved successfully to '{output_file}'")


def main():

    print("=" * 50)
    print("      AI TEXT RECOGNITION SYSTEM")
    print("=" * 50)

    image_path = input(
        "\nEnter image path (example: sample.jpg): "
    )

    text = extract_text(image_path)

    if text:

        print("\nExtracted Text:")
        print("-" * 50)
        print(text)

        save_text(text)

    else:
        print("No text detected.")


if __name__ == "__main__":
    main()