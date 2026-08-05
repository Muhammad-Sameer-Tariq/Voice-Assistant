# Voice Assistant

Voice Assistant is a Python-based project that I developed as a beginner to practice voice recognition, AI integration, and computer automation.

The aim of this project was to create a program that can listen to my voice, understand commands, and perform different tasks on my computer. I also integrated Gemini AI so it can answer questions that are not handled by the standard commands.

Through this project, I learned how Python libraries, APIs, speech recognition, text-to-speech, and computer automation can be combined into one project.

## Features

* Voice recognition using Faster-Whisper
* Text-to-speech using pyttsx3
* Wake word activation using "Jarvis"
* Open websites
* Search Google
* Search YouTube
* Tell the current time and date
* Check battery percentage
* Increase and decrease system volume
* Shut down, restart, and put the computer to sleep
* Play a random local music file
* Ask questions using Gemini AI
* Open desktop applications
* Search Wikipedia and provide summaries
* Deactivate the assistant using voice commands
* VAD filtering with Faster-Whisper

## Technologies Used

* Python
* Faster-Whisper
* SoundDevice
* SciPy
* pyttsx3
* PyCaw
* psutil
* Google Gemini API
* python-dotenv
* Wikipedia

## Project Structure

```text
Voice-Assistant/
│
├── main.py
├── commands.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── modules/
    ├── __init__.py
    ├── sites.py
    ├── ai.py
    ├── apps.py
    ├── music.py
    ├── volume_control.py
    └── wiki.py
```

## Installation

First, clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd Voice-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Gemini API Setup

The AI feature uses the Gemini API.

Create a `.env` file in the project folder and add:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not upload the `.env` file to GitHub.

Make sure the `.env` file is included in `.gitignore`.

## Running the Project

Run the following command:

```bash
python main.py
```

The Faster-Whisper model will load first. Once it has loaded, the assistant will start listening for the wake word.

Say:

```text
Jarvis
```

After it has been activated, you can give it commands.

To deactivate it, say:

```text
Deactivate
```

or:

```text
Exit
```

## Example Commands

```text
Open Google
opn youtube

Search Google for Python tutorials

Search YouTube for Python projects

What's the time?

Tell me the date

Tell me battery percentage

Increase volume

Decrease volume

Play music

Ask AI what is Python?

Open app Chrome

Open app VS Code

Wiki Albert Einstein

Shutdown PC

Restart PC

Sleep PC

Deactivate
```

## Local Music

The music feature selects a random audio file from a local music folder.

The music folder path is currently configured in `modules/music.py`.

For example:

```python
music_folder = r"D:\Music"
```

Change this path to the location of your own music folder.

## Limitations

The project is primarily designed for Windows.

The microphone currently uses a fixed recording duration.

Background noise and microphone quality can affect speech recognition.

Some desktop application paths need to be configured manually.

The local music folder path also needs to be configured manually.

The Gemini AI feature requires an internet connection and an API key.

The Faster-Whisper model can take some time to load when running on a CPU.

At the moment, the assistant relies on predefined commands rather than understanding every possible way of expressing a command.

## Future Improvements

Some things I want to improve in the future are:

* Better voice activity detection
* Better background noise handling
* More flexible voice commands
* Automatic application detection
* Reminder and to-do functionality
* Better error handling
* More language support
* GUI for the assistant
* More computer automation features

## What I Learned

While making this project, I learned about:

* Python functions and modules
* APIs
* Environment variables
* Speech recognition
* Text-to-speech
* Audio recording
* File handling
* Windows system commands
* Opening applications and websites
* Exception handling
* Third-party Python libraries
* Git and GitHub
* Debugging

The most important thing I learned from this project is that getting a program to work is only one part of programming. A lot of time is also spent finding bugs and understanding why something is not working.

## About the Project

I am a beginner Python developer, and I created this project to gain practical experience with Python.

My goal was to learn how Python, APIs, speech recognition, AI, and computer automation can be used together in one project.

This is a learning project, not a professional-level virtual assistant. It represents what I have learned so far and gives me a foundation to build more advanced projects in the future.
