from PyQt5 import QtWidgets
from src.MainWindow import MainWindow

app = QtWidgets.QApplication([])

mainWindow = MainWindow()
mainWindow.show()

exit(app.exec())
