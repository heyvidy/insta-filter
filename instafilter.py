# Import Image from PIL
from PIL import Image

# Load Images into Objects
base_img = Image.open("portrait.jpg")
img_filter = Image.open("kid.jpg")

# Set O/p Image Size
size = (760,760)

# Resize all images to o/p size
base_img = base_img.resize(size)
img_filter = img_filter.resize(size)

# Split each image into RGB vectors
r, g, b = base_img.split()
R,G,B = img_filter.split()

# Merge RGB vectors from different images
im = Image.merge("RGB", (r, Gg, b))
im.save("filtered.jpg", "JPG")

