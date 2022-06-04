import random

from MyMainForm_2 import Ui_mainForm
from PyQt5 import QtCore, QtGui, QtWidgets
from my_button import MyButton
#form MyMainFprm_3 import Ui_EndGame

class MyForm(QtWidgets.QWidget):

    def __init__(self, menuForm):
        super().__init__()
        self.__ui = Ui_mainForm()
        self.__ui.setupUi(self)
        self.__menuForm = menuForm
        self.__ui.pushButton.clicked.connect(self.in_menu)
        self.showMaximized()
        self.timerSec = QtCore.QTimer()
        self.timerSec.timeout.connect(self.onTimer)

        self.checkedCount = 0
        #self.moveCount = 20
        self.firstSpacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Expanding)
        self.__ui.gridLayout.addItem(self.firstSpacer, 0, 0, 1, 1)
        self.N = 10
        self.imageslist = ['romb.png', 'treyg.png','kwadr.png','shest.png']
        self.buttons = {}
        self.checkedButtons = {}
        for i in range(1, self.N):
            label1 = QtWidgets.QLabel('')
            label2 = QtWidgets.QLabel('')
            self.__ui.gridLayout.addWidget(label1, self.N, i)
            self.__ui.gridLayout.addWidget(label2, i, self.N)
            for j in range(1, self.N):
              # number += 1
                button_ij = QtWidgets.QPushButton(self)
                img = self.imageslist[random.randrange(0, 4)]
                button_ij = MyButton(i, j, img, self)
                button_ij.setFixedWidth(80)
                button_ij.setFixedHeight(80)
                button_ij.setCheckable(True)
                button_ij.setStyleSheet("background-color:rgba(0, 132, 255, 255)")
                #button_ij.setStyleSheet('background-images:'+imageslist[random.randrange(0, 2)])
                button_ij.clicked.connect(self.buttonIJClick)
                button_ij.setIcon(QtGui.QIcon(img))
                button_ij.setIconSize(button_ij.size())
                # button_ij_id = str(i) + '_' + str(j)
                self.__ui.gridLayout.addWidget(button_ij, i, j)
                self.buttons[i, j] = button_ij

        # button1 = QtWidgets.QPushButton("1", self)
        # self.__ui.gridLayout_4.addWidget(button1, 1, 1)
        # button2 = QtWidgets.QPushButton("2", self)
        # self.__ui.gridLayout_4.addWidget(button2, 2, 2)

        self.lastSpacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding,
                                                QtWidgets.QSizePolicy.Expanding)
        self.__ui.gridLayout.addItem(self.lastSpacer, 10, 10, 1, 1)
        self.reset()

    def buttonIJClick(self, checked):
        # print(self.sender().x, self.sender().y)
        if  checked:
            x = self.sender().x
            y = self.sender().y
            self.checkedButtons[x,y] = self.sender()
            self.checkedCount += 1
            if self.checkedCount > 2:
                self.clearAllChecked()
                self.sender().click()
                return
            else:
                if self.checkedCount == 2:
                    k=0;
                    b1 = None
                    b2 = None
                    for key in self.checkedButtons:
                        if k==0:
                            b1 = self.checkedButtons[key]
                        else:
                            b2 = self.checkedButtons[key]
                        k += 1
                    if abs(b1.x-b2.x)+abs(b1.y-b2.y)==1:
                        tmpImage = b1.images
                        b1.images = b2.images
                        b2.images = tmpImage
                        b1.setIcon(QtGui.QIcon(b1.images))
                        b2.setIcon(QtGui.QIcon(b2.images))
                        self.clearAllChecked()
                        self.destroySame()
                        # self.moveCount -= 1
                        #
                        #
                        # сделать сообщение об окончании ходов!
                        return

        else:
            self.checkedCount -= 1


    def clearAllChecked(self):
        self.checkedButtons.clear()
        self.checkedCount = 0
        for but in self.buttons:
            self.buttons[but].setChecked(False)

    def in_menu(self):
        self.__menuForm.setVisible(True)
        self.close()

    def onTimer(self):
        self.__ui.lineEdit.setText(str(self.secValue))
        self.secValue-=1
        if self.secValue ==-1:
            self.timerSec.stop()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Время вышло. Попробовать снова?")
            msgBox.setWindowTitle("Время вышло")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            #msgBox.buttonClicked.connect(self.msgButtonClick)

            returnValue = msgBox.exec()
            if returnValue == QtWidgets.QMessageBox.Yes:
                self.reset()
            else:
                self.__menuForm.setVisible(True)
                self.close()

    def reset(self):
        #сброс всего на форме
        for i in range(1, self.N):
            for j in range(1, self.N):
                img = self.imageslist[random.randrange(0, 4)]
                self.buttons[i, j].images=img
                self.buttons[i, j].setChecked(False)
                self.buttons[i, j].setIcon(QtGui.QIcon(img))
                self.buttons[i, j].setIconSize(self.buttons[i, j].size())
        self.secValue = 20
        self.timerSec.start(1000)

    def destroySame(self):
        countSameLeft = {}
        countSameUp = {}
        for i in range(1,self.N):
            for j in range(1,self.N):
                if (i,j) in self.buttons:
                    if not((i,j) in countSameLeft):
                        countSameLeft[i,j] = 0
                    if not((i,j) in countSameUp):
                        countSameUp[i, j] = 0
                    if i>1:
                        if (i-1,j) in self.buttons:
                            if (self.buttons[i,j].images == self.buttons[i-1,j].images):
                                countSameUp[i,j] = countSameUp[i-1,j] + 1
                    if j>1:
                        if (i, j - 1) in self.buttons:
                            if (self.buttons[i,j].images == self.buttons[i,j-1].images):
                                countSameLeft[i,j] = countSameLeft[i,j-1] + 1
                    if countSameLeft[i,j]==3 or countSameUp[i,j]==3:
                        self.removeSameButtons(i,j)
                        self.downAll()
                        self.fillEmpty()
                        self.destroySame()
                       # return

    def removeSameButtons(self,x,y):
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        img = self.buttons[x,y].images
        self.__ui.gridLayout.removeWidget(self.buttons[x, y])
        del self.buttons[x, y]
        # Счет очков ()()()()()()()()()()()
        #
        #
        #
        #
        for k in range(0,4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if (new_x,new_y) in self.buttons:
                if img == self.buttons[new_x,new_y].images:
                    self.removeSameButtons(new_x,new_y)


    def downAll(self):
        for k in range(0,self.N*2):
            for i in range(1, self.N - 1):
                for j in range(1, self.N):
                    if (i,j) in self.buttons:
                        if (i+1,j) not in self.buttons:
                            self.buttons[i+1,j]=self.buttons[i,j]
                            self.buttons[i + 1, j].x+=1
                            self.__ui.gridLayout.addWidget(self.buttons[i + 1, j],i+1,j)
                            del self.buttons[i, j]

    def fillEmpty(self):
        for i in range(1, self.N):
            for j in range(1, self.N):
                if (i,j) not in self.buttons:
                    button_ij = QtWidgets.QPushButton(self)
                    img = self.imageslist[random.randrange(0, 4)]
                    button_ij = MyButton(i, j, img, self)
                    button_ij.setFixedWidth(80)
                    button_ij.setFixedHeight(80)
                    button_ij.setCheckable(True)
                    button_ij.setStyleSheet("background-color:rgba(0, 132, 255, 255)")
                    button_ij.clicked.connect(self.buttonIJClick)
                    button_ij.setIcon(QtGui.QIcon(img))
                    button_ij.setIconSize(button_ij.size())
                    self.__ui.gridLayout.addWidget(button_ij, i, j)
                    self.buttons[i, j] = button_ij