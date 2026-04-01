import sys
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Numbers")
        #x, y, w, h
        self.setGeometry(400, 100, 200, 200)
       
        # Set up widgets
        self.label = QLabel()
        f = self.label.font()
        f.setPointSize(25)
        self.label.setFont(f)
        # --- Align the text to center horizontally and vertically ---
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        #Create the Button
        self.rand_button = QPushButton("Random Numbers")

        # Create layout and add widgets
        # Create a central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Optional: Visualize the label area
        self.label.setStyleSheet("QLabel { background-color: lightsteelblue; }")
        
        layout.addWidget(self.label)
        layout.addWidget(self.rand_button)
        
        # Set layout
        self.setLayout(layout)
        
        # Add button signal to slot
        self.rand_button.pressed.connect(self.update_label)

    def update_label(self):
        n = random.randint(1, 6)
        self.label.setText(f"{n}")


app = QApplication()
window = MainWindow()
window.show()
app.exec()
