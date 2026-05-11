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


class PolishedGradeCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Grade Calculator")
        self.resize(680, 840)
        self.setMinimumSize(680, 840)

        self.create_widgets()
        self.create_layout()
        self.connect_events()
        self.apply_styles()

    def prepare_input_field(self, input_field, placeholder_text):
        input_field.setPlaceholderText(placeholder_text)
        input_field.setFixedHeight(36)

    def create_widgets(self):

        self.title_label = QLabel("Student Grade Calculator")
        self.title_label.setObjectName("title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.subtitle_label = QLabel("Enter student details and grades to calculate the final result.")
        self.subtitle_label.setObjectName("subtitle_label")
        self.subtitle_label.setAlignment(Qt.AlignCenter)

        self.student_name_label = QLabel("Student Name:")
        self.student_name_input = QLineEdit()
        self.prepare_input_field(self.student_name_input, "Example: Dominic Anzano")

        self.course_name_label = QLabel("Course Name:")
        self.course_name_input = QLineEdit()
        self.prepare_input_field(self.course_name_input, "Example: Python Programming")

        self.grade_one_label = QLabel("Grade 1:")
        self.grade_one_input = QLineEdit()
        self.prepare_input_field(self.grade_one_input, "Required")

        self.grade_two_label = QLabel("Grade 2:")
        self.grade_two_input = QLineEdit()
        self.prepare_input_field(self.grade_two_input, "Required")

        self.grade_three_label = QLabel("Grade 3:")
        self.grade_three_input = QLineEdit()
        self.prepare_input_field(self.grade_three_input, "Required")

        self.grade_four_label = QLabel("Grade 4:")
        self.grade_four_input = QLineEdit()
        self.prepare_input_field(self.grade_four_input, "Required")

        self.grade_five_label = QLabel("Grade 5:")
        self.grade_five_input = QLineEdit()
        self.prepare_input_field(self.grade_five_input, "Required")

        self.calculate_button = QPushButton("Calculate Grade")
        self.clear_button = QPushButton("Clear Form")
        self.exit_button = QPushButton("Exit")

        self.student_result_label = QLabel("Student: Not entered")
        self.course_result_label = QLabel("Course: Not entered")
        self.average_result_label = QLabel("Average: Not calculated yet")
        self.letter_grade_result_label = QLabel("Letter Grade: Not calculated yet")
        self.feedback_result_label = QLabel("Feedback: Enter information and click Calculate Grade.")
        self.feedback_result_label.setWordWrap(True)

    def create_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(26, 22, 26, 22)
        main_layout.setSpacing(14)

        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.subtitle_label)

        student_group_box = QGroupBox("Student Information")
        student_grid_layout = QGridLayout()
        student_grid_layout.setSpacing(10)

        student_grid_layout.addWidget(self.student_name_label, 0, 0)
        student_grid_layout.addWidget(self.student_name_input, 0, 1)

        student_grid_layout.addWidget(self.course_name_label, 1, 0)
        student_grid_layout.addWidget(self.course_name_input, 1, 1)

        student_group_box.setLayout(student_grid_layout)

        grade_group_box = QGroupBox("Grade Information")
        grade_grid_layout = QGridLayout()
        grade_grid_layout.setHorizontalSpacing(10)
        grade_grid_layout.setVerticalSpacing(14)

        grade_grid_layout.addWidget(self.grade_one_label, 0, 0)
        grade_grid_layout.addWidget(self.grade_one_input, 0, 1)

        grade_grid_layout.addWidget(self.grade_two_label, 1, 0)
        grade_grid_layout.addWidget(self.grade_two_input, 1, 1)

        grade_grid_layout.addWidget(self.grade_three_label, 2, 0)
        grade_grid_layout.addWidget(self.grade_three_input, 2, 1)

        grade_grid_layout.addWidget(self.grade_four_label, 3, 0)
        grade_grid_layout.addWidget(self.grade_four_input, 3, 1)

        grade_grid_layout.addWidget(self.grade_five_label, 4, 0)
        grade_grid_layout.addWidget(self.grade_five_input, 4, 1)

        grade_group_box.setLayout(grade_grid_layout)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.exit_button)

        result_group_box = QGroupBox("Results")
        result_layout = QVBoxLayout()
        result_layout.setSpacing(8)

        result_layout.addWidget(self.student_result_label)
        result_layout.addWidget(self.course_result_label)
        result_layout.addWidget(self.average_result_label)
        result_layout.addWidget(self.letter_grade_result_label)
        result_layout.addWidget(self.feedback_result_label)

        result_group_box.setLayout(result_layout)

        main_layout.addWidget(student_group_box)
        main_layout.addWidget(grade_group_box)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(result_group_box)

        self.setLayout(main_layout)

    def connect_events(self):
        self.calculate_button.clicked.connect(self.calculate_grade_results)
        self.clear_button.clicked.connect(self.clear_all_fields)
        self.exit_button.clicked.connect(self.close)

    def calculate_grade_results(self):
        student_name = self.student_name_input.text().strip()
        course_name = self.course_name_input.text().strip()

        if student_name == "":
            QMessageBox.warning(
                self,
                "Missing Student Name",
                "Please enter a student name."
            )
            return

        if course_name == "":
            QMessageBox.warning(
                self,
                "Missing Course Name",
                "Please enter a course name."
            )
            return

        try:
            grade_one = float(self.grade_one_input.text())
            grade_two = float(self.grade_two_input.text())
            grade_three = float(self.grade_three_input.text())
            grade_four = float(self.grade_four_input.text())
            grade_five = float(self.grade_five_input.text())

            grades = [
                grade_one,
                grade_two,
                grade_three,
                grade_four,
                grade_five
            ]

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

            self.student_result_label.setText(f"Student: {student_name}")
            self.course_result_label.setText(f"Course: {course_name}")
            self.average_result_label.setText(f"Average: {average_grade:.2f}")
            self.letter_grade_result_label.setText(f"Letter Grade: {letter_grade}")
            self.feedback_result_label.setText(f"Feedback: {feedback_message}")

        except ValueError:
            QMessageBox.critical(
                self,
                "Invalid Input",
                "Please enter valid number grades in every grade box."
            )

    def determine_letter_grade(self, average_grade):
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
        if letter_grade == "A":
            return "Excellent work. The student is performing at a very high level."
        elif letter_grade == "B":
            return "Good job. The student is doing well overall."
        elif letter_grade == "C":
            return "The student is passing, but there is room for improvement."
        elif letter_grade == "D":
            return "The student should review the material and seek extra support."
        else:
            return "The student needs significant improvement and should ask for help soon."

    def clear_all_fields(self):
        self.student_name_input.clear()
        self.course_name_input.clear()
        self.grade_one_input.clear()
        self.grade_two_input.clear()
        self.grade_three_input.clear()
        self.grade_four_input.clear()
        self.grade_five_input.clear()

        self.student_result_label.setText("Student: Not entered")
        self.course_result_label.setText("Course: Not entered")
        self.average_result_label.setText("Average: Not calculated yet")
        self.letter_grade_result_label.setText("Letter Grade: Not calculated yet")
        self.feedback_result_label.setText("Feedback: Enter information and click Calculate Grade.")

        self.student_name_input.setFocus()

    def apply_styles(self):
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
                font-size: 26px;
                font-weight: bold;
                padding: 12px;
                background-color: {PRIMARY_COLOR};
                border-radius: 14px;
            }}

            QLabel#subtitle_label {{
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
    grade_calculator_window = PolishedGradeCalculator()
    grade_calculator_window.show()
    sys.exit(application.exec())