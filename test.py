from bs4 import BeautifulSoup
import requests
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas_datareader as pdr
from datetime import datetime, timedelta
import mplfinance as mpf
from PIL import Image, ImageTk
from threading import Thread

url = 'https://coinmarketcap.com/es/'
page = requests.get(url)
cont = page.text

listaMonedas = []
soup = BeautifulSoup(cont, 'lxml')

box = soup.find('html', lang='es')

tex = box.find('h1', class_='sc-1q9q90x-0 TyVlS')
titulo = tex.get_text()

# priemr a moneda
lista_paginas = ['https://coinmarketcap.com/es/currencies/bitcoin/',
                 'https://coinmarketcap.com/es/currencies/ethereum/',
                 'https://coinmarketcap.com/es/currencies/binance-coin/',
                 'https://coinmarketcap.com/es/currencies/tether/',
                 'https://coinmarketcap.com/es/currencies/solana/',
                 'https://coinmarketcap.com/es/currencies/cardano/',
                 'https://coinmarketcap.com/es/currencies/xrp/',
                 'https://coinmarketcap.com/es/currencies/polkadot-new/',
                 'https://coinmarketcap.com/es/currencies/dogecoin/',
                 'https://coinmarketcap.com/es/currencies/usd-coin/']
lista_valores = []
sumador = 1
for x in range(len(lista_paginas)):

    url = lista_paginas[x]

    page1 = requests.get(url)
    cont1 = page1.text

    soup2 = BeautifulSoup(cont1, 'lxml')

    v = soup2.find('div', class_='sc-16r8icm-0 kjciSH priceSection')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    optencion_valor = v.find('div', class_='sc-16r8icm-0 kjciSH priceTitle')
    valo = optencion_valor.find('div', class_='priceValue')
    for q in valo:
        valor = q

    minimo = v.find('span', class_='n78udj-5 dBJPYV').get_text()
    x = soup2.find('div', class_='sc-16r8icm-0 SjVBR')
    maximo = x.find('span', class_='n78udj-5 dBJPYV').get_text()
    a = soup2.find('div', class_='sc-16r8icm-0 fggtJu statsSection')
    con = 0

    # obtencion del volumen capital de la moneda

    for volu in a.findAll('div', class_='statsBlock'):
        if con == 2:
            for q in volu:
                if con == 3:
                    volumen = q.find('div', class_='statsValue').get_text()
                    listaVolumenMonedas.append(volumen)
                con = con + 1
        con = con + 1

    tex2 = soup2.find('h2', class_='sc-1q9q90x-0 jCInrl h1')
    titulo2 = tex2.get_text()

    # grafico de velas
    # int_date = datetime.now() - timedelta(days=30)
    # info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    # mpf.plot(info, type='candle', title='valor '+ titulo2, style='charles')
    listaMonedas.append(titulo2)
    listaMonedas.append(valor)
    listaMonedas.append(minimo)
    listaMonedas.append(maximo)
    listaMonedas.append(volumen)
    listaMonedas.append(moneda)


