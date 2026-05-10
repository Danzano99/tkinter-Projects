from model import TemperatureModel
from view import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class TemperatureController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = TemperatureModel()

        self.ui.convertButton.clicked.connect(self.convert_temperature)

    def convert_temperature(self):
        result = self.model.fahrenheit_to_celsius(self.ui.fahrenheitInput.text())

        if result is None:
            self.ui.resultLabel.setText("Please enter a valid number.")
            self.ui.resultLabel.setStyleSheet("""
                color: #b64f4f;
                font-weight: bold;
                border: none;
                background: transparent;
            """)
            return

        fahrenheit, celsius = result

        self.ui.resultLabel.setText(f"Converted Temperature: {celsius:.2f} °C")

        if celsius < 10:
            color = "#4f83cc"
        elif celsius < 25:
            color = "#4f8a78"
        else:
            color = "#c45f5f"

        self.ui.resultLabel.setStyleSheet(f"""
            color: {color};
            font-weight: bold;
            border: none;
            background: transparent;
        """)

        self.ui.converterFrame.setStyleSheet(f"""
            QFrame#converterFrame {{
                background-color: #eef4f8;
                border: 2px solid {color};
                border-radius: 14px;
            }}
        """)