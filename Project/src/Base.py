import time

from PyQt5 import QtWidgets, uic, QtGui
from view.Ventana_Ingreso import Ui_Window_Inicio
from view.Ventana_Registro import Ui_Window_Registro
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
    def Opacidad(self,Valor):
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


class Aplicacion(QtWidgets.QMainWindow):
    def __init__(self):
        super(Aplicacion, self).__init__()

        #Creacion repertorio de widgets
        self.Repertorio = QtWidgets.QStackedWidget(self)
        self.Pagina_Entrada = Entrada()
        self.Pagina_Creacion_Usuario = Creacion_Usuario()
        self.Repertorio.addWidget(self.Pagina_Entrada)
        self.Repertorio.addWidget(self.Pagina_Creacion_Usuario)

        #Widget central del repertorio
        self.setCentralWidget(self.Repertorio)
        self.Repertorio.setCurrentWidget(self.Pagina_Entrada)

        #Inicio
        self.Pagina_Entrada.ui.Ingresar.clicked.connect(self.Analisis)
        self.Pagina_Creacion_Usuario.ui.Boton_Registro.clicked.connect(self.Anadir)

    def Analisis(self):
        self.Usuario = self.Pagina_Entrada.ui.Line_Usuario.text()
        self.Contraseña = self.Pagina_Entrada.ui.Line_Contrasena.text()
        if self.Usuario == "Juan" and self.Contraseña == "12345":
            self.Cambio_A_Creacion_Usuario()
        else:
            self.Pagina_Entrada.Opacidad(1)

    def Anadir(self):
        pass

    def Cambio_A_Creacion_Usuario(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Creacion_Usuario)

    def Cambio_A_Inicio(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Entrada)


#Ejecutable
app = QtWidgets.QApplication([])
application = Aplicacion()
application.show()
sys.exit(app.exec())