def frameMoneda(valor):
    def graficoVela(valor):

        int_date = datetime.now() - timedelta(days=30)
        if valor - 1 == 0:
            info = pdr.get_data_yahoo(listaMonedas[5] + '-USD', start=int_date)
            mpf.plot(info, type='candle', title='Valor ' + listaMonedas[0], style='charles')
        else:
            info = pdr.get_data_yahoo(listaMonedas[6 * (valor - 1) + 5] + '-USD', start=int_date)
            mpf.plot(info, type='candle', title='Valor ' + listaMonedas[6 * (valor - 1)], style='charles')

    def graficoLineas(valor):

        int_date = datetime.now() - timedelta(days=30)
        if valor - 1 == 0:
            info = pdr.get_data_yahoo(listaMonedas[5] + '-USD', start=int_date)
            mpf.plot(info, type='line', title='Valor ' + listaMonedas[0], style='charles')
        else:
            info = pdr.get_data_yahoo(listaMonedas[6 * (valor - 1) + 5] + '-USD', start=int_date)
            mpf.plot(info, type='line', title='Valor ' + listaMonedas[6 * (valor - 1)], style='charles')

    lis_img = ['images_coins/1.png',
               'images_coins/2.png',
               'images_coins/3.png',
               'images_coins/4.png',
               'images_coins/5.png',
               'images_coins/6.png',
               'images_coins/7.png',
               'images_coins/8.png',
               'images_coins/9.png',
               'images_coins/10.png']

    top = Toplevel()
    if valor - 1 == 0:
        top.title(listaMonedas[0])
    else:
        top.title(listaMonedas[6 * (valor - 1)])
    top.geometry("800x600")
    header = Frame(top, width=1200, height=180, bg="white")
    header.pack()
    body = Frame(top, width=1200, height=480, bg="#E5F3F7")
    body.pack()

    img = Image.open(lis_img[valor - 1])
    img = ImageTk.PhotoImage(img)
    img_label = Label(top, image=img, bg="white")
    img_label.Image = img
    img_label.place(x=20, y=16)

    if valor - 1 == 0:
        texto_titulo = listaMonedas[0]
    else:
        texto_titulo = listaMonedas[6 * (valor - 1)]

    name = Label(top, text=texto_titulo, bg="white", font=("Aharoni", 25, 'bold'))
    name.place(x=200, y=75)

    if valor - 1 == 0:
        value = Label(top, text=listaMonedas[1], bg="white", font=("Aharoni", 25, 'bold'))
        value.place(x=500, y=75)
        volumenTitulo = Label(top, text="Volumen capital: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        volumen = Label(top, text=listaMonedas[4], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        inverTitulo = Label(top, text="Momento para invertir: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        inver = Label(top, text="SI", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        inverTitulo.place(x=30, y=240)
        inver.place(x=310, y=240)
        volumenTitulo.place(x=30, y=200)
        volumen.place(x=310, y=200)

    else:
        value = Label(top, text=listaMonedas[6 * (valor - 1) + 1], bg="white", font=("Aharoni", 25, 'bold'))
        value.place(x=500, y=75)
        volumenTitulo = Label(top, text="Volumen capital: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        volumen = Label(top, text=listaMonedas[6 * (valor - 1) + 4], bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        volumenTitulo.place(x=30, y=210)
        volumen.place(x=310, y=210)
        inverTitulo = Label(top, text="Momento para invertir: ", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        inver = Label(top, text="SI", bg="#E5F3F7", font=("Aharoni", 18, 'bold'))
        inverTitulo.place(x=30, y=240)
        inver.place(x=310, y=240)

    gv = Image.open('images_coins/gv-bc.png')
    imgAgregar = ImageTk.PhotoImage(gv)
    gv_ = Button(top, image=imgAgregar, borderwidth=0, bg="#E5F3F7", command=lambda: [graficoVela(valor)])
    gv_.place(x=50, y=420)

    gl = Image.open('images_coins/gl-bc.png')
    imgAgregarr = ImageTk.PhotoImage(gl)
    gl_ = Button(top, image=imgAgregarr, borderwidth=0, bg="#E5F3F7", command=lambda: [graficoLineas(valor)])
    gl_.place(x=150, y=420)
    top.mainloop()


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

            Thread(target=frameMoneda(valor)).start()

    # =======================
    # marcoTodos = LabelFrame(popup, text="Pacientes Con Alta Medica", bd=4, width=290, height=318, bg="#EDF0F2")
    # marcoTodos.place(x=50, y=30)
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
                              tags=('evenrow'))
        else:
            if x % 2 == 0:
                ever_add = 'addrow'
            else:
                ever_add = 'evenrow'
            tablaTodos.insert(parent='', index=x + 1, iid=x + 1,
                              values=(x + 1, listaMonedas[6 * x], listaMonedas[6 * x + 1], listaMonedas[6 * x + 2],
                                      listaMonedas[6 * x + 3]),
                              tags=(ever_add))

    tablaTodos.bind('<Double-1>', item_selected)


root = Tk()
root.title("Scrapping Crypto")
root.geometry("580x360")
tabla()

root.mainloop()
