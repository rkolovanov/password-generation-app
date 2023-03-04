from PyQt5 import QtWidgets
from password_generation_app.gui.MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()

    exit(app.exec())
