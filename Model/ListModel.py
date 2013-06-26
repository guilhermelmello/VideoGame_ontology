#! -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore, uic
import sys


class List_Model(QtCore.QAbstractListModel):
    
    def __init__(self, colors = [], parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.__colors = colors


    def headerData(self, section, orientation, role):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QString("Palette")
            else:
                return QtCore.QString("Color %1").arg(section)


    def rowCount(self, parent):
        return len(self.__colors)


    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            
            row = index.row()
            value = self.__colors[row]
            
            return value



    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        
        
        
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            
            row = index.row()
            color = QtGui.QColor(value)
            
            if color.isValid():
                self.__colors[row] = color
                self.dataChanged.emit(index, index)
                return True
        return False