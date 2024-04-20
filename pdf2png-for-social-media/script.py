import sys
from pdf2image import convert_from_path

def pdf_to_png(pdf_path, output_path):
    images = convert_from_path(pdf_path)
    if images:
        images[0].save(output_path, 'PNG')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <pdf_file_path>")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    pdf_file_name = pdf_file_path.split(".")[0]
    output_file_path = f"{pdf_file_name}.png"

    pdf_to_png(pdf_file_path, output_file_path)
    print(f"PDF converted to PNG: {output_file_path}")