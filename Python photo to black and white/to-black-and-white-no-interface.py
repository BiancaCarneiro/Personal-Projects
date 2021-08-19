from PIL import Image
import threading
import sys
import time

# we will transform the image into gray tones by using the formula bellow:
# new_pixel = RGB(c, c, c), where c = r*0.3 + g*0.59 + b*0.11 and old_pixel = RGB(r, g, b)
start = time.time()
num_threads = 1000
img_name = "pictures\Avatar the Last Airbender Backgrounds 3"
img_ext = ".jpg"
with Image.open(img_name + img_ext) as im:
    px = im.load()

width, height = im.size 

if width < num_threads:
    num_threads = width-1

class Th(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        j = 0
        i = self.num #takes the thread number
        while j < height:
            #sys.stdout.write("Thread"+str(self.num)+" i:" + str(i) +" j:" + str(j))
            #sys.stdout.flush()
            #print("Thread num: " + str(self.num))
            (r,g,b) = px[i,j]
            c = int(r*0.3 + g*0.59 + b*0.11)
            px[i,j] = (c,c,c)
            i += num_threads
            if i >= width:
                j += 1
                i = self.num
        
def main():
    a = []
    for k in range(num_threads):
        a.append(Th(k))
        a[k].start()

#im.show()
main()
lixo = True
while threading.active_count() > 1:
    #print(threading.active_count())
    lixo = False

print("--- %s seconds ---" % (time.time() - start))
#im.save(img_name + "_gray" + img_ext)
