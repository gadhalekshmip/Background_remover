# Remove background using python
from rembg import remove
from PIL import Image
input_path='D:\program\python pgm\img.jpg'
output_path='output.png'
input=Image.open(input_path)
output=remove(input)
output.save(output_path)
