# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadimageNew.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import myGraphicsView
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 731, 541))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = myGraphicsView.MyGraphicsView()
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsetDir = QtWidgets.QAction(MainWindow)
        self.actionsetDir.setObjectName("actionsetDir")
        self.actionmkNewDir = QtWidgets.QAction(MainWindow)
        self.actionmkNewDir.setObjectName("actionmkNewDir")
        self.menu.addAction(self.actionsetDir)
        self.menu_2.addAction(self.actionmkNewDir)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.public_variable()
        self.create_connect()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "next"))
        self.pushButton_2.setText(_translate("MainWindow", "done"))
        self.menu.setTitle(_translate("MainWindow", "设置文件夹"))
        self.menu_2.setTitle(_translate("MainWindow", "设置生成文件夹"))
        self.actionsetDir.setText(_translate("MainWindow", "setDir"))
        self.actionmkNewDir.setText(_translate("MainWindow", "mkNewDir"))


    def public_variable(self):
        self.image_dir=''
        self.newDir=''
        self.picture=None
        self.index=1
        self.classes='foot'

        pass
    def create_connect(self):
        self.actionsetDir.triggered.connect(self.setImagesDir)
        self.actionmkNewDir.triggered.connect(self.setNewImagesDir)
        self.pushButton.clicked.connect(self.nextImage)
        self.pushButton_2.clicked.connect(self.done)

    def setImagesDir(self):
        img_dir=QtWidgets.QFileDialog.getExistingDirectory()
        if img_dir:
            self.image_dir=img_dir
            self.names = iter(os.listdir(self.image_dir))
    def setNewImagesDir(self):
        new_img_dir=QtWidgets.QFileDialog.getExistingDirectory()
        if new_img_dir:
            self.newDir=new_img_dir
        print(self.newDir)
    def nextImage(self):
        if self.image_dir:
            try:
                #self.labelImage.setPixmap(QtGui.QPixmap(os.path.join(self.image_dir,self.names.__next__())))
                #w = QtWidgets.QWidget()
                self._set_graphicsView_scene(self.graphicsView,os.path.join(self.image_dir,self.names.__next__()))

            except Exception as info:
                print(info)
                print('没有图片了')#没图片提示
        else:
            print('未设置图片文件夹')
    def done(self):
        if self.newDir:
            self.index=len(os.listdir(self.newDir))
            crop_picture = self.picture.copy(self.graphicsView.rect)
            imgName=self.classes+str(self.index)+'.jpg'
            crop_picture.save(os.path.join(self.newDir,imgName),quality=100)
            print('done')
        else:
            print('请设置新的文件夹')
        self.graphicsView.scene().removeItem(self.graphicsView.scene().items()[0])


    def _set_graphicsView_scene(self, graphics_view, file_name):
        scene = QtWidgets.QGraphicsScene()
        graphics_view.hasImage = True
        # 适应窗口大小
        fill_scene_picture = QtGui.QPixmap(file_name).scaled(self.graphicsView.width(),
                                                             self.graphicsView.height(),
                                                             QtCore.Qt.KeepAspectRatio,
                                                             QtCore.Qt.SmoothTransformation)
        self.picture=fill_scene_picture
        scene.addItem(QtWidgets.QGraphicsPixmapItem(fill_scene_picture))
        graphics_view.setScene(scene)
        graphics_view.show()

