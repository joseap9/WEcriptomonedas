from tkinter import *
from PIL import Image,ImageTk
import requests as req
from io import BytesIO

#inicio de la interfaz
root = Tk()
root.geometry('200x200')

#url de la imagen
img_src = 'http://wx2.sinaimg.cn/mw690/ac38503ely1fesz8m0ov6j20qo140dix.jpg'
#request del url
response = req.get(img_src)
#transformacion formato de tkinter
image = Image.open(BytesIO(response.content))
img = ImageTk.PhotoImage(image)
#colocacion de la imagen en la interfaz
imgColocada = Label(root,image=img).pack()


root.mainloop()