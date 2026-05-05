# Temperature Converter(Celsius) MVC App

## Description

This is a simple desktop GUI application built with Python, PySide6, and Qt Designer. The app allows the user to enter a Fahrenheit temperature and convert it to Celsius.

The purpose of this project is to demonstrate a small proof of concept application that follows the Model-View-Controller architectural pattern.

## Features

- Accepts Fahrenheit temperature input from the user
- Converts Fahrenheit to Celsius
- Displays the converted Celsius result
- Shows an error message if the input is not a valid number
- Changes the result color and frame border based on the converted temperature

## MVC Overview

This project follows the Model-View-Controller design pattern.

### Model

The Model is located in `model.py`.

The Model handles the application logic. In this project, it converts the Fahrenheit input into Celsius and returns the result. The Model does not import or depend on PySide6.

### View

The View is created using Qt Designer and saved as `view.ui`.

The View contains the visual interface, including the input box, button, labels, and frame. The `view.ui` file is converted into `view.py` using `pyside6-uic`.

### Controller

The Controller is located in `controller.py`.

The Controller connects the View and the Model. It listens for the button click, gets the input from the View, sends the input to the Model, and updates the result label and frame color based on the conversion result.

## Project Structure

```text
GUI_Capstone/
│
├── main.py
├── model.py
├── controller.py
├── view.ui
├── view.py
└── README.md
```

## How to Run

### 1. Install PySide6

If PySide6 is not already installed, open a terminal and run:

```bash
pip install PySide6
```

### 2. Convert the UI file

The GUI was created in Qt Designer and saved as `view.ui`. To generate the Python version of the UI, run:

```bash
pyside6-uic view.ui -o view.py
```

Run this command from the same folder that contains `view.ui`.

### 3. Start the application

After `view.py` has been created, run:

```bash
python main.py
```

The Temperature Converter window should open.
