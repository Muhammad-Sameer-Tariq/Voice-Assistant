# Voice Assistant

Voice Assistant is a Python-based desktop assistant that I built as a beginner project.

The main idea was to create an assistant that can listen to my voice, understand commands, and perform different tasks on my computer. I also added Gemini AI, weather, and news features so it can do more than just handle basic computer commands.

While building this project, I learned about speech recognition, APIs, Python modules, automation, system control, and how different Python libraries can work together.

## Features

- Voice recognition using Faster-Whisper
- Text-to-speech using pyttsx3
- Wake word activation using "Jarvis"
- Open websites
- Search Google
- Search YouTube
- Tell the current time
- Tell the current date
- Check battery percentage
- Get current weather information
- Get latest news headlines
- Increase and decrease system volume
- Shut down the computer
- Restart the computer
- Put the computer to sleep
- Play a random song from a local music folder
- Ask questions using Gemini AI
- Open desktop applications
- Search Wikipedia and get short summaries
- Deactivate the assistant using voice commands
- VAD filtering with Faster-Whisper

## Technologies and Libraries

- Python
- Faster-Whisper
- SoundDevice
- SciPy
- pyttsx3
- PyCaw
- psutil
- Google GenAI
- python-dotenv
- Requests
- Wikipedia
- Weather API
- News API
- webbrowser
- os

## Project Structure

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
        ├── wiki.py
        ├── weather.py
        └── news.py

## Installation

### 1. Clone the repository

    git clone https://github.com/Muhammad-Sameer-Tariq/Voice-Assistant.git
    cd Voice-Assistant

### 2. Create a virtual environment

    python -m venv .venv

### 3. Activate the virtual environment

On Windows:

    .venv\Scripts\activate

### 4. Install the required libraries

    pip install -r requirements.txt

## API Setup

This project uses APIs for Gemini AI, weather information, and news.

Create a file named .env in the main project folder.

Add your API keys like this:

    GEMINI_API_KEY=your_gemini_api_key
    WEATHER_API_KEY=your_weather_api_key
    NEWS_API_KEY=your_news_api_key

Do not upload the .env file to GitHub.

Make sure .env is included in your .gitignore file.

## Running the Project

After installing the required libraries and setting up the API keys, run:

    python main.py

The Faster-Whisper model will load first.

After the model has loaded, the assistant will start listening for the wake word.

Say:

    Jarvis

After activation, you can give the assistant commands.

To deactivate the assistant, say:

    Deactivate

or:

    Exit

## Example Commands

    Open Google

    Search Google for Python tutorials

    Search YouTube for Python projects

    What's the time?

    Tell me the date

    Tell me battery percentage

    What's the weather in Islamabad?

    What's the weather in Peshawar?

    Give me the latest news

    News

    Increase volume

    Decrease volume

    Play music

    Ask AI what is Python?

    Open Chrome

    Open VS Code

    Wiki Albert Einstein

    Shutdown PC

    Restart PC

    Sleep PC

    Deactivate

## Weather Feature

The weather feature uses a weather API to get current weather information for a city.

It can provide:

- Temperature
- Feels-like temperature
- Weather description
- Humidity

Example:

    What's the weather in Islamabad?

The weather API key is stored in the .env file.

## News Feature

The news feature uses a news API to get recent news headlines.

Currently, it gets five news headlines related to Pakistan.

The headlines can be displayed in the terminal and read aloud by the assistant using text-to-speech.

Example:

    Give me the latest news

or:

    News

The news API key is stored in the .env file.

## Gemini AI Feature

The Gemini AI feature allows the assistant to answer questions that are not handled by the predefined commands.

Example:

    Ask AI what is Python?

The Gemini API key is stored in the .env file and should never be uploaded to GitHub.

## Local Music

The music feature plays a random audio file from a local music folder.

The folder path is configured inside modules/music.py.

For example:

    music_folder = r"D:\Music"

Change this path to the location of your own music folder.

Because this path is specific to my computer, this feature needs to be configured if someone else wants to use the project.

## Current Limitations

This is still a beginner learning project, so it has some limitations.

- It is mainly designed for Windows.
- The microphone uses a fixed recording duration.
- Background noise and microphone quality can affect speech recognition.
- Some desktop application paths need to be configured manually.
- The local music folder path needs to be configured manually.
- Gemini AI, weather, and news features require an internet connection and valid API keys.
- Faster-Whisper can take some time to load, especially when running on a CPU.
- The assistant currently relies on predefined commands rather than understanding every possible way of saying a command.

## Future Improvements

Some things I may improve in future versions:

- Better voice activity detection
- Better background noise handling
- More flexible voice commands
- Automatic application detection
- Reminder and to-do functionality
- Better error handling
- More language support
- GUI for the assistant
- More computer automation features

## What I Learned

This project helped me understand how different parts of a Python application can work together.

While making it, I practiced:

- Python functions and modules
- Organizing code into different files
- Working with APIs
- Using environment variables
- Speech recognition
- Text-to-speech
- Audio recording
- File handling
- Random file selection
- Windows system commands
- Opening applications and websites
- Exception handling
- Using third-party Python libraries
- Git and GitHub
- Debugging

One of the biggest things I learned from this project is that making a program work is only one part of programming. A lot of time is also spent finding bugs and understanding why something is not working.

## About the Project

I am a beginner Python developer, and I built this project to gain practical experience with Python.

My goal was to learn how Python, APIs, speech recognition, AI, and computer automation can be used together in one project.

This is a learning project, not a professional-level virtual assistant. It represents what I have learned so far and gives me a foundation to build more advanced projects in the future.