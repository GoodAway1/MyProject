import sys
from PyQt5 import QtWidgets
from MainForm import MyMainForm

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    sys.exit(app.exec())
