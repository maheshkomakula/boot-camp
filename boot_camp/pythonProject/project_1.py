from PIL import ImageTk,Image
import cv2
inputimage=cv2.imread('photo.jpeg')
blue,green,red=cv2.split(inputimage)
img=cv2.merge((red,green,blue))
im=Image.fromarray(img)
image1=im.resize((240,240))
image1=ImageTk.photoImage(image1)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
for (x, y, w, h) in faces_rect:
    outputimage=cv2.rectangle(inputimage, (x, y), (x + w, y + h), (0, 255, 0), 10)

    blue, green, red = cv2.split(outputimage)
    outputimage = cv2.merge((red, green, blue))
    oim = Image.fromarray(outputimage)
    image3 = oim.resize((240, 240))
    image3 = ImageTk.PhotoImage(image3)