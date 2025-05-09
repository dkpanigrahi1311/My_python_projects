
import speech_recognition as sr
import pyttsx3
import openai

# Set your OpenAI API key here
openai.api_key = "sk-proj-4Y8B58iYcJMurNw0VKLPeM6aKEZOF0-sk-proj-7mjxuVmV9EOjHaF-Zd3iOS0ZtMXCz7R18Ht0qcaWvayJunwpUEqq5pMvRjgJpGAJtMu3sAJYuqT3BlbkFJ6OnvlDpgsqdDc9B3kLxRjwPyuld4k6_G-dk6xWM8luMIuR1M3d66wlp7zZF-aXecpG_k9l69wA-u-toW4Yh68A"

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("DEVA:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("You:", query)
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are DEVA, a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("OpenAI API Error:", e)  # ✅ Show actual error
        return "I'm having trouble connecting to my brain."


def main():
    speak("Hello, I'm DEVA. How can I help you?")
    while True:
        query = listen()
        if query.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        if query:
            response = ask_gpt(query)
            speak(response)

if __name__ == "__main__":
    main()



