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
        #verificar_clave_exitosa
        if clave1 in verifica:
            menu_calculos() 
        #si no se eencuentra en el registro
        else:
            #no clave
            no_clave() 
    else:
        #no usuario registrado
        no_usuario() 


# Ventana de login exito
 
def menu_calculos():
    global menu_principal
    pestas_color="DarkGrey"
    menu_principal=Tk()
    menu_principal.geometry("600x300")#DIMENSIONES DE LA VENTANA
    menu_principal.title("Menu")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Poligonal", height="2", width="30", bg=pestas_color, command="poligonal").pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Nivelacio", height="2", width="30", bg=pestas_color, command="Nivelacion").pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    menu_principal.mainloop()
 
#Ventana emergente clave incorrecto.
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("VERIFIQUE")
    ventana_no_clave.geometry("300x100")
    Label(ventana_no_clave, text="Contraseña o  Usuario Incorrecto ").pack()
    #borrar clave de ventana
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() 
 
#Ventana Usuaario Incorrecto.
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("VERIFIQUE")
    ventana_no_usuario.geometry("300x100")
    Label(ventana_no_usuario, text="Contraseña o  Usuario Incorrecto").pack()
    #borrar usuario de ventana
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() 


def borrar_exito_login():
    ventana_exito.destroy()
 
 
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




def ventana_menu():
    global ventana_menu_inicio
    pestas_color="DarkGrey"
    vantana_menu_inicio =Tk()
    #creacion de dimenciones
    vantana_menu_inicio.geometry("300x250")
    #titulo de ventana
    vantana_menu_inicio.title("MENU ")
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    #boton acceder
    Button(text="Poligonal", height="2", width="30", bg=pestas_color, command=Poligonal).pack() 
    Label(text="").pack()
    #boton registrarse
    Button(text="Nivelacion", height="2", width="30", bg=pestas_color, command="Calculo_de_nivelacion").pack() 
    Label(text="").pack()
    vantana_menu_inicio.mainloop()

def Poligonal():
    global ventana_poligonal
    ventana_poligonal = Toplevel(ventana_menu)
    ventana_poligonal.title("Registro")
    ventana_poligonal.geometry("300x250")
 
    Button(ventana_poligonal, text="Poligonal", width=10, height=1, bg="LightGreen", command = "Poligonal_Opcion").pack() #BOTÓN "Registrarse"

ventana_menu()



    



#crear login
