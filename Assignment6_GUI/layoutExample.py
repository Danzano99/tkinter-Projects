import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Widget Display Example")
        self.resize(300, 200)

        # Create widgets
        self.label = QLabel("Hello, PySide6!", self)
        self.button = QPushButton("Click Me", self)

        # Create a layout
        layout = QVBoxLayout()
        
        # Add widgets to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the layout on the main window (self is a QWidget in this case)
        self.setLayout(layout)
        
        # Connect the button signal to a slot
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show() # Widgets are hidden by default and must be explicitly shown
    sys.exit(app.exec())
