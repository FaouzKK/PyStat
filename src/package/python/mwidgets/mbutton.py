from PySide6 import QtWidgets , QtCore

from package.python.api.constant import STYLEDIR

class MPushButton(QtWidgets.QPushButton) :
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        with open(STYLEDIR / "mbutton.css","r",encoding="utf-8") as f:
            self.setStyleSheet(f.read())