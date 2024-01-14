import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ergonomy_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ergonomy.ui",self)
        self.lineEdit.setEnabled(False)
        #self.inadecuada()

    def adecuada(self):
        self.lineEdit.setText("Postura adecuada")
    
    def inadecuada(self):
        self.lineEdit.setText("Postura inadecuada")

if __name__== '__main__':
    app=QApplication(sys.argv)
    GUI=ergonomy_gui()
    GUI.show()
    sys.exit(app.exec())