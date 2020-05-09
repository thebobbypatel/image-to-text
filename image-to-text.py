import pytesseract
from PIL import Image
import os

# Set directory to the location of the folder where all of your images are.
directory = './screenshots/'

# Choose the name of the text file that will be created.
notes = open('text_from_images.txt', 'a')


for filename in os.listdir(directory):
	
	image = Image.open(directory + filename)

	text = pytesseract.image_to_string(image)

	notes.write(text)

	notes.write('\n')
	notes.write('\n')

notes.close()