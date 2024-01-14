import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

class ergonomy_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ergonomy.ui",self)
        self.lineEdit.setEnabled(False)
        self.pushButton_2.clicked.connect(self.seleccion_handler)
        self.pushButton.clicked.connect(self.analizar)

    def seleccion_handler(self):
        self.d_box()

    def d_box(self):
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        print(path)
        self.photo.setPixmap(QtGui.QPixmap(path))
        self.photo.setScaledContents(True)

    def analizar(self):
        #self.lineEdit.setText("Postura adecuada")
        self.lineEdit.setText("Postura inadecuada")

if __name__== '__main__':
    app=QApplication(sys.argv)
    GUI=ergonomy_gui()
    GUI.show()
    sys.exit(app.exec())