__author__ = 'Anuj'

import ui_calender
from PyQt4 import QtCore,QtGui


class calender_form(QtGui.QDialog, ui_calender.Ui_Form_Calender):
    def __init__(self):
        super(calender_form, self).__init__()
        self.setupUi(self)
        self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = calender_form()
    ui.show()
    sys.exit(app.exec_())
