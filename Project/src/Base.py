import time
import smtplib #Nuevos imports para .env, mandar correo, ui y hacer el codigo
import os
from dotenv import load_dotenv

from PyQt5 import QtWidgets, uic, QtGui
from view.Ventana_Ingreso import Ui_Window_Inicio
from view.Ventana_Registro import Ui_Window_Registro
from view.Ventana_Codigo import Ui_Window_Codigo 
from random import randint
import sys


#Cargar archivo ui.py
class Entrada(QtWidgets.QMainWindow):
    def __init__(self):
        super(Entrada, self).__init__()
        self.ui = Ui_Window_Inicio()
        self.ui.setupUi(self)
        self.Opacidad(0)
        self.setFixedSize(810,522)

        #Fondo
        self.ui.Label_Imagen.setPixmap(QtGui.QPixmap("img\Fondo.png"))

    #Opacidad label de error
    def Opacidad(self,Valor): #parametro añadido para multiples labels
        self.Opa = QtWidgets.QGraphicsOpacityEffect()
        self.Opa.setOpacity(Valor)
        self.ui.Label_Datos_Erroneos.setGraphicsEffect(self.Opa)

class Creacion_Usuario(QtWidgets.QMainWindow):
    def __init__(self):
        super(Creacion_Usuario, self).__init__()
        self.ui = Ui_Window_Registro()
        self.ui.setupUi(self)

        # Fondo
        self.ui.Laber_Imagen.setPixmap(QtGui.QPixmap("img\Fondo.png"))

    

class Codigo_Seguridad(QtWidgets.QMainWindow): #pagina de codigo
    def __init__(self):
        super(Codigo_Seguridad,self).__init__()
        self.ui = Ui_Window_Codigo()
        self.ui.setupUi(self)

        self.Opacidad(0)
        #Fondo
        self.ui.Label_Imagen.setPixmap(QtGui.QPixmap("img\Fondo.png"))

    def Opacidad(self,Valor): #parametro añadido para multiples labels
            self.Opa = QtWidgets.QGraphicsOpacityEffect()
            self.Opa.setOpacity(Valor)
            self.ui.textoIncorrecto.setGraphicsEffect(self.Opa)
    
    def Mandar_Codigo(self):
        Codigo = ""
        for i in range(5):
            Codigo += str(randint(0,9))

        message = "Hola, tu codigo es: " + Codigo
        subject = "Envio de Codigo"
        message = 'Subject: {}\n\n{}'.format(subject,message)
        
        load_dotenv() #try if not working, pip install python_dotenv in bash terminal #TODO: add 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        password = os.getenv('passwordDev')
        server.starttls()
        server.login("myunapp3@gmail.com", password)
        server.sendmail ('myunapp3@gmail.com', 'savillotaa@unal.edu.co', message)
        server.quit()

        return Codigo


class Aplicacion(QtWidgets.QMainWindow):
    def __init__(self):
        super(Aplicacion, self).__init__()

        #Creacion repertorio de widgets
        self.Repertorio = QtWidgets.QStackedWidget(self)
        self.Pagina_Entrada = Entrada()
        self.Pagina_Creacion_Usuario = Creacion_Usuario()
        self.Pagina_Codigo_Seguridad = Codigo_Seguridad() #Añadidos para la página codigo
        self.Repertorio.addWidget(self.Pagina_Entrada)
        self.Repertorio.addWidget(self.Pagina_Creacion_Usuario)
        self.Repertorio.addWidget(self.Pagina_Codigo_Seguridad)

        #Widget central del repertorio
        self.setCentralWidget(self.Repertorio)
        self.Repertorio.setCurrentWidget(self.Pagina_Entrada)

        #Inicio
        self.Pagina_Entrada.ui.Ingresar.clicked.connect(self.Analisis)
        self.Pagina_Creacion_Usuario.ui.Boton_Registro.clicked.connect(self.Anadir)

    def Analisis(self):
        self.Correo = self.Pagina_Entrada.ui.Line_Usuario.text() #Correo y Usuario casi lo mismo, Usuario solo antes del @
        self.Usuario = self.Correo.split("@")[0] 
        self.Contraseña = self.Pagina_Entrada.ui.Line_Contrasena.text()
        if self.Correo == "Juan@gmail.com" and self.Contraseña == "12345": #TODO: Implementación con Base de Datos
            self.Cambio_A_Codigo()
            self.Codigo = self.Pagina_Codigo_Seguridad.Mandar_Codigo()
            self.Codigo_en_verificacion()
            

        else:
            self.Pagina_Entrada.Opacidad(1)

    def Anadir(self): #TODO: Añadir implementacion con Base de Datos
        pass

    def Cambio_A_Creacion_Usuario(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Creacion_Usuario)

    def Cambio_A_Inicio(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Entrada)

    def Cambio_A_Codigo(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Codigo_Seguridad)
        
    
    def Codigo_en_verificacion(self):
        self.Pagina_Codigo_Seguridad.ui.okButton.clicked.connect(self.Verificar_Codigo)
        self.Pagina_Codigo_Seguridad.ui.atrasButton.clicked.connect(self.Cambio_A_Inicio)


    def Verificar_Codigo(self):
        self.codigo_usr = self.Pagina_Codigo_Seguridad.ui.mostrar_texto()
        if self.Codigo == self.codigo_usr:
            print("Todo Correcto") #TODO: Conectar Menú
        else:
            self.Pagina_Codigo_Seguridad.Opacidad(1)




#Ejecutable
app = QtWidgets.QApplication([])
application = Aplicacion()
application.show()
sys.exit(app.exec())


