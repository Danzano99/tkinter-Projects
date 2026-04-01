# converter.py
# Student: <Your Name> | Course: <Course Name> | Project: Assignment 7 (PySide6) | Date: <Date>

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QMessageBox, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

INCH_TO_METER = 0.0254

class ConverterWindow(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Measurement Converter (PySide6)")
        self._build_ui()
        self._wire_events()
        self._reset_form()

    def _build_ui(self):
        central = QWidget(self)
        self.setCentralWidget(central)

        # Input
        self.lblPrompt = QLabel("Enter a value:")
        self.txtInput = QLineEdit()
        self.txtInput.setPlaceholderText("e.g., 10 or 5.5")

        # Radio group
        self.grp = QGroupBox("Conversion")
        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbMToIn = QRadioButton("Meters to Inches")
        vgrp = QVBoxLayout()
        vgrp.addWidget(self.rbInToM)
        vgrp.addWidget(self.rbMToIn)
        self.grp.setLayout(vgrp)

        # Buttons
        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")

        # Result
        self.lblResult = QLabel("")
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setStyleSheet("font-size: 16px;")

        # Image
        self.imgFrame = QFrame()
        self.imgLabel = QLabel(alignment=Qt.AlignCenter)
        pix = QPixmap("assets/house.png")
        self.imgLabel.setPixmap(pix.scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        vimg = QVBoxLayout(self.imgFrame)
        vimg.addWidget(self.imgLabel)

        # Layout
        grid = QGridLayout(central)
        grid.addWidget(self.lblPrompt, 0, 0)
        grid.addWidget(self.txtInput, 0, 1)
        grid.addWidget(self.grp, 1, 0, 1, 2)
        grid.addWidget(self.lblResult, 2, 0, 1, 2)
        grid.addWidget(self.imgFrame, 0, 2, 3, 1)

        hbtns = QHBoxLayout()
        hbtns.addStretch(1)
        hbtns.addWidget(self.btnConvert)
        hbtns.addWidget(self.btnClear)
        hbtns.addWidget(self.btnExit)
        grid.addLayout(hbtns, 3, 0, 1, 3)

        # Optional theming: ensure contrast/readability
        self.setStyleSheet("""
            QMainWindow { background: #243447; }
            QLabel, QGroupBox, QRadioButton { color: #f0f0f0; font-size: 14px; }
            QLineEdit { font-size: 14px; padding: 6px; }
            QPushButton { font-size: 14px; padding: 6px 12px; }
        """)

    def _wire_events(self):
        self.btnConvert.clicked.connect(self.on_convert)
        self.btnClear.clicked.connect(self.on_clear)
        self.btnExit.clicked.connect(QApplication.instance().quit)

    def _reset_form(self):
        self.txtInput.clear()
        self.lblResult.clear()
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()

    def _error(self, message: str):
        QMessageBox.critical(self, "Error", message)

    def on_clear(self):
        self._reset_form()

    def on_convert(self):
        text = self.txtInput.text().strip()
        if not text:
            self._error("Please enter a value.")
            return
        try:
            value = float(text)
        except ValueError:
            self._error("Value entered is not numeric.")
            return
        if value <= 0:
            self._error("Value must be positive.")
            return

        if self.rbInToM.isChecked():
            meters = value * INCH_TO_METER
            self.lblResult.setText(f"{value:.3f} inches = {meters:.3f} meters")
        else:
            inches = value / INCH_TO_METER
            self.lblResult.setText(f"{value:.3f} meters = {inches:.3f} inches")

def main():
    app = QApplication(sys.argv)
    w = ConverterWindow()
    w.resize(720, 320)
    w.show()
    sys.exit(app.exec())

#if name == "main":
   # main()
