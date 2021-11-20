from tkinter import *
import serial
import time

#------------------------------Creacion de la ventana------------------------------------------
ventana = Tk()
ventana.title("Estacionamiento")
ventana.config(bg="black")

#-------------------------Creacion de encabezado y paneles pricnipales-----------------------------------
encabezado = Label(ventana, text = "Estacionamiento Inteligente")
encabezado.grid(row=1, column= 0, columnspan=10)
encabezado.config(
    bg="black",
    fg="white",
    font =("Arial Nova", 35),
    pady=5

)

reco= Label(ventana, text= "Lugar recomendado: ")
reco.grid(row=2, column= 2, columnspan=5)
reco.config(
    bg="gray",
    fg="black",
    font =("Arial Nova", 25),
    pady=5

)
estado = Label(ventana, text = "Estado del estacionamiento: ")
estado.grid(row=3, column= 0)
estado.config(
    bg="black",
    fg="white",
    font =("Arial Nova", 15),
    pady=5
)

#-----------Funciones----------------------------------------
#------Lectura de la linea de texto con el valor de los sensores recibidos por arduino
def leer():
    serialArduino = serial.Serial("COM5", 9600)
    time.sleep(1)
    cad = serialArduino.readline().decode('ascii')
    
    serialArduino.close()
    
#---Valores iniciales de las variables para el estado del estacionamiento
    ocupados = 0
    libres = 0
    recomendado = "No hay lugares disponibles"

#---Mapeo de la entrada y salida del estacionamiento
    entrada = Label(ventana, text="Entrada")
    entrada.grid(row=5, column=0)
    entrada.config(
        bg="gray",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    salida = Label(ventana, text="Salida")
    salida.grid(row=11, column=0)
    salida.config(
        bg="gray",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )
    #----------------Separadores----------------------------------------------------------------

    separador = Label(ventana)
    separador.grid(row=6,column=0)
    separador.config(
        bg="black",
        fg="black"
    )

    separador2 = Label(ventana)
    separador2.grid(row=8,column=0)
    separador2.config(
        bg="black",
        fg="black"
    )

    separador3 = Label(ventana)
    separador3.grid(row=10,column=0)
    separador3.config(
        bg="black",
        fg="black"
    )

    separador4 = Label(ventana)
    separador4.grid(row=5,column=2)
    separador4.config(
        padx=5,
        height=4,
        width=10,
        bg="black",
        fg="black"
    )


    separador5 = Label(ventana)
    separador5.grid(row=5,column=4)
    separador5.config(
        bg="black",
        fg="black"
    )

    separador6 = Label(ventana)
    separador6.grid(row=5,column=6)
    separador6.config(
        padx=5,
        height=4,
        width=10,
        bg="black",
        fg="black"
    )

    separador7 = Label(ventana)
    separador7.grid(row=12,column=0)
    separador7.config(
        bg="black",
        fg="black"
    )

    #----------------Cajones--------------------------------------------------------------------
    
    A1 = Label(ventana, text="A1")
    A1.grid(row=5, column=1)
    A1.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    A2 = Label(ventana, text="A2")
    A2.grid(row=7, column=1)
    A2.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    A3 = Label(ventana, text="A3")
    A3.grid(row=9, column=1)
    A3.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    A4 = Label(ventana, text="A4")
    A4.grid(row=11, column=1)
    A4.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )



    B1 = Label(ventana, text="B1")
    B1.grid(row=5, column=3)
    B1.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    B2 = Label(ventana, text="B2")
    B2.grid(row=7, column=3)
    B2.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    B3 = Label(ventana, text="B3")
    B3.grid(row=9, column=3)
    B3.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    B4 = Label(ventana, text="B4")
    B4.grid(row=11, column=3)
    B4.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )





    C1 = Label(ventana, text="C1")
    C1.grid(row=5, column=5)
    C1.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    C2 = Label(ventana, text="C2")
    C2.grid(row=7, column=5)
    C2.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    C3 = Label(ventana, text="C3")
    C3.grid(row=9, column=5)
    C3.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    C4 = Label(ventana, text="C4")
    C4.grid(row=11, column=5)
    C4.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )




    D1 = Label(ventana, text="D1")
    D1.grid(row=5, column=7)
    D1.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    D2 = Label(ventana, text="D2")
    D2.grid(row=7, column=7)
    D2.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    D3 = Label(ventana, text="D3")
    D3.grid(row=9, column=7)
    D3.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )

    D4 = Label(ventana, text="D4")
    D4.grid(row=11, column=7)
    D4.config(
        bg="red",
        fg="black",
        font=("Arial Nova", 12),
        height=4,
        width=10,
        pady=5,
        padx=5
    )


    #consulta = input("Consultar estado del estacionamiento: ")
    consulta = True

    if consulta == True:
        #if vent == True:
         #   ventana.destroy()

        
        print(cad)
    
        print("**********************")
        CA1= int(cad[0])
        CA3= int(cad[2])
        CB2= int(cad[4])
        CB4= int(cad[6])
        CC1= int(cad[8])
        CC3= int(cad[10])
        CD2= int(cad[12])
        CD4= int(cad[14])

        lista = [CA1,CA3,CB2,CB4,CC1,CC3,CD2,CD4]

        for i in lista:
            if lista[i] == 1:
                ocupados = ocupados+1
            else:
                libres = libres+1

            
        ocupados = ocupados + 8
        

        if libres >0:
            if CD4 ==0:
                recomendado = "D4"
                #D4.config(bg="green")
            elif CD2==0:
                recomendado = "D2"
                #CD2.config(bg="green")
            elif CC3==0:
                recomendado = "C3"
                #C3.config(bg="green")
            elif CC1==0:
                recomendado = "C1"
                #CC1.config(bg="green")
            elif CB4==0:
                recomendado = "B4"
                #B4.config(bg="green")
            elif CB2==0:
                recomendado = "B2"
                #B2.config(bg="green")
            elif CA3==0:
                recomendado = "A3"
                #A3.config(bg="green")
            elif CA1==0:
                recomendado = "A1"
                #A1.config(bg="green")


            if CD4 ==0:
                
                D4.config(bg="green")

            if CD2==0:
                
                D2.config(bg="green")

            if CC3==0:
                
                C3.config(bg="green")

            if CC1==0:
                
                C1.config(bg="green")

            if CB4==0:
                
                B4.config(bg="green")

            if CB2==0:
               
                B2.config(bg="green")

            if CA3==0:
                
                A3.config(bg="green")

            if CA1==0:
                
                A1.config(bg="green")

            reco= Label(ventana, text= "Lugar recomendado: " + recomendado)
            reco.grid(row=2, column= 2, columnspan=5)
            reco.config(
                bg="gray",
                fg="black",
                font =("Arial Nova", 25),
                pady=5

                )
            

        print("***************************")
        print("Estado del estacionamiento")
        print("Lugares ocupados: " + str(ocupados))
        print("Lugares disponibles: " + str(libres))
        print("lugar recomendado: "+ recomendado)
        ocupados = 0
        libres = 0
        recomendado = ""
        ventana.update()
        
        




#-------------------Boton actualizar--------------------------------

refresh = Button (ventana, text="Ingresar", command=leer)
refresh.grid(row=14, column=1, columnspan=8)
refresh.config(
    bg="blue",
    fg="white",
    height=3,
    font= ("Arial Nova", 14),
    width=50
)

#-------------------------------------Loop-----------------------
ventana.mainloop()