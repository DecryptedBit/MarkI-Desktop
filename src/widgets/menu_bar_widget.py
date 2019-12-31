from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenuBar

from src import file_handler


class MenuBarWidget(QMenuBar):
    def __init__(self, parent=None):
        super(MenuBarWidget, self).__init__(parent)

        self.main_window = parent
        self.init_ui()

    def init_ui(self):
        self.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.setDefaultUp(False)
        self.setNativeMenuBar(True)
        self.setObjectName("MenuBar")

        # File item
        self.file_item = QtWidgets.QMenu(self)
        self.file_item.setObjectName("MenuBarFileMenu")

        self.new_action = QtWidgets.QAction(self)
        self.new_action.setObjectName("FileMenuNewAction")
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(lambda triggered: file_handler.create_file())

        self.open_action = QtWidgets.QAction(self)
        self.open_action.setObjectName("FileMenuOpenAction")
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(lambda triggered: file_handler.open_file())

        self.save_action = QtWidgets.QAction(self)
        self.save_action.setObjectName("FileMenuSaveAction")
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(lambda triggered: file_handler.save_file())

        self.save_as_action = QtWidgets.QAction(self)
        self.save_as_action.setObjectName("FileMenuSaveAsAction")
        self.save_as_action.triggered.connect(lambda triggered: file_handler.save_file_as())

        self.file_item.addAction(self.new_action)
        self.file_item.addAction(self.open_action)
        self.file_item.addSeparator()
        self.file_item.addAction(self.save_action)
        self.file_item.addAction(self.save_as_action)

        # Edit item
        self.edit_item = QtWidgets.QMenu(self)
        self.edit_item.setObjectName("MenuBarEditMenu")

        # Format item
        self.format_item = QtWidgets.QMenu(self)
        self.format_item.setObjectName("MenuBarFormatMenu")

        # View item
        self.view_item = QtWidgets.QMenu(self)
        self.view_item.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.view_item.setObjectName("MenuBarViewMenu")

        # Settings item
        self.settings_item = QtWidgets.QMenu(self)
        self.settings_item.setObjectName("MenuBarSettingsMenu")

        self.preferences_action = QtWidgets.QAction(self)
        self.preferences_action.setObjectName("SettingsMenuPreferencesAction")
        self.theme_action = QtWidgets.QAction(self)
        self.theme_action.setObjectName("SettingsMenuThemeAction")
        self.stylesheet_action = QtWidgets.QAction(self)
        self.stylesheet_action.setObjectName("SettingsMenuStylesheetAction")

        self.settings_item.addAction(self.preferences_action)
        self.settings_item.addAction(self.theme_action)
        self.settings_item.addAction(self.stylesheet_action)

        # Finalization
        self.addAction(self.file_item.menuAction())
        self.addAction(self.edit_item.menuAction())
        self.addAction(self.format_item.menuAction())
        self.addAction(self.view_item.menuAction())
        self.addAction(self.settings_item.menuAction())

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        # Items
        self.file_item.setTitle(_translate("MainWindow", "File"))
        self.edit_item.setTitle(_translate("MainWindow", "Edit"))
        self.format_item.setTitle(_translate("MainWindow", "Format"))
        self.view_item.setTitle(_translate("MainWindow", "View"))
        self.settings_item.setTitle(_translate("MainWindow", "Settings"))

        # Item actions
        self.new_action.setText(_translate("MainWindow", "New"))
        self.open_action.setText(_translate("MainWindow", "Open"))
        self.save_action.setText(_translate("MainWindow", "Save"))
        self.save_as_action.setText(_translate("MainWindow", "Save As"))
        
        self.preferences_action.setText(_translate("MainWindow", "Preferences"))
        self.theme_action.setText(_translate("MainWindow", "Theme"))
        self.stylesheet_action.setText(_translate("MainWindow", "Stylesheet"))
