# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editorv6.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class TableEditor(QtGui.QWidget):

    
    def __init__(self, row,col,sizeX,sizeY,*args,**kwargs):
        super(TableEditor, self).__init__(*args,**kwargs)
        self.row = row
        self.col = col
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.initUI()
    
    def initUI(self):
        self.intValidator = QtGui.QIntValidator()
        self.hexValidator = QtGui.QRegExpValidator(QtCore.QRegExp("0x[0-9A-F]{8}"))
        
        self.tableWidget = QtGui.QTableWidget(self.row,self.col,self)
        self.tableWidget.resize(self.sizeX,self.sizeY)
        self.tableWidget.move(0,20)
        self.tableWidget.horizontalHeader().setResizeMode(1) #All Cells Stretch to the size of the table.
        self.tableWidget.setDragEnabled(1)
        self.tableWidget.setAcceptDrops(1)



        
        self.plusBtn = QtGui.QPushButton('+',self)
        self.plusBtn.setToolTip('Adding a row')
        self.plusBtn.resize(self.plusBtn.sizeHint())
        
        self.minusBtn = QtGui.QPushButton('-',self)
        self.minusBtn.setToolTip('Removing a row')
        self.minusBtn.resize(self.plusBtn.sizeHint())

        
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.move(self.sizeX+10, 30)
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.addWidget(self.plusBtn)
        self.verticalLayout.addWidget(self.minusBtn)
            
        self.plusBtn.clicked.connect(self.addRow)
        self.minusBtn.clicked.connect(self.delRow)
        ####Crude Way to Distinguish if DAC/Delay or Pat#####
        if self.col == 4:
            self.tableWidget.cellChanged.connect(self.checkHex)
        else:
            self.tableWidget.cellChanged.connect(self.checkInt)
    #####################################################


    def addRow(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
    
    def delRow(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.removeRow(rowPosition-1)
       
    def checkInt(self):
        currentRow = self.tableWidget.currentRow()
        currentCol = self.tableWidget.currentColumn()
        currentItem = QtGui.QTableWidgetItem(self.tableWidget.item(currentRow,currentCol))
        state = self.intValidator.validate(currentItem.text(),0)[0]
        if state == QtGui.QValidator.Acceptable:
            self.tableWidget.item(currentRow,currentCol).setBackgroundColor(QtGui.QColor(152,251,152))
        else:
            self.tableWidget.item(currentRow,currentCol).setBackgroundColor(QtGui.QColor(255, 128, 128))
            self.tableWidget.item(currentRow,currentCol).setToolTip('Integer only please.')

    def checkHex(self):
        currentRow = self.tableWidget.currentRow()
        currentCol = self.tableWidget.currentColumn()
        currentItem = QtGui.QTableWidgetItem(self.tableWidget.item(currentRow,currentCol))
        state = self.hexValidator.validate(currentItem.text(),0)[0]
        
        if state == QtGui.QValidator.Acceptable:
            self.tableWidget.item(currentRow,currentCol).setBackgroundColor(QtGui.QColor(152,251,152))
        else:
            self.tableWidget.item(currentRow,currentCol).setBackgroundColor(QtGui.QColor(255, 128, 128))
            self.tableWidget.item(currentRow,currentCol).setToolTip('Hex# only please. (ie. 0x1234567F)')
       


class Ui_EditorMainWindow(object):
    def setupUi(self, EditorMainWindow):
        EditorMainWindow.setObjectName(_fromUtf8("EditorMainWindow"))
        EditorMainWindow.resize(718, 650)
        EditorMainWindow.setWindowOpacity(1.0)
        EditorMainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(EditorMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica Neue"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(12, 46, 691, 371))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.DACDelay = QtGui.QWidget()
        self.DACDelay.setObjectName(_fromUtf8("DACDelay"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.DACDelay)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.DACgroupBox = QtGui.QGroupBox(self.DACDelay)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.DACgroupBox.setFont(font)
        self.DACgroupBox.setObjectName(_fromUtf8("DACgroupBox"))
        self.horizontalLayout.addWidget(self.DACgroupBox)
        self.DELAYgroupBox = QtGui.QGroupBox(self.DACDelay)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.DELAYgroupBox.setFont(font)
        self.DELAYgroupBox.setObjectName(_fromUtf8("DELAYgroupBox"))
        self.horizontalLayout.addWidget(self.DELAYgroupBox)
        self.tabWidget.addTab(self.DACDelay, _fromUtf8(""))
        self.Pat = QtGui.QWidget()
        self.Pat.setObjectName(_fromUtf8("Pat"))
        self.tabWidget.addTab(self.Pat, _fromUtf8(""))
        self.CmtgroupBox = QtGui.QGroupBox(self.centralwidget)
        self.CmtgroupBox.setGeometry(QtCore.QRect(10, 430, 691, 180))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CmtgroupBox.setFont(font)
        self.CmtgroupBox.setObjectName(_fromUtf8("CmtgroupBox"))
        self.CmtlineEdit = QtGui.QLineEdit(self.CmtgroupBox)
        self.CmtlineEdit.setGeometry(QtCore.QRect(20, 30, 450, 100))
        self.CmtlineEdit.setObjectName(_fromUtf8("CmtLineEdit"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(520, 460, 150, 100))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.PreviewpushButton = QtGui.QPushButton(self.layoutWidget)
        self.PreviewpushButton.setAutoFillBackground(False)
        self.PreviewpushButton.setObjectName(_fromUtf8("PreviewpushButton"))
        self.verticalLayout.addWidget(self.PreviewpushButton)
        self.cancelpushButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelpushButton.setAutoFillBackground(False)
        self.cancelpushButton.setObjectName(_fromUtf8("cancelpushButton"))
        self.verticalLayout.addWidget(self.cancelpushButton)
        self.CmtgroupBox.raise_()
        self.layoutWidget.raise_()
        self.tabWidget.raise_()
        self.label.raise_()
        EditorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EditorMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        EditorMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(EditorMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EditorMainWindow.setStatusBar(self.statusbar)

        self.textView = QtGui.QTextEdit()

        self.actionSave = QtGui.QAction(EditorMainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip('Save File')
        self.actionSave.setIcon(QtGui.QIcon.fromTheme("document-save"))
        self.actionSave.triggered.connect(self.save_File)
        
        self.actionOpen = QtGui.QAction(EditorMainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.open_File)

        self.actionAbout = QtGui.QAction(EditorMainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionOpen)
        self.menubar.addAction(self.menuMenu.menuAction())


        self.dacTable = TableEditor(1,1,250,300,self.DACgroupBox)
        self.delayTable = TableEditor(1,1,250,300,self.DELAYgroupBox)
        self.patTable = TableEditor(1,4,550,300,self.Pat)
        self.patTable.move(50,0)

        self.cancelpushButton.clicked.connect(self.close_application)
        self.PreviewpushButton.clicked.connect(self.preview_File)
        


        self.retranslateUi(EditorMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(EditorMainWindow)

    def retranslateUi(self, EditorMainWindow):
        EditorMainWindow.setWindowTitle(_translate("EditorMainWindow", "MainWindow", None))
        self.label.setText(_translate("EditorMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic; color:#ff0000;\">parameter.dat </span><span style=\" color:#ff0000;\">Editor</span></p></body></html>", None))
        self.DACgroupBox.setTitle(_translate("EditorMainWindow", "DAC", None))
        self.DELAYgroupBox.setTitle(_translate("EditorMainWindow", "Delay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DACDelay), _translate("EditorMainWindow", "DAC/Delay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pat), _translate("EditorMainWindow", "Patterns", None))
        self.CmtgroupBox.setTitle(_translate("EditorMainWindow", "Comments", None))
        self.PreviewpushButton.setText(_translate("EditorMainWindow", "Preview/Save", None))
        self.cancelpushButton.setText(_translate("EditorMainWindow", "Cancel", None))
        self.menuMenu.setTitle(_translate("EditorMainWindow", "Menu", None))
        self.actionSave.setText(_translate("EditorMainWindow", "Save", None))
        self.actionOpen.setText(_translate("EditorMainWindow", "Open", None))
        self.actionAbout.setText(_translate("EditorMainWindow", "About", None))


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
            self.textView.append(str(self.dacTable.tableWidget.rowCount()))
            line = QtGui.QLineEdit()
            for i in range(0,self.dacTable.tableWidget.rowCount()):
                line.insert(self.dacTable.tableWidget.item(i,0).text() + " ")
                i += 1
            self.textView.append(line.text())
            self.textView.append(str(self.delayTable.tableWidget.rowCount()))
            line.clear()
            for i in range(0,self.delayTable.tableWidget.rowCount()):
                line.insert(self.delayTable.tableWidget.item(i,0).text() + " ")
                i += 1
            self.textView.append(line.text())
            self.textView.append(str(self.patTable.tableWidget.rowCount()))
            for a in range(0,self.patTable.tableWidget.rowCount()):
                line.clear()
                for b in range(0,4):
                    line.insert(self.patTable.tableWidget.item(a,b).text() + " ")
                    b += 1
                self.textView.append(line.text())
                a +=1
            if self.CmtlineEdit.isModified() == 1:
                self.textView.append("#" + self.CmtlineEdit.text())
            self.textView.setReadOnly(1)
            view.setCentralWidget(self.textView)
            view.setGeometry(QtCore.QRect(450, 100, 400,500))
            view.show()
    
        except AttributeError:
            error = QtGui.QMessageBox.warning(self.centralwidget, 'Error',
                                              "There are empty cells!",
                                              QtGui.QMessageBox.Ok)
            

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
    EditorMainWindow = QtGui.QMainWindow()
    ui = Ui_EditorMainWindow()
    ui.setupUi(EditorMainWindow)
    EditorMainWindow.show()
    sys.exit(app.exec_())

