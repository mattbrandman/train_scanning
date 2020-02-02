#!/usr/bin/env python3

from PIL import Image
from pyzbar.pyzbar import decode
import pytesseract

def main():
    """ Main entry point of the app """
    print(pytesseract.image_to_string(Image.open('/mnt/c/Users/Matt Brandman/Pictures/Test.jpg')))
    print(decode((Image.open('/mnt/c/Users/Matt Brandman/Pictures/Test.jpg'))))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()