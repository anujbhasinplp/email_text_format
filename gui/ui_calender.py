# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calender.ui'
#
# Created: Fri Jun 17 12:19:02 2016
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form_Calender(object):
    def setupUi(self, Form_Calender):
        Form_Calender.setObjectName("Form_Calender")
        Form_Calender.resize(359, 247)
        self.verticalLayout = QtGui.QVBoxLayout(Form_Calender)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtGui.QCalendarWidget(Form_Calender)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)

        self.retranslateUi(Form_Calender)
        QtCore.QMetaObject.connectSlotsByName(Form_Calender)

    def retranslateUi(self, Form_Calender):
        Form_Calender.setWindowTitle(QtGui.QApplication.translate("Form_Calender", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_Calender = QtGui.QWidget()
    ui = Ui_Form_Calender()
    ui.setupUi(Form_Calender)
    Form_Calender.show()
    sys.exit(app.exec_())

