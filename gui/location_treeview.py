__author__ = 'Anuj'

import ui_location_treeview
from PyQt4 import QtCore,QtGui


class location_treeview_form(QtGui.QWidget, ui_location_treeview.Ui_location_treeview):
    update_location = QtCore.pyqtSignal(str)

    def __init__(self):
        super(location_treeview_form, self).__init__()
        self.setupUi(self)
        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Dirs)
        self.location_path_treeview.setModel(self.model)

        self.location_path_treeview.hideColumn(1)
        self.location_path_treeview.hideColumn(2)
        self.location_path_treeview.hideColumn(3)
        self.location_path_treeview.clicked.connect(self.on_treeview_clicked)
        self.SelectedItem = ""

    def on_treeview_clicked(self, index):
        self.SelectedItem = str(self.model.filePath(index))

    def send_check_list(self):
        if self.SelectedItem:
            self.update_location.emit(self.SelectedItem)
        self.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = location_treeview_form()
    ui.show()
    sys.exit(app.exec_())

