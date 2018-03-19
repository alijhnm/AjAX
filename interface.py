from PyQt5 import QtCore, QtGui, QtWidgets
import os, shutil, os.path
import time

recent_directories_list = []
directories = []
tup = next(os.walk('/home/ali'))
os.chdir('/home/ali')
list_of_item = []
initial_list = [os.path.join(tup[0], i) for i in tup[1] + tup[2]]
dragged_item = []
selected_file=None
selected_file_to_copy=None
selected_file_to_cut=None
selected_file_to_paste=None

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()


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
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.triggered.connect(self.action_open)
        self.actionNew_file.setShortcut("Ctrl+N")
        self.actionNew_file.triggered.connect(self.action_newfile)
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.triggered.connect(self.action_quit)
        self.actionExit.setShortcut("Ctrl+E")
        self.actionExit.triggered.connect(self.action_exit)
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionCopy.triggered.connect(self.action_copy)
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCut.triggered.connect(self.action_cut)
        self.actionPaste.setShortcut("Ctrl+V")
        self.actionPaste.triggered.connect(self.action_paste)
        self.actionZip.setObjectName("actionZip")
        self.actionZip.triggered.connect(self.action_zip)
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
        self.actionOpen.setText(_translate("MainWindow", "open"))
        #self.actionOpen.clicked.connect(lambda :OpenFile("*","*"))
        self.actionNew_file.setText(_translate("MainWindow", "new file"))
        #self.actionNew_file.clicked.connect(lambda: NewFile("*", "*"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        #self.actionQuit.clicked.connect(lambda: Quit("*", "*"))
        self.actionCopy_Crtl_C.setText(_translate("MainWindow", "Copy"))
        #self.actionCopy_Crtl_C.clicked.connect(lambda: CopyFile("*", "*"))
        self.actionPaste_Ctrl_V.setText(_translate("MainWindow", "Paste"))
        #self.actionPaste_Ctrl_V.clicked.connect(lambda: PasteFile("*", "*"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        #self.actionExit.clicked.connect(lambda: QuitFile("*", "*"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionZip.setText(_translate("MainWindow", "Zip"))
        #self.actionZip.clicked.connect(lambda: ZipFile("*", "*"))

    #definingFunctions

    def show_items(self, lst):
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

            # contextMenu Policy
            self.item.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.item.customContextMenuRequested.connect(self.show_context)
            # setting menu actions
            self.popupMenu = QtWidgets.QMenu(self)
            self.popupMenu.addAction(QtWidgets.QAction('New Folder', self, triggered=self.newact))
            self.popupMenu.addAction(QtWidgets.QAction('Copy', self, triggered=self.copyact))
            self.popupMenu.addAction(QtWidgets.QAction('Cut', self, triggered=self.cutact))
            self.popupMenu.addSeparator()
            self.popupMenu.addAction(QtWidgets.QAction('test1', self, triggered=self.func1))
            self.popupMenu.addAction(QtWidgets.QAction('test2', self, triggered=self.func2))

            list_of_item.append(self.item)

        # defining func1 action

    def func1(self):
        print('test1 action done')

            # defining func2 action

    def func2(self):
        print('test2 action done')

            # defining newfolder action

    def newact(self):
        print('NewFolder act done')

            # defining copy action

    def copyact(self):
        print('Copy act done')

            # defining cut action

    def cutact(self):
        print('Cut act done')

            # showing context menu

    def show_context(self, event):
        self.popupMenu.exec_(self.mapToGlobal(event))

    def Search(self, dir, file_or_dirname):
        """Searches for file_or_dir_name in directory and its subdirectories"""
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

    def OpenFile(self, file_path):
        """Opens a file at file_path. Works exactly as double clicking in windows"""
        if os.path.isfile(file_path):
            os.startfile(file_path)

    def go_button(self):
        """Handles go button. If the path given to line edit is a dir shows dirs contents.
        If it is a file, Opens the file"""
        path = self.lineEdit.text()
        if os.path.isfile(path):
            self.OpenFile(path)
        else:
            try:
                self.Go_to_directory('qwe',path)
            except:
                pass

    def CopyFile(self, file_path, target_path):
        """Copies the file file_path to the file or directory target_path.
         File_path and target_path should be strings.
         If file_path specifies a directory,the file will be copied into
         target_path using the base filename from file_path"""
        shutil.copy2(file_path, target_path)

    def RenameFile(self, old_name, new_name):
        """Renames file old_name to new_name. new_name and old_name are either names
           at current working directory or full paths.
           If new name is a directory at a different path file will not rename"""
        try:
            os.rename(old_name, new_name)
        except OSError:
            pass    #####ALIBEHROOZI

    def RemoveFile(self, file_path):
        """Deletes file file_path"""
        os.remove(file_path)

    def RemoveDir(self, dir_path):
        """Removes an entire directory"""
        shutil.rmtree(dir_path)

    def CutFile(self, file_path, target_path):
        """Cuts a file from file_path and pastes it at target_path"""
        shutil.move(file_path, target_path)

    def MakeZip(self, dir, target_path, name):
        """Compreses a dir at dir_path into a zip file and moves it to target_path"""
        tmp_dir = os.getcwd()
        os.chdir(target_path)
        shutil.make_archive(name, 'zip', dir, dir)
        os.chdir(tmp_dir)

    def ExtractZip(self, archieve_path, extract_path):
        """Extracts a zip file from archieve_path to extract_path"""
        shutil.unpack_archive(archieve_path, extract_path)

    def MakeDir(self, path=os.getcwd()):
        """Makes a new directory at current working directory.
           If path is provided,
           the new directory will be created there"""
        os.mkdir(path)

    def selected_item(self):
        """DOC NEEDED"""
        global selected_file,selected_file_to_paste
        dragged_item.append(self.sender())
        self.sender().setFlat(False)
        selected_file = self.sender().text()
        if not os.path.isfile(selected_file):
            selected_file_to_paste = selected_file
        if len(dragged_item)>1:
            for i in dragged_item[0:-2]:
                i.setFlat(True)
        if not self.sender().isFlat() :
            path = self.sender().text()
            if os.path.isfile(path):
                func1 = lambda: self.OpenFile(path)
                self.sender().clicked.connect(func1)
            else:
                func2 = lambda: self.Go_to_directory(path)
                self.sender().clicked.connect(func2)

    def recent_directories(self):
        """DOC NEEDED"""
        for i,directory in enumerate(recent_directories_list[-5:]):
            self.RecentAdrresses.addItem("")
            self.RecentAdrresses.setItemText(i,directory)

    def Go_to_directory(self,address):
        """Changes the current working directory to address.
           Also makes necessary changes to files shown"""
        global selected_file,selected_file_to_paste
        recent_directories_list.append(address)
        directories.append(address)
        selected_file=None
        self.lineEdit.clear()
        self.lineEdit.insert(address)
        os.chdir(address)
        gen = os.walk(os.getcwd())
        tup = next(gen)
        lst = [os.path.join(tup[0], i) for i in tup[1] + tup[2]]
        self.show_items(lst)
        del gen

    def Back(self):
        """Returns to parent directory of current working directory.
           Also makes necessary changes to files shown and line_edit"""
        os.chdir(os.path.dirname(os.getcwd()))
        gen = os.walk(os.getcwd())
        tup = next(gen)
        lst = [os.path.join(tup[0], i) for i in tup[1] + tup[2]]
        del gen
        self.show_items(lst)
        self.lineEdit.setText(os.getcwd())


    def tree_double_click(self,event):
        """Handle the event of clicking on the items of Treeview"""
        global selected_file_to_paste
        if event.button()==QtCore.Qt.LeftButton :
            try:
                if os.path.isfile(self.model.filePath(self.tree_view.currentIndex())):
                    self.OpenFile(self.model.filePath(self.tree_view.currentIndex()))
                else:
                    if self.tree_view.isExpanded(self.tree_view.currentIndex()):
                        self.tree_view.collapse(self.tree_view.currentIndex())
                    else:
                        self.tree_view.expand(self.tree_view.currentIndex())
                    selected_file_to_paste=self.model.filePath(self.tree_view.currentIndex())
                    self.Go_to_directory(self.model.filePath(self.tree_view.currentIndex()))
            except:
                pass

    def action_open(self):
        if selected_file != None:
            os.startfile(selected_file)

    def action_newfile(self):
        print(654654321987)

    def action_quit(self):
        MainWindow.close()

    def action_exit(self):
        MainWindow.close()

    def action_copy(self):
        global selected_file_to_copy, selected_file_to_cut
        if selected_file != None:
            selected_file_to_copy = selected_file
            selected_file_to_cut = None

    def action_cut(self):
        global selected_file_to_cut, selected_file_to_copy
        if selected_file != None:
            selected_file_to_cut = selected_file
            selected_file_to_copy = None

    def action_paste(self):
        if selected_file_to_paste != None:
            if selected_file_to_copy != None:
                self.CopyFile(selected_file_to_copy, selected_file_to_paste)
            if selected_file_to_cut != None:
                self.CutFile(selected_file_to_cut, selected_file_to_paste)

    def action_zip(self):
        if selected_file != None:
            self.MakeZip(selected_file, selected_file, selected_file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
