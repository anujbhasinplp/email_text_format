# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'location_treeview.ui'
#
# Created: Thu Jun 16 18:05:40 2016
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_location_treeview(object):
    def setupUi(self, location_treeview):
        location_treeview.setObjectName("location_treeview")
        location_treeview.resize(636, 497)
        self.layoutWidget = QtGui.QWidget(location_treeview)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 10, 631, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtGui.QFrame(self.layoutWidget)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Browse_MY_Computer_label = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.Browse_MY_Computer_label.setFont(font)
        self.Browse_MY_Computer_label.setStyleSheet("color:#0F77B1")
        self.Browse_MY_Computer_label.setObjectName("Browse_MY_Computer_label")
        self.gridLayout_2.addWidget(self.Browse_MY_Computer_label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(328, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.close_label = QtGui.QLabel(self.frame_4)
        self.close_label.setObjectName("close_label")
        self.gridLayout_2.addWidget(self.close_label, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(611, 4))
        self.frame.setStyleSheet("background-color:#ADD8E6")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.layoutWidget)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtGui.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(320, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 2, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtGui.QSpacerItem(219, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.close_pushButton = QtGui.QPushButton(self.frame_2)
        self.close_pushButton.setStyleSheet("background-color:#0F77B1;\n"
"color:white")
        self.close_pushButton.setObjectName("close_pushButton")
        self.gridLayout_3.addWidget(self.close_pushButton, 0, 2, 1, 1)
        self.ok_pushButton = QtGui.QPushButton(self.frame_2)
        self.ok_pushButton.setStyleSheet("background-color:#0F77B1;\n"
"color:white")
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.gridLayout_3.addWidget(self.ok_pushButton, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 4, 0, 1, 1)
        self.location_path_treeview = Checkable_Dir_Model(self.layoutWidget)
        self.location_path_treeview.setObjectName("location_path_treeview")
        self.gridLayout_4.addWidget(self.location_path_treeview, 3, 0, 1, 1)

        self.retranslateUi(location_treeview)
        QtCore.QObject.connect(self.ok_pushButton, QtCore.SIGNAL("clicked()"), location_treeview.send_check_list)
        QtCore.QObject.connect(self.close_pushButton, QtCore.SIGNAL("clicked()"), location_treeview.close)
        QtCore.QMetaObject.connectSlotsByName(location_treeview)

    def retranslateUi(self, location_treeview):
        location_treeview.setWindowTitle(QtGui.QApplication.translate("location_treeview", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Browse_MY_Computer_label.setText(QtGui.QApplication.translate("location_treeview", "Browse My Computer", None, QtGui.QApplication.UnicodeUTF8))
        self.close_pushButton.setText(QtGui.QApplication.translate("location_treeview", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_pushButton.setText(QtGui.QApplication.translate("location_treeview", "OK", None, QtGui.QApplication.UnicodeUTF8))

from CheckableDirView import Checkable_Dir_Model

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    location_treeview = QtGui.QWidget()
    ui = Ui_location_treeview()
    ui.setupUi(location_treeview)
    location_treeview.show()
    sys.exit(app.exec_())

