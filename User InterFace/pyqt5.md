# PyQt5 Module

## Overview

This repository contains a PyQt5-based application designed to demonstrate the capabilities of the PyQt5 framework for building GUI applications in Python. The application provides a basic template that you can extend and customize for your own projects.

## Features

- **Simple User Interface:** A basic window with menus, buttons, and status bar.
- **Event Handling:** Demonstrates how to handle events like button clicks and menu selections.
- **Layout Management:** Uses layouts to arrange widgets in the window.
- **Custom Widgets:** Shows how to create and integrate custom widgets.
- **Dialogs and Messages:** Incorporates various dialogs and message boxes.
- **Resource Management:** Handles application resources like icons and images.

## Requirements

- Python 3.7+
- PyQt5

## Installation

To install the necessary dependencies, you can use `pip`:

```sh
pip install PyQt5
```

## Usage

To run the application, execute the following command in your terminal:

```sh
python main.py
```

## Project Structure

```plaintext
.
├── README.md
├── main.py
├── requirements.txt
├── resources/
│   └── icons/
│       └── app_icon.png
└── src/
    ├── __init__.py
    ├── main_window.py
    ├── custom_widget.py
    └── utils.py
```

- `main.py`: The entry point of the application.
- `src/main_window.py`: Contains the main window class definition.
- `src/custom_widget.py`: Contains custom widget definitions.
- `src/utils.py`: Utility functions used in the application.
- `resources/icons/`: Directory for storing icons and other resources.

## Example Code

Here is a brief example of how to create a simple PyQt5 window:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Example')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        label = QLabel('Hello, PyQt5!', self)
        layout.addWidget(label)

        button = QPushButton('Click Me', self)
        button.clicked.connect(self.showDialog)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setText('Button Clicked!')
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
```

## Key Methods and Abilities

### Main Window (`QMainWindow`)
- `setWindowTitle(str)`: Sets the window title.
- `setGeometry(x, y, width, height)`: Sets the window position and size.
- `setCentralWidget(QWidget)`: Sets the central widget of the window.

### Widgets
- `QLabel`: Displays text or an image.
  - `setText(str)`: Sets the label text.
  - `move(x, y)`: Moves the label to a specified position.
- `QPushButton`: A clickable button.
  - `clicked.connect(func)`: Connects the button click event to a function.
- `QVBoxLayout`: A vertical box layout.
  - `addWidget(widget)`: Adds a widget to the layout.
- `QWidget`: The base class for all UI objects.
  - `setLayout(QLayout)`: Sets the layout for the widget.

### Dialogs
- `QMessageBox`: A message box dialog.
  - `setText(str)`: Sets the message text.
  - `exec_()`: Executes the dialog and waits for the user response.

### Event Handling
- `clicked.connect(func)`: Connects a widget signal to a slot (function).

### Custom Widgets
- Custom widgets can be created by subclassing `QWidget` or any other widget class and overriding its methods.

### Resource Management
- Icons and images can be added to the application by placing them in the `resources` directory and referencing them in the code.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
