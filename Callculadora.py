#Calculadroa de 2 numeros
from tkinter import  *


raiz= Tk()
raiz.title("Calculadora")
raiz.geometry("800x600")


frame=Frame(raiz,bg="#707070")
frame.pack(fill="both",expand=1)
NAEntrada = IntVar()
NBEntrada= IntVar()

op=0


def C():
    NAEntrada.set(0)
    NBEntrada.set(0)
    Reslabel.config(text="")
    
def click(valor):
    global op
    if valor==1:
        op=1
    elif valor==2:
        op=2
    elif valor==3:
        op=3
    elif valor==4:
        op=4
       
        
       
        
def Operacion():
    if op==1:
        resultado=NAEntrada.get() + NBEntrada.get()
        print(resultado)
        Reslabel.config(text=resultado)
    elif op==2:
        resultado=NAEntrada.get() - NBEntrada.get()
        print(resultado)
        Reslabel.config(text=resultado)
    elif op==3:
         resultado=NAEntrada.get() * NBEntrada.get()
         print(resultado)
         Reslabel.config(text=resultado)
    elif op==4:
        resultado=NAEntrada.get()/NBEntrada.get()
        print(resultado)
        Reslabel.config(text=resultado)
        
    
    

#Etiqueta Calculadroa
Calculadora=Label(frame,text="Calculadora",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.4 ,rely=.1)

#Etiqueta NumeroA
etiquetaNB=Label(frame,text="Numero A: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.2 ,rely=.2)
#Entry  NumeroA
NAEntry=Entry(frame,
                  font=("Roboto",18,"bold"),
                  textvariable= NAEntrada)
NAEntry.place(relx=0.5,rely=0.2)

#Etiqueta  NumeroB
etiquetaNB=Label(frame,text="Numero B: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.2 ,rely=.3)
#Entry NumeroB
NBEntry=Entry(frame,
                  font=("Roboto",18,"bold"),
                  textvariable= NBEntrada)
NBEntry.place(relx=0.5,rely=0.3)

#Etiqueta Resultado
etiquetaResultado=Label(frame,text="Resultado: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.2 ,rely=.4)

Reslabel=Label(frame,text=" ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7")
Reslabel.place(relx=.5 ,rely=.4)



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                   B O T O N E S 


#Boton Suma
btSuma=Button(frame,text="Suma",
             font=("Roboto",20,"bold"),
             width=6,
             height=1,
             command=lambda:click(1))
btSuma.place(relx=.3,rely=.6)

#Boton Resta
btResta=Button(frame,text="Resta",
             font=("Roboto",20,"bold"),
             width=6,
             height=1,
             command=lambda:click(2))
btResta.place(relx=.3,rely=.75)

#Boton Multi
btMulti=Button(frame,text="Mult",
             font=("Roboto",20,"bold"),
             width=6,
             height=1,
             command=lambda:click(3))
btMulti.place(relx=.45,rely=.6)

#Boton Division
btDivision=Button(frame,text="División",
             font=("Roboto",20,"bold"),
             width=6,
             height=1,
             command=lambda:click(4))
btDivision.place(relx=.45,rely=.75)

#Boton C
btC=Button(frame,text=" C ",
             font=("Roboto",20,"bold"),
             width=6,
             height=1,
             command=C).place(relx=.6,rely=.6)

#Boton =
btEQU=Button(frame,text=" = ",
             font=("Roboto",20,"bold"),
             width=6,
             height=1,
             command=Operacion)
btEQU.place(relx=.6,rely=.75)

raiz.mainloop()