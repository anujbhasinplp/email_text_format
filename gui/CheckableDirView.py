__author__ = 'Anuj'

import os

from PyQt4 import QtGui, QtCore

# from backend.Util import fileread, GlobalData, getbckupsetfilename


class CheckableDir(QtGui.QFileSystemModel):
    def __init__(self, tView, parent=None):
        QtGui.QFileSystemModel.__init__(self, tView)
        self.tView = tView
        self.checks = {}
        backupstr = ''
        '''
        bcksetFilename = getbckupsetfilename(GlobalData.username, GlobalData.current_backupset)
        if bcksetFilename:
            backupstr = fileread(GlobalData.idriveConfUserPath, bcksetFilename, "utf-8")

        if backupstr:
            backuplist = backupstr.split('\n')
            for backupitem in backuplist:
                self.checks[backupitem] = QtCore.Qt.Checked
        '''

    def isallchildrenchecked(self, index):
        childIndex = index.child(0, 0)
        if not childIndex.isValid():
            return QtCore.Qt.Unchecked
        i = 1
        while childIndex.isValid():
            if unicode(self.filePath(childIndex)) in self.checks:
                childIndex = index.child(i, 0)
                i += 1
                continue
            return QtCore.Qt.Unchecked
        return QtCore.Qt.Checked

    def isanychildchecked(self, index):
        # checkedItems = []
        # for otherindex, othervalue in self.checks.items():
        #     if othervalue == QtCore.Qt.Checked:
        #         checkedItems.append(otherindex)
        if len(self.checks) == 0:
            return QtCore.Qt.Unchecked

        uncheckpath = unicode(self.filePath(index))
        indices = [removeindex for removeindex in self.checks if self.eligibleIndex(removeindex, uncheckpath)]

        if len(indices) > 0:
            return QtCore.Qt.PartiallyChecked
        return QtCore.Qt.Unchecked

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.CheckStateRole:
            if unicode(self.filePath(index)) in self.checks:
                return QtCore.Qt.Checked
            else:
                checked = QtCore.Qt.Unchecked

########## if parent is checked - check the children
                parent = index.parent()
                while parent.isValid():
                    if unicode(self.filePath(parent)) in self.checks:
                        checked = QtCore.Qt.Checked
                        break

                    parent = parent.parent()

########## if all of the children are checked, check the parent
                if checked == QtCore.Qt.Unchecked:
                    checked = self.isallchildrenchecked(index)

########## if any of the children is checked, partial check the parent
                if checked == QtCore.Qt.Unchecked:
                    checked = self.isanychildchecked(index)

            return checked
        else:
            return QtGui.QFileSystemModel.data(self, index, role)

    def flags(self, index):
        return QtGui.QFileSystemModel.flags(self, index) | QtCore.Qt.ItemIsUserCheckable

    def checkState(self, index):
        if index in self.checks:
            return self.checks[index]
        else:
            return QtCore.Qt.Unchecked

    def eligibleIndex(self, removeindex, uncheckpath):
        if removeindex.find(uncheckpath) != -1:
            if len(uncheckpath) == len(removeindex):
                return True
            else:
                if uncheckpath[-1] == os.altsep or uncheckpath[-1] == os.sep:
                    return True
                return removeindex[len(uncheckpath)] == os.altsep or removeindex[len(uncheckpath)] == os.sep
        return False

    def removesubfolders(self, index):
        # checkedItems = []

        # for otherindex, othervalue in self.checks.items():
        #     if othervalue == QtCore.Qt.Checked:
        #         checkedItems.append(otherindex)

        uncheckpath = unicode(self.filePath(index))
        indices = [removeindex for removeindex in self.checks if self.eligibleIndex(removeindex, uncheckpath)]

        for idx in indices:
            if idx in self.checks:
               self.checks.pop(idx)
            # localidx = self.index(idx)
            # if unicode(self.filePath(localidx)) in self.checks: # and (idx[len(uncheckpath)] == os.pathsep):
            #    self.checks.pop(unicode(self.filePath(localidx)))

    def checkforintermidiatestate(self, index):
        parent = index.parent()
        parentlist = []
        while parent.isValid():
            parentlist.insert(0, parent)
            if unicode(self.filePath(parent)) in self.checks:
                break
            parent = parent.parent()

        if parent.isValid():
            self.checks.pop(unicode(self.filePath(parent)))
            parentlist.append(index)
            for i in range(len(parentlist)):
                if i < len(parentlist) - 1:
                    count = self.rowCount(parentlist[i])

                    for j in range(count):
                        childindex = parentlist[i].child(j, 0)
                        if (childindex != parentlist[i + 1]) and (childindex not in self.checks):
                            #self.checks[unicode(self.filePath(childindex))] = QtCore.QVariant(QtCore.Qt.Checked)
                            self.checks[unicode(self.filePath(childindex))] = QtCore.Qt.Checked
                            self.dataChanged.emit(childindex.child(0, 0), childindex.child(self.rowCount(childindex), 0))
                self.tView.collapse(parentlist[i])
                self.tView.expand(parentlist[i])

    def setData(self, index, value, role):

        if (role == QtCore.Qt.CheckStateRole) and (index.column() == 0):
            self.tView.selectionchanged = True
            if value == QtCore.Qt.Checked:
                self.removesubfolders(index)
                self.checks[unicode(self.filePath(index))] = QtCore.Qt.Checked
                if self.isallchildrenchecked(index.parent()) == QtCore.Qt.Checked:
                    self.setData(index.parent(), QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
                count = self.rowCount(index)

                # for i in range(count):
                #     self.setData(index.child(i, 0), value, role)
                self.dataChanged.emit(index.child(0, 0), index.child(count - 1, 0))
                isexpanded = False
                if self.tView.isExpanded(index):
                    isexpanded = True
                self.tView.collapse(index)
                if isexpanded:
                    self.tView.expand(index)
                return True

            elif value == QtCore.Qt.Unchecked:
                self.removesubfolders(index)
                self.checkforintermidiatestate(index)
                isexpanded = False
                if self.tView.isExpanded(index):
                    isexpanded = True
                self.tView.collapse(index)
                if isexpanded:
                    self.tView.expand(index)
                #self.tView.collapse(index)
                return True

        return QtGui.QFileSystemModel.setData(self, index, value, role)


class Checkable_Dir_Model(QtGui.QTreeView):
    def __init__(self, parent=None):
        super(Checkable_Dir_Model, self).__init__(parent)
        self.model = CheckableDir(self)
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllEntries)
        self.setStyleSheet("background: #FBFBFB")
        self.setModel(self.model)
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dir = CheckableDirModel()
    Dir.show()
    sys.exit(app.exec_())

