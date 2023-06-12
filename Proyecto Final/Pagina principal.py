
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter.constants import END
from tkinter import  messagebox,Spinbox


#funcion


ventanab=tk.Tk()
ancho_ventana = 800
alto_ventana = 600

x_ventana = ventanab.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventanab.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventanab.geometry(posicion)

ventanab.resizable(0,0)
ventanab.title("Pagina principal")
ventanab.config(background="darkturquoise")

imagenKIA=PhotoImage(file="VW.png")
lblimagenVW=Label(ventanab, image=imagenKIA).grid(row=0, column=0)


def continuar():
    
    def piezas():
        
        def salir():
        
            respuesta=messagebox.askyesno("Close window ", "¿Deseas volver al menu?")
            if respuesta==True:
                ventana.destroy()
   
 
        ventana=tk.Toplevel()
        ancho_ventana = 800
        alto_ventana = 600

        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)

        ventana.resizable(0,0)
        ventana.title("Calcular tiempo de fabricacion para cada pieza")
        ventana.config(background="darkturquoise")


        def calcular():
            pieza = lista_pieza.get()
            cortem = lista_cortem.get()
            acabado = lista_acabado.get()
            horno = lista_horno.get()
            pintura = lista_pintura.get()
            transporte = lista_transporte.get()
            humano = lista_humano.get()
            extrusora = lista_extrusora.get()
            pieza = (pieza)
            cortem = float(cortem)
            acabado = float(acabado)
            horno = float(horno)
            pintura = float(pintura)
            transporte = float(transporte)
            humano = float(humano)
            extrusora = float(extrusora)
            timet=cortem+acabado+horno+pintura+transporte+humano+extrusora
            horasm=cortem+acabado+horno+pintura+transporte+extrusora
            horash=humano+0
            listbox.insert(END,("-------------------------------------------------------------------------"))
            listbox.insert(END,("\n"))
            listbox.insert(END,(pieza))
            listbox.insert(END,("\n"))
            
            
            listbox.insert(END,(" La duracion de cada pieza en las maquinas es de ",+ horasm,"horas/u"))
            listbox.insert(END,("\n"))
            listbox.insert(END,(" El tiempo empleado del recurso humano es de ",+ horash,"horas/u"))
            listbox.insert(END,("\n"))
            listbox.insert(END,(" La duracion de cada pieza es de ",+ timet,"horas/u"))


        def limpiar():
            listbox.delete(0,1000)
            
            
        def help():
            
            def salir2():
                
                respuesta=messagebox.askyesno("Close window ", "¿Deseas volver al menu?")
                if respuesta==True:
                    ventana.destroy()
    
            ventana=tk.Toplevel()
            ancho_ventana = 500
            alto_ventana = 500

            x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

            posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
            ventana.geometry(posicion)

            ventana.resizable(0,0)
            ventana.title("Calcular tiempo de fabricacion para cada pieza")
            ventana.config(background="white")
            
            label1=tk.Label(ventana, text="Pasos para utilizar el programa", font=("Times new roman",12), bg="white", fg="black")
            label1.pack()
            
            
            label2=tk.Label(ventana, text=" \n •Recuerde que los tiempos se miden en horas", font=("Times new roman",12), bg="white", fg="black")
            label2.pack()
            
            label3=tk.Label(ventana, text=" \n •Paso1: Ingrese los datos que desea calcular", font=("Times new roman",12), bg="white", fg="black")
            label3.pack()
            
            label4=tk.Label(ventana, text="\n •Paso2: Rectificar que los valores sean los correctos", font=("Times new roman",12), bg="white", fg="black")
            label4.pack()
            
            label5=tk.Label(ventana, text="\n •Paso 4: Oprima calcular", font=("Times new roman",12), bg="white", fg="black")
            label5.pack()
            
            label6=tk.Label(ventana, text="\n •Paso 5: Rectifique los valores proporcionados", font=("Times new roman",12), bg="white", fg="black")
            label6.pack()
            
            btnsalir=tk.Button(ventana,text="Volver al menu",command=salir2,bg="grey")
            btnsalir.place(relx= 0.45, rely=0.55)
            
            
            
            
        def exit1():
            respuesta=messagebox.askyesno("Close window ", "¿Desea cerrar todo el programa?")
            if respuesta==True:
                exit()
            
        


        #menu

        mi_menu=tk.Menu(ventana)
        
        mi_menu.add_command(label="Help", command=help)
        mi_menu.add_command(label="Exit", command=exit1)
        
        ventana.config(menu=mi_menu)

        #listbox

        listbox=tk.Listbox(ventana)
        listbox.place(relx=0.01, rely=0.01, relwidth=0.7, relheight=0.7)


        #cuadros con spinbox

        cuadro_pieza= tk.Entry(ventana)
        lista_pieza=Spinbox(ventana,values=("Capó","Cabrilla","Baúl"),state="readonly")
        lista_pieza.place(relx=0.06, rely=0.8)

        cuadro_cortem= tk.Entry(ventana)
        lista_cortem=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_cortem.place(relx=0.25, rely=0.8)

        cuadro_acabado= tk.Entry(ventana)
        lista_acabado=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_acabado.place(relx=0.45, rely=0.8)

        cuadro_horno= tk.Entry(ventana)
        lista_horno=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_horno.place(relx=0.65, rely=0.8)

        cuadro_pintura= tk.Entry(ventana)
        lista_pintura=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_pintura.place(relx=0.06, rely=0.9)

        cuadro_transporte= tk.Entry(ventana)
        lista_transporte=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_transporte.place(relx=0.25, rely=0.9)

        cuadro_humano= tk.Entry(ventana)
        lista_humano=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_humano.place(relx=0.45, rely=0.9)

        cuadro_extrusora= tk.Entry(ventana)
        lista_extrusora=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_extrusora.place(relx=0.65, rely=0.9)



        #boton calcular
        boton1= tk.Button(ventana, text="Calcular", bg="green", fg="white", command=calcular)
        boton1.place(relx=0.85, rely=0.8)

        #boton limpiar
        boton2= tk.Button(ventana, text="Limpiar", bg="red", fg="white",command=limpiar)
        boton2.place(relx=0.85, rely=0.7)


        ##boton para salir 
        btnsalir=tk.Button(ventana,text="Volver al menu",command=salir,bg="gray")
        btnsalir.place(relx=0.85, rely=0.9)


        #label
        label1=tk.Label(ventana, text="Tipo de pieza",bg="darkturquoise", font=("Times new roman",11))
        label1.place(relx=0.08, rely=0.75)

        label2=tk.Label(ventana, text="Corte mecanizado",bg="darkturquoise", font=("Times new roman",11))
        label2.place(relx=0.26, rely=0.75)

        label3=tk.Label(ventana, text="Acabado",bg="darkturquoise", font=("Times new roman",11))
        label3.place(relx=0.495, rely=0.75,)

        label4=tk.Label(ventana, text="Horno y \n tratamiento termico",bg="darkturquoise", font=("Times new roman",11))
        label4.place(relx=0.65, rely=0.72,)

        label5=tk.Label(ventana, text="Cabina de pintura",bg="darkturquoise", font=("Times new roman",11))
        label5.place(relx=0.0599, rely=0.85,)

        label6=tk.Label(ventana, text="Transporte",bg="darkturquoise", font=("Times new roman",11))
        label6.place(relx=0.289, rely=0.85,)

        label7=tk.Label(ventana, text="Recurso humano",bg="darkturquoise", font=("Times new roman",11))
        label7.place(relx=0.47, rely=0.85,)

        label8=tk.Label(ventana, text="Extrusora de frio",bg="darkturquoise", font=("Times new roman",11))
        label8.place(relx=0.67, rely=0.85,)

        label9=tk.Label(ventana, text="INSTRUCCIONES", bg="yellow", font=("Times new roman",11))
        label9.place(relx=0.78, rely=0.1)

        label10=tk.Label(ventana, text="•La medida de tiempo es en horas.", bg="darkturquoise", font=("Times new roman",11))
        label10.place(relx=0.73, rely=0.19)

        label11=tk.Label(ventana, text="•Si desea puede regresar al menu.", bg="darkturquoise", font=("Times new roman",11))
        label11.place(relx=0.73, rely=0.26)

        label12=tk.Label(ventana, text="•Se maneja un limite de horas \n por proceso (24h).", bg="darkturquoise", font=("Times new roman",11))
        label12.place(relx=0.73, rely=0.33)

        label13=tk.Label(ventana, text="•Si tiene mas dudas consulte \n el menu de ayuda.", bg="darkturquoise", font=("Times new roman",11))
        label13.place(relx=0.73, rely=0.41)



        ventana.mainloop()
        
        
    def pedidos():
        
        import tkinter as tk
        from tkinter.constants import END
        from tkinter import  IntVar, messagebox,Spinbox
        from tkinter import ttk
        
        
        def calcular():
            pieza = combopieza.get()
            cortem = lista_cortem.get()
            acabado = lista_acabado.get()
            horno = lista_horno.get()
            pintura = lista_pintura.get()
            transporte = lista_transporte.get()
            humano = lista_humano.get()
            extrusora = lista_extrusora.get()
            pedidos=lista_pedido.get()
    
            cantidad=lista_cantidad.get()
    
    
    
            pieza = (pieza)
            cortem = float(cortem)
            acabado = float(acabado)
            horno = float(horno)
            pintura = float(pintura)
            transporte = float(transporte)
            humano = float(humano)
            extrusora = float(extrusora)
            pedidos=float(pedidos)
            cantidad= float(cantidad)
    
    
    
            timet=(cortem+acabado+horno+pintura+transporte+humano+extrusora)*cantidad
            horasm=(cortem+acabado+horno+pintura+transporte+extrusora)*cantidad
            horash=humano*cantidad


            listbox.insert(END,("-------------------------------------------------------------------------"))
            listbox.insert(END,("\n"))
            listbox.insert(END,("Pedido ",pedidos))
            listbox.insert(END,("\n"))
            listbox.insert(END,(pieza))
            listbox.insert(END,("\n"))
            listbox.insert(END,(" La duracion de frabricacion de las piezas seleccionada es de", timet,"horas"))
            listbox.insert(END,("\n"))
            listbox.insert(END,(" La duracion en el proceso de las maquinas es de", horasm,"horas"))
            listbox.insert(END,("\n"))
            listbox.insert(END,(" La duracion de la pieza en el recurso humano es de ", horash,"horas"))
            listbox.insert(END,("\n"))
  
        def calcular1():
    
    
            capot=lista_capot.get()
            cabrilla=lista_cabrilla.get()
            baul=lista_baul.get()
            pedidos=lista_pedido.get()
            capot=float(capot)
            cabrilla=float(cabrilla)
            baul=float(baul)
            pedidos=float(pedidos)
    
            Duraciont=capot+cabrilla+baul
    
            resultados=open("Resultados.txt","w")
            resultados.write(" La duracion de frabricacion del pedido es de "+ str(Duraciont)+"horas"+"\n")
            resultados.close()

            listbox.insert(END,("-------------------------------------------------------------------------"))
            listbox.insert(END,("\n"))
    
            listbox.insert(END,("\n"))
            listbox.insert(END,(" La duracion de frabricacion del pedido es de ", Duraciont,"horas"))
            listbox.insert(END,("\n"))

            if Duraciont > 192:
                listbox.insert(END,("No se tiene suficiente tiempo para realizar el pedido",pedidos))
            if Duraciont <= 192:
                listbox.insert(END,("¡Excelente!, Hay tiempo suficiente para elaborar el pedido", pedidos))
        
    

        def salir():
    
            respuesta=messagebox.askyesno("Close window ", "¿Deseas volver al menu?")
            if respuesta==True:
             ventana.destroy()
   
 
        ventana=tk.Toplevel()
        ancho_ventana = 1400
        alto_ventana = 900

        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)

        ventana.resizable(0,0)
        ventana.title("Calcular la duracion de cada pedido")
        ventana.config(background="darkturquoise")





        def limpiar():
            listbox.delete(0,1000)
            
        def help():
            
                def salir2():
                
                    respuesta=messagebox.askyesno("Close window ", "¿Deseas volver al menu?")
                    if respuesta==True:
                        ventana.destroy()
    
            
                ventana=tk.Toplevel()
                ancho_ventana = 500
                alto_ventana = 500

                x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
                y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

                posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
                ventana.geometry(posicion)

                ventana.resizable(0,0)
                ventana.title("Calcular tiempo de fabricacion para cada pedido")
                ventana.config(background="white")
            
                label1=tk.Label(ventana, text="Pasos para utilizar el programa", font=("Times new roman",12), bg="white", fg="black")
                label1.pack()
            
            
                label2=tk.Label(ventana, text=" \n •Recuerde que los tiempos se miden en horas", font=("Times new roman",12), bg="white", fg="black")
                label2.pack()
            
                label3=tk.Label(ventana, text=" \n •Paso1: Ingrese los datos que desea calcular", font=("Times new roman",12), bg="white", fg="black")
                label3.pack()
            
                label4=tk.Label(ventana, text="\n •Paso 2: Rectificar que los valores sean los correctos", font=("Times new roman",12), bg="white", fg="black")
                label4.pack()
            
                label5=tk.Label(ventana, text="\n •Paso 3: Oprima el primer boton de calcular", font=("Times new roman",12), bg="white", fg="black")
                label5.pack()
            
                label6=tk.Label(ventana, text="\n •Paso 4: Colocar los valores proporcionados en las casillas correspondientes", font=("Times new roman",12), bg="white", fg="black")
                label6.pack()
                
                label7=tk.Label(ventana, text="\n •Paso 5: Oprimir el segundo boton de calcular", font=("Times new roman",12), bg="white", fg="black")
                label7.pack()
            
                btnsalir=tk.Button(ventana,text="Volver al menu",command=salir2,bg="grey")
                btnsalir.place(relx= 0.42, rely=0.6)
                
        def exit3():
                respuesta=messagebox.askyesno("Close window ", "¿Desea cerrar todo el programa?")
                if respuesta==True:
                    exit()    


    
        #menu

        mi_menu=tk.Menu(ventana)
        ventana.config(menu=mi_menu)


        
        mi_menu.add_command(label="Help",command=help)
        mi_menu.add_command(label="Exit", command=exit3)
        


        #listbox

        listbox=tk.Listbox(ventana)
        listbox.place(relx=0.44, rely=0.07, relwidth=0.5, relheight=0.6)

        #var

        var1 = IntVar()

        var1.set(0)


        #combobox

        combopieza = ttk.Combobox(ventana, 
                            values=[
                                    "Capot",
                                    "Cabrilla",
                                    "Baul"])
        combopieza.place(relx=0.02, rely=0.09)
        #cuadros con spinbox

        cuadro_cortem= tk.Entry(ventana)
        lista_cortem=Spinbox(ventana, from_=0,to=24,state="readonly", textvariable=var1)
        lista_cortem.place(relx=0.15, rely=0.09)

        cuadro_acabado= tk.Entry(ventana)
        lista_acabado=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_acabado.place(relx=0.28, rely=0.09)

        cuadro_horno= tk.Entry(ventana)
        lista_horno=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_horno.place(relx=0.02, rely=0.22)

        cuadro_pintura= tk.Entry(ventana)
        lista_pintura=Spinbox(ventana, from_=0,to=24, state="readonly")
        lista_pintura.place(relx=0.15, rely=0.22)

        cuadro_transporte= tk.Entry(ventana)
        lista_transporte=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_transporte.place(relx=0.28, rely=0.22)

        cuadro_humano= tk.Entry(ventana)
        lista_humano=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_humano.place(relx=0.02, rely=0.332)

        cuadro_extrusora= tk.Entry(ventana)
        lista_extrusora=Spinbox(ventana, from_=0,to=24,state="readonly")
        lista_extrusora.place(relx=0.021, rely=0.42)





        cuadro_cantidad= tk.Entry(ventana)
        lista_cantidad=Spinbox(ventana, from_=0,to=20,state="readonly")
        lista_cantidad.place(relx=0.15, rely=0.332)

        cuadro_pedido= tk.Entry(ventana)
        lista_pedido=Spinbox(ventana, from_=0,to=3,state="readonly")
        lista_pedido.place(relx=0.28, rely=0.332)



        cuadro_capot= tk.Entry(ventana)
        lista_capot=tk.Entry(ventana)
        lista_capot.place(relx=0.15, rely=0.57)

        cuadro_cabrilla= tk.Entry(ventana)
        lista_cabrilla=tk.Entry(ventana)
        lista_cabrilla.place(relx=0.28, rely=0.57)

        cuadro_baul= tk.Entry(ventana)
        lista_baul=tk.Entry(ventana)
        lista_baul.place(relx=0.02, rely=0.57)






        #boton calcular
        boton1= tk.Button(ventana, text="Calcular", bg="green", fg="white", command=calcular)
        boton1.place(relx=0.285, rely=0.4, width=120)

        #boton limpiar
        boton2= tk.Button(ventana, text="Limpiar", bg="red", fg="white",command=limpiar, width=10)
        boton2.place(relx=0.75, rely=0.69)


         ##boton para salir 
        btnsalir=tk.Button(ventana,text="Volver al menu",command=salir,bg="gray")
        btnsalir.place(relx=0.85, rely=0.69)

        boton4= tk.Button(ventana, text="Calcular", bg="green", fg="white", command=calcular1)
        boton4.place(relx=0.285, rely=0.68, width=120)


        #label
        label1=tk.Label(ventana, text="Tipo de pieza",bg="darkturquoise",font=("Times new roman",11))
        label1.place(relx=0.02, rely=0.06)

        label2=tk.Label(ventana, text="Corte mecanizado",bg="darkturquoise",font=("Times new roman",11))
        label2.place(relx=0.15, rely=0.06)

        label3=tk.Label(ventana, text="Acabado",bg="darkturquoise",font=("Times new roman",11))
        label3.place(relx=0.28, rely=0.06)

        label4=tk.Label(ventana, text="Horno y \n tratamiento termico",bg="darkturquoise",font=("Times new roman",11))
        label4.place(relx=0.02, rely=0.17)

        label5=tk.Label(ventana, text="Cabina de pintura",bg="darkturquoise",font=("Times new roman",11))
        label5.place(relx=0.15, rely=0.185)

        label6=tk.Label(ventana, text="Transporte",bg="darkturquoise",font=("Times new roman",11))
        label6.place(relx=0.28, rely=0.185)

        label7=tk.Label(ventana, text="Recurso humano",bg="darkturquoise",font=("Times new roman",11))
        label7.place(relx=0.02, rely=0.30)

        label8=tk.Label(ventana, text="Extrusora de frio",bg="darkturquoise",font=("Times new roman",11))
        label8.place(relx=0.021, rely=0.39)





        label11=tk.Label(ventana, text="Cantidad de piezas",bg="darkturquoise",font=("Times new roman",11))
        label11.place(relx=0.15, rely=0.30)

        label12=tk.Label(ventana, text=" Numero del pedido ",bg="darkturquoise",font=("Times new roman",11))
        label12.place(relx=0.28, rely=0.30)



        label14=tk.Label(ventana, text=" Tiempo del capot",bg="darkturquoise",font=("Times new roman",11))
        label14.place(relx=0.15, rely=0.54)

        label15=tk.Label(ventana, text=" Tiempo de la cabrilla",bg="darkturquoise",font=("Times new roman",11))
        label15.place(relx=0.28, rely=0.54)

        label16=tk.Label(ventana, text=" Tiempo del baul",bg="darkturquoise",font=("Times new roman",11))
        label16.place(relx=0.02, rely=0.54)






        ventana.mainloop()
        
    
    def salir():
        
        respuesta=messagebox.askyesno("Close window ", "¿Desea cerrar el programa?")
        if respuesta==True:
            exit()

    
    
    
    
    
    
    nombre1= nombre.get() 
    apellido1=apellido.get() 
    
    if nombre1.strip() =="" or apellido1.strip() =="":
        messagebox.showerror(message="Este campo es obligatorio")
    else:  
        labelbienvenida=Label(ventanab, text="Bienvenido, "+ nombre1 +" "+ apellido1, font=("Times new roman",11),)
        labelbienvenida.place(relx= 0.1, rely=0.5)
    
        labeltexto=Label(ventanab, text="Bienvenido a VKSC, este programa le permitira \n calcular los tiempos de fabricacion de la empresa. \n \n A continuacion Debe elegir una de las \n opciones que se muestran a la derecha. ", font=("Times new roman",11))
        labeltexto.place(relx=0.1, rely=0.6)
    
    
        labelv1=Label(ventanab, text="Desea calcular por duracion de: ",font=("Times new roman",11))
        labelv1.place(relx= 0.6, rely=0.6)
    
        boton1= tk.Button(ventanab, text="Piezas", command=piezas)
        boton1.place(relx=0.6, rely=0.7)
    
        boton2= tk.Button(ventanab, text="Pedidos", command= pedidos)
        boton2.place(relx=0.7, rely=0.7)
    
        boton3=tk.Button(ventanab, text="Salir", command=salir, bg="red",fg="white")
        boton3.place(relx=0.8, rely=0.7)
    
    
    
   
    
    

    

    
    
       


#bienvenido
label1=Label(ventanab,text="Bienvenido", font=("Times new roman", 18))
label1.place(relx=0.38, rely=0.06)

nombre= StringVar() 
apellido=StringVar() 


#nombre
label2=Label(ventanab,text="Debe ingresar su nombre:", font=("Times new roman", 11))
label2.place(relx=0.2, rely=0.2)
cuadro_nombre= tk.Entry(ventanab, textvariable=nombre)
cuadro_nombre.place(relx=0.42, rely=0.2)

#apellido
label3=Label(ventanab,text="Debe ingresar su apellido:", font=("Times new roman", 11))
label3.place(relx=0.2, rely=0.3)
cuadro_apellido= tk.Entry(ventanab,textvariable=apellido)
cuadro_apellido.place(relx=0.42, rely=0.3)

#boton
boton1= tk.Button(ventanab, text="Continuar", fg="black", command=continuar)
boton1.place(relx=0.48, rely=0.4, width=80, height=20)





ventanab.mainloop()