from PyQt5 import QtCore
from PyQt5.QtWidgets import QLineEdit


class ConsoleLineEdit(QLineEdit):
    traverseUpPressed = QtCore.pyqtSignal()
    traverseDownPressed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ConsoleLineEdit, self).__init__(parent)

    def keyPressEvent(self, event):
        key = event.key()

        if key > 0 and key == QtCore.Qt.Key_Up:
            self.traverseUpPressed.emit()
        if key > 0 and key == QtCore.Qt.Key_Down:
            self.traverseDownPressed.emit()

        super(ConsoleLineEdit, self).keyPressEvent(event)
