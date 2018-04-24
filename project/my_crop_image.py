# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 16:29
# @Author  : weic
# @FileName: my_crop_image.py
# @Software: PyCharm

from PyQt5 import QtWidgets,QtGui,QtCore
import sys

import loadimageNew
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    mW_ui=loadimageNew.Ui_MainWindow()
    mW_ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())