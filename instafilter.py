from PIL import Image

base_img = Image.open("portrait.jpg")
img_filter = Image.open("kid.jpg")
third = Image.open("art.jpg")

size = (760,760)

base_img = base_img.resize(size)
img_filter = img_filter.resize(size)
third = third.resize(size)

r, g, b = base_img.split()
R,G,B = img_filter.split()
Rr, Gg, Bb = third.split()

im = Image.merge("RGB", (r, Gg, B))
im.show()
# im.save('1_merged.jpg')

