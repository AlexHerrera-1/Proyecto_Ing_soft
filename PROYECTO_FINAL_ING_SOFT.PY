#Importar linrerias
from tkinter import *
import os


#Creacion de ventana.
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    #creacion de dimenciones
    ventana_principal.geometry("300x250")
    #titulo de ventana
    ventana_principal.title("LOGIN USUARIO")
    Label(text="ESCOJA SU OPCION", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    #boton acceder
    Button(text="ACCEDER", height="2", width="30", bg=pestas_color, command=login).pack() 
    Label(text="").pack()
    #boton registrarse
    Button(text="REGISTRARSE", height="2", width="30", bg=pestas_color, command=registro).pack() 
    Label(text="").pack()
    ventana_principal.mainloop()
    
    

#ventana de registro
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("REGISTRO")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    #nombre de usuario
    nombre_usuario = StringVar() 
    #clave de usuario
    clave = StringVar() 
 
    Label(ventana_registro, text="INTRODUSCA SUS DATOS", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="NOMBRE DE USUARIO * ")
    etiqueta_nombre.pack()
    #introdusca el nombre de usuario
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) 
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="CONTRASEÑA * ")
    etiqueta_clave.pack()
    #introdusca la contraseña
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') 
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="REGISTRESE", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

#ventana login

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("USUARIO REGISTRADO")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="INTRODUSCA NOMBRE DE USUARIO Y CONTRASEÑA").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="NOMBRE USUARIO * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="CONTRASEÑA * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="ACCEDER", width=10, height=1, command = verifica_login).pack()

#verificacion de login

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    #borrar ingormacion al mostrar nueva ventana
    entrada_login_usuario.delete(0, END) 
    #borrar contrasela al mostrar nueva venta
    entrada_login_clave.delete(0, END) 
 
    #generar lista de guardar registros
    lista_archivos = os.listdir() 
   #leer lista de usuarios registrados
    if usuario1 in lista_archivos:
        #abrir archivo para leer usuarios 
        archivo1 = open(usuario1, "r") 

        #leer el archivo de nombres y contraseñas
        verifica = archivo1.read().splitlines() 
        #verificar_clave_exitosa_ventana_menu
        if clave1 in verifica:
            menu_calculos() 
        #si no se eencuentra en el registro
        else:
            #no clave
            no_clave() 
    else:
        #no usuario registrado
        no_usuario() 



# Ventana de menu
 

#Ventana emergente clave incorrecto.
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("VERIFIQUE")
    ventana_no_clave.geometry("300x100")
    Label(ventana_no_clave, text="Contraseña o  Usuario Incorrecto ").pack()
    #borrar clave de ventana
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() 
 
#Ventana menu de calculo.
def menu_calculos():
    global ventana_menu
    ventana_menu = Toplevel(ventana_login)
    ventana_menu.title("MENU DE LEVANTAMIENTO")
    ventana_menu.geometry("400x200")
    Label(ventana_menu, text="TIPO DE LEVANTAMIENTO").pack()
    Label(ventana_menu, text= "").pack()
    Button(ventana_menu, text="POLIGONAL", command= opcion_equipo).pack()
    Label(ventana_menu, text= "").pack()
    Button(ventana_menu, text="NIVELACIOL", command=opcion_nivelacion).pack()
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("VERIFIQUE")
    ventana_no_usuario.geometry("300x100")
    Label(ventana_no_usuario, text="Contraseña o  Usuario Incorrecto").pack()
    #borrar usuario de ventana
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() 

#Aconsejar al usuario por equipo
def opcion_equipo():
    global ventana_opcion_equipo
    ventana_opcion_equipo = Toplevel(ventana_login)
    ventana_opcion_equipo.title("EQUIPOS")
    ventana_opcion_equipo.geometry("400x200")
    Label(ventana_opcion_equipo, text="ESCOJA EL EQUIPO CON EL QUE REALIZO LA POLIGONAL").pack()
    Label(ventana_opcion_equipo, text="").pack()
    Button(ventana_opcion_equipo, text="ESTACION TOTAL", command=consejo_estacion).pack()
    Label(ventana_opcion_equipo, text="").pack()
    Button(ventana_opcion_equipo, text="TEODOLITO", command=consejo_teodolito).pack()
    Label(ventana_opcion_equipo, text="").pack()
    Button(ventana_opcion_equipo, text="TRANSITO", command=consejo_transito).pack()

