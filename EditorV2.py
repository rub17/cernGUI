
from PyQt4 import QtCore, QtGui

from TableEditor import TableEditor

# ------------------------------------------------------------------------------------
#  Title: Calibration Editor

#  Runyu Bi 06.07.2017 (Pittsburgh)

# ------------------------------------------------------------------------------------                             
#  GUI for editing parameter.dat files.

# ------------------------------------------------------------------------------------   

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(635, 750)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.cmtGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.cmtGroupBox.setGeometry(QtCore.QRect(20, 600, 601, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cmtGroupBox.setFont(font)
        self.cmtGroupBox.setStyleSheet(_fromUtf8("border: 2px solid white;\n"
"border-radius: 10px;\n"
"background-color: white"))
        self.cmtGroupBox.setObjectName(_fromUtf8("cmtGroupBox"))
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 601, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica Neue"))
        font.setPointSize(36)
        font.setItalic(False)
        
        #self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        #self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        #self.gridLayout.setMargin(0)

        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setStyleSheet(_fromUtf8("border: 2px solid white;\n"
"border-radius: 10px;\n"
"background-color: beige;\n"
"color: rgb(128, 64, 0)"))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.abandonPushButton = QtGui.QPushButton(self.centralwidget)
        self.abandonPushButton.setGeometry(QtCore.QRect(520, 680, 110, 32))
        self.abandonPushButton.setObjectName(_fromUtf8("abandonPushButton"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 280, 601, 311))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.dacDelay = QtGui.QWidget()
        self.dacDelay.setObjectName(_fromUtf8("dacDelay"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.dacDelay)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 281))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dacGroupBox = QtGui.QGroupBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dacGroupBox.setFont(font)
        self.dacGroupBox.setStyleSheet(_fromUtf8("border: 2px solid white;\n"
"border-radius: 10px;\n"
"background-color: white"))
        self.dacGroupBox.setObjectName(_fromUtf8("dacGroupBox"))
        self.horizontalLayout.addWidget(self.dacGroupBox)
        self.delayGroupBox = QtGui.QGroupBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.delayGroupBox.setFont(font)
        self.delayGroupBox.setStyleSheet(_fromUtf8("border: 2px solid white;\n"
"border-radius: 10px;\n"
"background-color: white"))
        self.delayGroupBox.setObjectName(_fromUtf8("delayGroupBox"))
        self.horizontalLayout.addWidget(self.delayGroupBox)
        self.tabWidget.addTab(self.dacDelay, _fromUtf8(""))
        self.patTab = QtGui.QWidget()
        self.patTab.setObjectName(_fromUtf8("patTab"))
        self.patGroupBox = QtGui.QGroupBox(self.patTab)
        self.patGroupBox.setGeometry(QtCore.QRect(0, 0, 601, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.patGroupBox.setFont(font)
        self.patGroupBox.setStyleSheet(_fromUtf8("border: 2px solid white;\n"
"border-radius: 10px;\n"
"background-color: white"))
        self.patGroupBox.setObjectName(_fromUtf8("patGroupBox"))
        self.tabWidget.addTab(self.patTab, _fromUtf8(""))
        self.helpText = QtGui.QTextEdit(self.centralwidget)
        self.helpText.setGeometry(QtCore.QRect(20, 130, 300, 141))
        self.helpText.setStyleSheet(_fromUtf8("background-color: rgba(25, 25, 25, 128);"
                                              "border-radius: 10px;"
                                              "font-size: 13px"))
        self.helpText.setReadOnly(1)

        self.helpText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.helpText.setFrameShadow(QtGui.QFrame.Sunken)
        self.helpText.setObjectName(_fromUtf8("helpText"))
        self.helpText.setText("<h3 style=color:yellow>Tips:</h3>"
                              "<p style=color:orange>Double click a cell in pattern table to convert hex# into binary!</p>"
                              "<p style=color:white>The DAC value should be between <em>(0,65535)</em>, and the Delay value should be between <i>(0,240)</i> <\p> "
                              "<p style=color:white>The patterns are defined on 128 bits (1 bit per calibration line), represented by four words of 32 bits in hexadecimal format.</p>")
        self.helpText.setTextColor(QtGui.QColor("white"))
        self.helpText.verticalScrollBar().setStyleSheet("background-color: white;")
        self.patGraphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.patGraphicsView.setGeometry(QtCore.QRect(330, 130, 290, 141))
        self.patGraphicsView.setObjectName(_fromUtf8("patGraphicsView"))
        self.scene = QtGui.QGraphicsScene()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        self.scene.addText("Please:\n"
                           "Be careful NOT to overwrite \n"
                           "other parameter.dat files!",font)
        self.patGraphicsView.setScene(self.scene)
        self.pwdInfo = QtGui.QLineEdit(self.centralwidget)
        self.pwdInfo.setGeometry(QtCore.QRect(20, 90, 300, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pwdInfo.setFont(font)
        self.pwdInfo.setStyleSheet(_fromUtf8("color: rgb(255, 255, 0);\n"
"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 5px;\n"
""))
        self.pwdInfo.setObjectName(_fromUtf8("pwdInfo"))
        self.savePushButton = QtGui.QPushButton(self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(410, 680, 110, 32))
        self.savePushButton.setObjectName(_fromUtf8("savePushButton"))
        self.previewPushButton = QtGui.QPushButton(self.centralwidget)
        self.previewPushButton.setGeometry(QtCore.QRect(300, 680, 110, 32))
        self.previewPushButton.setObjectName(_fromUtf8("previewPushButton"))
        self.btmLabel = QtGui.QLabel(self.centralwidget)
        self.btmLabel.setGeometry(QtCore.QRect(30, 680, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(10)
        self.btmLabel.setFont(font)
        self.btmLabel.setOpenExternalLinks(False)
        self.btmLabel.setObjectName(_fromUtf8("btmLabel"))
        self.linkLabel = QtGui.QLabel(self.centralwidget)
        self.linkLabel.setGeometry(QtCore.QRect(160, 680, 141, 21))
        self.linkLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.linkLabel.setObjectName(_fromUtf8("linkLabel"))
        self.linkLabel.setOpenExternalLinks(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.open_File)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.save_File)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.triggered.connect(self.close_application)
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

##############################################################################################
        self.authorGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.authorGroupBox.setGeometry(QtCore.QRect(330,90,290,30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.authorGroupBox.setFont(font)
        self.authorGroupBox.setStyleSheet(_fromUtf8("border: 2px solid white;\n"
                                                 "border-radius: 10px;\n"
                                                 "background-color: white"))
        self.authorGroupBox.setObjectName(_fromUtf8("authorGroupBox"))
        
        self.authorLineEdit = QtGui.QLineEdit(self.authorGroupBox)
        self.authorLineEdit.setGeometry(QtCore.QRect(70,0,200,25))
        
        self.cmtLineEdit = QtGui.QLineEdit(self.cmtGroupBox)
        self.cmtLineEdit.setGeometry(QtCore.QRect(10, 20, 600, 50))
        self.cmtLineEdit.setStyleSheet("font-size: 20px")
        self.textView = QtGui.QTextEdit()
        
        self.hexToBin = QtGui.QLineEdit(self.patTab)
        self.hexToBin.setGeometry(QtCore.QRect(10, 245, 500, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(75)
        self.hexToBin.setFont(font)
        self.hexToBin.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
                                               ""))
        self.hexToBin.textEdited.connect(self.convertBin)
        
        self.dacTable = TableEditor(1,1,200,250,self.dacDelay)
        self.dacTable.move(20,0)
        self.dacTable.tableWidget.setHorizontalHeaderLabels(QtCore.QStringList()<<"DAC Value")

        self.delayTable = TableEditor(1,1,200,250,self.dacDelay)
        self.delayTable.move(320,0)
        self.delayTable.tableWidget.setHorizontalHeaderLabels(QtCore.QStringList()<<"Delay Values")
        self.patTable = TableEditor(1,4,500,220,self.patTab)
        channelLabels = QtCore.QStringList()<<"31-0" <<"63-32" << "95-64" << "127-96"
        self.patTable.tableWidget.setHorizontalHeaderLabels(channelLabels)
        self.patTable.move(10,0)
        
        #self.gridLayout.addWidget(self.titleLabel,0,0,1,2)
        #self.gridLayout.addWidget(self.pwdInfo,1,0,1,1)
        #self.gridLayout.addWidget(self.authorLineEdit,1,1,1,1)
        
        self.savePushButton.clicked.connect(self.save_File)
        self.abandonPushButton.clicked.connect(self.close_application)
        self.previewPushButton.clicked.connect(self.preview_File)
        self.patTable.tableWidget.cellDoubleClicked.connect(self.convertHex)
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.cmtGroupBox.setTitle(_translate("MainWindow", "Comments", None))
        self.authorGroupBox.setTitle(_translate("MainWindow", "Author:", None))
        self.titleLabel.setText(_translate("MainWindow", "Calibration Editor", None))
        self.abandonPushButton.setText(_translate("MainWindow", "Abandon", None))
        self.dacGroupBox.setTitle(_translate("MainWindow", "DAC", None))
        self.delayGroupBox.setTitle(_translate("MainWindow", "Delay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dacDelay), _translate("MainWindow", "DAC/Delay", None))
        self.patGroupBox.setTitle(_translate("MainWindow", "Patterns", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patTab), _translate("MainWindow", "Patterns", None))
        self.pwdInfo.setText("Current Path: " + QtCore.QString(QtCore.QDir.currentPath()))
        self.hexToBin.setText(_translate("MainWindow", "Bonjour!", None))
        self.savePushButton.setText(_translate("MainWindow", "Save", None))
        self.previewPushButton.setText(_translate("MainWindow", "Preview", None))
        self.btmLabel.setText(_translate("MainWindow", "Related Documents:", None))
        self.linkLabel.setText(_translate("MainWindow", "<a href=\"https://atlasop.cern.ch/twiki/bin/view/LAr/LArCalibration\" style=\"color: red;\">TwikiPage</a>", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Files", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save..", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

    def save_File(self):
        self.textView.clear()
        try:
            dialog = QtGui.QMessageBox.warning(self.centralwidget, 'Warning',
            "Please: only save into the UsersArea!!!",QtGui.QMessageBox.Ok)
            
            self.grab_Info()
            if self.textView.document().blockCount() > 1:
                saveFileName = QtGui.QFileDialog.getSaveFileName(self.centralwidget, 'Saving parameter.dat File','parameter.dat','', '*.dat')
                if saveFileName:
                    savefile = open(saveFileName,'w')
                    savefile.write(self.textView.toPlainText())
                    savefile.close()
        except AttributeError:
            error = QtGui.QMessageBox.warning(self.centralwidget, 'Error',
                                              "There are empty cells!",
                                              QtGui.QMessageBox.Ok)

    def open_File(self):
        self.dacTable.tableWidget.blockSignals(True)
        self.delayTable.tableWidget.blockSignals(True)
        self.patTable.tableWidget.blockSignals(True)
        openFileName = QtGui.QFileDialog.getOpenFileName(self.centralwidget,'Open File','parameter.dat','','*.dat')
        if openFileName:
            file = open(openFileName,'r')
            with file:
                position = 0
                text = file.readlines()
                textList = QtCore.QStringList()
                if text[0].startswith('#'): #Skipping comments
                    position = 1
                if text[1].startswith('#'):
                    position = 2
                dacNumber = int(text[0+position])
                delayNumber = int(text[2+position])
                patNumber = int(text[4+position])
                textList = text[1+position].split(" ")
                self.dacTable.tableWidget.setRowCount(dacNumber)
                self.delayTable.tableWidget.setRowCount(delayNumber)
                self.patTable.tableWidget.setRowCount(patNumber)
                for i in range(0,dacNumber):
                    values = QtGui.QTableWidgetItem("0")
                    values.setText(textList[i].strip())
                    self.dacTable.tableWidget.setItem(i,0,values)
                    i += 1

                textList = text[3+position].split(" ")
                for i in range(0,delayNumber):
                    values = QtGui.QTableWidgetItem("0")
                    values.setText(textList[i].strip())
                    self.delayTable.tableWidget.setItem(i,0,values)
                    i += 1

                for x in range(0,patNumber):
                    textList = text[x+5+position].split(" ")
                    for y in range(0,4):
                        values = QtGui.QTableWidgetItem("0")
                        values.setText(textList[y].strip())
                        self.patTable.tableWidget.setItem(x,y,values)
                        y += 1
                    x +=1
                self.dacTable.checkTableInt()
                self.delayTable.checkTableInt()
                self.patTable.checkTableHex()
                self.dacTable.tableWidget.blockSignals(False)
                self.delayTable.tableWidget.blockSignals(False)
                self.patTable.tableWidget.blockSignals(False)

    def preview_File(self):
        view = QtGui.QMainWindow(self.centralwidget)
        savepushButton = QtGui.QPushButton('Save',view)
        savepushButton.setAutoFillBackground(False)
        savepushButton.setObjectName(_fromUtf8("savepushButton"))
        savepushButton.clicked.connect(self.save_File)
        toolBar = view.addToolBar('')
        toolBar.addWidget(savepushButton)
        self.textView.clear()
        try:
            self.grab_Info()
            self.textView.setReadOnly(1)
            view.setCentralWidget(self.textView)
            view.setGeometry(QtCore.QRect(450, 100, 400,500))
            view.show()
    
        except AttributeError:
            error = QtGui.QMessageBox.warning(self.centralwidget, 'Error',
                                             "There are empty cells!",
                                             QtGui.QMessageBox.Ok)
            
    def grab_Info(self):
        tables = [self.dacTable,self.delayTable,self.patTable]
        anyEmpty = 0;
        for i in range (0,3):
            row = tables[i].tableWidget.rowCount()
            col = tables[i].tableWidget.columnCount()
            for x in range(0,row):
                for y in range(0,col):
                    if (tables[i].tableWidget.item(x,y).text().isEmpty()):
                        anyEmpty = 1
                        break
        if anyEmpty == 0:
            if self.cmtLineEdit.isModified() == 1:#Writing Comments
                self.textView.append("#" + self.cmtLineEdit.text())
            if self.authorLineEdit.isModified() == 1:#Writing author's name
                self.textView.append("#Edited by:" + self.authorLineEdit.text())
        #Writing DAC:
            self.textView.append(str(self.dacTable.tableWidget.rowCount()))#Writing # of DAC
            list = []
            for i in range(0,self.dacTable.tableWidget.rowCount()):
                list.append(str(self.dacTable.tableWidget.item(i,0).text()))#Writing DACs in one line
                i += 1

            writeIn = " ".join(list)
            self.textView.append(writeIn)
        #Writing Delay
            self.textView.append(str(self.delayTable.tableWidget.rowCount()))#Writing # of Delay
            list = []
            for i in range(0,self.delayTable.tableWidget.rowCount()):
                list.append(str(self.delayTable.tableWidget.item(i,0).text()))
                i += 1
            
            writeIn = " ".join(list)
            self.textView.append(writeIn)
        #Writing Patterns
            self.textView.append(str(self.patTable.tableWidget.rowCount()))#Writing Patterns
            for a in range(0,self.patTable.tableWidget.rowCount()):
                #line.clear()
                list =[]
                for b in range(0,4):
                    list.append(str(self.patTable.tableWidget.item(a,b).text()))
                    b += 1
                writeIn = " ".join(list)
                self.textView.append(writeIn)
                a +=1
                    
        else:
            error = QtGui.QMessageBox.warning(self.centralwidget, 'Error',
                                              "There are empty cells!",
                                              QtGui.QMessageBox.Ok)

    def convertHex(self):
        try:
            hex2bin_map = {"0":"0000",
                           "1":"0001",
                           "2":"0010",
                           "3":"0011",
                           "4":"0100",
                           "5":"0101",
                           "6":"0110",    
                           "7":"0111",
                           "8":"1000",
                           "9":"1001",
                           "A":"1010",
                           "B":"1011",
                           "C":"1100",
                           "D":"1101",
                           "E":"1110",
                           "F":"1111"}
            hexNumber = self.patTable.tableWidget.currentItem().text()
            value =  str(hexNumber)[2:]
            self.hexToBin.setText(" ".join(hex2bin_map[i] for i in value))
        except AttributeError:
            pass
    def convertBin(self):
        try:
            bin2hex_map = {"0000":"0",
                           "0001":"1",
                           "0010":"2",
                           "0011":"3",
                           "0100":"4",
                           "0101":"5",
                           "0110":"6",
                           "0111":"7",
                           "1000":"8",
                           "1001":"9",
                           "1010":"A",
                           "1011":"B",
                           "1100":"C",
                           "1101":"D",
                           "1110":"E",
                           "1111":"F"}
            binNumber = self.hexToBin.text()
            value =  str(binNumber).split(" ")
            hex = str("0x" + "".join(bin2hex_map[i] for i in value))
            self.patTable.tableWidget.currentItem().setText(hex)
        except KeyError:
            pass

    def close_application(self):
        choice = QtGui.QMessageBox.question(self.centralwidget, 'Exiting',
                                            "Are you sure to quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

