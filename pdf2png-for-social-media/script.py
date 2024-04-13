from pdf2image import convert_from_path

def pdf_to_png(pdf_path, output_path):
    images = convert_from_path(pdf_path)

    if images:
        images[0].save(output_path, 'PNG')

pdf_to_png('early bird opening post.pdf', 'output.png')
print("converted\n")