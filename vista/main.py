import  sys

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui

""" Importamos todas nuetras Ventana y funciones utiles"""
from home import  *
from analizador_lexico import *

class Main(QMainWindow):
    """ Clase principal de nuestra app"""
    def __init__(self):
        """ Incializamos nuestra app"""
        QMainWindow.__init__(self)


        # Instaciamos nuestra ventanas widget home
        self.home = Ui_home()
        self.home.setupUi(self)

        # Eventos
        self.home.bt_lexico.clicked.connect(self.ev_lexico)
        self.home.bt_sintactico.clicked.connect(self.ev_sintactico)

        self.home.bt_archivo.clicked.connect(self.ev_archivo)
        self.home.bt_limpiar.clicked.connect(self.ev_limpiar)

        self.home.estado.showMessage("Desarrollando por Michael Abril y Maryon Torres")

    def ev_lexico(self):
        print("lexico")
        datos = self.home.tx_ingreso.toPlainText().strip()

        resultado_lexico = prueba(datos)

       # self.home.tx_lexico.setText("Analizando lexico")
        cadena= ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
            print(lex)
        self.home.tx_lexico.setText(cadena)


    def ev_sintactico(self):
        print("sintactico")
        self.home.tx_sintactico.setText("Analisis sintactico")

    def ev_archivo(self):
        dlg = QFileDialog()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.home.tx_ingreso.setText(data)

    def ev_limpiar(self):
        self.home.tx_ingreso.setText('')
        self.home.tx_lexico.setText('')
        self.home.tx_sintactico.setText('')




def iniciar():
    # Instaciamos nuestro app por defecto esto no cambia
    app = QApplication(sys.argv)

    # Instaciomos nuestro ventana
    ventana = Main()
    # Mostramos nuestra app
    ventana.show()

    #Controlamos el cierre de la app
    sys.exit(app.exec_())


if __name__ == '__main__':
    iniciar()
