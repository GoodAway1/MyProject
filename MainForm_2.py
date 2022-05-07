from MyMainForm_2 import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets

class MyForm(QtWidgets.QWidget):

    def __init__(self, menuForm):
        super().__init__()
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
        self.__menuForm = menuForm
        self.__ui.pushButton.clicked.connect(self.in_menu)
        self.showMaximized()

    def in_menu(self):
        self.__menuForm.setVisible(True)
        self.close()
