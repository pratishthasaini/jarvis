# jarvis

A Python-based personal assistant project called "Simple Jarvis" that can perform speech recognition, text-to-speech, and execute basic tasks based on voice commands.

## Features
- Recognizes your voice commands using SpeechRecognition.
- Provides spoken feedback using pyttsx3.
- Simple and easy to extend.

## Requirements
Ensure you have Python 3.6+ installed on your system.

## Getting Started

### Step 1: Clone the Repository
```bash
# If not already done
mkdir SimpleJarvis
cd SimpleJarvis
```

### Step 2: Create a Virtual Environment
A virtual environment helps isolate dependencies for your project.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/MacOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required libraries: 

```bash
pip install --upgrade pip
pip install speechrecognition pyaudio setuptools pyttsx3
```

### Step 4: Run the Project
Create and save a script (e.g., `simple_jarvis.py`) with your Jarvis logic. Then, execute it.

```bash
python simple_jarvis.py
```

## Notes
- Ensure your microphone is properly configured for use with PyAudio.
- If PyAudio installation fails, you may need to install it using your system's package manager (e.g., `brew`, `apt`, or manually download the binaries for Windows).

### Troubleshooting PyAudio Installation
If you encounter issues installing PyAudio, you can try:

#### Linux
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

#### MacOS
```bash
brew install portaudio
pip install pyaudio
```

#### Windows
Download the appropriate `.whl` file for PyAudio from [PyAudio binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/) and install it:
```bash
pip install <path_to_downloaded_whl>
```
