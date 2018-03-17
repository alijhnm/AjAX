# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  os



recent_directories_list = ["C:/Users","C:/Descktop"]
directories = ["C:/Users","C:/Descktop","D","E","F","G"]
list_of_items_in_directory = ["ali","saeed","baby","jetli","ddd","qqq","tTT"]
pointer = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 511)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Title-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        #QTreeView
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.model=QtWidgets.QFileSystemModel()
        self.model.setRootPath("")
        self.tree_view=QtWidgets.QTreeView(self.centralwidget)
        self.tree_view.setModel(self.model)
        self.tree_view.setExpandsOnDoubleClick(False)
        self.tree_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tree_view.setAnimated(True)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.setIndentation(20)
        self.tree_view.mouseDoubleClickEvent=self.tree_double_click
        self.tree_view.setGeometry(QtCore.QRect(20, 50, 181, 401))
        self.tree_view.setObjectName("treeWidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 671, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Nueva Std Cond")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(250, 20, 370, 21))
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 20, 21, 21))
        self.pushButton_2.setText("B")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Back)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(670, 20, 21, 21))
        self.pushButton_1.setText("S")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon2)
        self.pushButton_1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setFlat(True)
        self.pushButton_1.setObjectName("pushButton_3")
        self.pushButton_1.clicked.connect(lambda: self.search(self.lineEdit.text()))
        MainWindow.setCentralWidget(self.centralwidget)


        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(250, 20, 390, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.raise_()
        self.comboBox.activated.connect(lambda: self.Go_to_directory(self.comboBox.currentText()))
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton_2.raise_()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(210, 50, 481, 401))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scrollArea.setWidget(QtWidgets.QPushButton(self.scrollAreaWidgetContents).setText("KF"))
        #self.scrollArea.setWidget(QtWidgets.QPushButton(self.scrollAreaWidgetContents).setText("LY"))
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 10, 461, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 20, 21, 21))
        self.pushButton_3.setText("Go")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda :self.search(self.lineEdit.text()))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew_file = QtWidgets.QAction(MainWindow)
        self.actionNew_file.setObjectName("actionNew_file")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCopy_Crtl_C = QtWidgets.QAction(MainWindow)
        self.actionCopy_Crtl_C.setObjectName("actionCopy_Crtl_C")
        self.actionPaste_Ctrl_V = QtWidgets.QAction(MainWindow)
        self.actionPaste_Ctrl_V.setObjectName("actionPaste_Ctrl_V")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionZip = QtWidgets.QAction(MainWindow)
        self.actionZip.setObjectName("actionZip")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew_file)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionZip)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
<<<<<<< HEAD
        self.show_items()
        self.recent_directories()

=======
>>>>>>> ec767eae0d2fa411f9d11874f2120d35273e9062
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Manager"))
        self.label.setText(_translate("MainWindow", "File Manager "))
        self.lineEdit.setAccessibleName(_translate("MainWindow", "address bar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "open               Ctrl+O"))
        self.actionNew_file.setText(_translate("MainWindow", "new file          Ctrl+N"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionCopy_Crtl_C.setText(_translate("MainWindow", "Copy              Crtl+C"))
        self.actionPaste_Ctrl_V.setText(_translate("MainWindow", "Paste              Ctrl+V"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy       Crtl+C"))
        self.actionCut.setText(_translate("MainWindow", "Cut          Crtl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste       Crtl+V"))
        self.actionZip.setText(_translate("MainWindow", "Zip"))

<<<<<<< HEAD
    def search(self,searchin_object):
        print(searchin_object)

    def show_items(self):
        i,j = 0,0
        for Item in list_of_items_in_directory :
            if j == 6 :
                j = 0
                i += 1
            j += 1
            self.item = QtWidgets.QPushButton(self.centralwidget)
            self.item.setGeometry(QtCore.QRect(150 + j*80, 60 + i*80, 50, 50))
            self.item.setText(Item)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/Go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.item.setIcon(icon2)
            self.item.setIconSize(QtCore.QSize(40, 40))
            self.item.setDefault(False)
            self.item.setFlat(True)
            self.item.setObjectName(Item)
            self.item.clicked.connect(lambda: print("Opened",self.item.objectName()))
            MainWindow.setCentralWidget(self.centralwidget)



    def recent_directories(self):
        for i,directory in enumerate(recent_directories_list[-5:]):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i,directory)
        print("FFF")

    def Go_to_directory(self,addres):
        recent_directories_list.append(addres)
        directories.append(addres)
        self.lineEdit.clear()
        self.lineEdit.insert(addres)
        print(addres)

    def Back(self):
        global pointer
        if len(directories)>1:
            self.Go_to_directory(directories[-2])
            directories.pop()
        else :
            self.Go_to_directory(directories[-1])






#import Icons_rc
=======
    def tree_double_click(self,event):
        if event.button()==QtCore.Qt.LeftButton :
            try :
                os.startfile(self.model.filePath(self.tree_view.currentIndex()))
            except :
                pass

>>>>>>> ec767eae0d2fa411f9d11874f2120d35273e9062

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

