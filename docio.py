#from docling.document_converter import DocumentConverter

#source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
#converter = DocumentConverter()
#result = converter.convert(source)
#print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"

import cv2 as cv
from pypdf import PdfReader
from pdf2image import convert_from_path


im_pages = convert_from_path("input/test.pdf", 1000)

for count, page in enumerate(im_pages):
    page.show()

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