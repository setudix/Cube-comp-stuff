import cv2

# Define the font type, size, color, and thickness for the text
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font_size = 15
font_color = (0, 0, 0)
font_thickness = 20

# Load the names from the text file
with open('names.txt', 'r') as f:
    names = f.readlines()


# Loop through each name, write it on the certificate image, and save the modified image to a PDF file
for index, name in enumerate(names):
    certificate = cv2.imread('template.png')
    name = name.strip()
    position = (2000, 4300)
    text_width, text_height = cv2.getTextSize(name, font, font_size, font_thickness)[0]
    CenterCoordinates = (int(certificate.shape[1] / 2) - int(text_width / 2), 4100 + int(text_height / 2))
    cv2.putText(certificate, name, CenterCoordinates, font,
                font_size, font_color, font_thickness)
    cv2.imwrite(f'./img/{index}.png', certificate)
    print(f'completed {index + 1}/{len(names)}')