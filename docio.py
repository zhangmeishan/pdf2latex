## This file is for PDF io
## either

import cv2 as cv
from pypdf import PdfReader
from pdf2image import convert_from_path
from PIL import Image
import base64


im_pages = convert_from_path("input/test.pdf", 1000)

for count, page in enumerate(im_pages):
    page.show()
    base64.b64encode(page).decode("utf-8")

reader = PdfReader("input/test.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]

im = page.get_object().write_to_stream
im.show()

for count, image_file_object in enumerate(page.images):
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)

text = page.extract_text()
print("test")