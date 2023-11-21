import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from guipalabra_ui import *
from PyQt5.QtWidgets import *
import re

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.validarPalabraEnDiccionario)

        imagen = QImage("C:/Users/aleja/PycharmProjects/Interfaz_G/gui/logo_eafit_completo.png")
        sImagen = imagen.scaled(120, 100)

        etiquetaImagen = QLabel(self)
        etiquetaImagen.setPixmap(QPixmap.fromImage(sImagen))

        layout = QVBoxLayout(self)
        layout.addWidget(etiquetaImagen, alignment=Qt.AlignTop | Qt.AlignLeft)

    def leer_diccionario(self, dics):
        word_list = []
        for archivos in os.listdir(dics):
            ruta_archivo = os.path.join(dics, archivos)
            if os.path.isfile(ruta_archivo) and archivos.endswith(".txt"):
                with open(ruta_archivo, 'r', encoding="utf-8") as f:
                    palabras = f.read()
                    palabras = palabras.split()
                    for palabra in palabras:
                        word_list.append(palabra)
        return word_list

    def analizador_lexicografico(self, cadena):
        try:
            cont_emojis = 0
            cont_cadena = 0
            emojis = {
                ":)": "😊",
                ":(": "😢",
                ":D": "😃",
                ";)": "😛",
                ":p": "😮",
                "xD": "😕",
                ":-)": "😉",
                ":-(": "😘",
                "(y)": "❤",
                "(n)": "😎",
                "<3": "😸",
                "\\m/": "😐",
                ":-o": "😖",
                ":o": "🙌",
                ":-|": "👍",
                ":|": "😅",
                ":*": "🫥",
                ">:(": "😶‍🌫️",
                "^^": "🤐",
                ":-]": "🤑"
            }
            dics = "C:/Users/aleja/PycharmProjects/Interfaz_G/dics"
            pattern = re.compile('|'.join(re.escape(k) for k in emojis.keys()), re.IGNORECASE)
            find = pattern.search(cadena)
            cadena_dic = cadena
            if find is None:
                return cadena
            while find is not None:
                cont_emojis += 1
                emoji = emojis[find.group(0)]     #Te devuelve la cadena encontrada, por ejemplo, ":)" te de vuelve el emoji
                span_inicio, span_final = find.span()
                cadena_delete = cadena[span_inicio:span_final]
                cadena = cadena.replace(cadena_delete, emoji)
                cadena_dic = cadena_dic.replace(cadena_delete, " ")
                find = pattern.search(cadena)

            diccionario = self.leer_diccionario(dics)
            str_dics = cadena_dic.lower()
            str_dics = str_dics.split()
            for word in str_dics:
                val = diccionario.__contains__(word)
                cont_cadena += 1 if val else 0

            print(cadena)
            print(f"Palabras: {cont_cadena} emojis: {cont_emojis}")
            self.ui.label_3.setText(cadena)
            self.ui.label_4.setText(f"Palabras: {cont_cadena} y emojis: {cont_emojis}")


        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"

    def validarPalabraEnDiccionario(self):
        palabra = self.ui.textoentrada.toPlainText()
        self.analizador_lexicografico(palabra)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

