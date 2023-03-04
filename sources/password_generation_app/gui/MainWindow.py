from PyQt5 import QtWidgets
from password_generation_app.common.text import generate_random_string, replace_characters
from password_generation_app.gui.forms.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.prefixLineEdit.textChanged.connect(self.update_password)
        self.ui.copyButton.clicked.connect(self.copy_password)

        self.update_password("")

    def update_password(self, prefix: str) -> None:
        prefix = replace_characters(prefix.lower(), r"[^a-zA-Z0-9_-]", "")
        self.ui.outputPasswordLabel.setText(prefix + generate_random_string(16))

    def copy_password(self) -> None:
        password = self.ui.outputPasswordLabel.text()
        QtWidgets.QApplication.clipboard().setText(password)
