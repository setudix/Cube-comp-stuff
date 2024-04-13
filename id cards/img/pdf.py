from PIL import Image
from fpdf import FPDF
import os

# Create an instance of FPDF class
pdf = FPDF('P', 'mm', 'A4')  # Portrait mode, millimeter unit, A4 page size

# List all .png files
files = [f for f in os.listdir('.') if f.endswith('.png')]

# Sort the files by their number
files.sort(key=lambda x: int(x.split('.')[0]))

# Group the images into groups of 8
groups = [files[n:n+8] for n in range(0, len(files), 8)]

for i, group in enumerate(groups):
    pdf.add_page()
    x_offset = 0
    y_offset = 0

    for j, image_file in enumerate(group):
        # Open the image file
        img = Image.open(image_file)
        # Calculate new size to maintain aspect ratio
        aspect_ratio = img.width / img.height
        new_width = int(210/2)
        new_height = int(new_width / aspect_ratio)
        # Resize image to fit into A4 page with 8 images
        img.thumbnail((new_width, new_height), Image.ANTIALIAS)
        # Remove alpha channel if present
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert('RGB')
        # Save the resized image with a unique filename
        temp_filename = f"temp_{i}_{j}.png"
        img.save(temp_filename)

        # Add image to pdf
        pdf.image(temp_filename, x=x_offset, y=y_offset, w=new_width, h=new_height)

        print(j)
        # Update offsets
        x_offset += new_width
        if x_offset >= 210:
            x_offset = 0
            y_offset += new_height

# Save the pdf file
pdf.output("output.pdf", "F")

# Clean up temporary files
for i, group in enumerate(groups):
    for j, _ in enumerate(group):
        os.remove(f"temp_{i}_{j}.png")
