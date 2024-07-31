import g4f
import re
from head.listen import take_command
from head.speak import speak

messages = [
    {"role": "system", "content": "your name is eniac and you are developed by computer science and design engineering students of government engineering college kozhikode"},
    {"role": "system", "content": "about csd, computer science and design engineering is a new branch of b tech degree in geck"},
    {"role": "system", "content": "provide simple answers only in very short words for simple questions"},
    {"role": "system", "content": "dont talk about openai or chat gpt or any information regarding you are chat gpt or you have limited information till 2021 and all, only provide information to what is being asked AND DONT TELL ANYTHING RELATED TO CHATGPT"},
    {"role": "system", "content": "if the question is simple answer the question in a simplified manner in less words without losing the needed details"},
    {"role": "system", "content": "use modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5 etc"},
    {"role": "system", "content": "don't use input function and subprocess in python code"},
    {"role": "system", "content": "*always use default paths in python code*"},
    {
        "role": "system",
        "content": "When user says 'show image,' use the following code to display the image:\n```python\nfrom PIL import Image\n\nimage_path = r'C:\\Users\\subed\\OneDrive\\Desktop\\code\\AI TUTORIAL\\output\\0.jpeg'\nimage = Image.open(image_path)\nimage.show()\n``` If you want to show another image, let me know."
    },
    {
        "role": "system",
        "content": "When the user says 'generate an image' and provides a prompt like 'generate an image about a horse,' extract the prompt from the user query. Then, give this code to the user:\n```python\nfrom cookies.bingcookie import u_cookie_value \nfrom os import system, listdir\n\ndef Generate_Images(prompt: str):\n    system(f'python -m BingImageCreator --prompt \"{prompt}\" -U \"{u_cookie_value}\"')\n    return listdir(\"output\")[-4:]\n\n# Example usage\nresult = Generate_Images('user_extracted_prompt')\nprint(result)\n``` While calling the function, replace 'user_extracted_prompt' with the actual prompt provided by the user to generate the desired image. don't write other things just say 'ok sir generating an image about user prompt' and give the code. Also, don't write other things like 'here's the code'. just give the code and write 'ok sir generating an image about user prompt' don't write 'here's the code' or other things."
    },
    {"role": "user", "content": "open Google Chrome"},
    {"role": "assistant", "content": "Sure, opening Google Chrome.\n```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')\n```"},
    {"role": "user", "content": "close Google Chrome"},
    {"role": "assistant", "content": "Alright, closing Google Chrome.\n```python\nimport os\nos.system('taskkill /F /IM chrome.exe')\n```"}
]

def GPT(*args):
    global messages
    assert args != ()

    message = ' '.join(args)
    messages.append({'role': 'user', 'content': message})

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a free or open model
            provider=g4f.Provider.FreeChatgpt,  # Use a free provider
            messages=messages
        )
        
        # Debugging the response structure
        print("Raw response:", response)
        speak(response)
        
        if isinstance(response, dict) and 'choices' in response:
            # Assuming 'choices' is a list of responses
            ms = response['choices'][0]['message']['content']
        else:
            ms = "   "
        
        print("Processed message:", ms)  # Print for debugging

        messages.append({'role': 'assistant', 'content': ms})
        return ms
    except Exception as e:
        print(f"Error with GPT call: {e}")
        return "Sorry, something went wrong."

def find_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return matches[0].strip()
    else:
        return None

while True:
    query = take_command()
    if query != '-':
        print('User query:', query)
        response = GPT(query)
        python_code = find_code(response)

        if python_code:
            response = response.replace(python_code, '').replace('python', '').replace('```', '')
            speak(response)
            try:
                exec(python_code)
            except Exception as e:
                print(f"Error executing code: {e}")
        else:
            speak(response)
    else:
        pass
