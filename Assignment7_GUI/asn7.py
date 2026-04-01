# asn7.py
# Student: Dominic Anzano | Course: Graph User Interface Dev | Project: Assignment 7 Project (Python/Qt): Measurement Converter GUI | Date: 03/28/26

import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QMessageBox, QFrame
)

INCH_TO_METER = 0.0254



class ConverterWindow(QMainWindow):
    """Main window for the measurement converter."""

    def __init__(self):
        """Initialize window and UI."""
        super().__init__()
        self.setWindowTitle("Measurement Converter")
        self.resize(850, 450)

        self._build_ui()          # Create UI elements
        self._connect_signals()  # Connect buttons to functions
        self._reset_form()       # Set default state

    def _build_ui(self):
        """Build and arrange all widgets."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout (grid for structure)
        main_layout = QGridLayout()
        central_widget.setLayout(main_layout)

        # ----- Title -----
        self.lblTitle = QLabel("Converter App")
        self.lblTitle.setFont(QFont("Arial", 18, QFont.Bold))
        self.lblTitle.setAlignment(Qt.AlignCenter)

        # ----- Input -----
        self.lblPrompt = QLabel("Enter a value and choose conversion")
        self.txtInput = QLineEdit()
        self.txtInput.setPlaceholderText("Example: 10 or 5.5")

        # ----- Radio Buttons -----
        self.grpConversion = QGroupBox("Convert Measurement")

        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbMToIn = QRadioButton("Meters to Inches")

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.rbInToM)
        radio_layout.addWidget(self.rbMToIn)
        self.grpConversion.setLayout(radio_layout)

        # ----- Result Display -----
        self.lblResult = QLabel("")
        self.lblResult.setAlignment(Qt.AlignCenter)

        # ----- Buttons -----
        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")

        # ----- Image Section -----
        self.imgFrame = QFrame()
        self.imgLabel = QLabel()
        self.imgLabel.setAlignment(Qt.AlignCenter)

        img_layout = QVBoxLayout(self.imgFrame)
        img_layout.addWidget(self.imgLabel)

        self._load_house_image()  # Load image into label

        # ----- Layout Assembly -----
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.lblTitle)
        left_layout.addWidget(self.lblPrompt)
        left_layout.addWidget(self.txtInput)
        left_layout.addWidget(self.grpConversion)
        left_layout.addWidget(self.lblResult)

        # Button row
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btnConvert)
        button_layout.addWidget(self.btnClear)
        button_layout.addWidget(self.btnExit)

        left_layout.addLayout(button_layout)

        # Place layouts in grid
        main_layout.addLayout(left_layout, 0, 0)
        main_layout.addWidget(self.imgFrame, 0, 1)

        # Style
        self.setStyleSheet("""
            QMainWindow {background-color: #E8E6FF;}
            QLabel {color: #1F1F1F;}
            QLineEdit {background-color: white; color: black; border: 2px solid #5C4B8A; border-radius: 6px; padding: 6px;}
            QLineEdit:focus {border: 3px solid #1E90FF;}
            QGroupBox {color: #1F1F1F; border: 2px solid #5C4B8A; border-radius: 8px; margin-top: 10px; padding-top: 10px; background-color: #F5F2FF;}
            QGroupBox::title {subcontrol-origin: margin; left: 10px; padding: 0 4px 0 4px;}
            QRadioButton {color: #1F1F1F; padding: 4px;}
            QPushButton {background-color: #D9D2FF; color: black; border: 2px solid #6A5ACD; border-radius: 8px; padding: 8px 14px;}
            QPushButton:hover {background-color: #C8BEFF;}
            QPushButton:focus {border: 3px solid #1E90FF;}
            QFrame {background-color: white;}
        """)

    def _load_house_image(self):
        """Load house image if found."""
        paths = ["house.png", os.path.join("assets", "house.png")]

        pixmap = QPixmap()

        # Try both possible locations
        for path in paths:
            if os.path.exists(path):
                pixmap = QPixmap(path)
                break

        # Display image or fallback text
        if not pixmap.isNull():
            self.imgLabel.setPixmap(
                pixmap.scaled(260, 260, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        else:
            self.imgLabel.setText("house.png not found")

    def _connect_signals(self):
        """Connect buttons to functions."""
        self.btnConvert.clicked.connect(self.on_convert)
        self.btnClear.clicked.connect(self.on_clear)
        self.btnExit.clicked.connect(QApplication.quit)

    def _reset_form(self):
        """Reset input, result, and default selection."""
        self.txtInput.clear()
        self.lblResult.clear()
        self.rbInToM.setChecked(True)  # Default selection
        self.txtInput.setFocus()

    def inches_to_meters(self, inches):
        """Convert inches to meters."""
        return inches * INCH_TO_METER

    def meters_to_inches(self, meters):
        """Convert meters to inches."""
        return meters / INCH_TO_METER

    def show_error(self, message):
        """Display an error message."""
        QMessageBox.critical(self, "Error", message)

    def on_convert(self):
        """Handle conversion when button is clicked."""
        text = self.txtInput.text().strip()

        # Check for empty input
        if not text:
            self.show_error("Please enter a value.")
            return

        # Check for numeric input
        try:
            value = float(text)
        except ValueError:
            self.show_error("Value entered is not numeric.")
            return

        # Check for positive value
        if value <= 0:
            self.show_error("Value must be positive.")
            return

        # Perform selected conversion
        if self.rbInToM.isChecked():
            result = self.inches_to_meters(value)
            self.lblResult.setText(f"{value:.3f} inches = {result:.3f} meters")
        else:
            result = self.meters_to_inches(value)
            self.lblResult.setText(f"{value:.3f} meters = {result:.3f} inches")

    def on_clear(self):
        """Clear inputs and reset form."""
        self._reset_form()

def main():
    """Run the application."""
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())

    # Entry point
if __name__ == "__main__":
    main()