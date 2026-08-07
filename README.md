Voice Assistant

Voice Assistant is a Python-based desktop assistant that I built as a learning project.

The main idea was to create an assistant that can listen to my voice, understand commands, and perform different tasks on my computer. I also added Gemini AI, weather, and news features so it can do more than just handle basic computer commands.

This project started as a simple voice assistant, but while building it I learned about speech recognition, APIs, Python modules, automation, system control, and working with different libraries together.


Features

Currently, Voice Assistant can:

- Recognize voice commands using Faster-Whisper
- Respond using pyttsx3
- Activate using the wake word "Jarvis"
- Open websites
- Search Google
- Search YouTube
- Tell the current time
- Tell the current date
- Check battery percentage
- Get current weather information
- Get the latest news headlines
- Increase and decrease system volume
- Shut down the computer
- Restart the computer
- Put the computer to sleep
- Play a random song from a local music folder
- Ask questions using Gemini AI
- Open desktop applications
- Search Wikipedia and give short summaries
- Deactivate the assistant using voice commands
- Use Faster-Whisper VAD to help filter non-speech audio


Technologies and Libraries

I used Python and the following libraries:

- Faster-Whisper - Speech recognition
- SoundDevice - Recording audio from the microphone
- SciPy - Saving recorded audio
- pyttsx3 - Text-to-speech
- PyCaw - Controlling Windows system volume
- psutil - Getting battery information
- Google GenAI - Gemini AI integration
- python-dotenv - Loading API keys from environment variables
- Requests - Making API requests
- Wikipedia - Getting Wikipedia summaries
- Weather API - Getting weather information
- News API - Getting news headlines
- webbrowser - Opening websites
- os - Working with files and Windows system commands


Project Structure

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


Installation

1. Clone the repository

git clone https://github.com/Muhammad-Sameer-Tariq/Voice-Assistant.git

cd Voice-Assistant


2. Create a virtual environment

I recommend using a virtual environment so the project dependencies stay separate from other Python projects.

python -m venv .venv


3. Activate the virtual environment

On Windows:

.venv\Scripts\activate


4. Install the required libraries

pip install -r requirements.txt


API Setup

Voice Assistant uses APIs for Gemini AI, weather information, and news.

Create a .env file in the main project folder and add:

GEMINI_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_weather_api_key
NEWS_API_KEY=your_news_api_key

The .env file should not be uploaded to GitHub.

Make sure .env is included in .gitignore.


Running the Project

After installing everything, run:

python main.py

The Faster-Whisper model will load first. After it loads, Voice Assistant will start listening for the wake word.

Say:

Jarvis

After activation, you can give it commands.

To deactivate it, say:

Deactivate

or:

Exit


Example Commands

Some commands you can try:

Jarvis

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


Weather

The weather feature uses a weather API to get current weather information for a city.

It can provide information such as:

- Temperature
- Feels-like temperature
- Weather description
- Humidity

For example:

What's the weather in Islamabad?

The weather API key is stored in the .env file.


News

The news feature uses a news API to get recent news headlines.

Currently, it gets five news headlines related to Pakistan.

The headlines can be displayed in the terminal and read aloud by the assistant using text-to-speech.

For example:

Give me the latest news

or:

News

The news API key is stored in the .env file.


Local Music

The music feature currently plays a random audio file from a local music folder.

The folder path is configured inside modules/music.py.

For example:

music_folder = r"D:\Music"

You should change this path to your own music folder.

Because this path is specific to my computer, the music feature will need to be configured if someone else wants to use the project.


Current Limitations

This project is still a learning project, so it has some limitations.

- It is currently designed mainly for Windows.
- The microphone recording uses a fixed recording duration.
- Voice recognition accuracy can be affected by background noise and microphone quality.
- Some desktop application paths are manually configured.
- The local music folder path needs to be configured manually.
- Gemini AI, weather, and news features require an internet connection and valid API keys.
- The Faster-Whisper model can take some time to load, especially on a CPU.
- The assistant currently understands a predefined set of commands rather than every possible way of saying something.


Future Improvements

Some things I may improve in future versions:

- Better microphone-level voice activity detection
- Better background noise handling
- More flexible natural-language commands
- Automatic application detection instead of hardcoded paths
- Reminder and to-do functionality
- Better error handling
- More languages and better multilingual recognition
- GUI for the assistant
- More computer automation features


What I Learned

This project helped me understand how different parts of a Python application can work together.

While making it, I practiced:

- Python functions and modules
- Importing and organizing code
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
- Debugging real problems instead of only following tutorials

One of the biggest things I learned from this project was that making something work is only one part of programming. Debugging and figuring out why something is not working took a significant part of the project.


About the Project

This is one of my Python projects while learning programming and building my skills in automation, APIs, AI integration, and software development.

I built this project mainly to learn by actually making something instead of only following Python tutorials.

More improvements will probably come as I learn more.