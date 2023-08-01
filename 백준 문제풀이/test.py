from rembg import remove
from PIL import Image
import os

def process_roi(image_path, output_path):
    image = Image.open(image_path)
    width, height = image.size

    # Crop the ROI centered at the middle of the image
    roi_left = max(0, width // 2 - 100)
    roi_top = max(0, height // 2 - 100)
    roi_right = min(width, width // 2 + 100)
    roi_bottom = min(height, height // 2 + 100)

    roi = image.crop((roi_left, roi_top, roi_right, roi_bottom))

    # Save the ROI to a temporary file
    temp_roi_path = 'temp_roi.png'
    roi.save(temp_roi_path)

    with open(temp_roi_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_data = i.read()
            output_data = remove(input_data)
            o.write(output_data)

    # Remove the temporary ROI file
    os.remove(temp_roi_path)

if __name__ == "__main__":
    input_path = './test2.png'
    output_path = 'output.jpg'

    process_roi(input_path, output_path)