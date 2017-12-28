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
        self.temp = 0
        self.equalButton.clicked.connect(self.equalClicked)
        self.clearButton.clicked.connect(self.clear)
        self.backspaceButton.clicked.connect(self.backspaceClicked)
        self.pushButton_22.clicked.connect(self.pointClicked)

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
        self.temp = float(self.display.text())
        self.display.clear()
        
    def multiplicativeOperatorClicked(self):
        '''乘或除按下後進行的處理方法'''
        pass
        
    def equalClicked(self):
        '''等號按下後的處理方法'''
        #pass
        #print(self.temp,  self.display.text())
        self.display.setText(str(self.temp + float(self.display.text())))
        self.wait = True
        
        
    def pointClicked(self):
        '''小數點按下後的處理方法'''
        pass
        
    def changeSignClicked(self):
        '''變號鍵按下後的處理方法'''
        pass
        
    def backspaceClicked(self):
        '''回復鍵按下的處理方法'''
        pass
        
    def clear(self):
        '''清除鍵按下後的處理方法'''
        pass
        
    def clearAll(self):
        '''全部清除鍵按下後的處理方法'''
        #pass
        self.wait = True
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
        
    def calculate(self):
        '''計算'''
        pass
