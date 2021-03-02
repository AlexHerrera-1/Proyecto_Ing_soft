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
    ventana_principal.title("Login Usuario ")
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    #boton acceder
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack() 
    Label(text="").pack()
    #boton registrarse
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() 
    Label(text="").pack()
    ventana_principal.mainloop()
    
    

#ventana de registro
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    #nombre de usuario
    nombre_usuario = StringVar() 
    #clave de usuario
    clave = StringVar() 
 
    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    #introdusca el nombre de usuario
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) 
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    #introdusca la contraseña
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') 
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

#ventana login

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Usuario Registrado")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

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
    ventana_menu.title("MENU DE PRINCIPAL")
    ventana_menu.geometry("200x200")
    Label(ventana_menu, text="MENU DE OPCIONES").pack()
    Button(ventana_menu, text="POLIGONAL", command= opcion_equipo).pack()
    Button(ventana_menu, text="NIVELACIOL", command=Nivelaciones_opcion).pack()
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("VERIFIQUE")
    ventana_no_usuario.geometry("300x100")
    Label(ventana_no_usuario, text="Contraseña o  Usuario Incorrecto").pack()
    #borrar usuario de ventana
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() 

#Aconsejar al usuario
def opcion_equipo():
    global ventana_opcion_equipo
    ventana_opcion_equipo = Toplevel(ventana_login)
    ventana_opcion_equipo.title("EQUIPOS")
    ventana_opcion_equipo.geometry("600x200")
    Label(ventana_opcion_equipo, text="ESCOJA EN EQUIPO CON EL QUE REALIZO LA POLIGONAL").pack()

    Button(ventana_opcion_equipo, text="ESTACION TOTAL", command=consejo_estacion).pack()


    Button(ventana_opcion_equipo, text="TEODOLITO", command=ajuste_transito).pack()
    

    Button(ventana_opcion_equipo, text="TRANSITO", command=ajuste_crandall).pack()

def consejo_estacion():
    global ventana_consejo_estacion
    ventana_consejo_estacion = Toplevel(ventana_login)
    ventana_consejo_estacion.title("EL MEJOR AJUSTE QUE SE PUEDE REALIZAR")
    ventana_consejo_estacion.geometry("500x200")
    Label(ventana_consejo_estacion, text="EL MEJOR METODO DE AJUSTE ").pack()
    Label(ventana_consejo_estacion, text="QUE SE PUEDE RALIZAR ES CRANDALL").pack()
    Label(ventana_consejo_estacion, text="POR EL EQUIPO CON EL QUE SE RALIZO").pack()

    Button(ventana_consejo_estacion, text="AJUSTE POR CRANDALL", command=ajuste_crandall).pack()


    Button(ventana_consejo_estacion, text="DESEO OTRO AJUSTE", command=Poligonales_opcion).pack()


def Poligonales_opcion():
    global ventana_Poligonal_opciones
    ventana_Poligonal_opciones = Toplevel(ventana_login)
    ventana_Poligonal_opciones.title("METODOS DE AJUSTE DE POLIGONALES")
    ventana_Poligonal_opciones.geometry("300x200")
    Label(ventana_Poligonal_opciones, text="AJUSTES MANEJADOS EN EL PROGRAMA").pack()
    Button(ventana_Poligonal_opciones, text="BRUJULA", command=ajuste_brujula).pack()
    Button(ventana_Poligonal_opciones, text="TRANSITO", command=ajuste_transito).pack()
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
    Label(ventana_Nivelaciones_opciones, text="AJUSTES MANEJADOS EN EL PROGRAMA").pack()
    Button(ventana_Nivelaciones_opciones, text="RELATIVO A NUMERO DE CAMBIOS", command=ajuste_por_cambios).pack()
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




