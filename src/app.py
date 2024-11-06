from PySide6 import QtWidgets

from package.python.main_window import MainWindow



app = QtWidgets.QApplication()
win = MainWindow()
win.show()
app.exec()