from PySide6 import QtWidgets , QtCore



class MSpinBox(QtWidgets.QSpinBox) :
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.setMinimumSize(25,10)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.setRange(0,1000)