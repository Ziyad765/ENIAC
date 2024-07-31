ENIAC: AI Robot Development Using Raspberry Pi and Python
Welcome to the ENIAC project repository! ENIAC is a cutting-edge AI robot developed using Raspberry Pi 4B and Python, designed to demonstrate advanced capabilities in speech recognition, text-to-speech, and natural language interaction.

Project Overview
ENIAC leverages the power of Raspberry Pi 4B and Python to create an intelligent robot capable of interacting with users through voice commands and responses. This project is the result of a collaborative effort by students from Computer Science and Design, showcasing the potential of combining hardware and software for innovative robotics solutions.

Key Components
Raspberry Pi 4B: The core hardware platform running Raspberry Pi OS, providing a stable environment for our AI algorithms.
Python: The primary programming language used for developing AI functionalities, chosen for its simplicity and extensive libraries.
AIML Module: Facilitates natural language processing and conversation management for human-like interaction.
GTTS Module: Converts text-based responses into speech using Google's text-to-speech capabilities.
Google Speech Recognition Module: Enables the robot to understand and interpret spoken commands through Google's speech recognition services.
Features
Speech Recognition: Accurate interpretation of spoken commands using Google's speech recognition.
Text-to-Speech: Conversion of text responses into audible speech with the GTTS module.
Natural Interaction: Engages in meaningful conversations using the AIML module for dynamic user interaction.
Installation
To set up ENIAC on your own Raspberry Pi, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/ENIAC.git
cd ENIAC
Install Dependencies:
Ensure you have Python 3 installed. Then, install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Setup Raspberry Pi:

Ensure your Raspberry Pi is running Raspberry Pi OS.
Configure your microphone and speaker.
Run the Application:

bash
Copy code
python main.py
Usage
After running the application, ENIAC will start listening for voice commands. You can interact with the robot by speaking commands and receive responses in audio form. The robot can perform various tasks and engage in conversations based on its programming.

Contributing
We welcome contributions from the community! If you have suggestions, improvements, or bug fixes, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
We’d like to thank our mentors, peers, and everyone who supported and contributed to this project. Special thanks to the Raspberry Pi community and the developers of the AI libraries we used.

