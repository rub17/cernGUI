from PyQt4 import QtCore, QtGui

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
        self.intValidator.setRange(0,65535)
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
        #self.plusBtn.setStyleSheet("background: orange")

        
        self.minusBtn = QtGui.QPushButton('-',self)
        self.minusBtn.setToolTip('Removing a row')
        self.minusBtn.resize(self.plusBtn.sizeHint())
        #self.minusBtn.setStyleSheet("border-radius: 5px")

        
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.resize(50,100)
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
    
    def checkTableInt(self):
        for i in range (0,self.tableWidget.rowCount()):
            state = self.intValidator.validate(self.tableWidget.item(i,0).text(),0)[0]
            if state == QtGui.QValidator.Acceptable:
                self.tableWidget.item(i,0).setBackgroundColor(QtGui.QColor(152,251,152))
            else:
                self.tableWidget.item(i,0).setBackgroundColor(QtGui.QColor(255, 128, 128))
                self.tableWidget.item(i,0).setToolTip('Integer only please.')
            i += 1

    def checkTableHex(self):
        for x in range (0,self.tableWidget.rowCount()):
            for y in range (0,self.tableWidget.columnCount()):
                state = self.hexValidator.validate(self.tableWidget.item(x,y).text(),0)[0]
                if state == QtGui.QValidator.Acceptable:
                    self.tableWidget.item(x,y).setBackgroundColor(QtGui.QColor(152,251,152))
                else:
                    self.tableWidget.item(x,y).setBackgroundColor(QtGui.QColor(255, 128, 128))
                    self.tableWidget.item(x,y).setToolTip('Hex# only please. (ie. 0x1234567F)')
                y += 1
        x += 1
    
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
       


