from PIL import Image
from threading import Thread

# we will transform the image into gray tones by using the formula bellow:
# new_pixel = RGB(c, c, c), where c = r*0.3 + g*0.59 + b*0.11 and old_pixel = RGB(r, g, b)
num_threads = 1

img_name = "pictures/4k-testing-pic"
img_ext = ".jpg"

with Image.open(img_name + img_ext) as im:
    px = im.load()


width, height = im.size 

if width < num_threads:
    num_threads = width

class Th(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        j = 0
        i = self.num
        while j < height:
            (r,g,b) = px[i,j]
            c = int(r*0.3 + g*0.59 + b*0.11)
            px[i,j] = (c,c,c)
            i += num_threads
            if i >= width:
                j += 1
                i = self.num

for k in range(num_threads):
    a = Th(k)
    a.start()

im.show()
im.save(img_name + "_gray" + img_ext)