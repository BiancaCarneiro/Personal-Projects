from PIL import Image
import threading
import sys
import tkinter as tk
import time

# we will transform the image into gray tones by using the formula bellow:
# new_pixel = RGB(c, c, c), where c = r*0.3 + g*0.59 + b*0.11 and old_pixel = RGB(r, g, b)

root = tk.Tk()
root.title("To black and white")

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def transform_img():
    start = time.time()

    num_threads = 8
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
    
    main()
    lixo = True
    while threading.active_count() > 1:
        #print(threading.active_count())
        lixo = False
    im.show()
    im.save(img_name + "_gray" + img_ext)
    print("--- %s seconds ---" % (time.time() - start))

button1 = tk.Button(text='Click Me',command=transform_img, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)



root.mainloop()