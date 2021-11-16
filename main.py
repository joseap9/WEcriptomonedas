from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas_datareader as pdr
from datetime import datetime, timedelta
import mplfinance as mpf
from PIL import Image, ImageTk
import requests as req
from io import BytesIO
from weCriptomonedas import listaMonedas,lista_img,lista_paginas,inversion



#creacion de las funciones para las ventanas
def frameMoneda(valor):
    top = Toplevel()
    if valor - 1 == 0:
        top.title(listaMonedas[0])
    else:
        top.title(listaMonedas[9 * (valor - 1)])
    top.geometry("700x550")
    header = Frame(top, width=1200, height=180, bg="white")
    header.pack()
    body = Frame(top, width=1200, height=480, bg="#E5F3F7")
    body.pack()

    response = req.get(lista_img[valor - 1])
    # transformacion formato de tkinter
    image = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(image)

    # colocacion de la imagen en la interfaz
    imgColocada = Label(top, image=img)
    imgColocada.place(x=60, y=60)

    if valor - 1 == 0:
        texto_titulo = listaMonedas[0]
    else:
        texto_titulo = listaMonedas[9 * (valor - 1)]

    name = Label(top, text=texto_titulo, bg="white", font=("Aharoni", 25, 'bold'))
    name.place(x=150, y=75)

    if valor - 1 == 0:
        value = Label(top, text=listaMonedas[1], bg="white", font=("Aharoni", 25, 'bold'))
        value.place(x=430, y=75)
        # momento de nivel de mercado de la moneda
        nivelT = Label(top, text="Nivel de la moneda: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        nivel = Label(top, text=listaMonedas[7], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        nivelT.place(x=30, y=210)
        nivel.place(x=400, y=210)
        # Capitalizacion en el mercado
        capT = Label(top, text="Capitalizacion en el mercado: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        cap = Label(top, text=listaMonedas[8], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        capT.place(x=30, y=250)
        cap.place(x=400, y=250)
        # dominio de la moneda en el mercado
        dominioMTitulo = Label(top, text="Dominio de mercado: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        dominioM = Label(top, text=listaMonedas[6], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        dominioMTitulo.place(x=30, y=290)
        dominioM.place(x=400, y=290)
        # volumen capital
        volumenTitulo = Label(top, text="Volumen de capital: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        volumen = Label(top, text=listaMonedas[4], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        volumenTitulo.place(x=30, y=330)
        volumen.place(x=400, y=330)
        # Momento para invertir
        dat = False
        inversionT = Label(top, text="Momento para invertir: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        if inversion(dat) == True:
            inv = Label(top, text='SI', bg="#84E77D", fg="#0FB404", font=("Aharoni", 18, 'bold'))
        else:
            inv = Label(top, text='NO', bg="#E8908C", fg="#C8221B", font=("Aharoni", 18, 'bold'))

        inversionT.place(x=30, y=390)
        inv.place(x=400, y=390)
    else:
        #valor
        value = Label(top, text=listaMonedas[9 * (valor - 1) + 1], bg="white", font=("Aharoni", 25, 'bold'))
        value.place(x=440, y=75)
        # momento de nivel de mercado de la moneda
        nivelT = Label(top, text="Nivel de la moneda: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        nivel = Label(top, text=listaMonedas[9 * (valor - 1) + 7], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        nivelT.place(x=30, y=210)
        nivel.place(x=400, y=210)
        # Capitalizacion en el mercado
        capT = Label(top, text="Capitalizacion en el mercado: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        cap = Label(top, text=listaMonedas[9 * (valor - 1) + 8], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        capT.place(x=30, y=250)
        cap.place(x=400, y=250)
        # dominio de la moneda en el mercado
        dominioMTitulo = Label(top, text="Dominio de mercado: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        dominioM = Label(top, text=listaMonedas[9 * (valor - 1) + 6], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        dominioMTitulo.place(x=30, y=290)
        dominioM.place(x=400, y=290)
        #volumen capital
        volumenTitulo = Label(top, text="Volumen de capital: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        volumen = Label(top, text=listaMonedas[9 * (valor - 1) + 4], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        volumenTitulo.place(x=30, y=330)
        volumen.place(x=400, y=330)
        # Momento para invertir
        dato=True
        inversionT = Label(top, text="Momento para invertir: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        if inversion(dato):
            inv = Label(top, text='SI', bg="#84E77D",fg="#0FB404", font=("Aharoni", 18, 'bold'))
        else:
            inv = Label(top, text='NO', bg="#E8908C", fg="#C8221B", font=("Aharoni", 18, 'bold'))

        inversionT.place(x=30, y=390)
        inv.place(x=400, y=390)


    gv = Image.open('images_coins/gv-bc.png')
    imgAgregar = ImageTk.PhotoImage(gv)
    gv_ = Button(top, image=imgAgregar, borderwidth=0, bg="#E5F3F7", command=lambda: [graficoVela(valor)])
    gv_.place(x=50, y=460)

    gl = Image.open('images_coins/gl-bc.png')
    imgAgregarr = ImageTk.PhotoImage(gl)
    gl_ = Button(top, image=imgAgregarr, borderwidth=0, bg="#E5F3F7", command=lambda: [graficoLineas(valor)])
    gl_.place(x=150, y=460)
    top.mainloop()
    # funcion de la ventana del grafico de velas

def graficoVela(valor):

    int_date = datetime.now() - timedelta(days=30)
    if valor - 1 == 0:
        if listaMonedas[5] == 'SOL' or listaMonedas[5]=='DOL':
            info = pdr.get_data_yahoo(listaMonedas[5] + '1-USD', start=int_date)
            mpf.plot(info, type='candle', title='Valor ' + listaMonedas[0], style='charles')
        else:
            info = pdr.get_data_yahoo(listaMonedas[5] + '-USD', start=int_date)
            mpf.plot(info, type='candle', title='Valor ' + listaMonedas[0], style='charles')
    else:
        if listaMonedas[9 * (valor - 1) + 5] == 'SOL' or listaMonedas[9 * (valor - 1) + 5]=='DOL':
            info = pdr.get_data_yahoo(listaMonedas[9 * (valor - 1) + 5] + '1-USD', start=int_date)
            mpf.plot(info, type='candle', title='Valor ' + listaMonedas[9 * (valor - 1)], style='charles')
        else:
            info = pdr.get_data_yahoo(listaMonedas[9 * (valor - 1) + 5] + '-USD', start=int_date)
            mpf.plot(info, type='candle', title='Valor ' + listaMonedas[9 * (valor - 1)], style='charles')

# funcion de la ventana de lgrafico de lineas
def graficoLineas(valor):
    int_date = datetime.now() - timedelta(days=30)
    if valor - 1 == 0:
        if listaMonedas[5] == 'SOL' or listaMonedas[5] == 'DOL':
            info = pdr.get_data_yahoo(listaMonedas[5] + '1-USD', start=int_date)
            mpf.plot(info, type='line', title='Valor ' + listaMonedas[0], style='charles')
        else:
            info = pdr.get_data_yahoo(listaMonedas[5] + '-USD', start=int_date)
            mpf.plot(info, type='line', title='Valor ' + listaMonedas[0], style='charles')
    else:
        if listaMonedas[9 * (valor - 1) + 5] == 'SOL' or listaMonedas[9 * (valor - 1) + 5] == 'DOL':
            info = pdr.get_data_yahoo(listaMonedas[9 * (valor - 1) + 5] + '1-USD', start=int_date)
            mpf.plot(info, type='line', title='Valor ' + listaMonedas[9 * (valor - 1)], style='charles')
        else:
            info = pdr.get_data_yahoo(listaMonedas[9 * (valor - 1) + 5] + '-USD', start=int_date)
            mpf.plot(info, type='line', title='Valor ' + listaMonedas[9 * (valor - 1)], style='charles')

#creacion de la tabla principal del programa
def tabla():
    def item_selected(e):

        for selected_item in tablaTodos.selection():
            # dictionary
            item = tablaTodos.item(selected_item)
            # list
            valor = item['values'][0]

            nombreOpcion = item['text']
            imagen = item['image']
            abierto = item['open']

            frameMoneda(valor)

    # =======================
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])

    # creacion de tabla
    tablaTodos = ttk.Treeview(root, columns=(0, 1, 2, 3, 4), show='headings', height=13)
    tablaTodos.pack()
    tablaTodos.tag_configure('oddrow', background="#26C1F4")
    tablaTodos.tag_configure('evenrow', background="#C0EAF8")
    tablaTodos.heading(0, text="N°")
    tablaTodos.heading(1, text="Nombre")
    tablaTodos.heading(2, text="valor")
    tablaTodos.heading(3, text="Precio Min 24h ")
    tablaTodos.heading(4, text="Precio Max 24h")
    tablaTodos.column(0, width=10, minwidth=25)
    tablaTodos.column(1, width=120)
    tablaTodos.column(2, width=120)
    tablaTodos.column(3, width=120)
    tablaTodos.column(4, width=120)

    # agregando elementos
    for x in range(len(lista_paginas)):
        if x == 0:
            tablaTodos.insert(parent='', index=x + 1, iid=x + 1,
                              values=(x + 1, listaMonedas[0], listaMonedas[1], listaMonedas[2], listaMonedas[3]),
                              tags=('addrow'))
        else:
            if x % 2 == 0:
                ever_add = 'addrow'
            else:
                ever_add = 'evenrow'
            tablaTodos.insert(parent='', index=x + 1, iid=x + 1,
                              values=(x + 1, listaMonedas[9 * x], listaMonedas[9 * x + 1], listaMonedas[9 * x + 2],
                                      listaMonedas[9 * x + 3]),
                              tags=(ever_add))

    tablaTodos.bind('<Double-1>', item_selected)


root = Tk()
root.title("Scrapping Crypto")
root.geometry("580x360")
tabla()

root.mainloop()
