from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil, os.path
import time

recent_directories_list = []
directories = []
tup = next(os.walk('C:\\'))
os.chdir('C:\\')
list_of_item = []

dragged_item = []

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

initial_list = [os.path.join(tup[0], i) for i in tup[1] + tup[2]]


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        #MainWindow
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

        #Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 671, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #NameLabel
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
        self.label.setObjectName("NameLabel")

        # RecentAdrresses
        self.RecentAdrresses = QtWidgets.QComboBox(self.frame)
        self.RecentAdrresses.setGeometry(QtCore.QRect(250, 20, 390, 20))
        self.RecentAdrresses.setObjectName("RecentAdrresses")
        self.RecentAdrresses.raise_()
        self.RecentAdrresses.activated.connect(lambda: self.Go_to_directory(self.RecentAdrresses.currentText()))
        self.label.raise_()

        #AdressBar
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(250, 20, 370, 21))
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.raise_()

        #BackButton
        self.BackButton = QtWidgets.QPushButton(self.frame)
        self.BackButton.setGeometry(QtCore.QRect(220, 20, 21, 21))
        self.BackButton.setText("B")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setIconSize(QtCore.QSize(20, 20))
        self.BackButton.setDefault(False)
        self.BackButton.setFlat(True)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(self.Back)
        self.BackButton.raise_()

        #SearchButton
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(670, 20, 21, 21))
        self.SearchButton.setText("S")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon2)
        self.SearchButton.setIconSize(QtCore.QSize(20, 20))
        self.SearchButton.setDefault(False)
        self.SearchButton.setFlat(True)
        self.SearchButton.setObjectName("SearchButton")
        self.SearchButton.clicked.connect(lambda: self.Search(os.getcwd(), self.lineEdit.text()))
        MainWindow.setCentralWidget(self.centralwidget)

        #GoButton
        self.GoButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoButton.setGeometry(QtCore.QRect(650, 20, 21, 21))
        self.GoButton.setText("Go")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GoButton.setIcon(icon2)
        self.GoButton.setIconSize(QtCore.QSize(20, 20))
        self.GoButton.setDefault(False)
        self.GoButton.setFlat(True)
        self.GoButton.setObjectName("GoButton")
        self.GoButton.clicked.connect(self.go_button)
        # ScrollArea
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(210, 50, 481, 401))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #FormLayout
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)

        #Menu
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #CallFunctions
        self.show_items(initial_list)
        self.recent_directories()
        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Manager"))
        self.label.setText(_translate("MainWindow", "File Manager "))
        self.lineEdit.setAccessibleName(_translate("MainWindow", "address bar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "open               Ctrl+O"))
        #self.actionOpen.clicked.connect(lambda :OpenFile("*","*"))
        self.actionNew_file.setText(_translate("MainWindow", "new file          Ctrl+N"))
        #self.actionNew_file.clicked.connect(lambda: NewFile("*", "*"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        #self.actionQuit.clicked.connect(lambda: Quit("*", "*"))
        self.actionCopy_Crtl_C.setText(_translate("MainWindow", "Copy              Crtl+C"))
        #self.actionCopy_Crtl_C.clicked.connect(lambda: CopyFile("*", "*"))
        self.actionPaste_Ctrl_V.setText(_translate("MainWindow", "Paste              Ctrl+V"))
        #self.actionPaste_Ctrl_V.clicked.connect(lambda: PasteFile("*", "*"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        #self.actionExit.clicked.connect(lambda: QuitFile("*", "*"))
        self.actionCopy.setText(_translate("MainWindow", "Copy       Crtl+C"))
        self.actionCut.setText(_translate("MainWindow", "Cut          Crtl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste       Crtl+V"))
        self.actionZip.setText(_translate("MainWindow", "Zip"))
        #self.actionZip.clicked.connect(lambda: ZipFile("*", "*"))

    #definingFunctions

    def show_items(self, lst):
        print('Start of show_items',lst)
        global list_of_item
        for k in list_of_item:
            k.setParent(None)
        list_of_item = []
        for j,Item in enumerate(lst) :
            self.item = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.item.setFlat(True)
            self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.label.setText(str(j))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.formLayout.setWidget(j, QtWidgets.QFormLayout.LabelRole, self.item)
            self.formLayout.setWidget(j, QtWidgets.QFormLayout.FieldRole, self.label)
            self.item.setText(Item)
            self.item.clicked.connect(self.selected_item)
            list_of_item.append(self.item)
        print('Shown', list_of_item)

    def Search(self, dir, file_or_dirname):
        searching_for = file_or_dirname.lower()
        search_generator = os.walk(dir)
        search_result = []
        while True:
            try:
                gen_result = next(search_generator)
                found = gen_result[1] + gen_result[2]
                for i in range(len(found)):
                    found_result = found[i].lower()
                    if searching_for in found_result:
                        search_result.append(os.path.join(gen_result[0], found[i]))
            except StopIteration:
                break
        self.show_items(search_result)
        print('Searched')

    def OpenFile(self, file_path):
        print(file_path)
        if os.path.isfile(file_path):
            os.startfile(file_path)
        else:
            print('Jakesh')

    def go_button(self):
        path = self.lineEdit.text()
        if os.path.isfile(path):
            self.OpenFile(path)
        else:
            try:
                self.Go_to_directory('qwe',path)
            except:
                pass

    def CopyFile(self, file_path, target_path):
        shutil.copy2(file_path, target_path)

    def RenameFile(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
        except OSError:
            print('File name already exists')

    def RemoveFile(self, file_path):
        os.remove(file_path)

    def RemoveDir(self, dir_path):
        shutil.rmtree(dir_path)

    def CutFile(self, file_path, target_path):
        shutil.move(file_path, target_path)

    def MakeZip(self, dir, target_path, name):
        tmp_dir = os.getcwd()
        os.chdir(target_path)
        shutil.make_archive(name, 'zip', dir, dir)
        os.chdir(tmp_dir)

    def ExtractZip(archieve_path, extract_path):
        shutil.unpack_archive(archieve_path, extract_path)

    def MakeDir(self, path=os.getcwd()):
        os.mkdir(path)

    def selected_item(self,event):
        print(self.sender().text(),self.sender().isFlat())
        dragged_item.append(self.sender())
        self.sender().setFlat(False)
        if len(dragged_item)>1:
            for i in dragged_item[0:-2]:
                i.setFlat(True)
        if not self.sender().isFlat() :
            print(self.sender().text(),4444444)
            self.sender().clicked.connect(lambda :self.Go_to_directory(self.sender().text()))



    def recent_directories(self):
        for i,directory in enumerate(recent_directories_list[-5:]):
            self.RecentAdrresses.addItem("")
            self.RecentAdrresses.setItemText(i,directory)

    def Go_to_directory(self,address):
        print('Start of go_to_directory')
        recent_directories_list.append(address)
        directories.append(address)
        self.lineEdit.clear()
        self.lineEdit.insert(address)
        os.chdir(address)
        gen = os.walk(os.getcwd())
        tup = next(gen)
        lst = [os.path.join(tup[0], i) for i in tup[1] + tup[2]]
        self.show_items(lst)
        print('Returnd to go')
        del gen
        print('Gone')

    def Back(self):
        print('Starting back')
        os.chdir(os.path.dirname(os.getcwd()))
        print('1')
        gen = os.walk(os.getcwd())
        tup = next(gen)
        lst = [os.path.join(tup[0], i) for i in tup[1] + tup[2]]
        print('2')
        del gen
        self.show_items(lst)
        print('Got Back')


    def tree_double_click(self,event):
        #control the reaction of the items in TreeView after clicking on them
        if event.button()==QtCore.Qt.LeftButton :
            try :
                if os.path.isfile(self.model.filePath(self.tree_view.currentIndex()))==True :
                    os.startfile(self.model.filePath(self.tree_view.currentIndex()))
                else :
                    if self.tree_view.isExpanded(self.tree_view.currentIndex()):
                        self.tree_view.collapse(self.tree_view.currentIndex())
                    else :
                        self.tree_view.expand(self.tree_view.currentIndex())
                    self.Go_to_directory(self.model.filePath(self.tree_view.currentIndex()))
            except :
                pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




