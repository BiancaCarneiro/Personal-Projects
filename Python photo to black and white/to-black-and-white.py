from PIL import Image
from threading import Thread
import sys
import tkinter as tk

# we will transform the image into gray tones by using the formula bellow:
# new_pixel = RGB(c, c, c), where c = r*0.3 + g*0.59 + b*0.11 and old_pixel = RGB(r, g, b)

root = tk.Tk()
root.title("To black and white")

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def transform_img():
    num_threads = 8
    img_name = "pictures/download"
    img_ext = ".jpg"
    with Image.open(img_name + img_ext) as im:
        px = im.load()

    width, height = im.size 

    if width < num_threads:
        num_threads = width-1

    class Th(Thread):
        def __init__(self, num):
            Thread.__init__(self)
            self.num = num

        def run(self):
            j = 0
            i = self.num #takes the thread number
            while j < height:
                #sys.stdout.write("Thread"+str(self.num)+" i:" + str(i) +" j:" + str(j))
                #sys.stdout.flush()
                (r,g,b) = px[i,j]
                c = int(r*0.3 + g*0.59 + b*0.11)
                px[i,j] = (c,c,c)
                i += num_threads
                if i >= width:
                    j += 1
                    i = self.num

    a = []
    for k in range(num_threads):
        a.append(Th(k))
        a[k].start()

    im.show()
    im.save(img_name + "_gray" + img_ext)

button1 = tk.Button(text='Click Me',command=transform_img, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)



root.mainloop()