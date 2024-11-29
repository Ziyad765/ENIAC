import g4f
import re
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
from g4f.client import Client
import time
import threading

# Initialize the speech engine
engine = pyttsx3.init()

# Initialize the g4f client
client = Client()

# Message history
messages = [
    {"role": "system", "content": "your name is eniac and you are developed by computer science and design engineering students of government engineering college kozhikode"},
    {"role": "system", "content": "about c s d, computer science and design engineering is a new branch of b tech degree in government engineering college kozhikode"},
    {"role": "system", "content": "provide simple answers for simple questions give details but in limited words"},
    {"role": "system", "content": "answer each question independently without referencing previous questions"},
    {"role": "system", "content": "consider each question and answer as separate and give question and answer separately , only refer previous question and answer if needed very much"},
    {"role": "system", "content": "don't talk about openai or chat gpt or any information regarding you are chat gpt or you have limited information till 2021 and all, only provide information to what is being asked AND DON'T TELL ANYTHING RELATED TO CHATGPT"},
]

def GPT(message):
    global messages
    messages.append({'role': 'user', 'content': message})

    try:
        # Send the user's input to the model
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Change to the correct model if needed
            messages=messages
        )

        # Check for a valid response
        if response and hasattr(response, 'choices') and len(response.choices) > 0:
            ms = response.choices[0].message.content  # Access the content correctly
            return ms

        else:
            ms = "Sorry, I couldn't get a valid response."
            return ms

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."

def GPT_with_retry(message, retries=2):
    """Handle retries for 404 error"""
    attempt = 0
    while attempt < retries + 1:
        response = GPT(message)
        
        # Check for the 404 error in the response and retry
        if "Request ended with status code 404" in response or not response.strip():
            print("Retrying due to invalid or empty response...")
            attempt += 1
            time.sleep(2)  # Delay before retrying
            if attempt > retries:
                return "Sorry, the service is still unavailable after retrying."
        else:
            return response  # Return valid response if no 404 error

    return "Sorry, something went wrong after retrying."

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please take your time to ask the question.")
        # Adjust the listening parameters
        audio = r.listen(source, timeout=10, phrase_time_limit=15)  # Increased timeout and phrase_time_limit
    try:
        user_query = r.recognize_google(audio)
        print(f"User query: {user_query}")
        return user_query
    except sr.UnknownValueError:
        # Skip response if the audio is not understandable
        print("Could not understand audio")
        return None
    except sr.RequestError:
        # Skip response if there's an error in the API request
        print("Error with the API request")
        return None

def find_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return matches[0].strip()
    else:
        return None

def update_ui_and_speak(response_text):
    """Helper function to update the UI and speak the response"""
    response_box.config(state=tk.NORMAL)
    response_box.insert(tk.END, f"Assistant: {response_text}\n")
    response_box.config(state=tk.DISABLED)
    response_box.yview(tk.END)  # Scroll to the end of the text box

    # Speak the response only once
    print(f"Speaking: {response_text}")  # Print response before speaking
    speak(response_text)

def run_ai():
    while True:
        query = listen()
        if query:
            response_box.config(state=tk.NORMAL)
            response_box.insert(tk.END, f"You: {query}\n")
            response_box.config(state=tk.DISABLED)
            response_box.yview(tk.END)  # Scroll to the end of the text box

            # Get response from GPT with retry
            response = GPT_with_retry(query)

            python_code = find_code(response)

            # If response contains Python code, execute it
            if python_code:
                response = response.replace(python_code, '').replace('python', '').replace('```', '')
                update_ui_and_speak(response)

                try:
                    exec(python_code)
                except Exception as e:
                    print(f"Error executing code: {e}")
            else:
                update_ui_and_speak(response)

# Set up the UI
window = tk.Tk()
window.title("ENIAC AI")
window.geometry("400x600")

# Create a scrolled text area for responses
response_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
response_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Start the AI processing in the background
threading.Thread(target=run_ai, daemon=True).start()

window.mainloop()
