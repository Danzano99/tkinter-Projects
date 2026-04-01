import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QSizePolicy
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Alignment Example")
        self.setGeometry(100, 100, 400, 300)

        # Create the label
        label = QLabel("Centered Text", self)
        
        # --- Align the text to center horizontally and vertically ---
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        # Optional: Visualize the label area
        label.setStyleSheet("QLabel { background-color: red; }")

        # Set the label as the central widget
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
