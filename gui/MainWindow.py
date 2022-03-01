from PyQt5 import QtWidgets
from gui.forms.MainWindow import Ui_MainWindow
from common.helpers import replace_characters


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.prefixLineEdit.textChanged.connect(self.update_password)
        self.ui.copyButton.clicked.connect(self.copy_password)
        self.update_password("")

    def update_password(self, prefix: str) -> None:
        prefix = replace_characters(prefix.lower(), r'[^a-zA-Z0-9]', '')
        self.ui.outputPasswordLabel.setText(prefix + "")

    def copy_password(self):
        password = self.ui.outputPasswordLabel.text()
        QtWidgets.QApplication.clipboard().setText(password)
