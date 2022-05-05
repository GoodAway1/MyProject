from MyMainForm import Ui_Dialog
from PyQt5 import QtWidgets

class MyMainForm(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.__ui.pushButton.clicked.connect(self.exit_click)
        self.show()

    def exit_click(self):
        self.close()
