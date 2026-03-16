import sys
import random

# Qt tools
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox
)
# Icon
from PySide6.QtGui import QIcon

#Main Application Window Class
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Assignment 6")
        self.setGeometry(100, 100, 350, 250)
        # Added icon, Image of dice
        self.setWindowIcon(QIcon("dice.png"))

        #Help label that tells the user what input is required
        self.lblHelp = QLabel("Enter an integer greater than 2")
        font = self.lblHelp.font()
        font.setPointSize(16)
        self.lblHelp.setFont(font)
        self.lblHelp.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.lblHelp.setStyleSheet("background-color: #fff4e6; color: black;")

        # Input box
        self.input = QLineEdit()
        self.input.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Output label for random number
        self.lblOutput = QLabel("")
        self.lblOutput.setStyleSheet("font-size: 25px; background-color: #ffeead; color: black;")
        self.lblOutput.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # Button for generating the random number
        self.btnRand = QPushButton("Random Numbers")

        # Connect signal to slot
        self.btnRand.pressed.connect(self.update_label)

        # Created vertical layout and add widgets in display order
        layout = QVBoxLayout()
        layout.setSpacing(12)

        layout.addWidget(self.lblHelp)
        layout.addWidget(self.input)
        layout.addWidget(self.lblOutput)
        layout.addWidget(self.btnRand)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self):
        text = self.input.text()
        try:
            number = int(text)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid number.")
            return
        if number < 2:
            QMessageBox.warning(self, "Input Error", "Number must be greater than 2.")
            return

        # random number generation between 1 and chosen number
        result = random.randint(1, number)

        # Display result
        self.lblOutput.setText(str(result))

# start the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())