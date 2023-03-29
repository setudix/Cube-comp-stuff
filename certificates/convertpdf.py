import os
import img2pdf

image_folder = './img/'
pdf_file = 'output.pdf'

image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.png')]

with open(pdf_file, "wb") as f:
    f.write(img2pdf.convert(image_files))
