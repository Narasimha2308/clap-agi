# 👏 ClapAGI – Double Clap Desktop Automation

ClapAGI is a real-time Python application that listens for a **double clap** using your computer's microphone and automatically performs desktop actions such as opening websites or launching applications.

It uses **PyAudio** for real-time audio input and **NumPy** for audio signal processing, making it a lightweight desktop automation tool.

---

## Features

* 👏 Real-time double clap detection
* 🚀 Launch websites or desktop applications
* 🌐 Cross-platform browser support
* ⚡ Lightweight and fast
* 🔧 Easily customizable for your own workflow

---

## Tech Stack

* Python 3.x
* PyAudio
* NumPy
* WebBrowser
* Real-Time Audio Processing

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/clap-agi.git
cd clap-agi
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

When the program starts, you'll see:

```text
==================================================
👏 Double Clap Detector Started
Listening... Press Ctrl+C to stop.
==================================================
```

Clap **twice** within one second to trigger the configured action.

---

## Current Functionality

After detecting a double clap, the application automatically:

* Opens Cristiano Ronaldo's official YouTube channel.
* Prevents repeated triggers using a cooldown timer.

---

## Customize Your Actions

Open `app.py` and edit the action inside:

```python
if clap_count == 2:
```

### Open a Website

```python
import webbrowser

webbrowser.open("https://www.youtube.com/@cristiano")
```

### Open VS Code

```python
import subprocess

subprocess.Popen([
    r"C:\Users\YOUR_USERNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe"
])
```

### Open Notepad

```python
subprocess.Popen("notepad.exe")
```

### Open Calculator

```python
subprocess.Popen("calc.exe")
```

### Open a Folder

```python
import os

os.startfile(r"D:\Projects")
```

You can combine multiple actions to create your own automated workspace.

---

## Project Structure

```text
clap-agi/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Improvements

* Voice command support
* AI assistant integration
* Machine learning-based clap recognition
* Custom hotkey automation
* Multi-clap gesture detection
* Desktop notification support

---

## License

This project is released under the MIT License.

---

## Author

Developed using Python for real-time audio-based desktop automation.
