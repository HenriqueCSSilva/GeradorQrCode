import sys
import os
from pathlib import Path
import pyqrcode
from geradorQR import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox



class GeradorQr(QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_gera.clicked.connect(self.gerarQrCode)

    def gerarQrCode(self):
        nome_arquivo = self.txt_nome_arquvo.text()
        link = self.txt_link.text()
        try:
            meuQR = pyqrcode.create(link)
            pasta = os.getcwd()+f'/QrCode/{nome_arquivo}'
            Path(pasta).mkdir(parents=True, exist_ok=True)
            os.chdir(pasta)

            meuQR.svg(f'{nome_arquivo}.svg', scale=6)
            meuQR.png(f'{nome_arquivo}.png', scale=6)
            meuQR.svg(f'{nome_arquivo}_escala_8.svg', scale=8)
            meuQR.png(f'{nome_arquivo}_escala_8.png', scale=8)

            QMessageBox.about(self, "Sucesso", "Gerado - Verifique a pasta")
        except:
            QMessageBox.about(self, "Erro", "Não Gerado")


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    setupQr = GeradorQr()
    setupQr.show()
    qt.exec_()