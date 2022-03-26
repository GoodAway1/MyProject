import sys
from PyQt5 import QtWidgets
from MainForm import MyMainForm

if __name__ == '__main__':
    app = QtWidgets.qApplication(sys.argv)
    sainWindow = MainForm()
    sys.exit(app.exee_())