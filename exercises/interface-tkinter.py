from tkinter import *
#texto="Welcome"
janela = Tk()
janela.title("Calculadora")
color = 'orange'
janela["bg"] = color
janela.geometry("300x300+250+300")
def  btClicado():
    texto = int(ed.get())
    lb["text"] = ed.get()
bt = Button(janela, width = 20, text ="OK", command=btClicado)
bt.place(x=100,y = 60)
lb = Label(janela, text = "Ola")
lb.place(x=100, y=200)
ed = Entry(janela, width=10)
ed.place(x=100,y=100)

janela.mainloop()
