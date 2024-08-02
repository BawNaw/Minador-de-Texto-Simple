#Minador de Texto de Luis Bowzer y Ramiro Romero Para la profesora Jahel Yeraldin

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.titulo = 'Minador de Texto de Bowzer'
        self.ancho = 800
        self.alto = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.titulo)
        self.setGeometry(100, 100, self.ancho, self.alto)
        self.setWindowIcon(QIcon('dragon-logo.jpg'))

        layout_principal = QVBoxLayout()

        widget_central = QWidget(self)
        self.setCentralWidget(widget_central)
        widget_central.setLayout(layout_principal)

        self.editor_texto = QTextEdit()
        self.boton_contar_palabras = QPushButton('Contar Palabras')
        self.entrada_busqueda = QLineEdit()
        self.boton_buscar_palabra = QPushButton('Buscar Palabra')
        self.etiqueta_resultado = QLabel('Resultado: ')

        layout_principal.addWidget(self.editor_texto)
        layout_principal.addWidget(self.entrada_busqueda)
        layout_principal.addWidget(self.boton_contar_palabras)
        layout_principal.addWidget(self.boton_buscar_palabra)
        layout_principal.addWidget(self.etiqueta_resultado)

        self.boton_contar_palabras.clicked.connect(self.contarPalabras)
        self.boton_buscar_palabra.clicked.connect(self.buscarPalabra)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #000;
            }
            QTextEdit {
                background-color: #0a0a0a;
                color: #fff;
            }
            QPushButton {
                background-color: #007bff;
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QLabel {
                color: #fff;
            }
        """)


    def contarPalabras(self):
        texto = self.editor_texto.toPlainText()
        total_palabras = len(texto.split())
        self.etiqueta_resultado.setText(f'Resultado: {total_palabras} palabras')

    def buscarPalabra(self):
        texto = self.editor_texto.toPlainText()
        palabra_buscar = self.entrada_busqueda.text()
        frecuencia = texto.lower().split().count(palabra_buscar.lower())
        self.etiqueta_resultado.setText(f'Resultado: La palabra "{palabra_buscar}" aparece {frecuencia} veces')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()