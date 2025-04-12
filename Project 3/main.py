from http import client
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import os
import time
import logging
from datetime import datetime
from openai import OpenAI
from gtts import gTTS
import tempfile

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Adjust recognizer sensitivity parameters
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

# Store API keys
newsapi = "your api key" #replace with your own newsapi key
openai_api_key = "your api key" #replace with your own openai api key

#openai integration
'''
def aiprocess(command):
    try:
        client = OpenAI(api_key=openai_api_key)
        
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, a virtual assistant skilled in general tasks like Alexa and Google Assistant. Provide brief, helpful responses."},
                {"role": "user", "content": command}
            ]
        )
        
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Error with OpenAI API: {e}")
        return "I'm having trouble connecting to my AI services. Please try again later."
'''

# Using pyttsx3 for text to speech (free)
def speak_old(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logging.error(f"Error with pyttsx3: {e}")
        print(f"Text-to-speech error: {text}")

# Using gTTS for text to speech (paid)
def speak(text):
    try:
        # Use a temporary file instead of fixed "output.mp3"
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_path = temp_file.name
            
        tts = gTTS(text=text, lang="en")
        tts.save(temp_path)
        
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        
        # Clean up temporary file
        os.remove(temp_path)
    except Exception as e:
        logging.error(f"Error with gTTS: {e}")
        # Fall back to pyttsx3
        speak_old(text)

def get_news(topic=None):
    """Get news headlines optionally filtered by topic."""
    import requests
    
    try:
        if topic:
            url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={newsapi}&pageSize=3"
        else:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}&pageSize=3"
            
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()
        
        if not news_data.get("articles"):
            return "I couldn't find any news at the moment."
            
        result = "Here are the latest news headlines. "
        
        for i, article in enumerate(news_data["articles"][:3], 1):
            title = article.get("title", "")
            source = article.get("source", {}).get("name", "Unknown source")
            result += f"Article {i}: {title} from {source}. "
            
        return result
    except Exception as e:
        logging.error(f"Error fetching news: {e}")
        return "I couldn't fetch the news at the moment. Please try again later."

def processcommand(command):
    command = command.lower().strip()
    logging.info(f"Processing command: {command}")
    
    # Website commands
    if "open google" in command:
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in command:
        speak("opening linkedin")
        webbrowser.open("https://www.linkedin.com")
    elif "open instagram" in command:
        speak("opening instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open x" in command or "open twitter" in command:
        speak("opening x")
        webbrowser.open("https://www.x.com")
    elif "open facebook" in command:
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com")
    
    # Music commands
    elif command.startswith("play"):
        try:
            song = command.split(" ")[1]
            if song in musiclibrary.music:
                link = musiclibrary.music[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                available_songs = ", ".join(list(musiclibrary.music.keys())[:5])
                speak(f"I couldn't find that song. Available songs include: {available_songs}")
        except (IndexError, KeyError) as e:
            logging.error(f"Error playing music: {e}")
            speak("I couldn't understand which song to play")
    
    # Time commands
    elif "what time" in command or "current time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    
    # News commands  
    elif "news" in command:
        # Check if asking for news about a specific topic
        if "about" in command:
            topic = command.split("about", 1)[1].strip()
            news_text = get_news(topic)
        else:
            news_text = get_news()
        speak(news_text)
    
    # Search commands
    elif command.startswith(("search", "look up", "find")):
        query = command.split(" ", 1)[1] if len(command.split(" ", 1)) > 1 else ""
        if query:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            speak(f"Searching for {query}")
            webbrowser.open(search_url)
        else:
            speak("What would you like me to search for?")
    
    # If no specific command matches, use AI
    # else:
    #     response = aiprocess(command)
    #     speak(response)

if __name__ == "__main__":
    speak("initializing jarvis.....")
    while True:
        # Listen for the wake word jarvis
        print("Recognizing...")
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                # Adjust for ambient noise for better recognition
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            # Make wake word detection more flexible by checking if 'jarvis' is in the text
            if "jarvis" in word.lower():
                speak("yes")

                # Listen for command
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                processcommand(command)
                
        except sr.UnknownValueError:
            # Just continue listening - no need to show error every time
            pass
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            time.sleep(1)  # Wait before trying again
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(1)  # Wait before trying again
