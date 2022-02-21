from PyQt5 import QtWidgets
from gui.forms.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.prefixLineEdit.textChanged.connect(self.prefix_changed)
        self.ui.copyButton.clicked.connect(self.copy)

        self.prefix_changed("")

    def prefix_changed(self, prefix: str):
        prefix = prefix.lower().replace('.', '').replace('-', '').replace('_', '')
        self.ui.outputPasswordLabel.setText(prefix + "")

    def copy(self):
        password = self.ui.outputPasswordLabel.text()
        QtWidgets.QApplication.clipboard().setText(password)