#ACONSEJAR Y AJUSTAR POR CRANDAL 
def consejo_estacion():
    global ventana_consejo_estacion
    ventana_consejo_estacion = Toplevel(ventana_login)
    ventana_consejo_estacion.title("EL MEJOR AJUSTE QUE SE PUEDE REALIZAR")
    ventana_consejo_estacion.geometry("500x200")
    Label(ventana_consejo_estacion, text="EL MEJOR METODO DE AJUSTE ").pack()
    Label(ventana_consejo_estacion, text=" ").pack()
    Label(ventana_consejo_estacion, text="QUE SE PUEDE RALIZAR ES CRANDALL").pack()
    Label(ventana_consejo_estacion, text=" ").pack()
    Label(ventana_consejo_estacion, text="POR EL EQUIPO CON EL QUE SE RALIZO").pack()
    Label(ventana_consejo_estacion, text=" ").pack()
    Button(ventana_consejo_estacion, text="AJUSTE POR METODO DE CRANDALL", command=ajuste_crandall).pack()
    Label(ventana_consejo_estacion, text=" ").pack()
    Button(ventana_consejo_estacion, text="DESEO OTRO AJUSTE", command=Poligonales_opcion).pack()


#ACONSEJAR Y AJUSTAR POR METODO DE BRUJULA
def consejo_teodolito():
    global ventana_consejo_teodolito
    ventana_consejo_teodolito = Toplevel(ventana_login)
    ventana_consejo_teodolito.title("EL MEJOR AJUSTE QUE SE PUEDE REALIZAR")
    ventana_consejo_teodolito.geometry("500x200")
    Label(ventana_consejo_teodolito, text="EL MEJOR METODO DE AJUSTE ").pack()
    Label(ventana_consejo_teodolito, text=" ").pack()
    Label(ventana_consejo_teodolito, text="QUE SE PUEDE RALIZAR ES BRUJULA").pack()
    Label(ventana_consejo_teodolito, text=" ").pack()
    Label(ventana_consejo_teodolito, text="POR EL EQUIPO CON EL QUE SE RALIZO").pack()
    Label(ventana_consejo_teodolito, text=" ").pack()
    Button(ventana_consejo_teodolito, text="AJUSTE POR METODO DE BRUJULA", command=ajuste_brujula).pack()
    Label(ventana_consejo_teodolito, text=" ").pack()
    Button(ventana_consejo_teodolito, text="DESEO OTRO AJUSTE", command=Poligonales_opcion).pack()

#CONSEJO Y AJUSTE POR TRANSITO
def consejo_transito():
    global ventana_consejo_transito
    ventana_consejo_transito = Toplevel(ventana_login)
    ventana_consejo_transito.title("EL MEJOR AJUSTE QUE SE PUEDE REALIZAR")
    ventana_consejo_transito.geometry("500x200")
    Label(ventana_consejo_transito, text="EL MEJOR METODO DE AJUSTE ").pack()
    Label(ventana_consejo_transito, text=" ").pack()
    Label(ventana_consejo_transito, text="QUE SE PUEDE RALIZAR ES TRANSITO").pack()
    Label(ventana_consejo_transito, text=" ").pack()
    Label(ventana_consejo_transito, text="POR EL EQUIPO CON EL QUE SE RALIZO").pack()
    Label(ventana_consejo_transito, text=" ").pack()
    Button(ventana_consejo_transito, text="AJUSTE POR METODO DE TRANSITO", command=ajuste_transito).pack()
    Label(ventana_consejo_transito, text=" ").pack()
    Button(ventana_consejo_transito, text="DESEO OTRO AJUSTE", command=Poligonales_opcion).pack()


#OPCIONES DE NIVELACION
def opcion_nivelacion():
    global ventana_opcion_nivelacion
    ventana_opcion_nivelacion = Toplevel(ventana_login)
    ventana_opcion_nivelacion.title("QUE DATOS TIENE")
    ventana_opcion_nivelacion.geometry("400x200")
    Label(ventana_opcion_nivelacion, text="QUE DATOS DE ESTOS TIENE EN SU NIVELACION").pack()
    Label(ventana_opcion_nivelacion, text="").pack()
    Button(ventana_opcion_nivelacion, text="DISTANCIAS", command=consejo_distancia).pack()
    Label(ventana_opcion_nivelacion, text="").pack()
    Button(ventana_opcion_nivelacion, text="CAMBIOS", command=consejo_cambios).pack()


