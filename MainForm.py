from MyMainForm import Ui_MainWindow
from PyQt5 import QtWidgets
from MainForm_2 import MyForm

class MyMainForm(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.pushButton.clicked.connect(self.exit_click)
        self.__ui.pushButton_2.clicked.connect(self.perehod)
        self.showMaximized()

    def exit_click(self):
        self.close()

    def perehod(self):
        self.gameForm=MyForm(self)
        self.setVisible(False)


