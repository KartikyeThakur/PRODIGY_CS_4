# PRODIGY_CS_4
This project implements a basic keylogger using Python. It records and logs all keystrokes pressed by the user and saves them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers. Always obtain explicit consent from users before running this software.

# Simple Keylogger

## Introduction
The **Simple Keylogger** project is a basic implementation of a keylogger using Python. It captures and logs all keystrokes pressed by the user and saves them to a file. This project is for educational purposes only, and ethical considerations and permissions are crucial for projects involving keyloggers. Always obtain explicit consent from users before running this software.

## Features
- **Keystroke Logging**: Captures and logs all keys pressed by the user.
- **File Logging**: Saves the recorded keystrokes to a log file (`keyfile.txt`).
- **Special Key Handling**: Recognizes and logs special keys like space, enter, and tab appropriately.
- **Background Operation**: Runs in the background, hiding the console window.
- **Stop Listener**: Stops the keylogger when the `Esc` key is pressed.

## Installation Guide

### Prerequisites
Ensure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/).

### Install Required Library
Install the `pynput` library, which is used to capture keyboard events:
```bash
pip install pynput
```

### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/KartikyeThakur/PRODIGY_CS_4.git
```

## Usage Instructions

### Running the Script
1. **Navigate to the Directory**:
   ```bash
   cd simple-keylogger
   ```
2. **Run the Application**:
   ```bash
   python keylogger.py
   ```

### Using the Tool
1. The keylogger will start running and capture all keystrokes.
2. Press the `Esc` key to stop the keylogger.
3. Check the `keyfile.txt` file for the recorded keystrokes.

### Example Output
The `keyfile.txt` file will contain logs like:
```
Hello World
This is a test
[Key.enter]
Logging keystrokes
```

## Detailed Features
- **Keystroke Logging**: 
  - Logs every keystroke, including uppercase and lowercase letters, numbers, and special characters.
- **File Logging**:
  - Stores the captured keystrokes in a text file (`keyfile.txt`) located in the script's directory.
- **Special Key Handling**:
  - Converts special keys (space, enter, tab) into their respective representations:
    - `Key.space` -> " "
    - `Key.enter` -> "\n"
    - `Key.tab` -> "\t"
- **Background Operation**:
  - The script runs in the background without displaying a console window.
- **Stop Listener**:
  - Pressing the `Esc` key will stop the keylogger and end the logging session.

## Lessons Learned
- **Event Handling**:
  - Implemented key event handling using the `pynput` library.
- **File I/O**:
  - Learned how to write captured keystrokes to a file for logging purposes.
- **Special Key Handling**:
  - Handled special keys appropriately to ensure readable log files.

## Optimizations
- **Encrypt Log File**:
  - Adding functionality to encrypt the log file to protect the captured keystrokes.
- **Stealth Mode**:
  - Implementing a stealth mode that hides the keylogger window completely (ensure ethical use).
- **Email Logs**:
  - Automatically send the log file via email at regular intervals (ensure ethical use).
## Sample Output
![Screenshot (132)](https://github.com/user-attachments/assets/709b6519-6adc-4861-b801-7e188254cc9a)
![Screenshot (131)](https://github.com/user-attachments/assets/317c07cd-859d-4a51-a9ea-2a96f9c26d88)

