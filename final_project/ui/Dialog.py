# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        '''以下為使用者自行編寫程式碼區'''
        self.display.setText('0')
        num = [self.one,  self.two,  self.three, \
            self.four,  self.five,  self.six, \
            self.seven,  self.eight,  self.nine,  self.zero]
        for i in num:
            i.clicked.connect(self.digitClicked)
        self.clearAllButton.clicked.connect(self.clearAll)
        self.waitingForOperand = True
        self.plusButton.clicked.connect(self.additiveOperatorClicked)
        self.minusButton.clicked.connect(self.additiveOperatorClicked)
        self.temp = 0
        self.equalButton.clicked.connect(self.equalClicked)
        self.clearButton.clicked.connect(self.clear)
        self.backspaceButton.clicked.connect(self.backspaceClicked)
        self.pushButton_22.clicked.connect(self.pointClicked)
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        for button in [self.timesButton, self.divisionButton]:
            button.clicked.connect(self.multiplicativeOperatorClicked)
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
    def digitClicked(self):
        '''
        使用者按下數字鍵, 必須能夠累積顯示該數字
        當顯示幕已經為 0, 再按零不會顯示 00, 而仍顯示 0 或 0.0
        
        '''
        button = self.sender()
        #避免重複 0。
        if self.display.text() == '0' and int(button.text())== 0.0:
            return
        #清除螢幕 (運算的時候)
        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False
        #疊加數字
        self.display.setText(self.display.text() + button.text())
    
        
    def unaryOperatorClicked(self):
        '''單一運算元按下後處理方法'''
        pass
        
    def additiveOperatorClicked(self):
        '''加或減按下後進行的處理方法'''
        #pass
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())
        #乘除運算
        if self.pendingMultiplicativeOperator:
            '''
            計算：self.calculate(乘數或除數, 運算子)
            回傳 bool 以知道運算成功與否
            Python 文法：[if not 結果:] 當失敗時執行 self.abortOperation()。
            '''
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            #上次的結果
            self.display.setText(str(self.factorSoFar))
            #交換 operand 和 self.factorSoFar
            operand, self.factorSoFar = self.factorSoFar, 0.0
            self.pendingMultiplicativeOperator = ''
        #加減運算
        if self.pendingAdditiveOperator:
            '''
            同上
            '''
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return
            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand
        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True
        
    def multiplicativeOperatorClicked(self):
        '''乘或除按下後進行的處理方法'''
        #pass
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand
        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True
    def equalClicked(self):    
        operand = float(self.display.text())
        '''
        同乘除
        '''
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''
        '''
        同加減
        '''
        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return
            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand
        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True
    
        
    def pointClicked(self):
        '''小數點按下後的處理方法'''
        if self.waitingForOperand:
            self.display.setText('0')
        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")
        self.waitingForOperand = False
        
    def changeSignClicked(self):
        '''變號鍵按下後的處理方法'''
        if self.waitingForOperand:
            self.display.setText('0')
        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")
        self.waitingForOperand = False
    
        
    def backspaceClicked(self):
        '''回復鍵按下的處理方法'''
        #pass
        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True
            self.display.clear()
 
        self.display.setText(text)
    def clear(self):
        '''清除鍵按下後的處理方法'''
        #pass
        self.waitingForOperand = True
        self.display.setText('0')
        
    def clearAll(self):
        '''全部清除鍵按下後的處理方法'''
        #pass
        self.waitingForOperand = True
        #self.temp = 0
        self.display.setText('0')
        
    def clearMemory(self):
        '''清除記憶體鍵按下後的處理方法'''
        pass
        
    def readMemory(self):
        '''讀取記憶體鍵按下後的處理方法'''
        pass
        
    def setMemory(self):
        '''設定記憶體鍵按下後的處理方法'''
        pass
        
    def addToMemory(self):
        '''放到記憶體鍵按下後的處理方法'''
        pass
        
    def createButton(self):
        ''' 建立按鍵處理方法, 以 Qt Designer 建立對話框時, 不需要此方法'''
        pass
        
    def abortOperation(self):
        '''中斷運算'''
        pass
        
    def calculate(self, rightOperand, pendingOperator):
        # 進入計算流程時, 用目前輸入的運算數值與 self.sumSoFar 執行計算
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
 
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
 
        elif pendingOperator == "*":
            self.factorSoFar *= rightOperand
 
        elif pendingOperator == "/":
            if rightOperand == 0.0:
                return False
 
            self.factorSoFar /= rightOperand
 
        return True
