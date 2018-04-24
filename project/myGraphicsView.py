# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 9:10
# @Author  : weic
# @FileName: myGraphicsView.py
# @Software: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtGui import QPainter,QPen
class MyGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.hasImage=False
        self.scale_factor=1
        self.leftButtonPressed=False
        self.lastPositionOfMouse=QtCore.QPoint(self.width(),self.height())
        self.view_center=QtCore.QPoint(self.viewport().width(),self.viewport().y())
        self.rect = QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QPointF(0, 0))

    def wheelEvent(self, event: QtGui.QWheelEvent):
        if self.hasImage:
            factor=event.angleDelta().y()/120
            if factor>0:
                #self.transform变换，获取放缩后的倍数，在变换的基础上
                s = self.transform().scale(1.1, 1.1).mapRect(QtCore.QRectF(0, 0, 1, 1)).width()
                self.scale(1.1,1.1)

                #print(self.transform().scale(factor*10,factor*10))
            else:
                s = self.transform().scale(0.9,0.9).mapRect(QtCore.QRectF(0, 0, 1, 1)).width()
                self.scale(0.9,0.9)
            self.scale_factor = s

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        #event.button() 1左2右,event.pos()坐标点，原点在中心

        if event.button()==1 and self.hasImage:
            self.leftButtonPressed=True
            self.lastPositionOfMouse=event.pos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if self.leftButtonPressed:
            if len(self.items())>1:
                self.scene().removeItem(self.scene().items()[0])
            position = QtCore.QRectF(self.lastPositionOfMouse, event.pos())
            rect = QtWidgets.QGraphicsRectItem(position)
            self.scene().addItem(rect)


    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        if event.button()==1:
            self.rect=QtCore.QRect(self.lastPositionOfMouse,event.pos())
            self.leftButtonPressed=False




