import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

#how to quit an app in Qt and PySide6

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quit Button Example")
        self.setGeometry(100, 100, 300, 200)

        # Create a central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 1. Create the Quit Button
        self.quit_button = QPushButton("Quit Application")
        
        # 2. Connect the button's clicked signal to the application's quit slot
        # QApplication.instance() retrieves the current application instance
        self.quit_button.clicked.connect(QApplication.instance().quit)

        # 3. Add the button to the layout
        layout.addWidget(self.quit_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
