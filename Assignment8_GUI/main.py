import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_root


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)

        self.ui.btnS.clicked.connect(self.submit_info)
        self.ui.btnR.clicked.connect(self.reset_fields)
        self.ui.btnQ.clicked.connect(self.close_app)

    def submit_info(self):
        first_name = self.ui.entFirst.text().strip()
        last_name = self.ui.entLast.text().strip()
        email = self.ui.entEmail.text().strip()
        phone = self.ui.entPhone.text().strip()

        if not first_name or not last_name:
            QMessageBox.warning(
                self,
                "Missing Required Fields",
                "First Name and Last Name are required."
            )
            return

        message = (
            f"First Name: {first_name}\n"
            f"Last Name: {last_name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}"
        )

        QMessageBox.information(self, "Submitted Information", message)

    def reset_fields(self):
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

    def close_app(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())