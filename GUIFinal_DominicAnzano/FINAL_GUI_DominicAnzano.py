# Name: Dominic Anzano
# Course: GUI Development CPSC 3118
# Final Project: Student Grade Calculator

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QGroupBox
)
from PySide6.QtCore import Qt

BACKGROUND_COLOR = "#EBEBEB"
CARD_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#9FE7EF"
SECONDARY_COLOR = "#8CD4DC"
ACCENT_COLOR = "#BCF0F6"
TEXT_COLOR = "#000000"
MUTED_TEXT_COLOR = "#333333"


class BasicGradeCalculator(QWidget):
    """
    A basic student grade calculator that accepts three number grades,
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Grade Calculator")
        self.resize(540, 560)
        self.setMinimumSize(540, 560)

        self.create_widgets()
        self.create_layout()
        self.connect_events()
        self.apply_styles()

    def prepare_input_field(self, input_field, placeholder_text):
        input_field.setPlaceholderText(placeholder_text)
        input_field.setFixedHeight(36)

    def create_widgets(self):
        """
        Creates all widgets used in the application.
        """

        self.title_label = QLabel("Student Grade Calculator")
        self.title_label.setObjectName("title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.instructions_label = QLabel("Enter three number grades between 0 and 100.")
        self.instructions_label.setObjectName("instructions_label")
        self.instructions_label.setAlignment(Qt.AlignCenter)

        self.grade_one_label = QLabel("Grade 1:")
        self.grade_one_input = QLineEdit()
        self.prepare_input_field(self.grade_one_input, "Example: 74.5")

        self.grade_two_label = QLabel("Grade 2:")
        self.grade_two_input = QLineEdit()
        self.prepare_input_field(self.grade_two_input, "Example: 88")

        self.grade_three_label = QLabel("Grade 3:")
        self.grade_three_input = QLineEdit()
        self.prepare_input_field(self.grade_three_input, "Example: 91.25")

        self.calculate_button = QPushButton("Calculate")
        self.clear_button = QPushButton("Clear")
        self.exit_button = QPushButton("Exit")

        self.average_result_label = QLabel("Average: Not calculated yet")
        self.letter_grade_result_label = QLabel("Letter Grade: Not calculated yet")
        self.feedback_result_label = QLabel("Feedback: Enter grades and click Calculate.")
        self.feedback_result_label.setWordWrap(True)

    def create_layout(self):
        """
        Organizes widgets using PySide6.
        """

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(26, 22, 26, 22)
        main_layout.setSpacing(16)

        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.instructions_label)

        input_group_box = QGroupBox("Grade Input")
        input_grid_layout = QGridLayout()
        input_grid_layout.setHorizontalSpacing(12)
        input_grid_layout.setVerticalSpacing(14)

        input_grid_layout.addWidget(self.grade_one_label, 0, 0)
        input_grid_layout.addWidget(self.grade_one_input, 0, 1)

        input_grid_layout.addWidget(self.grade_two_label, 1, 0)
        input_grid_layout.addWidget(self.grade_two_input, 1, 1)

        input_grid_layout.addWidget(self.grade_three_label, 2, 0)
        input_grid_layout.addWidget(self.grade_three_input, 2, 1)

        input_group_box.setLayout(input_grid_layout)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.exit_button)

        result_group_box = QGroupBox("Results")
        result_layout = QVBoxLayout()
        result_layout.setSpacing(10)

        result_layout.addWidget(self.average_result_label)
        result_layout.addWidget(self.letter_grade_result_label)
        result_layout.addWidget(self.feedback_result_label)

        result_group_box.setLayout(result_layout)

        main_layout.addWidget(input_group_box)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(result_group_box)

        self.setLayout(main_layout)

    def connect_events(self):
        """
        Connects button clicks to functions.
        """

        self.calculate_button.clicked.connect(self.calculate_grade_results)
        self.clear_button.clicked.connect(self.clear_all_fields)
        self.exit_button.clicked.connect(self.close)

    def calculate_grade_results(self):
        """
        Captures input, validates it, calculates the average,
        determines the letter grade, and updates the GUI.
        """

        try:
            grade_one = float(self.grade_one_input.text())
            grade_two = float(self.grade_two_input.text())
            grade_three = float(self.grade_three_input.text())

            grades = [grade_one, grade_two, grade_three]

            for grade in grades:
                if grade < 0 or grade > 100:
                    QMessageBox.warning(
                        self,
                        "Invalid Grade",
                        "Each grade must be between 0 and 100."
                    )
                    return

            average_grade = sum(grades) / len(grades)
            letter_grade = self.determine_letter_grade(average_grade)
            feedback_message = self.create_feedback_message(letter_grade)

            self.average_result_label.setText(f"Average: {average_grade:.2f}")
            self.letter_grade_result_label.setText(f"Letter Grade: {letter_grade}")
            self.feedback_result_label.setText(f"Feedback: {feedback_message}")

        except ValueError:
            QMessageBox.critical(
                self,
                "Invalid Input",
                "Please enter valid numeric grades in all three boxes."
            )

    def determine_letter_grade(self, average_grade):
        """
        Determines the letter grade based on the average.
        """

        if average_grade >= 90:
            return "A"
        elif average_grade >= 80:
            return "B"
        elif average_grade >= 70:
            return "C"
        elif average_grade >= 60:
            return "D"
        else:
            return "F"

    def create_feedback_message(self, letter_grade):
        """
        Creates a message based on the letter grade.
        """

        if letter_grade == "A":
            return "Excellent work. You are performing wonderfully. Get a snack, you deserve it!"
        elif letter_grade == "B":
            return "Good job. You are doing well overall. Keep up the good work!"
        elif letter_grade == "C":
            return "C's get degrees... but there is room to improve."
        elif letter_grade == "D":
            return "You may want to review the material and ask for help. Preferably soon."
        else:
            return "This grade needs improvement. Consider studying more and asking for support. Or Praying"

    def clear_all_fields(self):
        """
        Clears all input fields and resets results.
        """

        self.grade_one_input.clear()
        self.grade_two_input.clear()
        self.grade_three_input.clear()

        self.average_result_label.setText("Average: Not calculated yet")
        self.letter_grade_result_label.setText("Letter Grade: Not calculated yet")
        self.feedback_result_label.setText("Feedback: Enter grades and click Calculate.")

        self.grade_one_input.setFocus()

    def apply_styles(self):
        """
        Applies visuals to the application.
        """

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {BACKGROUND_COLOR};
                color: {TEXT_COLOR};
                font-family: Arial;
                font-size: 14px;
            }}

            QGroupBox QLabel {{
                background-color: transparent;
            }}

            QLabel#title_label {{
                color: {TEXT_COLOR};
                font-size: 24px;
                font-weight: bold;
                padding: 12px;
                background-color: {PRIMARY_COLOR};
                border-radius: 14px;
            }}

            QLabel#instructions_label {{
                color: {MUTED_TEXT_COLOR};
                font-size: 14px;
                padding-bottom: 6px;
                background-color: transparent;
            }}

            QGroupBox {{
                background-color: {CARD_COLOR};
                border: 2px solid {SECONDARY_COLOR};
                border-radius: 14px;
                margin-top: 12px;
                padding: 16px;
                font-weight: bold;
            }}

            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 14px;
                padding: 0 8px;
                color: {TEXT_COLOR};
                background-color: {BACKGROUND_COLOR};
            }}

            QLineEdit {{
                background-color: white;
                border: 1px solid #A8A8A8;
                border-radius: 8px;
                padding: 6px;
            }}

            QLineEdit:focus {{
                border: 2px solid {SECONDARY_COLOR};
                background-color: {ACCENT_COLOR};
            }}

            QPushButton {{
                background-color: {SECONDARY_COLOR};
                color: {TEXT_COLOR};
                border: none;
                border-radius: 10px;
                padding: 11px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: {PRIMARY_COLOR};
            }}

            QPushButton:pressed {{
                background-color: {ACCENT_COLOR};
            }}
        """)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    grade_calculator_window = BasicGradeCalculator()
    grade_calculator_window.show()
    sys.exit(application.exec())