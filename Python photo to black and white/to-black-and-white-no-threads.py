from PIL import Image
import sys
import time

# we will transform the image into gray tones by using the formula bellow:
# new_pixel = RGB(c, c, c), where c = r*0.3 + g*0.59 + b*0.11 and old_pixel = RGB(r, g, b)
start = time.time()
img_name = "pictures\Avatar the Last Airbender Backgrounds 3"
img_ext = ".jpg"
with Image.open(img_name + img_ext) as im:
    px = im.load()

width, height = im.size 


def run():
    j = 0
    i = 0 #takes the thread number
    while j < height:
        #sys.stdout.write("Thread"+str(self.num)+" i:" + str(i) +" j:" + str(j))
        #sys.stdout.flush()
        #print("Thread num: " + str(self.num))
        (r,g,b) = px[i,j]
        c = int(r*0.3 + g*0.59 + b*0.11)
        px[i,j] = (c,c,c)
        i += 1
        if i >= width:
            j += 1
            i = 0
        


run()
print("--- %s seconds ---" % (time.time() - start))
im.show()
#im.save(img_name + "_gray" + img_ext)
