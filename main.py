import sounddevice as sd
import pyttsx3
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import commands
import time

print("Loading model...")
# Load model 
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


print("Model loaded.")
# Recording settings
SAMPLE_RATE = 16000
DURATION = 5  # seconds

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)

    engine.say(text)
    engine.runAndWait()

    engine.stop()
    del engine

    time.sleep(0.5)


if __name__ == "__main__" :
    while True:        
        print("Listening...")
        
        # Record from microphone
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
            )
        
        sd.wait()
        
            # Save recording
        write("voice.wav", SAMPLE_RATE, audio)
        
        print("Recognizing Command...")
        
                    # Translate speech to English
        segments, info = model.transcribe(
            "voice.wav",
            task="translate",
            vad_filter=True
        )
        
                    # Combine all text
        words = ""
        
        for segment in segments:
                    words += segment.text
        
        print(f"Recognized Command: {words} ")
        
        words = words.lower().strip()
        
        wake_words = ["jarvis", "jarves", "jarwes", "javace", "jarways"]

        if any(word in words for word in wake_words):
            speak("Jarvis Activated")
            print("Activated")

            while True:

                print("Listening...")

                # Record from microphone
                audio = sd.rec(
                int(DURATION * SAMPLE_RATE),
                samplerate=SAMPLE_RATE,
                channels=1,
                dtype="int16"
                )
                

                sd.wait()

                # Save recording
                write("voice.wav", SAMPLE_RATE, audio)

                print("Recognizing Command...")

                            # Translate speech to English
                segments, info = model.transcribe(
                 "voice.wav",
                 task="translate",
                 vad_filter=True
                )

                # Combine all text
                command = ""

                for segment in segments:
                    command += segment.text

                
                print(f"Recognized Command: {command} ")
                command = command.lower().strip()

                if not command:
                    continue

                if "deactivate" in command or "exit" in command:
                    print("Jarvis deactivated")
                    speak("Jarvis deactivated")
                    break

                
                commands.route(command)