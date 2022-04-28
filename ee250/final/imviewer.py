from PIL import Image

def preview():
	with Image.open('image.jpg') as img:
		img.show()