from MyMainForm import Ui_MainWindow
from PyQt5 import QtWidgets

class MyMainForm(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow
        self.__ui.setupUi(self)
        self.show()