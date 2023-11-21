import sys
from guipalabra_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ventana(QWidget):
  def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.lector)

        imagen = QImage("logo_eafit_completo.png")
        sImagen = imagen.scaled(120, 100)

        etiquetaImagen = QLabel(self)
        etiquetaImagen.setPixmap(QPixmap.fromImage(sImagen))

        layout = QVBoxLayout(self)
        layout.addWidget(etiquetaImagen, alignment=Qt.AlignTop | Qt.AlignLeft)

  def lector(self):
        l = self.ui.textoentrada.toPlainText()#entrada
        self.ui.label_3.setText(l)
        

if __name__ == "__main__":
         mi_aplicacion = QApplication(sys.argv)
         mi_app = Ventana()
         mi_app.show()
         sys.exit(mi_aplicacion.exec_())
