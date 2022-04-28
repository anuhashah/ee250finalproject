from PIL import Image

# does not close window after opening
def preview():
	with Image.open('image.jpg') as img:
		img.show()