#CONSEJO MEJOR METODO Y AJUSTE NIVELACION DISTANCIAS
def consejo_distancia():
    global ventana_consejo_distancia
    ventana_consejo_distancia = Toplevel(ventana_login)
    ventana_consejo_distancia.title("EL MEJOR AJUSTE QUE SE PUEDE REALIZAR")
    ventana_consejo_distancia.geometry("500x200")
    Label(ventana_consejo_distancia, text="EL MEJOR METODO DE AJUSTE ").pack()
    Label(ventana_consejo_distancia, text=" ").pack()
    Label(ventana_consejo_distancia, text="QUE SE PUEDE RALIZAR ES").pack()
    Label(ventana_consejo_distancia, text=" ").pack()
    Label(ventana_consejo_distancia, text="RELATIVO A LAS DISTANCIAS").pack()
    Label(ventana_consejo_distancia, text=" ").pack()
    Button(ventana_consejo_distancia, text="AJUSTE POR METODO DE DISTANCIAS", command=ajuste_por_distancias).pack()
    Label(ventana_consejo_distancia, text=" ").pack()
    Button(ventana_consejo_distancia, text="DESEO OTRO AJUSTE", command=Nivelaciones_opcion).pack()

#CONSEJO MEJOR METODO Y AJUSTE NIVELACION CAMBIOS
def consejo_cambios():
    global ventana_consejo_cambios
    ventana_consejo_cambios = Toplevel(ventana_login)
    ventana_consejo_cambios.title("EL MEJOR AJUSTE QUE SE PUEDE REALIZAR")
    ventana_consejo_cambios.geometry("500x200")
    Label(ventana_consejo_cambios, text="EL MEJOR METODO DE AJUSTE ").pack()
    Label(ventana_consejo_cambios, text=" ").pack()
    Label(ventana_consejo_cambios, text="QUE SE PUEDE RALIZAR ES").pack()
    Label(ventana_consejo_cambios, text=" ").pack()
    Label(ventana_consejo_cambios, text="RELATIVO A LOS CAMBIOS").pack()
    Label(ventana_consejo_cambios, text=" ").pack()
    Button(ventana_consejo_cambios, text="AJUSTE POR METODO DE CAMBIOS", command=ajuste_por_cambios).pack()
    Label(ventana_consejo_cambios, text=" ").pack()
    Button(ventana_consejo_cambios, text="DESEO OTRO AJUSTE", command=Nivelaciones_opcion).pack()



#OPCIONES DE AJUSTE DE POLIGONAL
def Poligonales_opcion():
    global ventana_Poligonal_opciones
    ventana_Poligonal_opciones = Toplevel(ventana_login)
    ventana_Poligonal_opciones.title("METODOS DE AJUSTE DE POLIGONALES")
    ventana_Poligonal_opciones.geometry("300x200")
    Label(ventana_Poligonal_opciones, text="AJUSTES MANEJADOS EN EL PROGRAMA").pack()
    Label(ventana_Poligonal_opciones,text= " ").pack()
    Button(ventana_Poligonal_opciones, text="BRUJULA", command=ajuste_brujula).pack()
    Label(ventana_Poligonal_opciones,text= " ").pack()
    Button(ventana_Poligonal_opciones, text="TRANSITO", command=ajuste_transito).pack()
    Label(ventana_Poligonal_opciones,text= " ").pack()
    Button(ventana_Poligonal_opciones, text="CRANDALL", command=ajuste_crandall).pack()

 
def ajuste_brujula():
    j="nose"

def ajuste_transito():
    k="h"
def ajuste_crandall():
    l="Nose"


#ventana ajuste de nivelacion
def Nivelaciones_opcion():
    global ventana_Nivelaciones_opciones
    ventana_Nivelaciones_opciones = Toplevel(ventana_login)
    ventana_Nivelaciones_opciones.title("METODOS DE AJUSTE DE NIVELACIONES")
    ventana_Nivelaciones_opciones.geometry("300x200")
    Label(ventana_Nivelaciones_opciones, text= " ").pack()
    Label(ventana_Nivelaciones_opciones, text="AJUSTES MANEJADOS EN EL PROGRAMA").pack()
    Label(ventana_Nivelaciones_opciones, text= " ").pack()
    Button(ventana_Nivelaciones_opciones, text="RELATIVO A NUMERO DE CAMBIOS", command=ajuste_por_cambios).pack()
    Label(ventana_Nivelaciones_opciones, text= " ").pack()
    Button(ventana_Nivelaciones_opciones, text="RELATIVO A DISTANCIA NIVELADA", command=ajuste_por_distancias).pack()

def ajuste_por_cambios():
    ñ="nose"

def ajuste_por_distancias():
    g="Nose"
 



def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()



#Registro de usuario
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
    #abrir archivo nombre y clave
    file = open(usuario_info, "w") 
    #escribir archivo nombre y clave
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
 #Cerrar ventanas



ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.




