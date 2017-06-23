# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorV2.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from TableEditor import TableEditor


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
        self.partComboBox = QtGui.QComboBox(self.centralwidget)
        self.partComboBox.setGeometry(QtCore.QRect(140, 80, 121, 51))
        self.partComboBox.setObjectName(_fromUtf8("partComboBox"))
        self.helpText = QtGui.QTextEdit(self.centralwidget)
        self.helpText.setGeometry(QtCore.QRect(20, 130, 241, 141))
        self.helpText.setStyleSheet(_fromUtf8("background-color: rgba(25, 25, 25, 128);\n"
"border-radius: 10px\n"
""))
        self.helpText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.helpText.setFrameShadow(QtGui.QFrame.Sunken)
        self.helpText.setObjectName(_fromUtf8("helpText"))
        self.patGraphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.patGraphicsView.setGeometry(QtCore.QRect(270, 90, 351, 181))
        self.patGraphicsView.setObjectName(_fromUtf8("patGraphicsView"))
        self.tempLabel = QtGui.QLabel(self.centralwidget)
        self.tempLabel.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tempLabel.setFont(font)
        self.tempLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 5px;\n"
""))
        self.tempLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.tempLabel.setObjectName(_fromUtf8("tempLabel"))
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
        font.setPointSize(14)
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
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

###########################################################################################################
        self.cmtLineEdit = QtGui.QLineEdit(self.cmtGroupBox)
        self.cmtLineEdit.setGeometry(QtCore.QRect(10, 20, 600, 50))
        self.cmtLineEdit.setStyleSheet("font-size: 20px")
        self.textView = QtGui.QTextEdit()
        
        self.dacTable = TableEditor(1,1,200,250,self.dacDelay)
        self.dacTable.move(20,0)
        self.dacTable.tableWidget.setHorizontalHeaderLabels(QtCore.QStringList()<<"DAC Value")

        self.delayTable = TableEditor(1,1,200,250,self.dacDelay)
        self.delayTable.move(320,0)
        self.delayTable.tableWidget.setHorizontalHeaderLabels(QtCore.QStringList()<<"Delay Values")
        self.patTable = TableEditor(1,4,500,250,self.patTab)
        channelLabels = QtCore.QStringList()<<"0-31" <<"32-63" << "64-95" << "96-127"
        self.patTable.tableWidget.setHorizontalHeaderLabels(channelLabels)
        self.patTable.move(10,0)
        
        self.abandonPushButton.clicked.connect(self.close_application)
        self.previewPushButton.clicked.connect(self.preview_File)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.cmtGroupBox.setTitle(_translate("MainWindow", "Comments", None))
        self.titleLabel.setText(_translate("MainWindow", "Calibration Editor", None))
        self.abandonPushButton.setText(_translate("MainWindow", "Abandon", None))
        self.dacGroupBox.setTitle(_translate("MainWindow", "DAC", None))
        self.delayGroupBox.setTitle(_translate("MainWindow", "Delay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dacDelay), _translate("MainWindow", "DAC/Delay", None))
        self.patGroupBox.setTitle(_translate("MainWindow", "Patterns", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patTab), _translate("MainWindow", "Patterns", None))
        self.tempLabel.setText(_translate("MainWindow", "    Templates", None))
        self.savePushButton.setText(_translate("MainWindow", "Save", None))
        self.previewPushButton.setText(_translate("MainWindow", "Preview", None))
        self.btmLabel.setText(_translate("MainWindow", "Related Documents:", None))
        self.linkLabel.setText(_translate("MainWindow", "<a href=\"https://goo.gl/D1Bdhy\" style=\"color: red;\">https://goo.gl/D1Bdhy</a>", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Files", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save..", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

    def save_File(self):
        saveFileName = QtGui.QFileDialog.getSaveFileName(self.centralwidget, 'Saving parameter.dat File','parameter.dat','', '*.dat')
        if saveFileName:
            savefile = open(saveFileName,'w')
            #stream = QtCore.QTextStream(openfile)
            #stream << self.textView.toPlainText()
            savefile.write(self.textView.toPlainText())
            savefile.close()

    def open_File(self):
        openFileName = QtGui.QFileDialog.getOpenFileName(self.centralwidget,'Open File','parameter.dat','','*.dat')
        if openFileName:
            file = open(openFileName,'r')
            #input = QtCore.QTextStream(openFileName)
            string = QtCore.QString()
            with file:
                text = file.read()
                print text

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
        
        if self.cmtLineEdit.isModified() == 1:#Writing Comments
            self.textView.append("#" + self.cmtLineEdit.text())
        
        self.textView.append(str(self.dacTable.tableWidget.rowCount()))#Writing # of DAC
        line = QtGui.QLineEdit()
        for i in range(0,self.dacTable.tableWidget.rowCount()):
            line.insert(self.dacTable.tableWidget.item(i,0).text() + " ")#Writing DACs in one line
            i += 1
        self.textView.append(line.text())
        
        self.textView.append(str(self.delayTable.tableWidget.rowCount()))#Writing # of Delay
        line.clear()
        for i in range(0,self.delayTable.tableWidget.rowCount()):
            line.insert(self.delayTable.tableWidget.item(i,0).text() + " ")
            i += 1
        self.textView.append(line.text())

        self.textView.append(str(self.patTable.tableWidget.rowCount()))#Writing Patterns
        for a in range(0,self.patTable.tableWidget.rowCount()):
            line.clear()
            for b in range(0,4):
                line.insert(self.patTable.tableWidget.item(a,b).text() + " ")
                b += 1
            self.textView.append(line.text())
            a +=1


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
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

