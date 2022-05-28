from PyQt5.QtWidgets import QPushButton

class MyButton(QPushButton):
    def __init__(self, x, y, images, parent):
        super(MyButton, self).__init__(parent)
        self.x = x
        self.y = y
        self.images = images